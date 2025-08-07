from custom_interface.srv import AddFourFloat

import rclpy
from rclpy.node import Node

class MinimalService(Node):
    def __init__(self):
        super()._init__('minimal_service')
        self.srv = self.create_service(AddFourFloat, 'add_four_float', self.add_four_float_callback)
    
    def add_four_float_callback(self, request: AddFourFloat.Request,response: AddFourFloat.Response):
        response.result = request.a + request.b + request.c + request.d
        self.get_logger().info(f'Incommit requests...\na: {request.a},b: {request.b},c: {request.c},d:{request.d}')
        return response
    

def main(args=None):
    rclpy.init(args=args)
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

