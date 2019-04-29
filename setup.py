from setuptools import setup
from setuptools import find_packages

import openpyscad

with open('README.rst', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    requirements = fh.readlines()


setup(
    name=openpyscad.__name__,
    packages=find_packages(exclude=['tests*', 'example*']),
    version=openpyscad.__version__,
    author=openpyscad.__author__,
    author_email=openpyscad.__email__,
    description='Python library to generate OpenSCAD source code',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url=openpyscad.__url__,
    license=openpyscad.__license__,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=requirements,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Code Generators'
    ]
)
