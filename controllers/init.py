#!/usr/bin/env python3
from core.controller import Controller


class Init(Controller):

    def run(self, *args):
        # Test model.
        user = self.load_model("user")
        data = user.data()

        # Test view.
        view = self.load_view("init", app="MVC-with-Bottle", data=data)
        return view