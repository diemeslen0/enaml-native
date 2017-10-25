# enaml-native
Build native mobile apps in python using enaml and native widgets! [![Build Status](https://travis-ci.org/codelv/enaml-native.svg?branch=master)](https://travis-ci.org/codelv/enaml-native) [![codecov](https://codecov.io/gh/codelv/enaml-native/branch/master/graph/badge.svg)](https://codecov.io/gh/codelv/enaml-native)


[![Python Playground](https://img.youtube.com/vi/2IfRrqOWGPA/0.jpg)](https://youtu.be/2IfRrqOWGPA)

The goal of this project is to be an alternative to using [kivy](https://kivy.org/) for building mobile apps with python. 

I made this because wanted to have a more "React Native" like environment that: 
1. Uses python 
2. Uses native widgets (Android / iOS)
3. Can be run from Android Studio / XCode (ie no bootstraps)
4. Uses enaml's models, and declarative and dynamic widget framework instead of kvlang

Android apps are currently working and have a lot of components. iOS works, but is limited to only a few components at the moment (implementation is in the works see #10).

### Docs and Examples ###

See the [project site](https://www.codelv.com/projects/enaml-native/). There's also some short tutorials and examples on [youtube](https://www.youtube.com/playlist?list=PLXUaMWWFaOjT2WdIrJdTYjEMJmrjuvVz0).

> Need help? Try the gitter group https://gitter.im/enaml-native/Lobby

### Features ###
1. Enaml's features: declarative syntax, conditional and looper rendering, automatic data binding
2. Web code editor via the [Python Playground](https://play.google.com/store/apps/details?id=com.frmdstryr.pythonplayground)!
3. Layouts with flexbox
4. Live app code reloading (like react-native's live reload)

### Apps ###

Apps using enaml-native can be found [here](https://www.codelv.com/projects/enaml-native/apps/).

### Demos ###
1. Try out the beta demo app here [on google play](https://play.google.com/store/apps/details?id=com.frmdstryr.enamlnative.demo)
2. Try out code without installing the android SDK or NDK via the [Python Playground](https://play.google.com/store/apps/details?id=com.frmdstryr.pythonplayground)!


### Thanks to ###
 
This project is built on top of several existing projects:

1. [enaml](https://github.com/nucleic/enaml)
2. [python-for-android](https://github.com/kivy/python-for-android/)
3. [pybridge](https://github.com/joaoventura/pybridge)
4. [react-native](https://github.com/facebook/react-native) (inspiration)
5. [pyjnius](https://github.com/kivy/pyjnius/)
6. [kivy-ios](https://github.com/kivy/kivy-ios/)

