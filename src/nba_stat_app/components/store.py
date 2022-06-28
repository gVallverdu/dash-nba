# coding: utf-8

""" This module implement a `dcc.Store` component in which the data are
stored and extracted from it in others callback. """

from dash import dcc, callback
from dash.dependencies import Input, Output

from nba_stat_data import df_nba


def store_layout():
    """ Make a layout with a store component """
    return dcc.Store(id="data-storage")


@callback(
    Output("data-storage", "data"),
    Input("data-storage", "modified_timestamp")
)
def set_storage(ts):
    """ fill in the store component with the data frame. Using the
    timestamp as input is implemented to fill in the Store at startup. 
    """
    return df_nba.to_dict("records")
