from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'speech_to_goal'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='igor',
    maintainer_email='igoririondo2004@gmail.com',
    description='Speech to Goal Node',
    license='Apache-2.0',

    extras_require={
        'test': ['pytest'],
    },

    entry_points={
        'console_scripts': [
            'speech_to_goal_node = speech_to_goal.speech_to_goal_simple_node:main',
            'speech_to_goal_llm_node = speech_to_goal.speech_to_goal_llm_service:main',
            'speech_to_goal_main_planner_node = speech_to_goal.speech_to_goal_main_planner:main',
            'speech_to_goal_main_planner_node_logs = speech_to_goal.speech_to_goal_main_planner_logs:main',
            'intent_classifier_node = speech_to_goal.intent_detection_llm_service:main',
        ],
    },
)