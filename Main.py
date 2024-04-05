from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivyuix.label import Label
from database import DataBase

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text !="" and self.email.text.count("@") ==1 and self.email.text.count(".")>0:
            if self.password !="":
                db.add_user(self.mail.text, self.password.text, self.namee.text)
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
                else:
                    invalidFom()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.name.text = ""

    class LoginWindow(Screen):
        email = ObjectProperty(None)
        password = ObjectProperty(None)

        def loginBtn(self):
            if db.validate(self.email.text, self.password.text):
                MainWindow.current = self.email.text
                self.reset()
                sm.current = "main"
            else:
                invalidLogin()

        def createBtn(self):
            self.reset()
            sm.current = "create"

        def reset(self):
            self.email.text = ""
            self.password.text = ""

        class MainWindow(Screen):
            n = ObjectProperty(None)
            created = ObjectProperty(None)
            email = ObjectProperty(None)
        current = ""

        def LogOut(self):
            sm.current = "login"

        def on_enter(self, *args):
            password, name, created = db.get_user(self.current)
            self.n.text = "Acount Name: " + name
            self.email.text = "Email: " + self.current
            self.created.text = "Created On: " + created

        class WindowManager(ScreenManager):
            pass

    def invalidLogin():
        pop = Popup(title = 'Invalid Login',
                    content = Label(text = 'Invalid username or password.'),
                    size_hint = (None, None), size = (400, 400))
        pop.open()

    def invalidForm():
        pop = Popup(title = 'Invalid Form',
                    content = Label(text = 'Please fill in all inputs with valid information.')
                    size_hint = (None, None), size=(400, 400))
        pop.open()

    