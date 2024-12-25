class Attribute:

    def __init__(self, name):

        self._names = name.split(".")
        self._aliases = name.split(".")

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