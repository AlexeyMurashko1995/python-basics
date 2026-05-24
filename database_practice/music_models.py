from sqlmodel import SQLModel, Field, Session, select, Relationship, create_engine

sql_file_name = 'music_db.db'
url = f'sqlite:///{sql_file_name}'

engine = create_engine(url)

class Artist(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    tracks: list['Track']= Relationship(back_populates='artist')

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
        track_one = Track(title='Loose Yourself')

        track_one.artist = artist_one

        session.add(artist_one)
        session.add(track_one)

        session.commit()


if __name__ == '__main__':
    init_db()
    create_music_data()
