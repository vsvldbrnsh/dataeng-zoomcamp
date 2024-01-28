
1. start postgresql service:

docker run -it \
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=admin \
    -e POSTGRES_DB=ny_taxi \
    -p 5432:5432 \
    -v C:/Users/barna/Projects/dataeng-zoomcamp/1_intro/db-data:/var/lib/postgresql/data \
    --network pg-db \
    --name postgres \
postgres:13

2. start ubuntu service:

docker run -it \
    --network pg-db \
    --name ubuntu \
    -p 8888:8888 \
ubuntu:custom

3. pgcli -h postgresql -U admin -d ny_taxi

4. python data_ingestion.py \
    --user=admin \
    --password=admin \
    --host=postgres \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

5. docker run -it \
    --network=pg-db \
    taxi_ingest:v001 \
      --user=admin \
      --password=admin \
      --host=postgres \
      --port=5432 \
      --db=ny_taxi \
      --table_name=yellow_taxi_trips \
      --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"