from sqlalchemy import select

from fast_zero.models import Todo, User


def test_create_user(session):
    new_user = User(
        username="matheus", email="matheus@mail.com", password="senha123"
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == "matheus"))

    assert user.username == "matheus"


def test_create_todo(session, user: User):
    todo = Todo(
        title="Test Todo",
        description="Test Desc",
        state="draft",
        user_id=user.id,
    )

    session.add(todo)
    session.commit()
    session.refresh(todo)

    user = session.scalar(select(User).where(User.id == user.id))

    assert todo in user.todos
