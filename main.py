from ursina import *
from scenes.newGame import newGame, refresh
from static.valueStatic import staticValue


def main():

  app = Ursina()

  newGame()

  button = Button(text='Refresh', position=Vec3(.7,-.35,0), scale=Vec3(.2,.1,0))
  button.on_click = refresh
  
  app.run()

main()