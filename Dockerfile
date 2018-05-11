FROM python:2.7

ADD metrics.py /

ENV ps.PROCFS_PATH /host_proc

RUN pip install psutil && pip install argparse

VOLUME /proc:/host_proc

CMD python ./metrics.py all
