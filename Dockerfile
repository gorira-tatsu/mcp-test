FROM python:3.12.0a4-alpine3.17
RUN apk update && apk add mysql-client=10.6.11-r0 --no-cache && rm -r /var/cache/apk/*
WORKDIR /main
RUN pip3 install mysql-connector-python==8.0.32 --no-cache-dir
COPY . /main
CMD ["sh", "main_run.sh"]