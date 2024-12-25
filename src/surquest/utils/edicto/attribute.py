class Attribute:

    def __init__(self, name, data=None):

        self._names = name.split(".")
        self._aliases = name.split(".")
        self._data = data

    def get_alias(self, index=0):

        alias = self._aliases[index]

        return alias

    def get_name(self, index=0):

        name = self._names[index]

        return name

    def alias(self, alias):
        "Method to set alias for the attribute"

        # owerwrite the last alias in aliases with value from parameter alias
        self._aliases[-1] = alias
        return self

    def get(self, name):
        "Method to get nested attribute"
        self._names.append(name)
        self._aliases.append(name)
        return self
    
    @property
    def names(self):
        return self._names
    
    @property
    def aliases(self):
        return self._aliases
    
    @property
    def depth(self):
        return len(self._names)

    def get_value(self, data):
        """Method returns value from multi-level nested dictionary
        
        Args:
            data (dict): Dictionary to get value from

        Returns:
            dict: Value from the dictionary
        """

        for name in self._names:
            if name == self._names[-1]:
                return data.get(name, None)
            data = data.get(name, {})
        
        return data
    
    def __gt__(self, other):
        return lambda item: self.get_value(item) > other

    def __lt__(self, other):
        return lambda item: self.get_value(item) < other

    def __eq__(self, other):
        return lambda item: self.get_value(item) == other

    def __ge__(self, other):
        return lambda item: self.get_value(item) >= other

    def __le__(self, other):
        return lambda item: self.get_value(item) <= other

    def __ne__(self, other):
        return lambda item: self.get_value(item) != other
    
    def is_in(self, other):
        return lambda item: self.get_value(item) in other
    
    def is_not_in(self, other):
        return lambda item: self.get_value(item) not in other



    
