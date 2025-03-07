FROM python:3.8

WORKDIR /app
COPY . /app

RUN pip install flask scikit-learn
CMD ["python", "src/app.py"]
