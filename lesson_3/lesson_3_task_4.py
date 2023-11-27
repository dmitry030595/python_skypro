import turtle

# Создаем экземпляр черепахи
t = turtle.Turtle()

# Рисуем круг в качестве тела животного
t.circle(50)

# Рисуем голову
t.penup()
t.goto(0, 60)
t.pendown()
t.circle(20)

# Рисуем глаза
t.penup()
t.goto(-15, 80)
t.pendown()
t.dot(10)
t.penup()
t.goto(15, 80)
t.pendown()
t.dot(10)

# Рисуем ноги
t.penup()
t.goto(-30, 30)
t.pendown()
t.goto(-50, 10)
t.penup()
t.goto(30, 30)
t.pendown()
t.goto(50, 10)

# Завершаем программу
t.screen.exitonclick()
t.screen.mainloop()
