from datetime import datetime
import json
import glob
import random

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from hoverable import HoverBehavior
from pathlib import Path

Builder.load_file('design.kv')

# LoginScreen same name as in design.kv inherits Screen


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "signup_screen"

    def login(self, uname, pword):
        self.manager.transition.direction = "right"
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            print(users[uname]["username"], users[uname]["password"])
            self.manager.current = "login_screen_success"
        else:
            self.ids.failed_login.text = "Wrong Username or Password,"


# RootBudget same name as in design.kv, inherits Screen Manager
class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)

        users[uname] = {
            'username': uname,
            'password': pword,
            'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        with open("users.json", 'w', encoding='utf8') as file:
            json.dump(users, file, ensure_ascii=False)

        self.manager.current = "signup_screen_success"


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def enlighten(self, mood):
        mood = mood.lower()
        available_mood = glob.glob("quotes/*txt")
        available_mood = [Path(filename).stem for filename in available_mood]

        if mood in available_mood:
            with open(f"quotes/{mood}.txt") as file:
                quotes = file.readlines()
            self.ids.enlight_text.text = random.choice(quotes)
        else:
            self.ids.enlight_text.text = "Try another feeling ..."


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

# Main App inherits App


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
