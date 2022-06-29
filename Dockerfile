FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN python3 -m venv env
RUN source env/bin/activate
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["view.py" ]
