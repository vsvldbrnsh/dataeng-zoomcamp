locals {
  data_lake_bucket = "de_data_lake_unique12345"  # Must be globally unique
  location = "EU"
}

variable "project" {
  description = "Your GCP Project ID"
  default = "data-eng-363618"
}

variable "region" {
  description = "Region for GCP resources (e.g., europe-west1)"
  default = "europe-west1"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset ID"
  default = "trips_data_all"
}