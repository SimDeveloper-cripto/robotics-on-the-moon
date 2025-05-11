import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtlePublisher(Node):
    def __init__(self):
        super().__init__('turtle_publisher')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_turtle)
        self.count = 0

    def move_turtle(self):
        msg = Twist()
        if self.count % 2 == 0:
            # Forward
            msg.linear.x  = 2.0
            msg.angular.z = 0.0
            self.get_logger().info('\033[92m[PUBLISHER] Moving forward\033[0m')
        else:
            # Rotate
            msg.linear.x = 0.0
            msg.angular.z = 1.57  # ~90 gradi
            self.get_logger().info('\033[92m[PUBLISHER] Rotating left\033[0m')

        self.publisher_.publish(msg)
        self.count += 1
        if self.count > 8:  # After completing the square
            self.count = 0

def main(args=None):
    rclpy.init(args=args)

    node = TurtlePublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()