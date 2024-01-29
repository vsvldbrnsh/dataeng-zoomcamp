
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


## Terraform

$ terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be created
  + resource "google_bigquery_dataset" "dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "trips_data_all"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "europe-west1"
      + max_time_travel_hours      = (known after apply)
      + project                    = "data-eng-363618"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

  # google_storage_bucket.data-lake will be created
  + resource "google_storage_bucket" "data-lake" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EU"
      + name                        = "de_data_lake"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }
          + condition {
              + age                   = 30
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }

      + versioning {
          + enabled = true
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.