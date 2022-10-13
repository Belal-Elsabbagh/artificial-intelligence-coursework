from labs.lab_3.point import Point
from labs.lab_3.rectangle import Rectangle
from labs.lab_3.rectangle.cuboid import Cuboid
from labs.lab_3.bank.account import Account
from labs.lab_3.vehicle.bus import Bus
from labs.lab_3.vehicle import Vehicle


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
    a = Point(1, 2)
    b = Point(7, 8)
    print(a)
    a.move(3, 2)
    print(a)
    print(b)
    print(b - a)


def run():
    test_point()
