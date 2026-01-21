#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Keito Tadano
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    low = LaunchConfiguration("low_threshold")
    high = LaunchConfiguration("high_threshold")

    return LaunchDescription([

        DeclareLaunchArgument(
            "low_threshold",
            default_value="30.0",
            description="LOW / MID boundary"
        ),

        DeclareLaunchArgument(
            "high_threshold",
            default_value="70.0",
            description="MID / HIGH boundary"
        ),

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
            output="screen",
            parameters=[{
                "low_threshold": low,
                "high_threshold": high
            }]

        ),
    ])

