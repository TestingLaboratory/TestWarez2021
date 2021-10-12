FROM python

WORKDIR /restful-booker-collector

COPY requirements.txt .

CMD 'python -m pip install --upgrade pip'

RUN pip install -r requirements.txt

COPY custom_collector_package/ .

CMD ["python", "./restful_booker_collector.py"]

EXPOSE 9099