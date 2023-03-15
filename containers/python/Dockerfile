FROM python:3.11.2
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
ENV TZ="Asia/Tokyo"
RUN echo $TZ > /etc/timezone
WORKDIR /code
COPY ./application/pyproject.toml /code/
RUN pip install --upgrade pip && pip install poetry
RUN poetry install
COPY ./application /code/
COPY ./containers/python/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh