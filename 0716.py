class Person:
    def init(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        print(self._name)

    def info(self):
        print(f"Имя: {self._name}\nВозвраст: {self._age}")


class Student(Person):
    def init(self, name, age, grade):
        super(Student, self).init(name, age)
        self.__grade = grade

    def info(self):
        super().info()
        l = []
        l.append(self._name);
        l.append(self._age);
        l.append(self.__grade)
        for i in l:
            print(i)


person = Person("Сергей", 34)
student = Student("Алина", 24, "Физика")
person.get_name()
person.info()
print()
student.info()