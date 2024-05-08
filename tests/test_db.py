from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(username="matheus", email="matheus@mail.com", password="senha123")
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == "matheus"))

    assert user.username == "matheus"
