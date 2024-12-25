# Introduction

This python package simplifies the manipulation with the lists of multi-dimensional dictionaries as you would use SQL or pyspark dataframes. The basic set of supported operations are:

* selection of the attributes
* filtering of the records
* joining of the lists

The package is designed to simplify to operate small and mid-size datasets but it is not optimized for the big data processing.

## Getting Started

The package is available on the PyPi and can be installed by the following command:

```bash
pip install edicto
```

Once the package is installed you can start using it by importing the `edicto` module:

```python
import edicto

# Create the edicto dataset
authors = edicto.Dataset([
    {'id': 1, 'name': 'Charles Dickens', 'yearOfBirth': 1812, 'yearOfDeath': 1870, 'location': {'city': 'London', 'country': 'UK'}},
    {'id': 2, 'name': 'Jane Austen', 'yearOfBirth': 1775, 'yearOfDeath': 1817, 'location': {'city': 'Steventon', 'country': 'UK'}},
    {'id': 3, 'name': 'Mark Twain', 'yearOfBirth': 1835, 'yearOfDeath': 1910, 'location': {'city': 'Florida', 'country': 'USA'}},
    {'id': 4, 'name': 'Ernest Hemingway', 'yearOfBirth': 1899, 'yearOfDeath': 1961, 'location': {'city': 'Oak Park', 'country': 'USA'}},
    {'id': 5, 'name': 'F. Scott Fitzgerald', 'yearOfBirth': 1896, 'yearOfDeath': 1940, 'location': {'city': 'St. Paul', 'country': 'USA'}}
])

# Select the attributes
authors.select("id", "name")

# Select the attributes and the nested attributes
authors.select("id", "name", "location.country")

# Filter the records
authors.filter("yearOfBirth" > 1800).select("id", "name")

# Complex filter
authors.filter("yearOfBirth" > 1800).filter("location.country" == "UK").select("id", "name")

# Join the datasets
books = edicto.Dataset([
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
    dataset=books,
    left_on="id",
    right_on="authorId"
    join_type="inner"
).select("name", "location.country", "title", "year")
```

# Local development

You are more than welcome to contribute to this project. To make your start easier we have prepared a docker image with all the necessary tools to run it as interpreter for Pycharm or to run tests.


## Build docker image
```
docker build `
     --tag surquest/utils/edicto `
     --file package.base.dockerfile `
     --target test .
```

## Run tests
```
docker run --rm -it `
 -v "${pwd}:/opt/project" `
 -w "/opt/project/test" `
 surquest/utils/edicto pytest
```