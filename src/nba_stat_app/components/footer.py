# coding: utf-8

from dash import html

def footer():
    """ make the page footer """
    return html.Div(
        className="footer",
        children=[
            html.H5("Germain Salvato Vallverdu"),
            html.H5("https://github.com/gVallverdu/dash-nba"),
        ],
    )
