import numpy
from PIL import Image


class ForImg:

    def __init__(self, path):
        self.img = Image.open(path, 'r')
        self.width = self.img.width
        self.height = self.img.height
        self.pixels = numpy.array(list(self.img.getdata()))
        self.pixel_number, self.channels_number = self.pixels.shape

    def swap_img_data(self, bit_mes):
        self.add_bit_mes(bit_mes)
        self.pixels = self.pixels.reshape((self.height, self.width, self.channels_number))

    def add_bit_mes(self, bit_mes):
        index = 0
        for i, pixel in enumerate(self.pixels):
            for j, channel_value in enumerate(pixel):
                if index < len(bit_mes):
                    channel_value = format(channel_value, '08b')
                    new_channel_value = (int(channel_value[:-1] + bit_mes[index], 2))
                    self.pixels[i][j] = new_channel_value
                    index += 1
                else:
                    return

    def get_bit_mes(self):
        ret=list()
        for pixel in self.pixels:
            for channel_value in pixel:
                binary_channel_value = format(channel_value, '08b')
                encoded_bit = binary_channel_value[-1]
                ret.append(encoded_bit)
        return ret
