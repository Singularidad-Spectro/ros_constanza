import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init_('subscriber')

        self.subscription = self.create_subscription(String, 'topic',  self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        # print(msg.data)
        # self.get_logger().info('I heard: "%s"' % msg.data)
        
    def main(args=None):
        rclpy.init(args=args)
        subscriber = Subscriber()
        rclpy.spin(subscriber)
        subscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()