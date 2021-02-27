#!/usr/bin/env python3
from core.controller import Controller

class Sum(Controller):

    def run(self, n1="", n2="", *args):
        n2 = 0 if not n2.strip() else int(n2)
        n1 = 0 if not n1.strip() else int(n1)
        sum  = int(n1) + int(n2)
        view = self.load_view("sum", n1=n1, n2=n2, sum=sum)
        return view