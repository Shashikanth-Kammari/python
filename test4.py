from dataclasses import dataclass
@dataclass
class profile:
    name: str
    age: int
information = profile("shashikanth", 29)
print(information.name, information.age)