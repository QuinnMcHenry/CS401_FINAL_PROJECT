FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY routes.py test_routes.py ./

RUN chmod +rx app.py test_app.py

ENV PATH="/code:$PATH"
