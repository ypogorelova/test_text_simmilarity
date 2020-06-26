FROM python:3.7

WORKDIR /sentense_similarity
COPY . ./backend
EXPOSE 8000

RUN pip install -r ./requirements.txt

CMD backend.main:app --reload