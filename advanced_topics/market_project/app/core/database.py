from sqlmodel import create_engine, Session

filename = 'sandbox.db'
url = f'sqlite:///{filename}'

engine = create_engine(url)

def get_session():
    with Session(engine) as session:
        yield session