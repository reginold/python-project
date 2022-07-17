from dataclasses import dataclass, field

@dataclass
class Person():
    first_name: str = ''
    last_name: str = ''
    age: int = 0
    family: list = field(default_factory=list)


# >>> Person()
# Person(first_name='', last_name='', age=0, family=[])