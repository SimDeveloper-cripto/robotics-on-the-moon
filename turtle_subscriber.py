import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtleSubscriber(Node):
    def __init__(self):
        super().__init__('turtle_subscriber')
        self.subscription = self.create_subscription(
            Pose, 'turtle1/pose', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'\033[94m[SUBSCRIBER] Pose - x: {msg.x:.2f}, y: {msg.y:.2f}, theta: {msg.theta:.2f}\033[0m')

def main(args=None):
    rclpy.init(args=args)

    node = TurtleSubscriber()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()