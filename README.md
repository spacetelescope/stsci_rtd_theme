# stsci_rtd_theme
STScI branded sphinx theme that inherits from sphinx_rtd_theme

This theme is based off of the sphinx_rtd_theme, from which it inherits, but the CSS styling
has been altered for easier reading on a variety of platforms and browsers.

## Installation
You can apply this theme to your current documents by installing this repository like any other python package:

Either from GIT:
```
git clone https://github.com/spacetelescope/stsci_rtd_theme.git
python setup.py install
```
Or with PIP (furture release on pypi, but you can always pip install from the repo):
```
pip install -e https://github.com/spacetelescope/stsci_rtd_theme.git
```
## Adding to your Sphinx docs
If you haven't already created your Sphinx documentation, you can start sphinx with
`sphinx-quickstart` and follow the guided steps. When you are finished, 
add these lines to your `conf.py` file:
```
import stsci_rtd_theme
html_theme = 'stsci_rtd_theme'
html_theme_path = [stsci_rtd_theme.get_html_theme_path()]
```
![Example theme render](stsci_rtd_theme_example.png)
