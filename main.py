import argparse
from typing import Optional

import numpy
from PIL import Image

from for_img import ForImg

_inImg = 'test.png'
_outImg = 'test_end.png'
_endWord = "lemon"


def mes_to_bit(message):
    ret = ''
    for i in message:
        ret += format(ord(i), "08b")
    return ret


def bit_to_mes(bit):
    ret = []
    for byte in bit:
        char = chr(int((''.join(byte)), 2))
        ret.append(char)
    return ''.join(ret)


def encode_message(message):
    img = ForImg(_inImg)
    bit_mes = mes_to_bit(message + _endWord)
    if len(bit_mes) > img.pixel_number:
        print('error')
        return
    img.swap_img_data(bit_mes)
    enc_img = Image.fromarray(img.pixels.astype('uint8'), img.img.mode)
    enc_img.save(_outImg)
    print('message be encoding')


def decode_message():
    img = ForImg(_outImg)
    message = img.get_bit_mes()
    message = bit_to_mes([message[i:i + 8] for i in range(0, len(message), 8)])
    print('message be decoding:', message.split(_endWord)[0])


def main():
    message = "haha"
    encode_message(message)
    decode_message()


if __name__ == '__main__':
    main()
