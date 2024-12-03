FROM python:3.9


WORKDIR /src


COPY ./requirements.txt /src/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt


COPY ./src /src


CMD ["fastapi", "run", "api/main.py", "--port", "5000"]