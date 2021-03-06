docker run -it ^
  -e POSTGRES_USER="root" ^
  -e POSTGRES_PASSWORD="root" ^
  -e POSTGRES_DB="ny_taxi" ^
  -v C:/_gitRepos/DE_Zoomcamp/DE_Zoomcamp/week_1/ny_taxi_postgres_data/:/var/lib/postgresql/data ^
  -p 5432:5432 ^
  --network=pg-network ^
  --name pg-database ^
  postgres:13