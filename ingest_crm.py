import argparse
import pandas as pd
import psycopg2
from sqlalchemy import create_engine, schema
from ref.panels import panel
from ref.config import *


def write_df_to_db(table_name,df):
    engine = create_engine(POSTGRES_CONNECTION)
    if not engine.dialect.has_schema(engine, SCHEMA_NAME):
        engine.execute(schema.CreateSchema(SCHEMA_NAME))
    df.to_sql(table_name, engine,schema='dkatalis_crm',if_exists='replace')

def mappingfields(raw_df,fields):
    sheet_fields = [i['column_src'] for i in fields]
    mapping = {i['column_src']: i['column_dst'] for i in fields}
    df = raw_df[sheet_fields].copy()
    df.rename(mapping, axis=1, inplace=True)
    return df

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--object', required=True)
    args = parser.parse_args()
    obj_name = args.object

    conf_args = panel[obj_name]
    filename = conf_args['filename']
    fields = conf_args['fields']

    csv_file = CSV_DIR+filename
    raw_df = pd.read_csv(csv_file)
    df = mappingfields(raw_df,fields)
    if not df.empty:
        write_df_to_db(obj_name,df)


if __name__ == '__main__':
    main()
