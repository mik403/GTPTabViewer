from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle, Line
from kivy.core.image import Image
from functools import partial
from kivy.core.text import Label as CoreLabel

import guitarpro
import CoreDrawTools as Drawer

class MusicTextures:
    def __init__(self):
        self.logo = Image('mylogo.png').texture


class TabViewerApp(App):

    def init_resources(self):
        self.img = MusicTextures()
        self.string_step = 0.15
        self.curl = guitarpro.parse('nirvana-smells_like_teen_spirit.gp3')

    def draw_frame(self, wid, *largs):
        wid.canvas.clear()
        self.draw_background(wid)
        self.draw_tab(wid)

    def draw_background(self, wid):
        with wid.canvas:
            Color(1, 1, 1)
            Drawer.draw_rect(wid, 0, 0, wid.width, wid.height)

    def draw_measure(self, wid, pos_x, pos_y, width, height, beats):

        with wid.canvas:

            Color(0, 0, 0)
            Drawer.draw_rect_border(wid, pos_x, pos_y, width, height)

            string_step = 1/5.
            for i in range(1, 6):
                pos_y_per = i*string_step
                print(pos_y_per)
                Drawer.draw_line(wid, pos_x,  pos_y + height*pos_y_per, pos_x + width, pos_y + height*pos_y_per)

            # all notes should be aligned with some empty space from both side
            empty_space = 20
            pos_x += empty_space
            width -= empty_space

            beat_number = 0.
            for beat in beats:
                beat_pos_x = pos_x + width *(beat_number/len(beats))
                for note in beat.notes:
                    beat_pos_y = string_step * (note.string-2)
                    font_size = 20
                    Drawer.draw_text(wid=wid, pos_x=beat_pos_x, pos_y=pos_y+height*beat_pos_y + font_size/4, font_size=font_size,
                                   text="%d" % note.value)
                beat_number += 1.

    def draw_tab(self, wid):
        track = self.curl.tracks[0]

        key_width = 10

        self.draw_measure(wid, 0, 0, wid.width/2, wid.height/2,track.measures[0].voices[0].beats)
        self.draw_measure(wid, wid.width/2, 0, wid.width/2, wid.height/2, track.measures[1].voices[0].beats)

    def build(self):
        wid = Widget()
        label = Label(text='0')

        btn_add100 = Button(text='run',
                            on_press=partial(self.draw_frame, wid))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_add100)
        layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        self.init_resources()

        return root

if __name__ == '__main__':
    TabViewerApp().run()