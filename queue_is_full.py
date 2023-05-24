class Demo_Queue:
    def __init__(self, max_capacity):
        self.queue = list()
        self.max_capacity = max_capacity

    def insert_element(self, val):
        if len(self.queue) < self.max_capacity:
            self.queue.insert(0, val)
            return True
        return False

    def is_full(self):
        return len(self.queue) >= self.max_capacity


demo_queue = Demo_Queue(max_capacity=5)
demo_queue.insert_element("A")
demo_queue.insert_element("B")
demo_queue.insert_element("C")
demo_queue.insert_element("D")

print("Is the queue full?", demo_queue.is_full())
