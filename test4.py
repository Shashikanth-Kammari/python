from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
    experience: float
    Information: bool
doc = Person("shashi", 29, 4.2, True )
doc = Person("shashikanth", 19, 4.1, False )
print(doc.name, doc.age, doc.experience, doc.Information)