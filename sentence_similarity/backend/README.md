## To run backend application

Set environment variables and create database.
```
export MONGO_DB=rwdb MONGO_PORT=5432
docker run --name mongodb --rm -e MONGO_DB="$MONGO_DB" MONGO
export MONGO_HOST=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pgdb)
mongo --host=$MONGO_HOST --port=$MONGO_PORT $MONGO_DB
```

Then create ``.env``file
```
touch .env
echo DATABASE_URL=mongo://MONGO_HOST:$MONGO_PORT/$MONGO_DB >> .env
pip install requirements.txt
```

```
uvicorn sentence_similarity.backend.sentence_similarity.main:app --reload
```

## To run in docker
```
docker-compose up -d
```

Application will be available on ``localhost`` or ``127.0.0.1`` in your browser.
All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.