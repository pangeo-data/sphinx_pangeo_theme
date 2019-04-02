# -*- coding: utf-8 -*-
"""`sphinx_pangeo_theme` lives on `Github`_.

.. _github: https://github.com/rtfd/sphinx_pangeo_theme

"""
from io import open
from setuptools import setup
from sphinx_pangeo_theme import __version__


setup(
    name='sphinx_pangeo_theme',
    version=__version__,
    url='https://github.com/pangeo-data/sphinx_pangeo_theme/',
    license='MIT',
    author='Ryan Abernathey',
    author_email='rpa@ldeo.columbia.edu',
    description='Pangeo theme for Sphinx',
    long_description=open('README.rst', encoding='utf-8').read(),
    zip_safe=False,
    packages=['sphinx_pangeo_theme'],
    package_data={'sphinx_pangeo_theme': [
        'theme.conf',
        '*.html',
        'static/*.css',
        'static/*.otf'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_pangeo_theme = sphinx_pangeo_theme',
        ]
    },
    install_requires=[
       'sphinx'
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
