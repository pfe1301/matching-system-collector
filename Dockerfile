FROM python:latest

WORKDIR /matching-system-collector

COPY . .

RUN python -m pip install -r requirements.txt

ENTRYPOINT [ "./entrypoint.sh" ]