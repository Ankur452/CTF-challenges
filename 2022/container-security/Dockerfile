FROM python:3

USER root
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

RUN cd / && mkdir CTF2022
COPY FLAG.txt /CTF2022

ENTRYPOINT [ "python" ]
CMD ["app.py"] 