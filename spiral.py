import turtle
import random

#classes
class ScreenManager:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Colorful Spirals with Turtle Graphics")
        self.colors = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "cyan", "white"]
        
    def change_bgcolor(self):
        self.screen.bgcolor(random.choice(self.colors))

    def setup_events(self, spiral_manager):
        self.screen.listen()
        self.screen.onkey(self.change_bgcolor, "space")
        self.screen.onkey(spiral_manager.reset_spirals, "r")

#drawing 
class SpiralTurtle:
    def __init__(self, colors):
        self.turtle = turtle.Turtle()
        self.colors = colors
        self.turtle.speed(0)
        self.turtle.width(2)
        self.turtle.color(random.choice(colors))
        self.turtle.penup()
        self.turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        self.turtle.pendown()
    
    def draw_spiral(self, size, angle, increment, num_turns):
        for _ in range(num_turns):
            self.turtle.color(random.choice(self.colors))
            self.turtle.forward(size)
            self.turtle.right(angle)
            size += increment
    
    def reset(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        self.turtle.pendown()

#multiple spirals
class SpiralManager:
    def __init__(self, num_spirals, colors):
        self.spirals = [SpiralTurtle(colors) for _ in range(num_spirals)]
        self.colors = colors

    def draw_spirals(self, size, angle, increment, num_turns):
        for spiral in self.spirals:
            spiral.draw_spiral(size, angle, increment, num_turns)
    
    def reset_spirals(self):
        for spiral in self.spirals:
            spiral.reset()

# functions to run the program
def main():
    screen_manager = ScreenManager()
    num_spirals = 5
    spiral_manager = SpiralManager(num_spirals, screen_manager.colors)
    
    screen_manager.setup_events(spiral_manager)
    
    size = int(screen_manager.screen.numinput("Spiral Size", "Enter the initial size of the spiral:", 5, minval=1, maxval=20))
    angle = int(screen_manager.screen.numinput("Spiral Angle", "Enter the angle for the spiral:", 45, minval=1, maxval=360))
    increment = int(screen_manager.screen.numinput("Size Increment", "Enter the size increment for each step:", 3, minval=1, maxval=10))
    num_turns = int(screen_manager.screen.numinput("Number of Turns", "Enter the number of turns:", 100, minval=10, maxval=1000))
    
    spiral_manager.draw_spirals(size, angle, increment, num_turns)

    turtle.done()

if __name__ == "__main__":
    main()
