import tkinter
import time
import asyncio


window = tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("1600x900+100+100")

canvas = tkinter.Canvas(window, width="1280",
                        height="720", relief="solid", offset="1000,1000", bd=2)

canvas.create_line(10, 10, 20, 20, 20, 130, 30, 140, fill="red")
polygon = canvas.create_polygon(50, 50, 170, 170, 100, 170, outline="yellow")
oval = canvas.create_oval(100, 200, 150, 250, fill="blue", width=3)
arc = canvas.create_arc(100, 100, 300, 300, start=0, extent=150, fill='red')

canvas.pack(fill="both", expand=True)


window.update()
print("test")
time.sleep(10)
# import turtle
# t = turtle.Turtle()
# t.fd(100)


# class Asdf:
#     def __init__(self, x):
#         self.material = x

#     def jejil():
#         print()

#     def aaaa2(self, x):
#         print(self.bbbb2(x))

#     def bbbb2(self, x):
#         return x*2

#     @staticmethod
#     def cccc2(x):
#         return x*5


# def cccc(x):
#     return x*5


# a = Asdf("철")
# b = Asdf("금")
# c = Asdf("구리")

# print(a.material)
# print(b.material)
# print(c.material)

# print(cccc("asdf"))
# print(Asdf.cccc2("asdf"))
# # print(Asdf.cccc2("asdf"))


# class Bridge:
#     def __init__(self, a, b):
#         self.jwapyo1 = a
#         self.jwapyo2 = b

#     def jwapyoChange(self, a, b):
#         self.jwapyo1 = a
#         self.jwapyo2 = b

#     @staticmethod
#     def aaaa(self):
#         a = 1
#         print(a)


# def aaaa():
#     a = 1
#     print(a)


# dari1 = Bridge([0, 4], [1, 5])
# dari2 = Bridge([0, 5], [1, 6])
# dari3 = Bridge([1, 4], [2, 5])

# dari1.jwapyoChange([2, 4], [3, 5])

# Bridge.aaaa()
