import pandas as pd
from time import time
from sqlalchemy import create_engine
import argparse
import os

parser = argparse.ArgumentParser(description='Ingest CSV data to PostgreSQL')

# user, password, host, port, database, table, csv url

def main(params):

    if params.user is None:
        user = 'root'
        password = 'root'
        host = 'localhost'
        port = 5432
        database = 'ny_taxi'
        table_name = 'yellow_taxi_trips'
        csv_url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv'
    else:
        user = params.user
        password = params.password
        host = params.host
        port = params.port
        database = params.database
        table_name = params.table
        csv_url = params.csv_url

    csv_name = './data/output.csv'

    print('CWD', os.getcwd())
    print('LISTDIR:', os.listdir())

    print('Downloading dataset')
    df = pd.read_csv(csv_url)

    # Make sure to use index=False because pandas automatically adds an additional INDEX column
    print('Saving temp dataset to data folder')
    df.to_csv(csv_name, index=False)

    print('Connecting to Postgresql')
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    engine.connect()
    
    print('Changing datatypes for Timestamp columns')
    df = df.astype({
        'tpep_pickup_datetime': 'datetime64'
        , 'tpep_dropoff_datetime': 'datetime64'
    })

    print(pd.io.sql.get_schema(df, name=table_name, con=engine))

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=50000)

    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')

    print('INGESTING Data!')
    while True:
        
        try:
            t0 = time()
            df_tmp = next(df_iter)

            df_tmp = df_tmp.astype({
                'tpep_pickup_datetime': 'datetime64'
                , 'tpep_dropoff_datetime': 'datetime64'
            })

            df_tmp.to_sql(name=table_name, con=engine, if_exists='append')
            
            tx = time()
        
            print('Inserted chunk, iteration took %.3f seconds' % (tx - t0))
        except StopIteration:
            print('Finished adding rows - no more rows to be added')
            break


if __name__ == '__main__':
    parser.add_argument('--user', help='username for database')
    parser.add_argument('--password', help='password for database')
    parser.add_argument('--host', help='host for database')
    parser.add_argument('--port', help='port for database')
    parser.add_argument('--database', help='target database')
    parser.add_argument('--table', help='target table')
    parser.add_argument('--csv_url', help='data source URL')

    args = parser.parse_args()

    main(args)