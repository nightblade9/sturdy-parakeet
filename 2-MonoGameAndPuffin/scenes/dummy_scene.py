from Puffin.Core import Scene

class DummyScene(Scene):
    def __init__(self):
        super.__init__()
    
    def ready(self):
        self.ShowScene(DummyScene())