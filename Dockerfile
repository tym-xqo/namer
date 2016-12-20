FROM alpine:edge
MAINTAINER yagermadden@gmail.com

RUN apk update && apk add --upgrade python3

RUN pip3 install flask \
    gunicorn \
    requests

RUN mkdir -m 755 /app
WORKDIR /app

ADD namer-svc.py /app
ADD wordlists.py /app

EXPOSE 8880

CMD ["gunicorn", "-b", "0.0.0.0:8880", "namer-svc:app", "--log-file=-"]

