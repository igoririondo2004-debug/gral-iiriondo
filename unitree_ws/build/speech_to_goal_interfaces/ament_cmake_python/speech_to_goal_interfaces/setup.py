from setuptools import find_packages
from setuptools import setup

setup(
    name='speech_to_goal_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('speech_to_goal_interfaces', 'speech_to_goal_interfaces.*')),
)
