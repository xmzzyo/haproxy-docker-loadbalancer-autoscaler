FROM python:3.6-alpine
WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
ADD . /app
EXPOSE 5678
ENTRYPOINT [ "python3","api.py" ]