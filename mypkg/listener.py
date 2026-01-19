#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Keito Tadano
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class ThresholdListener(Node):
    def __init__(self):
        super().__init__("threshold_listener")

        self.sub = self.create_subscription(
            Float32,
            "input_value",
            self.callback,
            10
        )

        self.pub = self.create_publisher(
            String,
            "judge_result",
            10
        )

        self.get_logger().info("Threshold Listener Node started")

    def callback(self, msg):
        value = msg.data

        if value < 30.0:
            result = "LOW"
        elif value < 70.0:
            result = "MID"
        else:
            result = "HIGH"

        out = String()
        out.data = result
        self.pub.publish(out)

        self.get_logger().info(f"value={value:.2f} -> {result}")

def main():
    rclpy.init()
    node = ThresholdListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()

