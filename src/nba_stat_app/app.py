#!/usr/bin/env python
# coding: utf-8

import dash

from components import make_layout
from nba_stat_data import df_nba

# Set up app
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# HTML page Layout
app.layout = make_layout(df_nba)

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')
