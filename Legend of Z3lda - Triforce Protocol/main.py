#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

### NEW IDEA : screen.load_image(source) USE THIS
### have an image that apears in the middle of the screen and refreshes it every frame
# Create your objects here.
ev3 = EV3Brick()
A = TouchSensor(Port.S1)
def iseven(number):
    number = number % 2
    return number
class Player():
    def __init__(self):
        self.x = 10
        self.y = 10
        self.image = "assets/link/link_down.png"
        self.anim_state = 0
        self.save = (self.x, self.y)
    def update(self):
        self.save = (self.x, self.y)
        
        if iseven(self.anim_state):
            if Button.UP in ev3.buttons.pressed():
                self.y -= 0.2
                self.image = "assets/link/link_up1.png"
            if Button.DOWN in ev3.buttons.pressed():
                self.y += 0.2
                self.image = "assets/link/link_down1.png"
            if Button.RIGHT in ev3.buttons.pressed():
                self.x += 0.2
                self.image = "assets/link/link_right1.png"
            if Button.LEFT in ev3.buttons.pressed():
                self.x -= 0.2
                self.image = "assets/link/link_left1.png"
            if Button.RIGHT_UP in ev3.buttons.pressed():
                self.y -= 0.1
                self.x += 0.1
            if Button.RIGHT_DOWN in ev3.buttons.pressed():
                self.y += 0.1
                self.x += 0.1
            if Button.LEFT_UP in ev3.buttons.pressed():
                self.y -= 0.1
                self.x -= 0.1
            if Button.LEFT_DOWN in ev3.buttons.pressed():
                self.y += 0.1
                self.x -= 0.1
        elif not iseven(self.anim_state):
            if Button.UP in ev3.buttons.pressed():
                self.y -= 0.2
                self.image = "assets/link/link_up2.png"
            if Button.DOWN in ev3.buttons.pressed():
                self.y += 0.2
                self.image = "assets/link/link_down2.png"
            if Button.RIGHT in ev3.buttons.pressed():
                self.x += 0.2
                self.image = "assets/link/link_right2.png"
            if Button.LEFT in ev3.buttons.pressed():
                self.x -= 0.2
                self.image = "assets/link/link_left2.png"
            if Button.RIGHT_UP in ev3.buttons.pressed():
                self.y -= 0.1
                self.x += 0.1
            if Button.RIGHT_DOWN in ev3.buttons.pressed():
                self.y += 0.1
                self.x += 0.1
            if Button.LEFT_UP in ev3.buttons.pressed():
                self.y -= 0.1
                self.x -= 0.1
            if Button.LEFT_DOWN in ev3.buttons.pressed():
                self.y += 0.1
                self.x -= 0.1
    
        if Button.CENTER in ev3.buttons.pressed():
            
            if self.image == "assets/link/link_up1.png" or self.image == "assets/link/link_up2.png":
                
                ev3.screen.draw_image(self.x+7, self.y-16, "assets/sword/sword_up.png", Color.RED)
                

            elif self.image == "assets/link/link_down1.png" or self.image == "assets/link/link_down2.png":
                

                ev3.screen.draw_image(self.x+7, self.y+16, "assets/sword/sword_down.png", Color.RED)
                
            elif self.image == "assets/link/link_right1.png" or self.image == "assets/link/link_right2.png":
                

                ev3.screen.draw_image(self.x+14, self.y+7, "assets/sword/sword_right.png", Color.RED)
                
            elif self.image == "assets/link/link_left1.png" or self.image == "assets/link/link_left2.png":
                

                ev3.screen.draw_image(self.x-14, self.y+7, "assets/sword/sword_left.png", Color.RED)
                
        if self.x <= 0:
            self.x = 1
        elif self.x >= 168:
            self.x = 167
        elif self.y <= 0:
            self.y = 1
        elif self.y >= 118:
            self.y = 117
        self.anim_state +=1
        ev3.screen.draw_image(self.x, self.y, self.image, Color.RED)
        
        
                
# Write your program here.
ev3.speaker.beep(1000)
wait(100)
ev3.speaker.beep(500)
wait(100)
ev3.speaker.beep(550)
wait(100)
ev3.speaker.beep(1100)
wait(100)
ev3.speaker.beep(3000)
sy = 0
ev3.screen.draw_image(0, 0, "splash.png")
wait(1000)
for i in range(20):
    ev3.screen.draw_image(0, sy, "splash.png")
    sy -= 8
    wait(100)
    ev3.screen.clear()
ev3.screen.clear()


player = Player()
running = True
while running:
    

    
    
    if player.save != (player.x, player.y):
        #ev3.screen.load_image("refresher.png")
        ev3.screen.clear()
    player.update()
   