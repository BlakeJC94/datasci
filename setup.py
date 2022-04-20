"""Setup script.

Install package:
    $ pip install -e .

Requirements can be updated using `pip-compile`:
    $ pip install pip-tools
    $ pip-compile
"""
# TODO: change name of datasci
# TODO: update requirements
from setuptools import setup, find_packages

setup(
    name="datasci",
    version="0.0.0",
    description='Python package template for data science and algorithms',
    author="BlakeJC94",
    url="https://github.com/BlakeJC94/datasci",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=[
        'fire',
        'numpy',
        'pandas',
        'tqdm',
    ],
    entry_points={
        'console_scripts': ['datasci=datasci.__main__:main'],
    },
)

