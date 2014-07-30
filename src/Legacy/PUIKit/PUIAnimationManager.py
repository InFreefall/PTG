from PUITimeline import PUITimeline

timelines = []

def update(dt):
    for timeline in timelines:
        timeline.update(dt)

def addTimeline(timeline):
    try:
        timelines.index(timeline)
    except:
        timelines.append(timeline)

def removeTimeline(timeline):
    try:
        timelines.remove(timeline)
    except:
        pass