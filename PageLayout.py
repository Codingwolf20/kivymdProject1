# import kivymd
# from kivymd.app import MDApp
# # from kivymd.lang import MDBuilder
# # from kivymd.uix.button import MDButton

# # from kivy.uix.gridlayout  import MDGridLayout
# # from kivy.uix.floatlayout  import MDFloatLayout
# # # from kivy.core.window import Window
# # from kivy.uix.pagelayout import MDPageLayout
# class MyPageLayout(PageLayout):

#     pass 
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.uix.pagelayout import PageLayout

class MYPageLayout(PageLayout):
    pass
class PageLayout(MDApp):
    def build(self):
        Window.size=[300,600]
        return MYPageLayout()
if __name__=="__main__":
    
   PageLayout().run()



    # def __init__(self,*args,**kwargs):
    #     super(MyPageLayout,self).__init__()

    #     btn1=Button(text="btn1")
    #     btn2=Button(text="btn2")
    #     btn3=Button(text="btn3")
    #     btn4=Button(text="btn4")
    #     btn5=Button(text="btn5")

    #     self.add_widget(btn1)
    #     self.add_widget(btn2)
    #     self.add_widget(btn3)
    #     self.add_widget(btn4)
    #     self.add_widget(btn5)
        


# class PageLayout(MDApp):
#     def build(self):
#         # Window.size=[300,600]
#         return MyPageLayout()


# if __name__=="__main__":
#     PageLayout().run()
            