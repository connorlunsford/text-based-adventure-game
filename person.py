from interactable import Interactable

class Person(Interactable):

    def __init__(self, id: str, name: str, desc: str, sdesc: str, interactions: dict):
        super().__init__(id, name, desc, sdesc, interactions)
