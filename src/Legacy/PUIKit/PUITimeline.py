import pdb
import PUIAnimationManager

class PUITimeline:
    def __init__(self, target, property):
        self.keys = []
        self.slopes = []
        self.target = target
        self.property = property
        self.dirty = False
        self.time = 0
        PUIAnimationManager.addTimeline(self)
        self.type = type(getattr(target, property))
    
    def setValueAtTime(self, seconds, value):
        self.dirty = True
        for i, keyframe in enumerate(self.keys):
            if keyframe[0] > seconds:
                self.keys.insert(i,(seconds,value))
                return
        self.keys.append((seconds,value))
    
    def valueAtTime(self, seconds):
        if self.dirty:
            self.calculateSlope()
        preKeyframe = None
        postKeyframe = None
        for i, keyframe in enumerate(self.keys):
            if keyframe[0] == seconds:
                return keyframe[1]
            if keyframe[0] < seconds:
                if i+1 == len(self.keys):
                    return keyframe[1]   # Don't calculate animation beyond the last frame
                if self.keys[i+1][0] > seconds:
                    if self.type is type(()):
                        retVal = []
                        for j, param in enumerate(keyframe[1]):
                            retVal.append(keyframe[1][j] + (seconds-keyframe[0]) * self.slopes[i][1][j])
                        return tuple(retVal)
                    else:
                        return keyframe[1] + (seconds-keyframe[0]) * self.slopes[i][1]
    
    def calculateSlope(self):
        self.slopes = []
        self.dirty = False
        for i, keyframe in enumerate(self.keys):
            if (i+1 == len(self.keys)):
                break
            nextKeyframe = self.keys[i+1]
            
            # Assume number values
            if self.type is type(()):
                list = []
                for j,value in enumerate(nextKeyframe[1]):
                    list.append(float(nextKeyframe[1][j]-keyframe[1][j]) / float(nextKeyframe[0]-keyframe[0]))
                nextSlope = (keyframe[0], tuple(list))
            else:
                nextSlope = (keyframe[0], float(nextKeyframe[1]-keyframe[1]) / float(nextKeyframe[0]-keyframe[0]) )
            self.slopes.append(nextSlope)
    
    def duration(self):
        if len(self.keys) is 0:
            return 0
        return self.keys[-1][0]
    
    def update(self, dt):
        self.time += dt
        try:
            setattr(self.target, self.property, self.valueAtTime(self.time))
        except:
            pdb.set_trace()

class Spud:
    def __init__(self):
        self.position = (0,0)

if __name__ == '__main__':
    t = PUITimeline(Spud(), "position")
    t.setValueAtTime(0,(0,0))
    t.setValueAtTime(3,(5,3))
    t.setValueAtTime(7,(1,-2))
    for i in range(1,8):
        print i, t.valueAtTime(i)
    pdb.set_trace()