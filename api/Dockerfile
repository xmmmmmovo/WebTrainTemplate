FROM python:3.7

COPY requirements.txt /tmp
RUN  ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && pip install -r /tmp/requirements.txt
# 如果太慢了再加上这句 不然镜像站有可能同步不全导致包安装失败
# -i https://pypi.tuna.tsinghua.edu.cn/
COPY . /code
WORKDIR /code
CMD gunicorn app:app -c gunicorn.conf.py
