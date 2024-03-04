FROM python:3.11

WORKDIR /app

ADD . /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 80

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]