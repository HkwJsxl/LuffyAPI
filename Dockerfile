FROM python:python39
MAINTAINER hkw
EXPOSE 8080
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt -i https://pypi.douban.com/simple/
COPY . /tmp/
VOLUME ["/home"]
WORKDIR /home/luffyapi
CMD ["uwsgi", "--ini", "/home/luffyapi/uwsgi.ini"]
CMD ["python", "/home/luffyapi/manage_pro.py", "makemigrations"]
CMD ["python", "/home/luffyapi/manage_pro.py", "migrate"]
CMD ["python", "/home/luffyapi/manage_pro.py", "runserver","0.0.0.0:8080"]