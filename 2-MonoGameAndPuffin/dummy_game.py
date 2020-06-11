from Puffin.Core.Ecs.Components import ColourComponent
from Puffin.Infrastructure.MonoGame import PuffinGame

from dummy_scene import DummyScene

class DummyGame(PuffinGame):
    def __init__(self, x, y):
        print("Inside: x={} y={}".format(x, y))
        super(DummyGame, self).__init__(x, y)
        print(dir(self))
    
    def Ready(self):
        self.ShowScene(DummyScene())