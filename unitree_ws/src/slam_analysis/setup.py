from setuptools import find_packages, setup

package_name = 'slam_analysis'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tknika',
    maintainer_email='igoririondo2004@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'slam_benchmark = slam_analysis.slam_benchmark:main',
            'slam_benchmark_hex = slam_analysis.slam_benchmark2:main',
        ],
    },
)
