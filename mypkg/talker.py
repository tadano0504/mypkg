#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Keito Tadano
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import os

class LoadTalker(Node):
    def __init__(self):
        super().__init__("load_talker")
        self.load_pub = self.create_publisher(Float32, "cpu_load", 10)
        self.create_timer(1.0, self.publish_load)  # 1秒ごとに送信
        self.get_logger().info("Load Talker Node started")

    def publish_load(self):
        load_1min = os.getloadavg()[0]  # 1分平均の負荷
        msg = Float32()
        msg.data = float(load_1min)
        self.load_pub.publish(msg)

def main():
    rclpy.init()
    node = LoadTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()

