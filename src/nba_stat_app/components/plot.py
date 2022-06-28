# coding: utf-8

from dash import html, dcc, callback
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

import pandas as pd
from nba_stat_data import nba_scatter


def plot_layout(df):
    """ Set up a layout with a plot from two column of a data frame 

    Args:
        df (DataFrame): The dataframe from which plots are produced

    """
    layout = html.Div([
        # a sub title
        html.H3("A scatter plot"),
        # first dropdown selector
        dcc.Dropdown(
            id="x-dropdown",
            value="height",
            # all values in the menu
            options=[{"label": name, "value": name} for name in df.columns],
        ),

        # second dropdown selector
        dcc.Dropdown(
            id="y-dropdown",
            value="weight",
            options=[{"label": name, "value": name} for name in df.columns],
        ),

        # a place for the plot with an id
        html.Div(dcc.Graph(id='graph')),
    ])

    return layout


@callback(
    Output('graph', 'figure'),
    [Input("x-dropdown", "value"),
     Input("y-dropdown", "value"),
     # this one is to trigger the callback after the store is filled
     Input("data-storage", "modified_timestamp")],
    State("data-storage", "data")
)
def display_graph(xvalue, yvalue, ts, data):
    """ 
    This function produce the plot.

    The output is the "figure" of the graph
    The inputs, are the values of the two dropdown menus
    """
    if data is None:
        raise PreventUpdate

    df = pd.DataFrame(data)

    return nba_scatter(df, xvalue, yvalue)
