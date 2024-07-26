FROM python:latest

WORKDIR /usr/app/src

COPY cmdspg.py ./

CMD [ "python", "./cmdspg.py"]