from model import Creature

_creatures: list[Creature] = [
    Creature(name="Pikachu", age=25, country="Japan", area="Kanto"),
    Creature(name="Charmander", age=28, country="Japan", area="Kanto"),
]

def get_creature() -> list[Creature]:
    return _creatures