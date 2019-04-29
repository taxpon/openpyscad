from setuptools import setup
from setuptools import find_packages

import openpyscad

with open("README.rst", "r") as fh:
    long_description = fh.read()


setup(
    name=openpyscad.__name__,
    packages=find_packages(exclude=['tests*', 'example*']),
    version=openpyscad.__version__,
    author=openpyscad.__author__,
    author_email=openpyscad.__email__,
    description="Python library to generate OpenSCAD source code",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url=openpyscad.__url__,
    license=openpyscad.__license__,
    install_requires=[
        'six',
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Code Generators"
    ]
)
