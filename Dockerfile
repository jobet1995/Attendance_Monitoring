FROM python:3.9-slim

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

RUN apt-get update  && apt-get install -y \
    build-essential \
    libpq-dev \
    gettext \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY .dockerignore /
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8000

HEALTHCHECK CMD curl --fail http://localhost:8000/health/ || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "attendance_monitoring.wsgi:application"]