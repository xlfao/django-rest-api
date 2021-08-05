FROM python:3.6
ENV PYTHONUNBUFFERED 1
ADD /config/requirements.txt /
RUN pip install --upgrade pip; \
    pip install -r /requirements.txt; mkdir /src; \
    pip install --upgrade django; \
    apt update; apt install -y gettext;
WORKDIR /src