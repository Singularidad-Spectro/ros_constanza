import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Publisher(Node):

    def _init_(self):
        super()._init_('publisher')
        self.publisher = self.create_publisher(String, 'topic', 10)

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.i = 0

    def timer_callback(self):

        msg = String()

        msg.data = 'Hola Constanza: %d' % self.i 

        self.publisher.publish(msg)
        self.get_loggger().info('Publishing: "%s"' % msg.data)

        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()