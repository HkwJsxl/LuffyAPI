FROM python:python39
MAINTAINER hkw
EXPOSE 8080
RUN pip install -r ./requirements.txt -i https://pypi.douban.com/simple/
VOLUME ["/home"]
WORKDIR /home/luffyapi/
CMD ["python", "/home/luffyapi/manage_pro.py", "makemigrations"]
CMD ["python", "/home/luffyapi/manage_pro.py", "migrate"]
CMD ["python", "/home/luffyapi/manage_pro.py", "runserver","0.0.0.0:8080"]