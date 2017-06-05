import os
from setuptools import setup

setup(
    name='stsci_rtd_theme',
    version='0.0.1',
    author='STScI',
    author_email='help@stsci.edu',
    description='STScI Branded Sphinx theme',
    zip_safe=False,
    packages=['stsci_rtd_theme'],
    package_data={'stsci_rtd_theme': [
                 'theme.conf',
                 'static/*',
                 '*.html'
    ]},
    include_package_data=True,
    url='https://github.com/spacetelescope/stsci_rtd_theme/',
    license='BSD',
    entry_points={
        'sphinx_themes': [
            'path = stsci_rtd_theme:get_html_theme_path',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    install_requires=('sphinx>=1.3', ),
)
