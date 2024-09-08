FROM python:3.12.4
WORKDIR /app
COPY . /app
COPY ../helpers.py /app
COPY ../conftest.py /app
COPY ../requirements.txt /app
RUN pip install -r requirements.txt
ENTRYPOINT ["pytest"]
CMD ["--version"]

