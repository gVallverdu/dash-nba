# dash-nba

This repository contains a [Dash app](https://dash.plotly.com) example 
that aims to provide a minimal working example of a Dash application with 
a command line entry point from which the application can be launched.

The example is not really minimal in a sense that it tries to provide 
a structured project and include typical files you may find in a real
app with `assets`.

This repository includes the followings:
* `nba_data` is a python module with function that can be used in the app 
  or elsewhere (in a notebook for example).
* the `app` folder contains everything about the dash application
* the `app/assets` folder contains files needed by the application. These file
  need to be included in the distribution using `MANIFEST.in`


