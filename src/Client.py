from custom_interface.srv import AddFourFloat
import sys
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):
    def __init__(self):
        super().init('minimal_client_async')
        while not self.cli.wait_for_service(AddFourFloat, 'add_four_float'):
            self.get_logger().info('service not available...')

        self.req = AddFourFloat.Request()

    
    def send_request(self):
        self.req.a = 0.1
        self.req.b = 0.2
        self.req.c = 0.3
        self.req.d = 0.4

        self.future = self.cli.call_async(self.req)



def main(args=None):
    rclpy.init(args=args)
    
    minimal_client = MinimalClientAsync()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(f"service call faild {e}")
            else:
                minimal_client.get_logger().info(f'Result of add_four_float: {minimal_client.req.a} + {minimal_client.req.b} + {minimal_client.req.c} + {minimal_client.req.d} = {response.result}')
            break

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()