# coding:utf-8
import base64
from PIL import Image
from api import Api


class Code(object):
    def __init__(self):
        self.index = 0

    def is_has_red(self, r, g, b):
        return r >= 180 and g < 70 and b < 70

    def get_red_index(self, num):
        index_list = []
        for i in range(num):
            image = Image.open('images/{0}.png'.format(i))
            colors = image.getcolors(image.size[0] * image.size[1])
            for count, (r, g, b) in colors:
                if self.is_has_red(r, g, b):
                    index_list.append(i)
                    break
        return index_list

    def save_code_img(self, img_str):
        img_data = base64.b64decode(img_str)
        with open('images/{0}.png'.format(self.index), 'wb') as f:
            f.write(img_data)
            self.index += 1

    def test_save_code(self, count=10):
        api = Api()
        for i in range(count):
            res = api.get_validate_code()
            for img_data in res['data']:
                self.save_code_img(img_data)


if __name__ == '__main__':
    code = Code()
    # code.test_save_code()
    print(code.get_red_index(60))

