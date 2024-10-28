FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy 

COPY ["predict.py", "./"]

EXPOSE 1212

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:1212", "predict:app"]