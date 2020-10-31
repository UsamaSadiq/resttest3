FROM python:3.5-alpine
MAINTAINER Abhilash Joseph C. <abhilash@softlinkweb.com>
# Install packages
RUN apk add --no-cache libcurl

# Needed for pycurl
ENV PYCURL_SSL_LIBRARY=openssl
RUN apk add --no-cache --virtual .build-dependencies build-base curl-dev \
    && pip install pycurl \
    && apk del .build-dependencies
RUN pip install --upgrade pip
RUN pip install flake8 pytest coverage
COPY requirements.txt /tmp/requirements.txt

#RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /py3resttest
WORKDIR /py3resttest


RUN python setup.py bdist_wheel
RUN pip install -U dist/*
RUN flake8 py3resttest --count --select=E9,F63,F7,F82 --show-source --statistics
RUN flake8 py3resttest --count --exit-zero --max-complexity=30 --max-line-length=127 --statistics
# RUN python -m pytest tests
RUN coverage run --source py3resttest -m pytest tests/test_*.py
RUN coverage report
#RUN resttest3 --url https://www.courtlistener.com --test tests/fun_test.yaml

