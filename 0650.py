class Note:
    tasks = {"Пусто": "[ ]"}
    counter = 1
        
    def init(self):
        print("• СПИСОК ЗАДАЧ •")
    
    def add(self):
        if self.counter == 1:
            self.tasks.popitem()
            self.counter -= 1
        self.tasks[input("Задача: ")] = "[ ]"
        self.show()
    
    def show(self):
        for k, v, in self.tasks.items():
            print("-" * 20); print(f"{k} – {v}")
        self.add()
    
note = Note()
note.add()