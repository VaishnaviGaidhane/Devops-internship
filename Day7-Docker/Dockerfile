#FROM python
#ADD app.py /
#CMD ["python","app.py"]

FROM python:alpine3.10
WORKDIR /app
COPY . /app
RUN pip install -r text.text
EXPOSE 5000
CMD python ./weApp.py

