FROM python:3-alpine

ADD ./app /app/

RUN pip install -r /app/requirements.txt

ENTRYPOINT [ "python", "/app/api.py"  ]