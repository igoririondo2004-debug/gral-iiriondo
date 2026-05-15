from setuptools import setup
from glob import glob
import os

package_name = 'asr'

setup(
    name=package_name,
    version='0.0.1',

    packages=[package_name],

    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),

        (
            'share/' + package_name,
            ['package.xml']
        ),

        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')
        ),
    ],

    install_requires=['setuptools'],

    zip_safe=True,

    maintainer='you',
    maintainer_email='you@email.com',

    description='ROS2 ASR package',

    license='MIT',

    entry_points={
        'console_scripts': [
            'vosk_node = asr.vosk_node:main',
            'whisper_medium_node = asr.whisper_medium_node:main',
        ],
    },
)