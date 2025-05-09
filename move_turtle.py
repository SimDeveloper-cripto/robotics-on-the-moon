import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleMover(Node):
    def __init__(self):
        super().__init__('turtle_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def move(self):
        msg = Twist()
        msg.linear.x = 2.0   # Forward    velocity
        msg.angular.z = 1.0  # Rotational velocity

        for _ in range(50):
            self.publisher_.publish(msg)
            time.sleep(0.1)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleMover()
    node.move()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()