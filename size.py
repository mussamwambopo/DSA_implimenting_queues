class Demo_Queue:
    def __init__(self):
        self.queue = list()

    # Inserting the elements
    def insert_element(self, val):
        if val not in self.queue:
            self.queue.insert(0, val)
            return True
        return False

    def size(self):
        return len(self.queue)


demo_queue = Demo_Queue()
demo_queue.insert_element("A")
demo_queue.insert_element("B")
demo_queue.insert_element("C")
demo_queue.insert_element("D")

print("The length of Demo Queue is:", demo_queue.size())
