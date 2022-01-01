from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty

class Widgets():
    button = MDRectangleFlatButton(
        text = "quote",
        valign = 'bottom',
        theme_text_color = "custom",
        text_color = "1, 0, 0, 1" , 
        line_color = "0, 0, 1, 1", 
        on_press = app.aw.check_net(),
    )

class AcessWeb():
    def check_net():
        UrlRequest('https://quoteli.herokuapp.com', on_sucess=self.net_success, on_failure=self.net_failure)
    def net_success(self, req, r):
        dict = r
        quote = dict['quoteText']
        author = dict['quoteAuthor']

class MainApp(MDApp):
    aw = AcessWeb()
    wg = Widgets()
    def build(self):
        quote = MDLabel(text = aw.quote, halign = 'center')
        author = MDLabel(text = aw.author, halign = 'bottom')
        button = wg.button()
        return quote, author, button

MainApp().run() 
