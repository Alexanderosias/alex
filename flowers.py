class Flower:
    def __init__(self, color):
        self.color = color

    def draw_flower(self):
        if self.color.lower() == "red":
            flower = """
                   .-^-.
                   !oYo!
                   \\()/
                   7""7
                   """
        elif self.color.lower() == "blue":
            flower = """
                   .--.
                   |o_o |
                   |:_/ |
                   // \\ \\
                   (|  | )
                   '---'
                   """
        elif self.color.lower() == "yellow":
            flower = """
                   .--.
                   |o_o |
                   |:_/ |
                   // \\ \\
                   (|  | )
                   '---'
                   """
        else:
            flower = "Sorry, I don't have that color for the flower."
        return flower

def generate_flower():
    color = input("Enter flower color (red, blue, or yellow): ")
    flower = Flower(color)
    print(flower.draw_flower())

generate_flower()
