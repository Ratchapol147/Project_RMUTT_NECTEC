FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /project_nectec
WORKDIR /project_nectec
COPY requirements.txt /project_nectec/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /project_nectec/