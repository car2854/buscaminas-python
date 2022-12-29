from ursina import *

from theme.colorsObject import ColorNone, ColorSelected, ColorMine, ColorMineGreen
from static.valueStatic import staticValue

class Object(Button):

  def __init__(self,id, isMine = False, text='', radius=0.0,**kwargs):
    super().__init__(
      id = id, 
      isMine = isMine,
      text = text, 
      radius = radius,
      nodoObjets = [], 
      isSelected = False,
      isMarked = False,
      **kwargs
    )

  

  def on_mouse_enter(self):

    if not(staticValue.winGame):
      if (self.isSelected == False):
        self.color = color.blue
      else:
        if (self.isMine == True):
          self.color = ColorMine
        else:
          self.color = ColorSelected


  def on_mouse_exit(self):
    if not(staticValue.winGame):
      if (self.isSelected == False):
        self.color = ColorNone
      else:
        if (self.isMine == True):
          self.color = ColorMine
        else:
          self.color = ColorSelected

  def add_nodo(self,nodo):
    self.nodoObjets.append(nodo)

  def on_click(self):
    if ((not (staticValue.gameOver)) and (not (staticValue.winGame))):
      if (self.isSelected == False):
        self.activeNodoNoMine(self)
        if (staticValue.discoveredNodes == 54):
          staticValue.winGame = True
          for i in staticValue.nodoMines:
            i.text = 'X'
            i.color = ColorMineGreen


  def activeNodoNoMine(self, nodo):
    if (nodo.isMine == False):
      
      staticValue.discoveredNodes = staticValue.discoveredNodes + 1
      nodo.isSelected = True
      countMine = 0
      
      for i in nodo.nodoObjets:
        if (i.isMine):
          countMine = countMine + 1
      
      nodo.text = str(countMine)
      nodo.color = ColorSelected

      if (countMine == 0):
        for i in nodo.nodoObjets:
          if (i.isSelected == False):
            self.activeNodoNoMine(i)
    else:
      nodo.text = 'Mine'
      nodo.color = ColorMine
      staticValue.gameOver = True
      for i in staticValue.nodoMines:
        i.text = 'Mine'
        i.color = ColorMine
        i.isSelected = True


    # nodo.isSelected = True
    # mine = 0
    # for i in self.nodoObjets:
    #   if (i.isMine):
    #     mine = mine + 1
    # self.text = str(mine)