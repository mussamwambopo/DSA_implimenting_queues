
class Demo_Queue:
    def __init__(self):
        self.items = []
    def Is_Empty(self): # This function will check whether the queue is empty or not
        return self.items == []
    def Enqueue(self, data):
        self.items.append(data) # here we are appending the elements in the queue
    def Dequeue(self):
        return self.items.pop(0) # here we are performing the Dequeue operation 
demo_queue = Demo_Queue()
while True:
    print('Enqueue operation ')
    print('Dequeue operation’')
    print('Quit')
    task = input('What would you like to do? ').split()
  
    operations = task[0].strip().lower()
    if operations == 'Enqueue': # Condition
        demo_queue.Enqueue(int(task[1]))  # Append the element in the queue
    elif operations == 'Enqueue':
        if demo_queue.Is_empty():
          print('Demo Queue is empty.')
        else:
            print('Dequeued value: ', demo_queue.Dequeue())
    elif operations == 'Quit':
        break