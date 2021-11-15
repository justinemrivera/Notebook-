from string import ascii_lowercase
from random import randint, choice
from time import sleep


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self, item):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


def register_visitors(visitor_queue):
    for char in ascii_lowercase:
        pass


def service_customers(visitor_queue):
    bank_tellers = ["A", "B", "C", "D", "E", "F", "G"]
    while not __:
        visitor =
        print("thank you for waiting %s, station %s is ready for you.")
                % (visitor, choice(bank_tellers)))
        sleep(randint(1, 2))
    print("Empty visitor queue.")

def main():
    visitor_queue=Queue()
    register_visitors(visitor_queue)
    service_customers(visitor_queue)from string import ascii_lowercase
from random import randint, choice
from time import sleep

def register_visitors(visitor_queue):
    for char in ascii_lowercase:
        pass

def service_customers(visitor_queue):
    bank_tellers=["A", "B", "C", "D", "E", "F", "G"]
    while not __:
        visitor=
        print("thank you for waiting %s, station %s is ready for you.")
                % (visitor, choice(bank_tellers)))
        sleep(randint(1, 2))
    print("Empty visitor queue.")

def main():
    visitor_queue=Queue()
    register_visitors(visitor_queue)
    service_customers(visitor_queue)
