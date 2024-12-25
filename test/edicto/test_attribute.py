import pytest
from surquest.utils.edicto.attribute import Attribute

class TestAttribute:

    def test_simple_string_attribute(self):

        attribute = Attribute("name")

        assert attribute.get_name() == "name"
        assert attribute.get_alias() == "name"
        assert attribute.depth == 1
        assert attribute.names == ["name"]
        assert attribute.aliases == ["name"]


    def test_simple_attribute_with_alias(self):
            
        attribute = Attribute("name").alias("surname")

        assert attribute.get_name() == "name"
        assert attribute.get_alias() == "surname"
        assert attribute.depth == 1
        assert attribute.names == ["name"]
        assert attribute.aliases == ["surname"]

    def test_nested_simple_string_attribute(self):

        attribute = Attribute("location.city")

        assert attribute.depth == 2
        assert attribute.names == ["location", "city"]
        assert attribute.aliases == ["location", "city"]
        assert attribute.get_name(index=0) == "location"
        assert attribute.get_name(index=1) == "city"
        assert attribute.get_alias(index=0) == "location"
        assert attribute.get_alias(index=1) == "city"

    def test_nested_attribute_with_alias(self):

        attribute = Attribute("location").alias("loc").get("city").alias("town")

        assert attribute.depth == 2
        assert attribute.names == ["location", "city"]
        assert attribute.aliases == ["loc", "town"]
        assert attribute.get_name(index=0) == "location"
        assert attribute.get_name(index=1) == "city"
        assert attribute.get_alias(index=0) == "loc"
        assert attribute.get_alias(index=1) == "town"
