# Data Engineering Zoomcamp - Week 1 Homework

This file contains the homework for week 1 as well as additional information that might be helpful for evaluating the homework.

## Question 1. Google Cloud SDK

Install Google Cloud SDK. What's the version you have?

To get the version, run gcloud --version

## <u>Answer</u>:
C:\Users\Radu>gcloud --version

    Google Cloud SDK 370.0.0
    bq 2.0.73
    core 2022.01.21
    gsutil 5.6

## Question 2. Terraform

Now install terraform and go to the terraform directory (week_1_basics_n_setup/1_terraform_gcp/terraform)

After that, run

terraform init
terraform plan
terraform apply
Apply the plan and copy the output (after running apply) to the form.

It should be the entire output - from the moment you typed terraform init to the very end.

## <u>Answer</u>:

    (de_zoomcamp) C:\_gitRepos\DE_Zoomcamp\DE_Zoomcamp\week_1\terraform>terraform init

    Initializing the backend...

    Successfully configured the backend "local"! Terraform will automatically
    use this backend unless the backend configuration changes.

    Initializing provider plugins...
    - Finding latest version of hashicorp/google...
    - Installing hashicorp/google v4.8.0...
    - Installed hashicorp/google v4.8.0 (signed by HashiCorp)

    Terraform has created a lock file .terraform.lock.hcl to record the provider
    selections it made above. Include this file in your version control repository
    so that Terraform can guarantee to make the same selections by default when
    you run "terraform init" in the future.

    Terraform has been successfully initialized!

    You may now begin working with Terraform. Try running "terraform plan" to see
    any changes that are required for your infrastructure. All Terraform commands
    should now work.

    If you ever set or change modules or backend configuration for Terraform,
    rerun this command to reinitialize your working directory. If you forget, other
    commands will detect it and remind you to do so if necessary.

---

    (de_zoomcamp) C:\_gitRepos\DE_Zoomcamp\DE_Zoomcamp\week_1\terraform>terraform plan

    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
    + create

    Terraform will perform the following actions:

    # google_bigquery_dataset.dataset will be created
    + resource "google_bigquery_dataset" "dataset" {
        + creation_time              = (known after apply)
        + dataset_id                 = "trips_all_data"
        + delete_contents_on_destroy = false
        + etag                       = (known after apply)
        + id                         = (known after apply)
        + last_modified_time         = (known after apply)
        + location                   = "europe-west6"
        + project                    = "snappy-spanner-338514"
        + self_link                  = (known after apply)

        + access {
            + domain         = (known after apply)
            + group_by_email = (known after apply)
            + role           = (known after apply)
            + special_group  = (known after apply)
            + user_by_email  = (known after apply)

            + view {
                + dataset_id = (known after apply)
                + project_id = (known after apply)
                + table_id   = (known after apply)
                }
            }
        }

    # google_storage_bucket.data-lake-bucket will be created
    + resource "google_storage_bucket" "data-lake-bucket" {
        + force_destroy               = true
        + id                          = (known after apply)
        + location                    = "EUROPE-WEST6"
        + name                        = "dtc_data_lake_snappy-spanner-338514"
        + project                     = (known after apply)
        + self_link                   = (known after apply)
        + storage_class               = "STANDARD"
        + uniform_bucket_level_access = true
        + url                         = (known after apply)

        + lifecycle_rule {
            + action {
                + type = "Delete"
                }

            + condition {
                + age                   = 30
                + matches_storage_class = []
                + with_state            = (known after apply)
                }
            }

        + versioning {
            + enabled = true
            }
        }

    Plan: 2 to add, 0 to change, 0 to destroy.

    ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 

    Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.

---

    (de_zoomcamp) C:\_gitRepos\DE_Zoomcamp\DE_Zoomcamp\week_1\terraform>terraform apply

    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
    + create

    Terraform will perform the following actions:

    # google_bigquery_dataset.dataset will be created
    + resource "google_bigquery_dataset" "dataset" {
        + creation_time              = (known after apply)
        + dataset_id                 = "trips_all_data"
        + delete_contents_on_destroy = false
        + etag                       = (known after apply)
        + id                         = (known after apply)
        + last_modified_time         = (known after apply)
        + location                   = "europe-west6"
        + project                    = "snappy-spanner-338514"
        + self_link                  = (known after apply)

        + access {
            + domain         = (known after apply)
            + group_by_email = (known after apply)
            + role           = (known after apply)
            + special_group  = (known after apply)
            + user_by_email  = (known after apply)

            + view {
                + dataset_id = (known after apply)
                + project_id = (known after apply)
                + table_id   = (known after apply)
                }
            }
        }

    # google_storage_bucket.data-lake-bucket will be created
    + resource "google_storage_bucket" "data-lake-bucket" {
        + force_destroy               = true
        + id                          = (known after apply)
        + location                    = "EUROPE-WEST6"
        + name                        = "dtc_data_lake_snappy-spanner-338514"
        + project                     = (known after apply)
        + self_link                   = (known after apply)
        + storage_class               = "STANDARD"
        + uniform_bucket_level_access = true
        + url                         = (known after apply)

        + lifecycle_rule {
            + action {
                + type = "Delete"
                }

            + condition {
                + age                   = 30
                + matches_storage_class = []
                + with_state            = (known after apply)
                }
            }

        + versioning {
            + enabled = true
            }
        }

    Plan: 2 to add, 0 to change, 0 to destroy.

    Do you want to perform these actions?
    Terraform will perform the actions described above.
    Only 'yes' will be accepted to approve.

    Enter a value: yes

    google_bigquery_dataset.dataset: Creating...
    google_storage_bucket.data-lake-bucket: Creating...
    google_storage_bucket.data-lake-bucket: Creation complete after 1s [id=dtc_data_lake_snappy-spanner-338514]
    google_bigquery_dataset.dataset: Creation complete after 2s [id=projects/snappy-spanner-338514/datasets/trips_all_data]

    Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

## Prepare Postgres (Additional?)

Run Postgres and load data as shown in the videos

We'll use the yellow taxi trips from January 2021:

    wget https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv
You will also need the dataset with zones:

    wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv
Download this data and put it to Postgres

## Question 3. Count records

How many taxi trips were there on January 15?

Consider only trips that started on January 15.

## <u>Answer</u>:
    
    select count(*)
    from yellow_taxi_trips
    where cast(tpep_pickup_datetime as date) = '2021-01-15';

    Result: 53024

## Question 4. Largest tip for each day

Find the largest tip for each day. On which day it was the largest tip in January?

Use the pick up time for your calculations.

(note: it's not a typo, it's "tip", not "trip")


## <u>Answer</u>:

    select tpep_pickup_datetime
    from yellow_taxi_trips
    where tip_amount = (
        select max(tip_amount)
        from yellow_taxi_trips
    );

    Result: "2021-01-20 11:22:05"

## Question 5. Most popular destination

What was the most popular destination for passengers picked up in central park on January 14?

Use the pick up time for your calculations.

Enter the zone name (not id). If the zone name is unknown (missing), write "Unknown".

## <u>Answer</u>:

    select tzl."Zone"
    from yellow_taxi_trips as ytt
        inner join taxi_zone_lookup as tzl
            on ytt."DOLocationID" = tzl."LocationID"
    where ytt.tpep_pickup_datetime >= '2021-01-14' and ytt.tpep_pickup_datetime < '2021-01-15'
    group by tzl."Zone"
    order by count(tzl."Zone") desc
    limit 1

    Result: "Upper East Side North"

## Question 6. Most expensive locations

What's the pickup-dropoff pair with the largest average price for a ride (calculated based on total_amount)?

Enter two zone names separated by a slash

For example:

"Jamaica Bay / Clinton East"

If any of the zone names are unknown (missing), write "Unknown". For example, "Unknown / Clinton East".

## <u>Answer</u>:

    select
        trip
        , avg(total_amount) as trip_average
    from 
    (
        select CONCAT(pick_tzl."Zone", ' / ' , CASE WHEN dest_tzl."Zone" IS NULL THEN 'Unknown' ELSE dest_tzl."Zone" END) as trip
            , ytt."total_amount"
        from yellow_taxi_trips as ytt
            inner join taxi_zone_lookup as dest_tzl
                on ytt."DOLocationID" = dest_tzl."LocationID"
            inner join taxi_zone_lookup as pick_tzl
                on ytt."PULocationID" = pick_tzl."LocationID"
    ) as tmp
    group by trip
    order by trip_average desc
    limit 1

    Result: "Alphabet City / Unknown", 2292.4