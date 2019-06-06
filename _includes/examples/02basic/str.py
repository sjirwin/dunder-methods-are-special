class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __repr__(self):
    '''for Point(1,2) repr will be "Point(x=1, y=2)" '''
    return (f'{self.__class__.__qualname__}(x={self.x!r}, y={self.y!r})')
  def __str__(self):
    '''for Point(1,2) str will be "(1, 2)" '''
    return (f'({self.x!r}, {self.y!r})')