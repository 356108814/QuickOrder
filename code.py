# coding:utf-8
import base64
import os
from PIL import Image
from api import Api
import config


class Code(object):
    def __init__(self, api):
        self.index = 0
        self.api = api
    
    def is_has_red(self, r, g, b):
        return r >= 180 and g < 70 and b < 70
    
    def get_red_index(self, order_no, num):
        index_list = []
        order_img_dir = config.base_image_dir + '/' + order_no
        for i in range(num):
            image = Image.open(order_img_dir + '/{0}.png'.format(i))
            colors = image.getcolors(image.size[0] * image.size[1])
            for count, (r, g, b) in colors:
                if self.is_has_red(r, g, b):
                    index_list.append(str(i))
                    break
        return index_list
    
    def save_code_img(self, img_str):
        img_data = base64.b64decode(img_str)
        with open('images/{0}.png'.format(self.index), 'wb') as f:
            f.write(img_data)
            self.index += 1
    
    def save_code_img_by_order_no(self, order_no):
        res = self.api.get_validate_code()
        images = res['data']
        order_img_dir = config.base_image_dir + '/' + order_no
        if not os.path.exists(order_img_dir):
            os.mkdir(order_img_dir)
        for i in range(0, len(images)):
            img_data = base64.b64decode(images[i])
            with open(order_img_dir + '/{0}.png'.format(i), 'wb') as f:
                f.write(img_data)
        return res['code_id'], len(images)
    
    def get_validate_code(self, order_no):
        code_id, num = self.save_code_img_by_order_no(order_no)
        red_indexes = self.get_red_index(order_no, num)
        return {'code_id': code_id, 'code_value': ''.join(red_indexes)}
    
    def test_save_code(self, count=10):
        api = Api()
        for i in range(count):
            res = api.get_validate_code()
            for img_data in res['data']:
                self.save_code_img(img_data)


if __name__ == '__main__':
    code = Code(Api())

