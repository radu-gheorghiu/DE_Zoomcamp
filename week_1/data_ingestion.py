import pandas as pd
from time import time
from sqlalchemy import create_engine
import argparse

parser = argparse.ArgumentParser(description='Ingest CSV data to PostgreSQL')

# user, password, host, port, database, table, csv url

def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database = params.database
    table_name = params.table
    csv_url = params.csv_url

    csv_name = './data/output.csv'

    print('Downloading dataset')
    df = pd.read_csv(csv_url)

    print('Saving temp dataset to data folder')
    df.to_csv(csv_name)

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    engine.connect()

    df = df.astype({
        'tpep_pickup_datetime': 'datetime64'
        , 'tpep_dropoff_datetime': 'datetime64'
    })

    print(pd.io.sql.get_schema(df, name=table_name, con=engine))

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=50000)

    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')

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