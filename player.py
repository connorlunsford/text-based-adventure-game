class Player:

    def __init__(self, id: str, inventory: list):
        # contains id for the player
        self._id = id
        # contains list of objects player currently has
        self._inventory = inventory

    # methods