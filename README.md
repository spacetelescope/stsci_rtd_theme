# `stsci-rtd-theme`

This is a Sphinx theme for packages maintained by the Space Telescope Sciences Institute (STScI).

![Example](stsci_rtd_theme_example.png)

This theme inherits from `sphinx-rtd-theme`; however, the CSS styling has been altered for easier reading on a variety
of platforms and browsers.

## Installation

You can apply this theme to your current documents by installing the latest release from PyPI:

```shell
pip install stsci-rtd-theme
```

If you need the most up-to-date version of the `master` branch, you can install directly from GitHub:

```shell
pip install https://github.com/spacetelescope/stsci_rtd_theme.git
```

If you wish to modify the source code, you should clone the repository locally and install editable (`-e`):

```shell
git clone https://github.com/spacetelescope/stsci_rtd_theme.git
cd stsci_rtd_theme
pip install -e .
```

### Sphinx configuration

If you haven't already created your Sphinx documentation, you can start sphinx with
`sphinx-quickstart` and follow the guided steps. When you are finished, add these lines to your `docs/conf.py` file:

```python
# docs/conf.py

import stsci_rtd_theme

html_theme = 'stsci_rtd_theme'
html_theme_path = [stsci_rtd_theme.get_html_theme_path()]
```

### ReadTheDocs configuration

Add the following lines to your `docs/conf.py` file:

```python
# docs/conf.py

import sphinx
import os
from packaging.version import Version


def setup(app):
    app.add_css_file("stsci.css")


extensions = [
    ...
]

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    extensions.append('sphinx.ext.mathjax')
elif Version(sphinx.__version__) < Version('1.4'):
    extensions.append('sphinx.ext.pngmath')
else:
    extensions.append('sphinx.ext.imgmath')
```

Finally, make sure to include `stsci-rtd-theme` to the `docs` extra, or alternatively add `stsci-rtd-theme` to
a `rtd-requirements.txt` file. Then, in `.readthedocs.yaml`, include the following (depending on which of the two methods
are used to define the `stsci-rtd-theme` dependency):

```yaml
# .readthedocs.yaml
install:
  - method: pip
    path: .
    extra_requirements:
      - docs
```

```yaml
# .readthedocs.yaml
install:
  - requirements: .rtd-requirements.txt
  - method: pip
    path: .
```