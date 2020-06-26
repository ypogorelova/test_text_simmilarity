FROM python:3.7

WORKDIR /app
COPY sentence_similarity /app/sentence_similarity
COPY requirements.txt /app/
EXPOSE 8000

RUN pip install -r ./requirements.txt

CMD uvicorn sentence_similarity.main:app --reload