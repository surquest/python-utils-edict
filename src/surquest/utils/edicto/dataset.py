
from .attribute import Attribute

class Dataset:

    def __init__(self, data: list[dict]):
        self.data = data

    def __len__(self):
        return len(self.data)
    
    def select(self, attributes: list[str]) -> 'Dataset':
        """Method to select attributes from the dataset

        Args:
            attributes (list[str]): List of attributes to select

        Returns:
            Dataset: New dataset with selected attributes

        Example:

        ```python

        dataset = Dataset([
            {'id': 1, 'name': 'Charles Dickens', 'yearOfBirth': 1812, 'yearOfDeath': 1870, 'location': {'city': 'London', 'country': 'UK'}},
            {'id': 2, 'name': 'Jane Austen', 'yearOfBirth': 1775, 'yearOfDeath': 1817, 'location': {'city': 'Steventon', 'country': 'UK'}},
            {'id': 3, 'name': 'Mark Twain', 'yearOfBirth': 1835, 'yearOfDeath': 1910, 'location': {'city': 'Florida', 'country': 'USA'}},
            {'id': 4, 'name': 'Ernest Hemingway', 'yearOfBirth': 1899, 'yearOfDeath': 1961, 'location': {'city': 'Oak Park', 'country': 'USA'}},
            {'id': 5, 'name': 'F. Scott Fitzgerald', 'yearOfBirth': 1896, 'yearOfDeath': 1940, 'location': {'city': 'St. Paul', 'country': 'USA'}}
        ])
        
        # Select attributes 'name', 'yearOfBirth', 'location.city'
        out = dataset.select(['name', 'yearOfBirth', 'location.city'])

        # Output:
        out.show()
        # [
        #    {'name': 'Charles Dickens', 'yearOfBirth': 1812, 'location': {'city': 'London'}},
        #    {'name': 'Jane Austen', 'yearOfBirth': 1775, 'location': {'city': 'Steventon'}},
        #    {'name': 'Mark Twain', 'yearOfBirth': 1835, 'location': {'city': 'Florida'}},
        #    {'name': 'Ernest Hemingway', 'yearOfBirth': 1899, 'location': {'city': 'Oak Park'}},
        #
        # ]
        ```
        """

        selected_data = []
        for item in self.data:
            new_item = {}
            for attr in attributes:
                
                attribute = self.get_attribute(attr)

                new_item.update(self.get_nested(item, attribute))
            
            selected_data.append(new_item)
        
        return Dataset(selected_data)
    
    def filter(self, condition):
        return Dataset([item for item in self.data if condition(item)])
    
    @staticmethod
    def get_attribute(attribute):
        """Method to get attribute from a string
        
        Args:
            attribute (str): Attribute to get

        Returns:
            Attribute: Attribute object
        """

        if isinstance(attribute, Attribute):
            return attribute
        
        else:
            keys = attribute.split('.')
            
            if len(keys) == 1:
                attribute = Attribute(keys[0])

            else:
                attribute = Attribute(keys[0])
                for key in keys[1:]:
                    attribute.get(key)
            
            return attribute

    @staticmethod
    def get_nested(d, attribute):
        """Method to get nested value from a dictionary

        Args:
            d (dict): Dictionary to get nested value from
            attribute Attribute: Attribute object

        Returns:
            dict: Nested value from the dictionary
        """
    
        names = attribute.names
        aliases = attribute.aliases

        nested_value = Dataset.get_nested_value(d, names)
        
        renamed_dict = nested_value
        for key, alias in zip(reversed(names), reversed(aliases)):
            renamed_dict = {alias: renamed_dict}
        
        return renamed_dict
    
    @staticmethod
    def get_nested_value(d, keys):
        """Method to get nested value from a dictionary

        Args:
            d (dict): Dictionary to get nested value from
            keys (list[str]): List of keys to get nested value from

        Returns:
            dict: Nested value from the dictionary
        """

        for idx, key in enumerate(keys):
            if idx == len(keys) - 1:
                return d.get(key)
            d = d.get(key, {})
        return d