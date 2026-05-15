from glob import glob
from setuptools import find_packages, setup

package_name = 'standing_mode'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/script', glob('script/*.py')),  # <--- ADD THIS
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bee',
    maintainer_email='juan9eche@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'standing_mode = standing_mode.standing_mode:main',
        ],
    },
)
