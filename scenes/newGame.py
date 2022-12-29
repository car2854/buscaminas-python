from ursina import *

import random

from model.object import Object
from theme.colorsObject import ColorNone

from static.valueStatic import staticValue

from const import MINES, NUMBERNODO


def newGame():

  positionMines = []

  for i in range(MINES):
    state = False
    while(state == False):
      num = random.randint(0,NUMBERNODO - 1)
      if num not in positionMines:
        positionMines.append(num)
        state = True

  positionMines.sort()
  firstNumber = positionMines.pop(0)

  for i in range(NUMBERNODO):

    size = 0.1
    horizontal = ((i % 8) * size) - 0.35
    vertical = ((i//8) * size) - 0.35
    vectorPosition = Vec3(horizontal,vertical,0)

    if (i == firstNumber):
      staticValue.listNodo.append(Object(isMine=True,id=i, text='?', position=vectorPosition, scale=(size,size,.5), color=ColorNone))
      if (len(positionMines)):
        firstNumber = positionMines.pop(0)
    else:
      staticValue.listNodo.append(Object(id=i, text='?', position=vectorPosition, scale=(size,size,.5), color=ColorNone))

  for i in staticValue.listNodo:

    if (i.isMine):
      staticValue.nodoMines.append(i)

    if ( (i.id-9) in range(0,NUMBERNODO) and (((i.id) % 8) != 0)):
      i.add_nodo(staticValue.listNodo[i.id-9])
    
    if ((i.id-8) in range(0,NUMBERNODO)):
      i.add_nodo(staticValue.listNodo[i.id-8])
    
    if ((i.id-7) in range(0,NUMBERNODO) and (((i.id - 7)%8)!= 0)):
      i.add_nodo(staticValue.listNodo[i.id-7])

    if ((i.id-1) in range(0,NUMBERNODO) and (((i.id) % 8) != 0)):
      i.add_nodo(staticValue.listNodo[i.id-1])
    
    if ((i.id+1) in range(0,NUMBERNODO) and (((i.id - 7)%8)!= 0)):
      i.add_nodo(staticValue.listNodo[i.id+1])
    
    if ((i.id+7) in range(0,NUMBERNODO) and (((i.id) % 8) != 0)):
      i.add_nodo(staticValue.listNodo[i.id+7])
    
    if ((i.id+8) in range(0,NUMBERNODO)):
      i.add_nodo(staticValue.listNodo[i.id+8])
    
    if ((i.id+9) in range(0,NUMBERNODO) and (((i.id - 7)%8)!= 0)):
      i.add_nodo(staticValue.listNodo[i.id+9])

def refresh():
  
  for i in staticValue.listNodo:
    destroy(i)
  staticValue.listNodo.clear()

  for i in staticValue.nodoMines:
    destroy(i)
  staticValue.nodoMines.clear()

  staticValue.controllerClick = False

  staticValue.gameOver = False
  staticValue.discoveredNodes = 0
  staticValue.winGame = False

  newGame()