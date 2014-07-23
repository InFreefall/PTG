
"""
Python implementation of Cocoa NSNotificationCenter

"""

notifications = {}
observerKeys = {}

def addObserver(observer, method, notificationName, observedObject=None):
    global notifications
    global observerKeys
    if not notifications.has_key(notificationName):
        notifications[notificationName] = {}
    notificationDict = notifications[notificationName]
    if not notificationDict.has_key(observedObject):
        notificationDict[observedObject] = {}
    notificationDict[observedObject][observer] = method
    if not observerKeys.has_key(observer):
        observerKeys[observer] = []
    observerKeys[observer].append((notificationName,observedObject))

def removeObserver(observer, notificationName=None, observedObject=None):
    global notifications
    global observerKeys
    try:
        observerKeys = observerKeys.pop(observer)
    except KeyError:
        return
    for observerKey in observerKeys:
        if notificationName and observerKey[0] != notificationName:
            continue
        if observedObject and observerKey[1] != observedObject:
            continue
        try:
            notifications[observerKey[0]][observerKey[1]].pop(observer)
        except KeyError:
            return
        if len(notifications[observerKey[0]][observerKey[1]]) == 0:
            notifications[observerKey[0]].pop(observerKey[1])
            if len(notifications[observerKey[0]]) == 0:
                notifications.pop(observerKey[0])

def postNotification(notificationName, notifyingObject, userInfo=None):
    global notifications
    global observerKeys
    try:
        notificationDict = notifications[notificationName]
    except KeyError:
        return
    for key in (notifyingObject,None):
        try:
            methodsDict = notificationDict[key]
        except KeyError:
            continue
        for observer in methodsDict:
            if not userInfo:
                methodsDict[observer](notifyingObject)
            else:
                methodsDict[observer](notifyingObject,userInfo)
