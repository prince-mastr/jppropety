FROM python:3.6
LABEL author="codemastr"

ENV PYTHONBUFFERED=1

ARG RDS_DB_NAME
ARG RDS_HOST
ARG RDS_PASSWORD
ARG RDS_PORT
ARG RDS_USER_NAME
ARG REDIS_HOST
ARG CACHE_HOST

ENV REDIS_HOST=${REDIS_HOST}
ENV CACHE_HOST=${CACHE_HOST}
ENV RDS_DB_NAME=${RDS_DB_NAME}
ENV RDS_HOST=${RDS_HOST}
ENV RDS_PASSWORD=${RDS_PASSWORD}
ENV RDS_PORT=${RDS_PORT}
ENV RDS_USER_NAME=${RDS_USER_NAME}

RUN apt-get update
# RUN apt-get install -y zlib1g-dev libjpeg-dev python3-pythonmagick inkscape xvfb poppler-utils libfile-mimeinfo-perl qpdf libimage-exiftool-perl ufraw-batch ffmpeg

# RUN apt install -y  python3-pip

# RUN pip3 install preview-generator

# RUN apt-get install -y libreoffice

# RUN apt-get install -y scribus

RUN pip3 install gunicorn gunicorn[eventlet]
RUN apt-get install -y nginx nano curl
COPY ./django_prod_nginx.conf /etc/nginx/sites-enabled
RUN echo PROJECT_MOVE
COPY . /opt/codemastr/tagifiles
ADD ./requirements.txt /opt/codemastr/tagifiles
WORKDIR /opt/codemastr/tagifiles

RUN pip3 install --upgrade setuptools
RUN apt-get -f install

RUN pip3 install --upgrade pip
# RUN pip3 install MarkupSafe==1.0
RUN pip3 install mysqlclient==1.3.12
RUN pip3 install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN ["chmod", "+x", "/opt/codemastr/tagifiles/docker_entrypoint.sh"]

EXPOSE 4500

ENTRYPOINT ["./docker_entrypoint.sh"]

