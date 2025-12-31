#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Keito Tadano
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Float32

class ActivityMonitorListener(Node):
    def __init__(self):
        super().__init__("activity_monitor_listener")

        self.create_subscription(Int32, "keyboard_count", self.kb_callback, 10)
        self.create_subscription(Int32, "mouse_click_count", self.click_callback, 10)
        self.create_subscription(Float32, "mouse_move_distance", self.move_callback, 10)

        self.get_logger().info("Activity Monitor Listener Node started")

    def kb_callback(self, msg):
        self.get_logger().info(f"Keyboard count: {msg.data}")

    def click_callback(self, msg):
        self.get_logger().info(f"Mouse click count: {msg.data}")

    def move_callback(self, msg):
        self.get_logger().info(f"Mouse move distance: {msg.data:.2f}")

def main():
    rclpy.init()
    node = ActivityMonitorListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()

