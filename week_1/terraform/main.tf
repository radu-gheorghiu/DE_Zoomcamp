terraform {
    required_version = ">= 1.0"
    backend "local" {}
    required_providers {
        google = {
            source = "hashicorp/google"
        }
    }
}

provider "google" {
    project = var.project_id
    region = var.region

    # credentials = file(var.credentials) # Use this if you don't want to set env-var GOOGLE_APPLICATION_CREDENTIALS
}

# Data Lake Buckets
# Reference: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket

resource "google_storage_bucket" "data-lake-bucket" {
    name = "${local.data_lake_bucket}_${var.project_id}" # Concatenate bucket & project for uniqueness
    location = var.region

    # Optional, but recommended
    storage_class = var.storage_class
    uniform_bucket_level_access = true

    versioning {
        enabled = true
    }

    lifecycle_rule {
        action {
            type = "Delete"
        }
        condition {
            age = 30 # days
        }
    }

    force_destroy = true
}

resource "google_bigquery_dataset" "dataset" {
    dataset_id = var.BQ_Dataset
    project = var.project_id
    location = var.region
}