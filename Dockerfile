FROM alpine:3.6

COPY app/ /app/

RUN apk update
RUN apk add python3
RUN pip3 install -r /app/requirements.txt
