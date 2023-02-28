FROM python:python39
MAINTAINER hkw
EXPOSE 8080
COPY requirements.txt /tmp/
RUN pip install uwsgi -i https://pypi.douban.com/simple/
RUN pip install -r /tmp/requirements.txt -i https://pypi.douban.com/simple/
COPY . /tmp/
VOLUME ["/tmp"]
WORKDIR /tmp
CMD ["uwsgi", "--ini", "/tmp/uwsgi.ini"]
#CMD ["python", "/tmp/manage_pro.py", "runserver", "0.0.0.0:8080"]