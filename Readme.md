# Overview

An overview will be provided as soon as possible!

## Build and Run Docker Container

```sh
docker-compose up --build -d
```

```sh
# To stop and re-run the application
docker-compose down
ocker-compose up -d
```

## Get Started

```sh
docker exec -it ros2-turtlesim-vnc bash
source /opt/ros/humble/setup.bash
cd ~
mkdir -p ros2_ws/src
cd ros2_ws/src
ros2 pkg create --build-type ament_python turtle_controller --dependencies rclpy geometry_msgs
cd turtle_controller/turtle_controller
touch turtle_publisher.py
touch turtle_subscriber.py
touch turtle_teleport.py
```

All the codes for the python files are already provided! <br />
Now what you should do is to modify the file: __/ros2_ws/src/turtle_controller/setup.py__ with all of this

```python
from setuptools import find_packages, setup

package_name = 'turtle_controller'
setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/turtle_controller']),
        ('share/turtle_controller', ['package.xml']),
        ('share/turtle_controller/launch', ['launch/turtles_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description=' ',
    license=' ',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'turtle_publisher = turtle_controller.turtle_publisher:main',
                'turtle_subscriber = turtle_controller.turtle_subscriber:main',
                'turtle_teleport = turtle_controller.turtle_teleport: main',
        ],
    },
)
```

Then

```shell
cd ~/ros2_ws/src/turtle_controller
mkdir launch && touch turtles_launch.py
```

```python
# turtles_launch.py
from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():
    return LaunchDescription([
        # Run turtlesim
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),

        # Run il publisher
        Node(
            package='turtle_controller',
            executable='turtle_publisher',
            name='my_publisher'
        ),

        # Run il subscriber
        Node(
            package='turtle_controller',
            executable='turtle_subscriber',
            name='my_subscriber'
        ),

        # Run il teleporter
        Node(
            package='turtle_controller',
            executable='turtle_teleport',
            name='my_teleporter'
        ),
    ])
```

Last thing, modify __/ros2_ws/src/turtle_controller/setup.py__ package.xml inserting this two lines of code

```sh
<exec_depend>launch</exec_depend>
<exec_depend>launch_ros</exec_depend>
```

Now, using a text editor, inside the container you can write move_turtle.py with the example provided! <br />

```sh
cd ros2_ws && colcon build
source install/setup.bash
ros2 launch turtle_controller turtles_launch.py
```

## LICENSE

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

Copyright © 2025 Simone Catapano "SimDeveloper-cripto" <br />
Copyright © 2025 Fabio Barbato <br />
Copyright © 2025 Paolo Cammardella <br />