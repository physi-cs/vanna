FROM python:3.8

RUN sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list

RUN apt-get update && apt-get -y install vim

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/ && rm -rf `pip3 cache dir`

EXPOSE 5000

# CMD ["python","-u", "chat_db.py"]