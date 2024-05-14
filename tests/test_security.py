from jwt import decode

from fast_zero.security import create_access_token, settings


def test_jwt():
    data = {"test": "test"}
    token = create_access_token(data)

    decoded = decode(token, settings.SECRET_KEY, algorithms=["HS256"])

    assert decoded["test"] == "test"
    assert decoded["exp"]
