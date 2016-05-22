__author__ = 'Michael'

from kivy.graphics import Color, Rectangle, Line

import guitarpro
import core_draw_tool as Drawer


class TabDrawer:
    def set_tab(self, source):
        self.string_step = 0.15
        self.curl = guitarpro.parse(source)

    def draw_background(self, wid):
        with wid.canvas:
            Color(1, 1, 1)
            Drawer.draw_rect(wid, 0, 0, wid.width, wid.height)

    def draw_measure(self, wid, pos_x, pos_y, width, height, beats):
        with wid.canvas:

            Color(0, 0, 0)
            Drawer.draw_rect_border(wid, pos_x, pos_y, width, height)

            string_step = 1 / 5.
            for i in range(1, 6):
                pos_y_per = i * string_step
                print(pos_y_per)
                Drawer.draw_line(wid, pos_x, pos_y + height * pos_y_per, pos_x + width, pos_y + height * pos_y_per)

            # all notes should be aligned with some empty space from both side
            empty_space = 20
            pos_x += empty_space
            width -= empty_space

            beat_number = 0.
            for beat in beats:
                beat_pos_x = pos_x + width * (beat_number / len(beats))
                for note in beat.notes:
                    beat_pos_y = string_step * (note.string - 2)
                    font_size = 20
                    Drawer.draw_text(wid=wid, pos_x=beat_pos_x, pos_y=pos_y + height * beat_pos_y + font_size / 4,
                                     font_size=font_size,
                                     text="%d" % note.value)
                beat_number += 1.

    def draw_tab(self, wid):
        track = self.curl.tracks[0]

        self.draw_measure(wid, 0, 0, wid.width / 2, wid.height / 2, track.measures[0].voices[0].beats)
        self.draw_measure(wid, wid.width / 2, 0, wid.width / 2, wid.height / 2, track.measures[1].voices[0].beats)
