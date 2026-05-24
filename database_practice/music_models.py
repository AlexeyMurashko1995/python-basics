from sqlmodel import SQLModel, Field, Session, select, Relationship, create_engine

class Artist(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    tracks: list['Track']= Relationship(back_populates='artist')

class Track(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    artist_id: int = Field(foreign_key='artist.id')
    artist: 'Artist' = Relationship(back_populates='tracks')