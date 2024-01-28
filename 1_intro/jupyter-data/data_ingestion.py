import pandas as pd
import sqlalchemy
import psycopg2
from time import time
from sqlalchemy import create_engine
import sys
import argparse
import os 


def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    url = params.url
    table = params.table_name
    source_file = 'result.csv'
    look_up_file = 'taxi_zone_lookup.csv'
    url_lookup = 'https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv'

    # url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
    # engine = create_engine(f'postgresql://{admin}:{admin}@postgres:{5432}/{ny_taxi}')

    os.system(f"wget {url} -O {source_file}")
    os.system(f"wget {url_lookup} -O {look_up_file}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    df_iter = pd.read_csv(f'{source_file}', compression='gzip', iterator=True, chunksize=100000)
    df = next(df_iter)
    df.head(0).to_sql(name=f'{table}', con=engine, if_exists='replace')
    while True:
        try:
            t_start = time()
            df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
            df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])
            df.to_sql(name=f'{table}', con=engine, if_exists='append')
            t_end = time()
            print(f'inserted next chunk..., it took : {t_end-t_start}')
            df = next(df_iter)
        except StopIteration:
            print("All chunks processed.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        
    try:
        lookup = pd.read_csv(f'{look_up_file}')
        lookup.to_sql(name="taxi_lookup", con=engine, if_exists='replace')
    except Exception as e:
        print(f"An error occured: {e}")

    print(f'!!! Job succeefully finished!!!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Ingest CSV data to Postgresql')
    parser.add_argument('--user', help="user for name for postgres")
    parser.add_argument('--password', help="password postgres db")
    parser.add_argument('--host', help="host for postgres db")
    parser.add_argument('--port', help="port for postgres db")
    parser.add_argument('--db', help="database name in postgres db")
    parser.add_argument('--table_name', help="name of table in postgres")
    parser.add_argument('--url', help="user for name for postgres")
    
    args = parser.parse_args()

    main(args)