#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Keito Tadano
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Float32
from pynput import keyboard, mouse
import math

class ActivityMonitorNode(Node):
    def __init__(self):
        super().__init__("activity_monitor")

        self.kb_pub = self.create_publisher(Int32, "keyboard_count", 10)
        self.click_pub = self.create_publisher(Int32, "mouse_click_count", 10)
        self.move_pub = self.create_publisher(Float32, "mouse_move_distance", 10)

        self.kb_count = 0
        self.click_count = 0
        self.prev_pos = None
        self.move_distance = 0.0

        self.kb_listener = keyboard.Listener(on_press=self.on_key_press)
        self.mouse_listener = mouse.Listener(on_click=self.on_click, on_move=self.on_move)
        self.kb_listener.start()
        self.mouse_listener.start()

        self.create_timer(1.0, self.publish_counts)

        self.get_logger().info("Activity Monitor Node started")

    def on_key_press(self, key):
        self.kb_count += 1

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.click_count += 1

    def on_move(self, x, y):
        if self.prev_pos is not None:
            dx = x - self.prev_pos[0]
            dy = y - self.prev_pos[1]
            self.move_distance += math.hypot(dx, dy)
        self.prev_pos = (x, y)

    def publish_counts(self):
        kb_msg = Int32()
        kb_msg.data = self.kb_count
        self.kb_pub.publish(kb_msg)
        self.kb_count = 0

        click_msg = Int32()
        click_msg.data = self.click_count
        self.click_pub.publish(click_msg)
        self.click_count = 0

        move_msg = Float32()
        move_msg.data = float(self.move_distance)
        self.move_pub.publish(move_msg)
        self.move_distance = 0.0

def main():
    rclpy.init()
    node = ActivityMonitorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()

