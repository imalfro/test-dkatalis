import argparse
import pandas as pd
import plotly.express as px
import dash
from dash import dcc 
from dash import html
from dash.dependencies import Input, Output
from ref.panels import panel
from ref.config import *

app = dash.Dash()

def dash_visualization(df):
    fig1 = px.box(df, x="duration_years", y="interest_rate")
    fig2 = px.scatter(df, x="funded_date", y="interest_rate")
    fig3 = px.histogram(df, x="employment_length_group", color="tax_class_at_time_of_sale", category_orders=dict(employment_length_group=["<5", "5-10", "10-15", ">15"]))

    app.layout = html.Div([
        html.H1('DASHBOARD'),

        html.Div(children='''
            Interest rate and loan analysis based on employement length group
        '''),
        
        dcc.Graph(
            id='fig1graph',
            figure=fig1
        ),

        dcc.Graph(
            id='fig2graph',
            figure=fig2
        ),

        dcc.Graph(
            id='fig3graph',
            figure=fig3
        )
    ])
    app.run_server(port=4050)

def employment_length_group(row):
    if row['employment_length'] <= 5:
        return '<5'
    elif row['employment_length'] > 5 and row['employment_length'] <= 10:
        return '5-10'
    elif row['employment_length'] >= 10 and row['employment_length'] < 15:
        return '10-15'
    else:
        return '>15'

def data_cleaning(df):
    df.drop(df[(df['funded_amount'] >20000000)].index, inplace = True)
    df['employment_length_group'] = df.apply(employment_length_group, axis=1) 
    return df

def mapping_fields(raw_df,fields):
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
    raw_df = mapping_fields(raw_df,fields)
    df = data_cleaning(raw_df)
    if not df.empty:
        dash_visualization(df)


if __name__ == '__main__':
    main()
