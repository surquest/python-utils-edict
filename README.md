![GitHub](https://img.shields.io/github/license/surquest/python-utils-qdict?style=flat-square)
![GitHub Workflow Status (with branch)](https://img.shields.io/github/actions/workflow/status/surquest/python-utils-qdict/test.yml?branch=main&style=flat-square)
![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/surquest/fcc48097b42581382bdd136320dca7f9/raw/f354104d2686c02ffd8c14253879ca004a488264/python-utils-qdict.json&style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/surquest-utils-qdict?style=flat-square)

# Introduction

This Python package provides a straightforward way to manipulate lists of multi-dimensional dictionaries. It includes support for the following core operations:

* **Attribute Selection**: Easily select specific attributes from your data and nested attributes.
* **Record Filtering**: Filter records based on custom conditions using a simple syntax.
* **List Joining**: Perform joins between lists of dictionaries based on a defined key.
* **Aggregation**: Aggregation function as `count` and `count_distinct` to summarize the data.

The package is designed for handling small to medium-sized datasets, offering convenience and simplicity. However, it is not optimized for large-scale big data processing.


## Getting Started

The package is available on the PyPi and can be installed by the following command:

```bash
pip install surquest-utils-qdict
```

Once the package is installed you can start using it by importing the `qdict` module:

```python
from surquest.utils.qdict import Dataset, Attribute as Attr, AND, OR

# Create the edicto dataset
authors = Dataset([
    {'id': 1, 'name': 'Charles Dickens', 'yearOfBirth': 1812, 'yearOfDeath': 1870, 'location': {'city': 'London', 'country': 'UK'}},
    {'id': 2, 'name': 'Jane Austen', 'yearOfBirth': 1775, 'yearOfDeath': 1817, 'location': {'city': 'Steventon', 'country': 'UK'}},
    {'id': 3, 'name': 'Mark Twain', 'yearOfBirth': 1835, 'yearOfDeath': 1910, 'location': {'city': 'Florida', 'country': 'USA'}},
    {'id': 4, 'name': 'Ernest Hemingway', 'yearOfBirth': 1899, 'yearOfDeath': 1961, 'location': {'city': 'Oak Park', 'country': 'USA'}},
    {'id': 5, 'name': 'F. Scott Fitzgerald', 'yearOfBirth': 1896, 'yearOfDeath': 1940, 'location': {'city': 'St. Paul', 'country': 'USA'}}
])

# Select the attributes
authors.select("id", "name").show(pretty=True)

# Select the attributes and the nested attributes
authors.select(Attr("id"), Attr("name"), "location.country").show(pretty=True)

# Alternative way to select the attributes and the nested attributes
authors.select(Attr("id"), Attr("name"), Attr("location").get("country")).show(pretty=True)

# Select the attributes and the nested attributes and alias the columns
authors.select(Attr("id"), Attr("name"), Attr("location").alias("loc").get("city").alias("town")).show(pretty=True)

# Filter the records
authors.filter(Attr("yearOfBirth") < 1800).select("id", "name").show(pretty=True)

# Complex filter
authors.filter(Attr("yearOfBirth") > 1800).filter(Attr("location.country") == "UK").select("id", "name").show(pretty=True)

# Join the datasets
books = Dataset([
    {'id': 1, 'title': 'A Tale of Two Cities', 'year': 1859, "author": {"id": 1}},
    {'id': 2, 'title': 'Great Expectations', 'year': 1861, "author": {"id": 1}},
    {'id': 3, 'title': 'Pride and Prejudice', 'year': 1813, "author": {"id": 2}},
    {'id': 4, 'title': 'Sense and Sensibility', 'year': 1811, "author": {"id": 2}},
    {'id': 5, 'title': 'Adventures of Huckleberry Finn', 'year': 1884, "author": {"id": 3}},
    {'id': 6, 'title': 'The Adventures of Tom Sawyer', 'year': 1876, "author": {"id": 3}},
    {'id': 7, 'title': 'The Old Man and the Sea', 'year': 1952, "author": {"id": 4}},
    {'id': 8, 'title': 'A Farewell to Arms', 'year': 1929, "author": {"id": 4}},
    {'id': 9, 'title': 'The Great Gatsby', 'year': 1925, "author": {"id": 5}},
    {'id': 10,'title': 'Tender Is the Night', 'year': 1934, "author": {"id": 5}}
])

authors.join(
    other=books,
    left_on="id",
    right_on="author.id",
    how="inner"
).select("name", "location.country", "title", "year").show(pretty=True)
```

# Local development

You are more than welcome to contribute to this project. To make your start easier we have prepared a docker image with all the necessary tools to run it as interpreter for Pycharm or to run tests.


## Build docker image
```
docker build `
     --tag surquest/utils/qdict `
     --file package.base.dockerfile `
     --target test .
```

## Run tests
```
docker run --rm -it `
 -v "${pwd}:/opt/project" `
 -w "/opt/project/test" `
 surquest/utils/qdict pytest
```