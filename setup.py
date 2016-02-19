from setuptools import setup
from setuptools import find_packages

import openpyscad

setup(
    name=openpyscad.__name__,
    packages=find_packages(exclude=['tests*', 'example*']),
    version=openpyscad.__version__,
    author=openpyscad.__author__,
    author_email=openpyscad.__email__,
    description="Python library to generate OpenSCAD source code",
    url=openpyscad.__url__,
    license=openpyscad.__license__,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Code Generators"
    ]
)
