#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Keito Tadano
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="mypkg",
            executable="talker",
            name="test_talker",
            output="screen"
        ),
        Node(
            package="mypkg",
            executable="listener",
            name="threshold_listener",
            output="screen"
        ),
    ])

