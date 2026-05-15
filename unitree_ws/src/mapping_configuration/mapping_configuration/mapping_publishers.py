import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool, String


class MappingPublishers(Node):

    def __init__(self):
        super().__init__('mapping_publishers')

        self.enable_pub = self.create_publisher(
            Bool,
            '/mapping/enable',
            10
        )

        self.save_map_pub = self.create_publisher(
            String,
            '/mapping/save_map',
            10
        )

        self.load_map_pub = self.create_publisher(
            String,
            '/mapping/load_map',
            10
        )

        self.get_logger().info('Mapping publishers ready')

    def publish_enable(self, value: bool):
        msg = Bool()
        msg.data = value
        self.enable_pub.publish(msg)

    def publish_save_map(self, name: str):
        msg = String()
        msg.data = name
        self.save_map_pub.publish(msg)

    def publish_load_map(self, name: str):
        msg = String()
        msg.data = name
        self.load_map_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = MappingPublishers()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()