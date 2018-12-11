FROM python:3-slim
WORKDIR /usr/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/code
WORKDIR /usr/src/code
CMD ["python","manage.py","runserver_plus","0.0.0.0:8000"]
