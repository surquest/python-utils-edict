import pytest
from surquest.utils.edicto.dataset import Dataset
from surquest.utils.edicto.attribute import Attribute


class TestDataset:

    DATASET = Dataset([
        {'id': 1, 'name': 'Charles Dickens', 'yearOfBirth': 1812, 'yearOfDeath': 1870, 'location': {'city': 'London', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
        {'id': 2, 'name': 'Jane Austen', 'yearOfBirth': 1775, 'yearOfDeath': 1817, 'location': {'city': 'Steventon', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
        {'id': 3, 'name': 'Mark Twain', 'yearOfBirth': 1835, 'yearOfDeath': 1910, 'location': {'city': 'Florida', 'country': 'USA', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
        {'id': 4, 'name': 'Ernest Hemingway', 'yearOfBirth': 1899, 'yearOfDeath': 1961, 'location': {'city': 'Oak Park', 'country': 'USA', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
        {'id': 5, 'name': 'F. Scott Fitzgerald', 'yearOfBirth': 1896, 'yearOfDeath': 1940, 'location': {'city': 'St. Paul', 'country': 'USA', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}
    ])

    @pytest.mark.parametrize(
        "selection, output",
        [
            (
                ["name", "yearOfBirth"],
                [
                    {'name': 'Charles Dickens', 'yearOfBirth': 1812},
                    {'name': 'Jane Austen', 'yearOfBirth': 1775},
                    {'name': 'Mark Twain', 'yearOfBirth': 1835},
                    {'name': 'Ernest Hemingway', 'yearOfBirth': 1899},
                    {'name': 'F. Scott Fitzgerald', 'yearOfBirth': 1896}
                ]
            ),
            (
                ["name", "yearOfBirth", "location.city"],
                [
                    {'name': 'Charles Dickens', 'yearOfBirth': 1812, 'location': {'city': 'London'}},
                    {'name': 'Jane Austen', 'yearOfBirth': 1775, 'location': {'city': 'Steventon'}},
                    {'name': 'Mark Twain', 'yearOfBirth': 1835, 'location': {'city': 'Florida'}},
                    {'name': 'Ernest Hemingway', 'yearOfBirth': 1899, 'location': {'city': 'Oak Park'}},
                    {'name': 'F. Scott Fitzgerald', 'yearOfBirth': 1896, 'location': {'city': 'St. Paul'}}
                ]
            ),
            (
                ["name", "yearOfBirth", "location.geo.lat"],
                [
                    {'name': 'Charles Dickens', 'yearOfBirth': 1812, 'location': {'geo': {'lat': 51.5074}}},
                    {'name': 'Jane Austen', 'yearOfBirth': 1775, 'location': {'geo': {'lat': 51.5074}}},
                    {'name': 'Mark Twain', 'yearOfBirth': 1835, 'location': {'geo': {'lat': 51.5074}}},
                    {'name': 'Ernest Hemingway', 'yearOfBirth': 1899, 'location': {'geo': {'lat': 51.5074}}},
                    {'name': 'F. Scott Fitzgerald', 'yearOfBirth': 1896, 'location': {'geo': {'lat': 51.5074}}}
                ]
            ),
            (
                ["name", "yearOfBirth", "location"],
                [
                    {'name': 'Charles Dickens', 'yearOfBirth': 1812, 'location': {'city': 'London', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
                    {'name': 'Jane Austen', 'yearOfBirth': 1775, 'location': {'city': 'Steventon', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
                    {'name': 'Mark Twain', 'yearOfBirth': 1835, 'location': {'city': 'Florida', 'country': 'USA', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
                    {'name': 'Ernest Hemingway', 'yearOfBirth': 1899, 'location': {'city': 'Oak Park', 'country': 'USA', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
                    {'name': 'F. Scott Fitzgerald', 'yearOfBirth': 1896, 'location': {'city': 'St. Paul', 'country': 'USA', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}
                ]
            ),
            (
                ["name", "sex"],
                [
                    {'name': 'Charles Dickens', 'sex': None},
                    {'name': 'Jane Austen', 'sex': None},
                    {'name': 'Mark Twain', 'sex': None},
                    {'name': 'Ernest Hemingway', 'sex': None},
                    {'name': 'F. Scott Fitzgerald', 'sex': None}
                ]
            ),
            (
                ["name", "location.street"],
                [
                    {'name': 'Charles Dickens', 'location': {'street': None}},
                    {'name': 'Jane Austen', 'location': {'street': None}},
                    {'name': 'Mark Twain', 'location': {'street': None}},
                    {'name': 'Ernest Hemingway', 'location': {'street': None}},
                    {'name': 'F. Scott Fitzgerald', 'location': {'street': None}}
                ]
            )
        ]
    )
    def test_select(self, selection, output):

        out = self.DATASET.select(selection)
        assert out.data == output

    @pytest.mark.parametrize(
        "selection, output",
        [
            (
                [Attribute("name"), Attribute("yearOfBirth")],
                [
                    {
                        'name': 'Charles Dickens',
                        'yearOfBirth': 1812
                    },
                    {
                        'name': 'Jane Austen',
                        'yearOfBirth': 1775
                    },
                    {
                        'name': 'Mark Twain',
                        'yearOfBirth': 1835
                    },
                    {
                        'name': 'Ernest Hemingway',
                        'yearOfBirth': 1899
                    },
                    {
                        'name': 'F. Scott Fitzgerald',
                        'yearOfBirth': 1896
                    }
                ]
                
            )
        ]
    )
    def test_select_with_attribute(self, selection, output):

        out = self.DATASET.select(selection)
        assert out.data == output



    def test_get_nested_value(self):

        d = {'location': {'city': 'London', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}
        keys = ['location', 'geo', 'lat']
        assert Dataset.get_nested_value(d, keys) == 51.5074

        d = {'location': 'London'}
        keys = ['location']
        assert Dataset.get_nested_value(d, keys) == 'London'

        d = {'location': {'city': 'London', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}
        keys = ['location', 'city']
        assert Dataset.get_nested_value(d, keys) == 'London'

        d = {'a': 1}
        keys = ()
        assert Dataset.get_nested_value(d, keys) == d

    def test_dataset_len(self):

        assert len(self.DATASET) == 5

    @pytest.mark.parametrize(
        "condition, output",
        [
            (
                Attribute("id") == 1,
                [{'id': 1, 'name': 'Charles Dickens', 'yearOfBirth': 1812, 'yearOfDeath': 1870, 'location': {'city': 'London', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}]
            ),
            (
                Attribute("id") < 2,
                [{'id': 1, 'name': 'Charles Dickens', 'yearOfBirth': 1812, 'yearOfDeath': 1870, 'location': {'city': 'London', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}]
            ),
            (
                Attribute("id") <= 2,
                [
                    {'id': 1, 'name': 'Charles Dickens', 'yearOfBirth': 1812, 'yearOfDeath': 1870, 'location': {'city': 'London', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
                    {'id': 2, 'name': 'Jane Austen', 'yearOfBirth': 1775, 'yearOfDeath': 1817, 'location': {'city': 'Steventon', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}
                ]
            ),
            (
                Attribute("id") > 4,
                [
                    {'id': 5, 'name': 'F. Scott Fitzgerald', 'yearOfBirth': 1896, 'yearOfDeath': 1940, 'location': {'city': 'St. Paul', 'country': 'USA', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}
                ]
            ),
            (
                Attribute("id") >= 5,
                [
                    {'id': 5, 'name': 'F. Scott Fitzgerald', 'yearOfBirth': 1896, 'yearOfDeath': 1940, 'location': {'city': 'St. Paul', 'country': 'USA', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}
                ]
            ),
            (
                Attribute("location.country").is_in(["UK"]),
                [
                    {'id': 1, 'name': 'Charles Dickens', 'yearOfBirth': 1812, 'yearOfDeath': 1870, 'location': {'city': 'London', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
                    {'id': 2, 'name': 'Jane Austen', 'yearOfBirth': 1775, 'yearOfDeath': 1817, 'location': {'city': 'Steventon', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}
                ]
            ),
            (
                Attribute("location.country").is_not_in(["USA"]),
                [
                    {'id': 1, 'name': 'Charles Dickens', 'yearOfBirth': 1812, 'yearOfDeath': 1870, 'location': {'city': 'London', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
                    {'id': 2, 'name': 'Jane Austen', 'yearOfBirth': 1775, 'yearOfDeath': 1817, 'location': {'city': 'Steventon', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}
                ]
            ),
            (
                Attribute("location.country") != "USA",
                [
                    {'id': 1, 'name': 'Charles Dickens', 'yearOfBirth': 1812, 'yearOfDeath': 1870, 'location': {'city': 'London', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}},
                    {'id': 2, 'name': 'Jane Austen', 'yearOfBirth': 1775, 'yearOfDeath': 1817, 'location': {'city': 'Steventon', 'country': 'UK', 'geo': {'lat': 51.5074, 'lon': 0.1278}}}
                ]
            )
        ]
        )
    def test_filter(self, condition, output):

        out = self.DATASET.filter(condition)
        assert out.data == output
