# coding: utf-8

""" The components module gather all the part of the application and
provides a function that returns the app layout """

from dash import html

from .footer import footer
from .header import header

from .store import store_layout
from .table import table_layout
from .plot import plot_layout


def make_layout(df):
    """ gather the whole app layout from the different parts in the 
    submodule """
    return html.Div([
        # a store components
        store_layout(),

        # -- header --
        header(),

        # -- body --
        html.Div(className="container", children=[
            plot_layout(df),
            table_layout(),
        ]),

        # -- footer --
        footer()
    ])
