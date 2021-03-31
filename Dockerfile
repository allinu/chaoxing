FROM python:3.8-alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
RUN apk add --no-cache --virtual .build-deps gcc libc-dev libxslt-dev && \
    apk add --no-cache libxslt && \
    pip install lxml --no-cache-dir && \
    apk del .build-deps
ENV COOKIE="" CLASSID="" COURSEID="" SLEEP_TIME="0.1" PASS_TIME="30"
COPY . /Chaoxing
WORKDIR /Chaoxing
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python","-u","run.py" ]
