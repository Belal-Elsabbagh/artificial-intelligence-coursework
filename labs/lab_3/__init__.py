from point import Point
from rectangle import Rectangle
from rectangle.cuboid import Cuboid
from bank.account import Account
from vehicle.bus import Bus
from vehicle import Vehicle


def test_bank():
    acc = Account(3, 'belal', 1000)
    print(acc)
    print(f"Deposit 100 = {acc.deposit(100)}, Withdraw 600 = {acc.withdraw(600)}")


def test_bus():
    vehicle_1 = Vehicle(120, 12000)
    bus_1 = Bus(70, 300000)
    print(vehicle_1)
    print(bus_1)


def test_rectangle():
    rect = Rectangle(3, 4)
    print(rect)
    cuboid = Cuboid(3, 4, 5)
    print(cuboid)


def test_point():
    a = Point(3, 4)
    b = Point(7, 8)
    print(a)
    print(b)
    print(b - a)
