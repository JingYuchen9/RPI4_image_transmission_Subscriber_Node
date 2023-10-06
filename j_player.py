import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2
import numpy as np

class Subscribe_bytes_data(Node):
    def __init__(self):
        super().__init__('byte_subscriber')
        self.subscription = self.create_subscription(
            CompressedImage,
            'byte_data_topic',  # 订阅'my_topic'话题
            self.message_callback,
            10  # 队列大小
        )
        self.cv_bridge = CvBridge()
        self.subscription  # 防止Python回收subscription对象

    def message_callback(self, data):
        print("callback has been called!")
        # 在这里处理接收到的bytes数据
        image = self.cv_bridge.compressed_imgmsg_to_cv2(data,'bgr8')
        #byte_data = image.tobytes()
        #decoding = cv2.imdecode(np.frombuffer(image,np.uint8), cv2.IMREAD_COLOR)
        #print("decoding type = ", type(decoding))
        if not image is None:#and not image.empty():

            cv2.imshow('show image', image)
            cv2.waitKey(1)
        else:
            print("image 无法播放")


def main(args=None):
    rclpy.init(args=args)
    node = Subscribe_bytes_data()
    rclpy.spin(node)
    node.destory_node()
    rclpy.shutdown()
    cv2.destoryAllWindows()

if __name__ == '__main__':
    main()
