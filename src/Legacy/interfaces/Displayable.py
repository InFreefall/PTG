class Displayable:
  def absoluteRect(self):
    raise NotImplementedError # try catch NameError with self.parent
  
  def positionInSelf(self, position):
    return (position[0] - self.absoluteRect().x, position[1] - self.absoluteRect().y)