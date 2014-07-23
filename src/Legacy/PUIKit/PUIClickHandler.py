import pygame

groups = {}
clickable = {}

currentDelegate = None
modal = None

def addClickable(delegate, group, button=1):
    if group in groups:
        list = groups[group]
    else:
        list = []
        groups[group] = list
        clickable[group] = True
    try:
        list.index(delegate)
    except:
        list.append(delegate)

def removeClickable(delegate):
    for group in groups.keys():
        list = groups[group]
        if delegate in list:
            list.remove(delegate)
            if len(list) is 0:
                del groups[group]
                del clickable[group]

def removeGroup(group):
    try:
        del groups[group]
    except:
        pass

def setClickable(group, bool):
    clickable[group] = bool

def isClickable(group):
    return clickable[group]

def setModal(clickable):
    global modal
    modal = clickable

def click(position, button):
    global currentDelegate
    global modal
    if modal is None:
        for group in groups.keys():
            list = groups[group]
            if not clickable[group]:
                continue
            for currentClickable in list:
                if currentClickable.absoluteRect().collidepoint(position):
                    if currentClickable.click(position, button):
                        currentDelegate = currentClickable
                        return
    else:
        modal.click(position, button)

def move(position):
    global currentDelegate
    if currentDelegate is not None and modal is None:
        currentDelegate.move(position)
    elif modal is not None:
        modal.move(position)

def endClick(position, button):
    global currentDelegate
    if currentDelegate is not None and modal is None:
        currentDelegate.endClick(position)
        currentDelegate = None
    elif modal is not None:
        modal.endClick(position)
