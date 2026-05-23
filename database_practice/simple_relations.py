from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str

class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    user_id: int = Field(foreign_key='user.id')

sql_file_name = 'simple_db.db'
url = f'sqlite:///{sql_file_name}'
engine = create_engine(url)


def init_db_and_fill():
    user_one = User(username='Alex')

    post_one = Post(title='Relax', user_id=1)
    post_two = Post(title='Sleep', user_id=1)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(user_one)

        session.add(post_one)
        session.add(post_two)

        session.commit()


def show_users_and_their_posts():
    with Session(engine) as session:
        all_users = select(User)
        result_users = session.exec(all_users)

        for user in result_users:
            print(f'Name: {user.username}')

            all_posts = select(Post).where(Post.user_id == user.id)
            result_posts = session.exec(all_posts)

            for post in result_posts:
                print(f'Post: {post.title}')


if __name__ == '__main__':
    init_db_and_fill()
    show_users_and_their_posts()


