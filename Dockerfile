FROM python:3.9.12
LABEL maintainer="rapzmary@gmail.com"
ENV PYTHONNUMBUFFERED=1
WORKDIR /Test_MHTech

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

CMD [ "python", "manage.py","runserver" ]