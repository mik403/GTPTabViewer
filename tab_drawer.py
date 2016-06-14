__author__ = 'Michael'

from kivy.graphics import Color
from kivy.core.image import Image

import guitarpro
import core_draw_tool as Drawer

class MusicTextures:
    def __init__(self):
        self.background_measure = Image('background_measure.png').texture


class TabDrawer:
    def __init__(self):
        self.img = MusicTextures()

    def set_tab(self, source):
        self.string_step = 1 / 5.
        self.curl = guitarpro.parse(source)
        self.count_ver = 2
        self.count_hor = 3

    def draw_background(self, wid):
        with wid.canvas:
            Color(1, 1, 1)
            Drawer.draw_rect(wid, 0, 0, wid.width, wid.height)

    def draw_measure(self, wid, pos_x, pos_y, width, height, beats):
        with wid.canvas:

            Color(1, 1, 1)

            texture_pos_y = pos_y + height
            Drawer.draw_texture(wid, self.img.background_measure, pos_x, texture_pos_y, width, height)

            # all notes should be aligned with some empty space from both side
            empty_space = 20
            pos_x += empty_space
            width -= empty_space

            beat_number = 0.
            for beat in beats:
                beat_pos_x = pos_x + width * (beat_number / len(beats))
                for note in beat.notes:
                    beat_pos_y = self.string_step * (note.string-3)
                    font_size = 20
                    Drawer.draw_text(wid=wid, pos_x=beat_pos_x, pos_y=pos_y + height * beat_pos_y + font_size,
                                     font_size=font_size,
                                     text="%d" % note.value)
                beat_number += 1.

    # measure position and count to draw
    def draw_tab(self, wid, page_number):
        track = self.curl.tracks[0]
        curr_measure = page_number * (self.count_ver * self.count_hor)
        measure_width = wid.width / (self.count_hor+1)
        measure_height = wid.height / (self.count_ver+1)

        empty_space_ver = measure_height*0.1
        empty_space_hor = measure_width*0.2
        curr_padding_ver = 0

        for ver_i in range(0, self.count_ver):
            curr_padding_ver += empty_space_ver
            for hor_i in range(0, self.count_hor):
                self.draw_measure(wid, hor_i*measure_width + empty_space_hor, ver_i*measure_height + curr_padding_ver,
                                  measure_width, measure_height, track.measures[curr_measure].voices[0].beats)
                curr_measure += 1
