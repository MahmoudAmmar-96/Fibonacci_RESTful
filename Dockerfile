FROM python:2.7

COPY . /fibonacci

WORKDIR /fibonacci

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["fibonacci.py"]
