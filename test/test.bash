#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Keito Tadano
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "NG"
    exit 1
}

cd /root/ros2_ws || ng
colcon build > /dev/null 2>&1 || ng

source /opt/ros/humble/setup.bash
source install/setup.bash

timeout 10 ros2 launch mypkg talk_listen.launch.py \
  > /tmp/mypkg.log 2>&1 || true

grep -q "Load Talker Node started" /tmp/mypkg.log || ng
grep -q "Listener" /tmp/mypkg.log || ng

echo "OK"
exit 0

