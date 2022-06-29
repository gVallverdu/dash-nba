#coding: utf-8

""" This is the main function to be used as an entry point in order to
run the application. """

import webbrowser
from threading import Timer

from nba_stat_app.app import app

TITLE = r"""
  ___          _      _  _ ___   _   
 |   \ __ _ __| |_   | \| | _ ) /_\  
 | |) / _` (_-< ' \  | .` | _ \/ _ \ 
 |___/\__,_/__/_||_| |_|\_|___/_/ \_\
                                     
 
 Authors: Germain Salvato Vallverdu
 Contact: germain.vallverdu@gmail.com
 """


def main():
    """ Run the app from an entry point defined in setup.cfg
    TODO: need to check port is available and host ?
    """

    print(TITLE)

    # set up the url and a threading Timer
    host = "localhost"
    port = 8080
    folder = "dash-nba"
    url = f"http://{host}:{port}/{folder}/"
    Timer(10, webbrowser.open_new(url))

    # run app
    app.run(
        host=host,
        port=port,
        debug=False
    )
