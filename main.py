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
        self.string_step = 0.1
        self.curl = guitarpro.parse('nirvana-smells_like_teen_spirit.gp3')

    def draw_frame(self, wid, *largs):
        wid.canvas.clear()
        self.draw_background(wid)
        self.draw_tab(wid)

    def draw_background(self, wid):
        with wid.canvas:
            Color(1, 1, 1)
            Drawer.draw_rect(wid, 0, 0, wid.width, wid.height)

            self.draw_measure(wid, 0, 0, wid.width, wid.height)

    def draw_measure(self, wid, pos_x, pos_y, width, height):
        with wid.canvas:
            pos_y_per = 0.1
            Color(1, 1, 1)
            Drawer.draw_rect_border(wid, pos_x, pos_y, width, height)

            for i in range(1, 7):
                pos_y_per += self.string_step
                Drawer.draw_line(wid, pos_x,  pos_y + height*pos_y_per, pos_x + width, pos_y + height*pos_y_per)


    def draw_tab(self, wid):
        with wid.canvas:
            measure = self.curl.tracks[0].measures[0]
            voice = measure.voices[0]
            beat_number = 0.
            for beat in voice.beats:
                pos_x = wid.x + wid.width *(beat_number/len(voice.beats))
                beat_number += 1.
                for note in beat.notes:
                    pos_y = self.string_step * ( 8 - note.string)
                    Drawer.draw_text(wid=wid, pos_x=pos_x, pos_y=wid.height*pos_y + wid.y, font_size=20,
                                   text="%d" % note.value)

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