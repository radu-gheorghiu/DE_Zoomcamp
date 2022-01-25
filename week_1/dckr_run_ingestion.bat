docker run taxi_ingest:v001 ^
    --user=root ^
    --password=root ^
    --host=localhost ^
    --port=5432 ^
    --database=ny_taxi ^
    --table=yellow_taxi_trips ^
    --csv_url="https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv"