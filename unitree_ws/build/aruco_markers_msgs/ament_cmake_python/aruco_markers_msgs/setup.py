from setuptools import find_packages
from setuptools import setup

setup(
    name='aruco_markers_msgs',
    version='0.0.3',
    packages=find_packages(
        include=('aruco_markers_msgs', 'aruco_markers_msgs.*')),
)
