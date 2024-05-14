from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá mundo!"}


def test_exercise_1_deve_retornar_html_ola_mundo(client):
    response = client.get("/exercise-1")

    assert response.status_code == HTTPStatus.OK
    assert "<h1>Olá mundo!</h1>" in response.text
