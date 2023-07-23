import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Sim_pub(Node):
    def __init__(self):
        super().__init__('simple_mypub')
        self.pub = self.create_publisher(String, 'message', 10)
        self.create_timer(1, self.publisher)

    def publisher(self):
        msg = String()
        msg.data = 'Hellow'
        self.pub.publish(msg)
        

def main():
    rclpy.init()
    node = Sim_pub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Keyboard Interrupt!!')    
    finally:
        node.destroy_node
        rclpy.shutdown()
    
if __name__ == '__main__':
    main()