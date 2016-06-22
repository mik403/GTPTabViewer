from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.clock import Clock
from functools import partial
from tab_drawer import TabDrawer
import WebFileLoader

class TabViewerApp(App):

    def init_resources(self):
        #self.tab_name = 'nirvana-smells_like_teen_spirit.gp3'
        self.tab_name = WebFileLoader.download_tab(self)
        print(self.tab_name)
        self.tab_drawer = TabDrawer()
        self.tab_drawer.set_tab(self.tab_name)
        self.page_number=0

        self.update_labels()



    def update_labels(self):
        self.tab_name_label.text = self.tab_name
        self.page_label.text = str(self.page_number)

    def draw_frame(self, *largs):
        self.canvas_widget.canvas.clear()
        self.tab_drawer.draw_background(self.canvas_widget)
        self.tab_drawer.draw_tab(self.canvas_widget, self.page_number)

    def change_page(self, value, *largs):
        new_value = self.page_number + value
        if(new_value >= 0):
            self.page_number=new_value
            self.update_labels()
            self.draw_frame()

    def build(self):
        self.canvas_widget = Widget()
        self.page_label = Label(text='')
        self.tab_name_label = Label(text='')

        btn_prev_page = Button(text='<|',
                            on_press=partial(self.change_page, -1))

        btn_next_page = Button(text='|>',
                            on_press=partial(self.change_page, 1))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(self.tab_name_label)
        layout.add_widget(btn_prev_page)
        layout.add_widget(btn_next_page)
        layout.add_widget(self.page_label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(self.canvas_widget)
        root.add_widget(layout)

        self.init_resources()
        Clock.schedule_interval(self.draw_frame, 1.0 / 60.0)

        return root

if __name__ == '__main__':
    TabViewerApp().run()