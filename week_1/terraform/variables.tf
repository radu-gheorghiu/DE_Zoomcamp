# Locals are local variables, like constants
locals {
    data_lake_bucket = "dtc_data_lake"
}

variable "project_id" {
    default = "snappy-spanner-338514"
}

variable "region" {
    default = "europe-west6"
    type = string
}

variable "bucket_name" {
    default = ""
}

variable "storage_class" {
    default = "STANDARD"
}

variable "BQ_Dataset" {
    type = string
    default = "trips_all_data"
}

variable "TABLE_NAME" {
    type = string
    default = "ny_trips"
}