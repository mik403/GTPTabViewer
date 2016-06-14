from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from functools import partial
from tab_drawer import TabDrawer

class TabViewerApp(App):

    def init_resources(self):
        self.tab_drawer = TabDrawer()
        self.tab_drawer.set_tab('nirvana-smells_like_teen_spirit.gp3')

    def draw_frame(self, wid, *largs):
        wid.canvas.clear()
        self.tab_drawer.draw_background(wid)
        self.tab_drawer.draw_tab(wid)

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