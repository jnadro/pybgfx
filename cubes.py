import bgfx
from bgfx_ex import App

class Cubes(App):

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

    def init(self):
        pass

    def shutdown(self):
        pass

    def update(self):
        pass

app = Cubes(1280, 720, "Cubes")
app.run()
