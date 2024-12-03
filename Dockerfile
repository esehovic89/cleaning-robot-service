FROM python:3.10

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./src /src

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "5000"]