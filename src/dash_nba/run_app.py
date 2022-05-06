#coding: utf-8

import webbrowser
from threading import Timer
from pathlib import Path

from icp_ms_map.app import app

TITLE = """
  ___ ____ ____       __  __ ____        __  __    _    ____  
 |_ _/ ___|  _ \     |  \/  / ___|      |  \/  |  / \  |  _ \ 
  | | |   | |_) |____| |\/| \___ \ _____| |\/| | / _ \ | |_) |
  | | |___|  __/_____| |  | |___) |_____| |  | |/ ___ \|  __/ 
 |___\____|_|        |_|  |_|____/      |_|  |_/_/   \_\_|   
 
 Authors: G. Salvato Vallverdu, B. Bouyssière, S. Mounicou
 Contact: germain.vallverdu@univ-pau.fr

 IPREM - UMR CNRS 5254
 
 """

def main():
    """ Run the app from an entry point 
    TODO: need to check port is available and host ?
    """

    print(TITLE)

    # set up the url and a threading Timer
    host = "localhost"
    port = 8080
    folder = "icp-ms-map"
    url = f"http://{host}:{port}/{folder}/"
    Timer(10, webbrowser.open_new(url))

    # get back the location of the assets folder
    assets_folder = Path(app.__file__).parent / "assets"
    app.app.assets_folder = assets_folder

    # run app
    app.app.run_server(
        host=host,
        port=port,
        debug=False
    )