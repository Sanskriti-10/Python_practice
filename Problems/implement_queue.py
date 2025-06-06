#Implement a queue using a Python list. Include enqueue, dequeue, and display operations.
#(Hint: Use append() for enqueue and pop(0) for dequeue)

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to the queue.")

    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"{removed} removed from the queue.")
        else:
            print("Queue is empty. Cannot dequeue.")

    def display(self):
        if not self.is_empty():
            print("Current queue:", self.queue)
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.queue) == 0

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
