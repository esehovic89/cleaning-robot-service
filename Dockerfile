FROM python:3.10


WORKDIR /src


COPY ./requirements.txt /src/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt


COPY ./src /src


CMD ["fastapi", "run", "api/main.py", "--port", "5000"]
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "5000"]