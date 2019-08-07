FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /proj
WORKDIR /proj
ADD /proj/requirements.txt /proj/
RUN pip install -r requirements.txt
ADD conf /proj/