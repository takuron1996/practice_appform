FROM python:3
ENV PYTHONUNBUFFERED 1
ENV TZ="Asia/Tokyo"
RUN echo $TZ > /etc/timezone
RUN mkdir /code
WORKDIR /code
COPY /application/pyproject.toml /code/
RUN pip install --upgrade pip && pip install poetry
RUN poetry install
COPY . /code/