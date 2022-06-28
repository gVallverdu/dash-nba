# coding: utf-8

from dash import html, dcc, callback, dash_table
from dash.dash_table.Format import Format
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

import pandas as pd
from nba_stat_data import nba_pivot_table


def table_layout():
    """ Produce the layout for a dash table and a dropdown """

    layout = html.Div([
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
        dash_table.DataTable(id="pivot-table")
    ])

    return layout


@callback(
    [Output("pivot-table", "data"),
     Output("pivot-table", "columns")],
    [Input("pivot-dropdown", "value"),
     # this one is to trigger the callback after the store is filled
     Input("data-storage", "modified_timestamp")],
    State("data-storage", "data")
)
def show_pivot_table(value, ts, data):
    """ This function return a pivot Table in a dash_table component """

    if data is None:
        raise PreventUpdate

    df = pd.DataFrame(data)
    pivot_df = nba_pivot_table(df, value)
    data = pivot_df.to_dict("records")
    cols = [{
        "name": col,
        "id": col,
        "type": "numeric",
        "format": Format(precision=5)
    } for col in pivot_df.columns]

    return data, cols
