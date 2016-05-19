__author__ = 'Michael'

from kivy.graphics import Color, Rectangle, Line
from kivy.core.image import Image
from kivy.core.text import Label as CoreLabel


def draw_text(wid, pos_x, pos_y, font_size, text):
    label = CoreLabel(text=text, font_size=font_size)
    label.refresh()
    texture = label.texture
    Color(1, 1, 1)
    Rectangle(pos=(pos_x, pos_y - texture.size[1]/2), size=texture.size)
    Color(0, 0, 0)
    Rectangle(texture=texture, pos=(pos_x, pos_y - texture.size[1]/2), size=texture.size)


def draw_line(wid, pos_x1, pos_y1, pos_x2, pos_y2, width=1.1):
    Color(0, 0, 0)
    Line(points=[wid.x + pos_x1, wid.y + pos_y1, wid.x + pos_x2, wid.y + pos_y2], width=width)


def draw_rect(wid, pos_x, pos_y, width, height):
    Rectangle(pos=(pos_x + wid.x, pos_y + wid.y), size=(width, height))


def draw_rect_border(wid, pos_x, pos_y, width, height):
    draw_line(wid, 0, 0, width, 0)
    draw_line(wid, width, 0, width, height)
    draw_line(wid, width, height, 0, height)
    draw_line(wid, 0, height, 0, 0)
