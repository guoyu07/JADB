#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: marco@cruncher.ch -*-
# -*- source: https://github.com/mbi/django-simple-captcha -*-

import os
import random
from cStringIO import StringIO
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from django.contrib.staticfiles.finders import find


def _getsize(font, text):
    return [x + y for x, y in zip(font.getsize(text), font.getoffset(text))]


def generate_image(text):
    font = ImageFont.truetype(find(os.path.join('fonts', 'Vera.ttf')), 22)

    size = _getsize(font, text)
    size = (size[0] * 2, int(size[1] * 1.4))

    image = Image.new('RGB', size, '#ffffff')

    xpos = 2

    for char in text:
        char = ' %s ' % char
        fgimage = Image.new('RGB', size, '#001100')
        charimage = Image.new('L', _getsize(font, char), '#000000')
        chardraw = ImageDraw.Draw(charimage)
        chardraw.text((0, 0), char, font=font, fill='#ffffff')

        charimage = charimage.rotate(random.randrange(-35, 35), resample=Image.BICUBIC)
        charimage = charimage.crop(charimage.getbbox())
        maskimage = Image.new('L', size)

        maskimage.paste(charimage, (xpos, 4, xpos + charimage.size[0], 4 + charimage.size[1]))
        size = maskimage.size
        image = Image.composite(fgimage, image, maskimage)
        xpos = xpos + 2 + charimage.size[0]

    image = image.crop((0, 0, xpos + 1, size[1]))
    draw = ImageDraw.Draw(image)

    # noise_arcs
    draw.arc([-20, -20, image.size[0], 20], 0, 295, fill='#001100')
    draw.line([-20, 20, image.size[0] + 20, image.size[1] - 20], fill='#001100')
    draw.line([-20, 0, image.size[0] + 20, image.size[1]], fill='#001100')

    # noise_dots
    for p in range(int(image.size[0] * image.size[1] * 0.1)):
        draw.point((random.randint(0, image.size[0]), random.randint(0, image.size[1])), fill='#001100')

    # post_smooth
    image = image.filter(ImageFilter.SMOOTH)

    out = StringIO()
    image.save(out, 'JPEG')
    out.seek(0)

    return out
