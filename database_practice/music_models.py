from fastapi import FastAPI
from sqlmodel import (
    SQLModel, Field, Session, select, Relationship, create_engine
)


sql_file_name = 'music_db.db'
url = f'sqlite:///{sql_file_name}'

engine = create_engine(url)

app = FastAPI()

class Artist(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    tracks: list['Track'] = Relationship(back_populates='artist')


class Track(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    artist_id: int = Field(foreign_key='artist.id')
    artist: 'Artist' = Relationship(back_populates='tracks')


def init_db():
    SQLModel.metadata.create_all(engine)
    print('Database created successfully')


def create_music_data():
    with Session(engine) as session:
        artist_one = Artist(name='Eminem')
        track_one = Track(title='Lose Yourself')

        track_one.artist = artist_one

        session.add(artist_one)
        session.add(track_one)

        session.commit()


@app.get('/artists')
def read_music_data():
    with Session(engine) as session:
        query = select(Artist)
        result = session.exec(query)

        target_artists = result.all()
        return target_artists


@app.post('/artists')
def create_artist_endpoint(artist: Artist):
    with Session(engine) as session:
        session.add(artist)

        session.commit()
        session.refresh(artist)

        return artist


@app.get('/tracks')
def read_tracks_data():
    with Session(engine) as session:
        query = select(Track)
        result = session.exec(query)

        target_tracks = result.all()
        return target_tracks


def update_music_data():
    with Session(engine) as session:
        query = select(Artist).where(Artist.id == 1)

        result = session.exec(query)
        for first_artist in result:
            first_artist.name = 'Eminem ft. Rihanna'

        session.commit()


def delete_music_data():
    with Session(engine) as session:
        target_track = session.get(Track, 1)

        if target_track:
            session.delete(target_track)
            session.commit()
            print('Track deleted successfully')
        else:
            print('Track not found, nothing to delete')


if __name__ == '__main__':
    init_db()
