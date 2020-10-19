# utgeo_rtd_theme
UTGEO branded sphinx theme that adapts from stsci_rtd_theme

The stsci_rtd_theme theme itself is based off of the sphinx_rtd_theme, from which it inherits, but the CSS styling
has been altered for easier reading on a variety of platforms and browsers.

## Installation
You can apply this theme to your current documents by installing this repository like any other python package:

clone/copy from GIT:
```
git clone https://github.com/allixender/utgeo_rtd_theme.git
cd utgeo_rtd_theme
python setup.py install
```

## Adding to your Sphinx docs
If you haven't already created your Sphinx documentation, you can start sphinx with
`sphinx-quickstart` and follow the guided steps. When you are finished,
add these lines to your `conf.py` file:
```
import stsci_rtd_theme
html_theme = 'stsci_rtd_theme'
html_theme_path = [stsci_rtd_theme.get_html_theme_path()]

html_logo = '_static/img/TYGI_w_logo_transp.png'
```
![Example theme render](utgeo_rtd_theme_example.png)

## Making this theme work on Readthedocs
