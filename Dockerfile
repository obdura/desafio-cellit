FROM python:3.10.5-bullseye
WORKDIR /desafio
COPY ./requirements.txt /desafio/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /desafio/requirements.txt
COPY ./app /desafio/app
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]