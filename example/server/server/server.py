import rclpy
import rclpy.node

from asebaros_msgs.msg import Event

class Master(rclpy.node.Node):

    def __init__(self):
        super().__init__('robomaster')

        self.get_logger().info('[robomaster] started')

        # Create data publisher
        self.publisher = self.create_publisher(
            Event,
            '/node_51214/aseba/events/control',
            10)

        # Create data subscriber
        def foo(msg):
            self.perception = msg.data

        self.subscription = self.create_subscription(
            Event,
            '/node_51214/aseba/events/perception',
            foo,
            10)

        # Set a periodic control event
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Computing')

        self.get_logger().info(f'Perception: {self.perception}')

        # Make the robot turn whenever it perceives an obstacle
        msg = Event()
        if any([v > 1000 for v in self.perception[0:5]]):
            msg.data = [100, -100]
        else:
            msg.data = [100, 100]

        self.get_logger().info(f'Control: {msg.data}')

        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = Master()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
