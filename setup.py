"""Package definition"""
from setuptools import find_packages, setup

setup(
    name='spark-playground',
    packages=find_packages(),
    install_requires=open('requirements.txt', 'r').read().splitlines(),
)
