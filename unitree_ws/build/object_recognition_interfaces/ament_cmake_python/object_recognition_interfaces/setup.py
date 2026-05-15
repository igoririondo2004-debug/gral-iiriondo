from setuptools import find_packages
from setuptools import setup

setup(
    name='object_recognition_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('object_recognition_interfaces', 'object_recognition_interfaces.*')),
)
