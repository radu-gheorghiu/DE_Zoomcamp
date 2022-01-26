docker run -it ^
    --network=pg-network ^
    taxi_ingest_zones:v001 ^
    --user=root ^
    --password=root ^
    --host=pg-database ^
    --port=5432 ^
    --database=ny_taxi ^
    --table=taxi_zone_lookup ^
    --csv_url="https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"