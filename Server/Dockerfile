FROM python:3.6-alpine

ADD ./Server/app /usr/svc/app
WORKDIR /usr/svc/app

RUN pip install -r requirements.txt
RUN python create_database.py
RUN python create_all_objects.py

EXPOSE 5000
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "app:app"]