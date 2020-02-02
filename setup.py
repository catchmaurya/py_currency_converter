import os.path

from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="py_currency_converter",
    version="1.0.0",
    author="Maurya Allimuthu",
    author_email="catchmaurya@gmail.com",
    description="Python Currency Converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/catchmaurya/py_currency_converter",
    packages=find_packages(),
    # scripts=['pyawslog.py', '__init__.py'],
    install_requires=['requests>=2.22.0'],
    classifiers=[

        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
