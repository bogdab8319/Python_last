
class Figura :
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Фигура:  {self.name} посчитана и ее площадь составляет:  "



    def get_aria(self):
        return

    def __int__(self):
        return f"{self.get_aria()}"

    def print_aria(self):
        print(f" Фигура: {self.name}  \n Площадь : {self.get_aria()}")


class Triangle(Figura):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2
        super().__init__("Треугольник")

    def get_aria(self):
        return (self.side_1 * self.side_2)/2

tr= Triangle(10,30)
print(tr.print_aria())

class Circle(Figura):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(" Круг")
    def get_aria(self):
        return 3.14 * self.radius * self.radius
c= Circle(30)
print(c.print_aria())


class Pryamougol(Figura):
    def __init__(self,a,b):
        self.a =a
        self.b =b
        super().__init__("Прямоугольник")
    def get_aria(self):
        return self.a * self.b

pr=Pryamougol( 20,30)
pr.print_aria()

class Trapezoid(Figura):
    def __init__(self, side_a, side_b, height):
        self.side_a=side_a
        self.side_b=side_b
        self.height=height
        super().__init__(" Трапеция")

    def get_aria(self):
        return 0.5*(self.side_a+self.side_b)*self.height

trap=Trapezoid(20,40,30)
print(trap.print_aria())

print(tr.__str__(), tr.__int__())
print(c.__str__(), c.__int__())
print(pr.__str__(), pr.__int__())
print(trap.__str__(),trap.__int__())










