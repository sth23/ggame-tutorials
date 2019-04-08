from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,65,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 1
        
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        
        # Rotate right/left
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeftOn)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.rotateLeftOff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRightOn)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.rotateRightOff)
        
        # Move right/left
        SpaceGame.listenKeyEvent("keydown", "a", self.moveLeftOn)
        SpaceGame.listenKeyEvent("keyup", "a", self.moveLeftOff)
        SpaceGame.listenKeyEvent("keydown", "d", self.moveRightOn)
        SpaceGame.listenKeyEvent("keyup", "d", self.moveRightOff)
        
        # Move up/down
        SpaceGame.listenKeyEvent("keydown", "w", self.moveUpOn)
        SpaceGame.listenKeyEvent("keyup", "w", self.moveUpOff)
        SpaceGame.listenKeyEvent("keydown", "s", self.moveDownOn)
        SpaceGame.listenKeyEvent("keyup", "s", self.moveDownOff)
        
        self.fxcenter = self.fycenter = 0.5
        
    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0
        
    def rotateLeftOn(self, event):
        self.vr = 0.01
        
    def rotateLeftOff(self, event):
        self.vr = 0
        
    def rotateRightOn(self, event):
        self.vr = -0.01
        
    def rotateRightOff(self, event):
        self.vr = 0
        
    def moveLeftOn(self, event):
        self.vx += -1
    
    def moveLeftOff(self, event):
        self.vx = 0
        
    def moveRightOn(self, event):
        self.vx += 1
        
    def moveRightOff(self, event):
        self.vx = 0
        
    def moveUpOn(self, event):
        self.vy += -1
        
    def moveUpOff(self, event):
        self.vy = 0
        
    def moveDownOn(self, event):
        self.vy += 1
        
    def moveDownOff(self, event):
        self.vy = 0

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
        # manage thrust animation
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

myapp = SpaceGame()
myapp.run()