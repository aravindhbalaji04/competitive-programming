
import random

class RandomizedSet:

    def __init__(self):
        self.S = set()
        self.v = []

    def insert(self, val: int) -> bool:
        if len(self.S) == 0 or val not in self.S:
            self.S.add(val)
            self.v.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.S:
            self.S.remove(val)
            self.v.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.v)