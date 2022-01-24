# Data Engineering Zoomcamp

This repository contains the notes and source code for the Data Engineering Zoomcamp that is hosted by [DataTalks.club](https://datatalks.club/).

## Week 1

Goal for week 1 is to setup a GCP environment, learn basics of Docker, run PostgreSQL in a docker container and execute some queries on the database running in the container

## Prerequisites
You need to setup your own Python anaconda environment and activate it. Alternatively, you can just install Python on your machine, directly, if you don't have it already.

Then, you must install pip, if you don't have it already and run `pip install -r requirements.txt`, that will go over the [requirements.txt](../requirements.txt) file and install all dependencies.

## <u>Docker</u>

Essential steps for building and running a container
- Dockerfile - contains the description of the container and libraries installed inside the container
- `docker build -t test:pandas ./`  - is required to build the image for the container
    - `-t` option stands for: *Name and optionally a tag in the 'name:tag' format*
    - `./` option means that Docker will build an image in this directory
    - -it option would allow running the container with an interactive prompt (ex: `docker run -it test:pandas`) - allows you to see messages, prints, logs, bash command line etc, depending on the specification of `ENTRYPOINT`
    - the `test` parameter specifies the REPOSITORY for the container image and the `pandas` parameter specifies the TAG for a container image (check: `docker image list` in cmd) -> you can create multiple images in the same repository, with different tags

        ![](./imgs/docker_image_list.PNG)

- `docker run -it test:pandas 2022-01-12` - is an example of a docker command that can be executed to run the container and also pass it a set of arguments for execution

- `docker container prune` - from time to time, it might be a good idea to run this command to remove all stopped containers, since every execution of `docker run` will cause a NEW container to be initialized

## <u>Ingesting data into PostgreSQL in Docker container</u>
- docker compose is a way to run multiple Docker images
- running a container with PostgreSQL is as simple as running the command in [`docker_run_cmd.txt`](./docker_run_cmd.txt)
- connecting to the PostgreSQL database can be done through a cmd line <span style="color:orange">**pgcli**</span> and through a similar command: `pgcli -h localhost -p 5432 -u root -d ny_taxi`
- we will ingest data for NYC Yellow Taxi rides from [NYC.gov](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) website and download [this .CSV file](https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv)
- the dataset has a [Data Dictionary](https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf), explaining what each column means and what type of data is stored
- taxi rides in the main dataset refer to a pick-up and drop-off location, which is replaced with an ID. The main table with lookup values for pick-up and drop-off can be [downloaded from here](https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv)
- for a detailed process of ingesting the data into the PostgreSQL database, have a look at the [<span style="color:yellow">test_notebook.ipynb</span>](test_notebook.ipynb) file