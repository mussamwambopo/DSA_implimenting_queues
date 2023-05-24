class Demo_Queue:
    def __init__(self):
        self.queue = list()

    def insert_element(self, val):
        if val not in self.queue:
            self.queue.insert(0, val)
            return True
        return False

    def size(self):
        return len(self.queue)

    def get_front(self):
        if self.queue:
            return self.queue[0]
        return None


demo_queue = Demo_Queue()
demo_queue.insert_element("A")
demo_queue.insert_element("B")
demo_queue.insert_element("C")
demo_queue.insert_element("D")

front_element = demo_queue.get_front()
print("Front element of the queue:", front_element)
