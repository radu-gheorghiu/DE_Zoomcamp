# Data Engineering Zoomcamp

This repository contains the notes and source code for the Data Engineering Zoomcamp that is hosted by [DataTalks.club](https://datatalks.club/).

## Week 1

Goal for week 1 is to setup a GCP environment, learn basics of Docker, run PostgreSQL in a docker container and execute some queries on the database running in the container

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