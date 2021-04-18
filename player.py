import object


class Player:

    def __init__(self, id: str):
        # contains id for the player
        self._id = id
        # contains list of objects player currently has
        self._inventory = []

    # methods for managing ID

    def get_id(self):
        # returns the value of self._id
        return self._id

    def set_id(self, id: str):
        # takes a string and sets it as the value of self._id
        return self._id     

    # methods for managing inventory

    def get_inventory(self):
        # returns the list of items the player has
        return self._inventory

    def add_to_inventory(self, obj: object.Object):
        # takes an Object object and adds it to the player's inventory list
        self._inventory.append(obj)
        return True

    def remove_from_inventory(self, obj: object.Object):
        """takes an Object object and checks to see if it's in the inventory.
        Removes it from the inventory and returns True if found, otherwise
        returns False"""
        if object in self._inventory:
            self._inventory.remove(obj)
            return True
        else:
            return False

    def search_inventory(self, obj: object.Object):
        """takes an Object object and checks to see if it's in the inventory
        and returns True if found"""
        if object in self._inventory:
            return True
        else:
            return False
