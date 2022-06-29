#!/usr/bin/env python
# coding: utf-8

import dash
from dash.dependencies import Input, Output
from dash import dash_table, dcc, html
from dash.dash_table.Format import Format
import plotly.express as px

from pathlib import Path
import pandas as pd

# Set up app
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# read in data
# ----------------------------------------------------------------------
# filename = dash.get_asset_url("data/nba_physiques.csv")
filename = Path(__file__).parent / "assets/data/nba_physiques.csv"
df = pd.read_csv(filename, index_col=0, dtype={"Year": "int"})
df = df.assign(bmi=df.weight / ((df.height / 100) ** 2))
df_nba = df[["Year", "height", "weight",
             "bmi", "PER", "PTS", "pos_simple"]].copy()
df_nba = df_nba.assign(height_bins=pd.qcut(df.height, q=4))

# HTML page Layout
# ------------------------------------------------------------------------------
# Page is divided in three parts:
#    * header: at the top, a title
#    * body: the main containt
#    * footer: at the bottom, contact, informations, credits
app.layout = html.Div([
    # ------ header
    html.Div(
        className="header",
        children=[
            html.H2("Stats on NBA players - Dash app example"),
            html.Img(
                src=dash.get_asset_url("img/logo-nba.jpeg"),
                height="100px", style={"float": "right"}
            ),
        ],
    ),

    # ----- body
    html.Div(className="container", children=[
        # a sub title
        html.H3("A plot"),
        # first dropdown selector
        dcc.Dropdown(
            id="x-dropdown",  # identifier
            value="height",  # default value
            # all values in the menu
            options=[{"label": name, "value": name} for name in df_nba.columns],
        ),
        # second dropdown selector
        dcc.Dropdown(
            id="y-dropdown",
            value="weight",
            options=[{"label": name, "value": name} for name in df_nba.columns],
        ),
        # a place for the plot with an id
        html.Div(
            dcc.Graph(id='graph'),
        ),

        # a sub title
        html.H3("A table"),

        # a new dropdown
        dcc.Dropdown(
            id="pivot-dropdown",
            value="height",
            options=[
                {"label": name, "value": name} 
                for name in ["Year", "height", "weight", "bmi", "PER", "PTS"]
            ],
        ),
        # a table for data
        dash_table.DataTable(
            id="pivot-table",
        ),
    ]),

    # ----- footer
    html.Div(
        className="footer",
        children=[
            html.H5("Germain Salvato Vallverdu"),
            html.H5("https://github.com/gVallverdu/dash-nba"),
        ],
    ),
])

# Callback functions
# ----------------------------------------------------------------------
@app.callback(
    Output('graph', 'figure'),
    [Input("x-dropdown", "value"),
     Input("y-dropdown", "value")],
)
def display_graph(xvalue, yvalue):
    """ 
    This function produce the plot.

    The output is the "figure" of the graph
    The inputs, are the values of the two dropdown menus
    """

    figure = px.scatter(
        df_nba,
        x=xvalue, y=yvalue,
        color='pos_simple',
        category_orders=dict(pos_simple=['PG', 'SG', 'SF', 'PF', 'C']),
        marginal_x="histogram",
        marginal_y="histogram",
        template="plotly_white",
    )

    return figure



@app.callback(
    [Output("pivot-table", "data"),
     Output("pivot-table", "columns")],
    [Input("pivot-dropdown", "value")]
)
def show_pivot_table(value):
    """ This function return a pivot Table """

    pivot_df = pd.pivot_table(
        data=df_nba, values=value, columns="pos_simple", index="height_bins"
    )
    pivot_df = pivot_df.reset_index()
    pivot_df = pivot_df.astype({"height_bins": "str"})

    data = pivot_df.to_dict("records")
    cols = [
        {"name": col, "id": col, "type": "numeric", "format": Format(precision=5)} 
        for col in pivot_df.columns
    ]

    return data, cols


if __name__ == '__main__':
    app.run_server(debug=True)
