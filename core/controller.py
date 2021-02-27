#!/usr/bin/env python3
import os
import abc
import importlib
from core.exceptions.controllerexception import ControllerException
from core.libs.bottle import template


class Controller(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def run(self, *args):
        pass

    def load_model(self, model):
        mdl = model.lower()
        try:
            model = importlib.import_module("models.{}".format(mdl))
        except ImportError:
            raise ControllerException("{}: El módulo del modelo \"{}\" no "
                                "existe.".format(self.__class__.__name__, mdl))
        try:
            model = getattr(model, mdl.title())
        except AttributeError:
            raise ControllerException("{}: La clase \"{}\" del modelo no "
                        "existe.".format(self.__class__.__name__, mdl.title()))
        return model()

    def load_view(self, view, **args):
        try:
            with open("views{}{}.html".format(os.sep, view.lower())) as fview:
                view = fview.read()
        except FileNotFoundError:
            raise ControllerException("{}: La vista \"{}\" no existe."\
                                .format(self.__class__.__name__, view.lower()))
        return template(view, **args)