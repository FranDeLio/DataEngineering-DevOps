# Deployment guide

Useful commands to retrieve docker image and deploy. To be executed in succession.
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml'

mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env

docker-compose up airflow-init
docker-compose up
```

The following commands serve to check on the status of volumes, containers and execute commands within containers.
```bash
docker compose ps

docker ps
docker exec {CONTAINER_ID} airflow dags list 
```
