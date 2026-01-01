#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Keito Tadano
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class LoadListener(Node):
    def __init__(self):
        super().__init__("load_listener")
        self.create_subscription(Float32, "cpu_load", self.load_callback, 10)
        self.get_logger().info("Load Listener Node started")

    def load_callback(self, msg):
        self.get_logger().info(f"Current CPU load (1min avg): {msg.data:.2f}")

def main():
    rclpy.init()
    node = LoadListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()

