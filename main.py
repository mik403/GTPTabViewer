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
        self.page_number=0

    def draw_frame(self, *largs):
        self.canvas_widget.canvas.clear()
        self.tab_drawer.draw_background(self.canvas_widget)
        self.tab_drawer.draw_tab(self.canvas_widget, self.page_number)

    def change_page(self, value, *largs):
        new_value = self.page_number + value
        if(new_value >= 0):
            self.page_number=new_value
            self.label.text = str(new_value)
            self.draw_frame()

    def build(self):
        self.canvas_widget = Widget()
        self.label = Label(text='0')

        btn_run = Button(text='run',
                            on_press=partial(self.draw_frame))

        btn_prev_page = Button(text='<|',
                            on_press=partial(self.change_page, -1))

        btn_next_page = Button(text='|>',
                            on_press=partial(self.change_page, 1))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_run)
        layout.add_widget(btn_prev_page)
        layout.add_widget(btn_next_page)
        layout.add_widget(self.label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(self.canvas_widget)
        root.add_widget(layout)

        self.init_resources()

        return root

if __name__ == '__main__':
    TabViewerApp().run()