FROM daocloud.io/python:2-onbuild

MAINTAINER studywiller@gmail.com

RUN pip install
ADD app.tar.gz . 
RUN pwd && ls
ENTRYPOINT ["sh", "run.sh"]
