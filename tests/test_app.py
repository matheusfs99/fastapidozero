from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá mundo!"}


def test_exercise_1_deve_retornar_html_ola_mundo():
    client = TestClient(app)

    response = client.get("/exercise-1")

    assert response.status_code == HTTPStatus.OK
    assert "<h1>Olá mundo!</h1>" in response.text
