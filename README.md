# Python In Practice

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/CodeSolid/CodeSolid.github.io/HEAD)

Python in Practice is the companion documentation and runnable code site to [CodeSolid.com](https://codesolid.com). 

To use the source here, it's recommended to run this in a virtual environment.  For example, the following creates the virtual environment and runs

```
python3 -m venv .venv
source .venv/bin/activate  # Windows users substitute .venv/scripts/activate.bat
pip install -r requirements.txt
jupyter lab booksource
```

With the virtual environment active, you may prefer to use the Makefile, e.g.:

```
# Start
make lab

# Shut down
make labkill
```

To see the JupyterBook version, visit [CodeSolid.github.io](https://CodeSolid.github.io). This site is written using [JupyterBook](https://jupyterbook.org/). To learn more about how it was created, see the article, [My Journey to Beautiful Documentation With JupyterBook](https://codesolid.com/beautiful-documentation-with-jupyterbook/)