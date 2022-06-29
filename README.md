# dash-nba

This repository contains a [Dash app](https://dash.plotly.com) example 
that aims to provide a minimal working example of a Dash application and 
implement a command line to run the application. The aim is to provide
this command line automatically by using an entry point which implement
the command line at the installation of the python module.

Finally, the structure of the package is general enough to cover the
following use cases:

* deployment on a web service (such as heroku)
* run the application locally after cloning the repository
* install the package from a package manager or a GUI and run it using a command line

The example in the `main` branch is not really minimal in a sense that it 
tries to provide a structured project and include typical files you may 
find in a real app with `assets`.

The `min` branch tries to minimize the number of file and removed the
structure of the app in folder and subfolders trying to keep something
really simple.

## Motivation

One of the main benefit of this approach is to distribute a dash application
that can be run locally without too much technical operations made by the
end user. By installing the corresponding python package the dash application
can be run from anywhere using a simple command line.

For example, it can be the case of users that do not have any skills 
using neither a terminal, nor git and python. In such a case, using anaconda,
the installation can be done only using a GUI. The process is the following: 

1. Install anaconda
2. Launch `anconda-navigator`. This can be done from the start menu of many OS.
3. From the Environment tab of `anconda-navigator`, create a new environment
   by importing the provided `environment.yml` file
4. From the new environment, open a terminal and enter the defined command line
   that run the application.

Later, to run the application, the end user has to follow only steps 2 and 4,
from any path of its computer. There is no need to change to the directory of
the source code or give the path of the source code.

Obviously, it is still possible for more advanced users to clone the repository
and install the package by themselves in their python environment.

## Some bibliography

I first give here some general reading, although some points are explained
below.

Concerning the structure of the project and the structure of a python
project in general, you may want to read the
[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
page on the official python documentation.

Concerning the deployment of a Dash application on heroku, 
[this article](https://austinlasseter.medium.com/how-to-deploy-a-simple-plotly-dash-app-to-heroku-622a2216eb73)
on medium may certainly help you step by step. There is also this
[page on the official Dash documentation](https://dash.plotly.com/deployment).

## Common files

Some files are common to both `min` and `main` branches of the application.
They are mandatory for the deployment or the installation and part of them
does not depend on the structure of the project.

If you intend to deploy the application on a web server such as heroku
for example, the `requirements.txt` and `setup.py` files are one of the 
mandatory files that allow heroku to identify your repository as a python 
project.

* **`pyproject.toml`**: This file is used to build the project.
* **`environment.yml`**: This file is used to set up a complete working
  environment using `conda` which finally install the application which
  can be run from a command line.
* **`requirements.txt`**: This file lists the required python modules to
  run or install the application.
* **`setup.py`**: This file is used to install the python modules and the
  application.

One *key point* here, is that `requirements.txt` and `environment.yml` must
include the installation of the current package. That guaranties that the
modules will be installed and the command line implemented.

The `Procfile` and `setup.cfg` files are not exactly the same on both `min`
and `main` branches as their content depend on the structure tree of the
files of the project.

* **`Procfile`**: This file define the path to the server to be run.
* **`setup.cfg`**: This file provides the configuration of the installation.
  In particular, it defines the function to be executed as an entry point
  from which a script is implemented and linked to a command. This command
  allows the application to be run from the command line. See the Entry point
  section below.

The `MANIFEST.in` file *is crucial* to be sure that files which are not
python source code files will be installed. In the particular case of the
dash application, it is important for css files and for example pictures or
data you want to include in the application. These files must be listed
in the `MANIFEST.in` file. The [check-manifest](https://pypi.org/project/check-manifest/)
project may help to write this file without forgiven any file.

## Entry point

In order to automatically implement during the pacakge installation a command 
line that runs the application we will use the `entry_points` options of the
`setuptools`. You first have to
write a function that runs the application. In this repository, this function
is in the `run_app.py` file. It uses the `webbrowser` module, from the python standard
library to open the default browser and reach the url of the running dash
application. You can personalize the port and url.

This function (here the `main()` function in `run_app.py`)
will be the one called by the command line. Moreover, python needs to be
able to import this function, so the module file must be installed in the 
environment.

Then, you have to define the entry point in the `setup.cfg` file as follow:

```conf
[options.entry_points]
console_scripts=
    run_app = nba_stat_app.run_app:main
```

Here, `run_app` will be the name of the command line implemented by
`setuptools`. You can defined it as you whish.
You may see that we look for the `run_app` module as a submodule of the
`nba_stat_app` and then we call the `main()` function.

Actually, `setuptools` produce the following script in the `bin/` folder
of the python environment where you installed the package:

```py
#!/Users/toto/opt/miniconda3/envs/dashmwe/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from nba_stat_app.run_app import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
```

You can see how it imports the `main()` function from the 
`nba_stat_app.run_app` module of this package.

## `min` branch version


## `main` branch version

Hereafter are the specific configuration implemented in some files.

### src-layout structure

In the `main` branch, the repository is structured with all source files
in the `src/` folder. 

The package contains two modules in the `src/` folder:

* `nba_stat_app` which contains the app and the function to run it.
* `nba_stat_data` which contains the package functionality.

These two package could be independent, the `nba_stat_data` providing
a library on a given subject and the `nba_stat_app` implementing the
dash application. Nevertheless, the `nba_stat_app` relies on the
`nba_stat_data`. You can look at the example notebook in order to see
that the `nba_stat_data` can be used independently without the app.


```
.
├── LICENSE
├── MANIFEST.in
├── Procfile
├── README.md
├── environment.yml
├── pyproject.toml
├── requirements.txt
├── setup.cfg
├── setup.py
└── src
    ├── nba_stat_app
    │   ├── __init__.py
    │   ├── app.py
    │   ├── run_app.py
    │   ├── assets/
    │   └──  components/
    └── nba_stat_data
        ├── __init__.py
        ├── nba_data.py
        └── nba_physiques.csv
```

### setup configuration

As a consequence, in the `setup.cfg` file, you have to specify the
folder where it is necessary to look for the python files:

```conf
[options]
package_dir =
    =src
packages = find:
include_package_data = True

[options.packages.find]
where=src
```

The key `include_package_data` is set to `True` in order to include non
python files as defined in the `MANIFEST.in` file.

### Procfile

In the `Procfile` you have to change the path and pass to gunicorn
the server variable of the Dash application. Here is the contains
of this file:

```
web: gunicorn --chdir ./src/nba_stat_app app:server
```