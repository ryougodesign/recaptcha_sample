FROM python:3.10.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /recaptcha_sample
WORKDIR /recaptcha_sample
ADD requirements.txt /recaptcha_sample/
RUN pip install --upgrade pip && pip install -r requirements.txt