# MVC-with-Bottle.

*MVC-with-Bottle* is a web microframework based on the Model-View-Controller design pattern and built on top of the <a href="https://bottlepy.org" target="_blank">Bottle</a> library.

<img src="https://img.shields.io/badge/Python-3.5-blue" />

## Developer.

* Edgard Decena, edecena@gmail.com

## Requirements.

*MVC-with-Bottle* does not require the installation of any external library. The *Bottle* library is already included in the framework itself, in the `core/libs` folder.

## Use:

1. The `core` folder contains the implementation of the framework's abstract classes: `controller.py` and `model.py`, from which the controllers and models respectively of any project will inherit.

2. The `views`, `controllers` and `models` folders will contain the particular views, controllers and models for any given project.

3. The url pattern is `http://localhost:8080/ctler/p1/p2/p3/...` where `ctler` is the controller to be requested, and `p1`, `p2`, `p3` ... are the parameters to be received by that controller.

4. The `config.json` file contains the configuration parameters of the `Bottle` object, as well as the name of a Sqlite database to be stored in the `data` folder.

## Contributions.

Feel free to contribute to this project if you wish, by reporting [issues](https://github.com/ejdecena/ml_covid19_Oluwaseye/issues) or proposing improvements through pull-requests. Thank you.