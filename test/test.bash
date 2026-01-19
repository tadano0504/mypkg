#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Keito Tadano
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "NG"
    exit 1
}

cd "$(dirname "$0")/../.." || ng

source /opt/ros/humble/setup.bash || ng

mkdir -p ros2_ws/src
rsync -av ./ ros2_ws/src/mypkg > /dev/null

cd ros2_ws || ng
colcon build > /dev/null 2>&1 || ng
source install/setup.bash || ng

timeout 10 ros2 launch mypkg talk_listen.launch.py \
  > /tmp/mypkg.log 2>&1 || true

grep -q "Test Talker Node started" /tmp/mypkg.log || ng
grep -q "Threshold Listener Node started" /tmp/mypkg.log || ng
grep -E "LOW|MID|HIGH" /tmp/mypkg.log || ng

echo "OK"
exit 0

