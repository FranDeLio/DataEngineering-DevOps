# FastAPI-Docker-MLOps Documentation

The objective here was building a toy regression model to be hosted in a container and accessible via FastAPI. The model takes age, income and a loan ammount and output the probability that loan is payed back, along with a 95% predcition interval.

Note that first of all one should run [fit_model.py](./fit_model.py) in order to train the toy model before executing calling in docker.

Execute the following commands in succession to deploy the API within the container and test it via the API call.
```bash
docker build --pull --no-cache -t fastapi-docker-ml .
docker run -d -p 8000:8000 fastapi-docker-ml


curl --request POST --location http://localhost:8000/predict --header "Content-Type: application/json" --data '{"age":20, "income":30000, "loan":3000}'
```

The following commands could be useful for debugging.

```bash
docker container ls --all
docker logs -t {CONTAINER_ID}
```

