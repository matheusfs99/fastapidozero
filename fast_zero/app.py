from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .schemas import Message

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá mundo!"}


@app.get("/exercise-1", status_code=HTTPStatus.OK, response_class=HTMLResponse)
def exercise_1():
    return """
    <h1>Olá mundo!</h1>
    """
