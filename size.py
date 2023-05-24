class Demo_Queue:  
    def __init__(self):  
        self.queue = list()  
    # Inserting the elements
    def insert_element(self,val):   
            if val not in self.queue:  
                    self.queue.insert(0,val)  
                    return True 
            return False 
      
    def size(self):  
        return len(self.queue)  
      
demo_queue = Demo_Queue()  
demo_queue.insert_element(&quot;A&quot;)  
demo_queue.insert_element(&quot;B&quot;)  
demo_queue.insert_element(&quot;C&quot;)  
demo_queue.insert_element(&quot;D&quot;)  
      
print( &quot; The length of Demo Queue is: &quot;,demo_queue.size() ) 