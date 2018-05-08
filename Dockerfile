

FROM python:2
RUN  pip install psutil


WORKDIR /usr/src/app

COPY metrics.py /usr/src/app

ENTRYPOINT ["python","metrics.py"]

