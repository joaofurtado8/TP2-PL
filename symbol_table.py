import pprint

class SymbolTable:
    def init(self):
        self._data = {}

    def re_set(self, key, value):
        if key in self._data:
            self._data[key].append(value)
        else:
            self[key] = value

    def getitem(self, item):
        if item in self._data:
            return self._data[item][-1]
        else:
            raise Exception(f"Out of bounds: {item} not found")


    def setitem(self, key, value):
        if key in self._data:
            self._data[key][-1] = value
        else:
            self._data[key] = [value]

    def delitem(self, key):
        if key in self._data:
            if len(self._data[key]) == 1:
                del self._data[key]
            else:
                self._data[key].pop()
        else:
            raise Exception(f"Out of bounds: {key} not found")

    def contains(self, item):
        return item in self._data