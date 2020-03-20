class Queue:
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return self.queue == [] 
    def enqueue(self, entry):
        self.queue.append(entry)
    def length(self):
        return len(self.queue)
    
    def application(self):
        nur, kg, one = 0 , 0 , 0
        for i in self.queue:
            if i[2] == "Nursery":
                nur += 1
            elif i[2] == "KG":
                kg += 1
            else:
                one += 1
        print("No of application from nursery", nur)
        print("No of application from KG", kg)
        print("No of application from one", one)


q = Queue()
i = 1
n = int(input("Enter no of entries"))

class incorrectEntry(Exception):
    pass

while i <= n:
    try:
        l1 = input("Enter registration no: ")
        l2 = input("Enter name: ")
        l3 = input("Enter class of admission (Nursery/KG/I): ")
        if l3 != "Nursery" and l3 != "KG" and l3 != "I":
            raise incorrectEntry
    except:
        print("Data entry incorrect, try again!")
        continue
    
    q.enqueue([l1, l2, l3])
    print(q.queue)
    i += 1

print("Length of queue:", q.length())
q.application()

