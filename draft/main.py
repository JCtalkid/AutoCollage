from collections import namedtuple
from dataclasses import dataclass
import math
from pathlib import Path

from PIL import Image


SizeBox = namedtuple("SizeBox", ["wight", "height"])


class BasicFrame:
    def __init__(self, height, wight):
        self.size = SizeBox(wight=wight, height=height)
        self.amount = self.size.wight * self.size.height

        self.ratio = SizeBox(wight=self.size.wight / math.gcd(*self.size),
                             height=self.size.height / math.gcd(*self.size))

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount


class ImgReprObj(BasicFrame):
    def __init__(self,
                 img_path: str,
                 height: int = 0,
                 wight: int = 0):
        self.path = path
        super().__init__(height=height, wight=wight)

    def convert_filetype(self, type_to: str):
        pass


class SubFrame:
    @dataclass
    class _Indent:
        left: int
        down: int
        up: int
        right: int

        def __call__(self) -> tuple:
            return self.left, self.down, self.up, self.right

    def __init__(self, img: ImgReprObj, ind):
        self.indent = self._Indent(ind, ind, ind, ind)
        self.img = img
        size = SizeBox(height=img.size.height + self.indent.up + self.indent.down,
                       wight=img.size.wight + self.indent.left + self.indent.right)


class Layout(BasicFrame):
    def __init__(self, height=1, wight=1):
        super().__init__(height=height, wight=wight)


def img_pasta(img1: Image, img2: Image) -> tuple:
    return tuple(sum(i) for i in zip(img1.size, img2.size))


if __name__ == '__main__':
    path = r'E:\Pic\Meme_source'
    name = ['BlueChair (9).webp', 'BlueChair (10).webp']

    im1 = Image.open(Path(path, name[0]))
    im2 = Image.open(Path(path, name[1]))

    back_im = Image.new('RGB', (im1.size[0], im1.size[1]+im2.size[1]))
    back_im.paste(im1)
    back_im.paste(im2, (0, back_im.size[1]//2))
    back_im.save(Path(path, 'BlueChair_collage.webp'), quality=95)

    im1.close()
    im2.close()
