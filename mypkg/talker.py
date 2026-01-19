#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Keito Tadano
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TestTalker(Node):
    def __init__(self):
        super().__init__("test_talker")
        self.publisher = self.create_publisher(Float32, "input_value", 10)
        self.create_timer(1.0, self.publish_value)
        self.get_logger().info("Test Talker Node started")

    def publish_value(self):
        msg = Float32()
        msg.data = random.uniform(0.0, 100.0)
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = TestTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()

