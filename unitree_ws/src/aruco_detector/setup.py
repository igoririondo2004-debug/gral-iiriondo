from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'aruco_detector'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),

    data_files=[
        # ROS 2 package index
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        # package.xml
        ('share/' + package_name, ['package.xml']),

        # -------------------------------------------------
        # LAUNCH FILES (all .launch.py automatically)
        # -------------------------------------------------
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),

        # -------------------------------------------------
        # CONFIG FILES (all YAML automatically)
        # -------------------------------------------------
        (os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')),

        # -------------------------------------------------
        # OPTIONAL: EMPTY FOLDER FOR SAVED MAPS
        # (created at runtime, not installed)
        # -------------------------------------------------
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='igor',
    maintainer_email='igoririondo2004@gmail.com',
    description='ArUco marker detection + mapping system',
    license='TODO: License declaration',

    extras_require={
        'test': ['pytest'],
    },

    entry_points={
        'console_scripts': [
            'aruco_detector_node = aruco_detector.aruco_detector_node:main',
            'aruco_mapper_node = aruco_detector.aruco_mapper:main',
        ],
    },
)