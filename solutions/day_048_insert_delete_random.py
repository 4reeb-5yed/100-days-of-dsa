import random

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}
        self.vals = []
    
    def insert(self, val):
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.vals)
        self.vals.append(val)
        return True
    
    def remove(self, val):
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last = self.vals[-1]
        self.vals[index] = last
        self.val_to_index[last] = index
        self.vals.pop()
        del self.val_to_index[val]
        return True
    
    def get_random(self):
        if not self.vals:
            return None
        return random.choice(self.vals)