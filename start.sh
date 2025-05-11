#!/bin/bash

set -e

Xvfb :1 -screen 0 1024x768x16 &
export DISPLAY=:1
sleep 2

fluxbox &
sleep 1

x11vnc -display :1 -nopw -forever -shared &
sleep 2

ros2 run turtlesim turtlesim_node &
sleep 2

websockify --web=/opt/novnc 8080 localhost:5900

# TODO
# Understand how the python files cooperate one other
# Create a GRID MAP
# Add obstacles
# Apply A* or RRT*