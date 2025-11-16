import turtle



class pattern():

    # self.__angle integer
    # self.__times integer
    def __init__(self, angle: int, times: int):
        self.__angle = angle
        self.__times = times

    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

        for x in range(self.__times):
            turtle.pencolor(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.forward(x)
            turtle.left(self.__angle)



patterns = []

with open("Pattern.txt", "r") as file:
    for i in range(5):

        angle = int(file.readline().strip())
        times = int(file.readline().strip())

        patterns.append(pattern(angle, times))



turtle.setup(800, 600)  # setting window dimensions
window = turtle.Screen()
window.title("Press SPACE to draw the next pattern")
turtle.bgcolor('black')

index = 0

def execute_drawing():
    global index

    turtle.clear()
    turtle.penup()
    turtle.home()        # return to (0,0) and reset direction
    turtle.pendown()

    current_object = patterns[index]
    current_object.draw_pattern()

    index += 1

window.listen()
window.onkey(execute_drawing, "space")

turtle.done()