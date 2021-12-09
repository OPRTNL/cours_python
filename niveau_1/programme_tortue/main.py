import turtle

t = turtle.Turtle()

def one_step(step_size):
    t.forward(step_size)
    t.left(90)
    t.forward(step_size)
    t.right(90)

def stairs(number_of_steps, size):
    for i in range(0, number_of_steps):
        one_step(size)
        size -= 10
    t.forward(size)

# stairs(5, 50)

def arrete(size):
    t.forward(size)
    t.left(90)

def carre(size):
    for i in range(0, 4) : arrete(size)

def carres(size, qty):
    for i in range(0, qty) : carre((i+1)*size)

carres(10,5)

turtle.done()