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
cd /turtle_controller/turtle_controller && touch move_turtle.py
```

Now what you should do is to modify the file: __/ros2_ws/src/turtle_controller/setup.py__ inserting

```python
entry_point: 'move_turtle = turtle_controller.move_turtle:main', <br />
```

Now, using a text editor, inside the container you can write move_turtle.py with the example provided! <br />

```sh
cd ros2_ws && colcon build
source install/setup.bash
ros2 run turtle_controller move_turtle
```

## LICENSE

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

Copyright © 2025 Simone Catapano "SimDeveloper-cripto" <br />
Copyright © 2025 Fabio Barbato <br />
Copyright © 2025 Paolo Cammardella <br />