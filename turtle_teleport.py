import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute

class TurtleTeleporter(Node):
    def __init__(self):
        super().__init__('turtle_teleporter')
        self.cli = self.create_client(TeleportAbsolute, 'turtle1/teleport_absolute')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('\033[93m[TELEPORTER] Waiting for teleport service...\033[0m')

        self.timer = self.create_timer(10.0, self.teleport)

    def teleport(self):
        req = TeleportAbsolute.Request()
        req.x = 5.5
        req.y = 5.5
        req.theta = 0.0
        self.get_logger().info('\033[93m[TELEPORTER] Teleporting turtle to (5.5, 5.5)\033[0m')
        self.cli.call_async(req)

def main(args=None):
    rclpy.init(args=args)

    node = TurtleTeleporter()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()