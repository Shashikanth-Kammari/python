from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
    experience: float
    Information: bool
doc = Person("shashi", 29, 4.2, True, )
print(doc.name, doc.age, doc.experience, doc.Information)