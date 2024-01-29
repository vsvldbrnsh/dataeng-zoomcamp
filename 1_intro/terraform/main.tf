terraform {
    required_providers {
        google = {
            source = "hashicorp/google"
            version = "5.6.0"
        }
    }
}

provider "google" {
    project = var.project
    region = var.region  # Ensure this is a valid region
}

resource "google_storage_bucket" "data-lake" {
  name          = local.data_lake_bucket
  location      = local.location

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30
    }
  }

  force_destroy = true
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.BQ_DATASET
  project    = var.project
  location   = var.region  # Ensure this is a valid region
}
