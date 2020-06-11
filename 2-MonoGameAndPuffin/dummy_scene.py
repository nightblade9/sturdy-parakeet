from Puffin.Core import Scene
from Puffin.Core.Ecs import Entity
from Puffin.Core.Ecs.Components import ColourComponent

class DummyScene(Scene):

    def Ready(self):
        super(DummyScene, self).Ready()
        e = Entity()
        c = ColourComponent(e, 0xFF0000, 32, 32)
        e.Set(c)
        self.Add(e)