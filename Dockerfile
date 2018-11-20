FROM python:3-slim
WORKDIR /usr/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ /usr/src/code
WORKDIR /usr/src/code
CMD ["gunicorn","app_falcon:app","-c","gunicorn.py","--log-config","logging.conf"]
