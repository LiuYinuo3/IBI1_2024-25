class patient:
    def __init__(self,name,age,date,history):
        self.name=name
        self.age=age
        self.date=date
        self.history=history
    def information(self):
        print(f"name: {self.name} | age: {self.age} | admission date: {self.date} | medical history: {self.history}")
#example
patient1 = patient("Li Lei", 35, "2024-03-20", "diabetes")
patient1.information()