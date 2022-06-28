# coding: utf-8

import dash
from dash import html

def header():
    """ make the header page """
    return html.Div(
        className="header",
        children=[
            html.H2("Stats on NBA players - Dash app example"),
            html.Img(
                src=dash.get_asset_url("img/logo-nba.jpeg"),
                width="10%",
                style={"float": "right"}
            ),
        ],
    )
