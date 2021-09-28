FROM python:3.9

RUN mkdir -p /usr/src/synergy_test/

WORKDIR /usr/src/synergy_test/

COPY ./Synergy_test/ /usr/src/synergy_test/

COPY requirements.txt /usr/src/synergy_test/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]