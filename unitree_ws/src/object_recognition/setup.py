from setuptools import setup

package_name = 'object_recognition'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='igor',
    maintainer_email='igor@todo.todo',
    description='Object recognition package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'object_recognition_yolo_node = object_recognition.recognition_service_yolo:main',
            'object_recognition_vit_node = object_recognition.recognition_service_vit:main',
            'object_recognition_yolo_cls_node = object_recognition.recognition_service_yolo_cls:main',

        ],
    },
)