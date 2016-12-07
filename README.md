# Avro schema test suite [![Build Status](https://travis-ci.org/mcupak/avro-schema-test-base.svg?branch=develop)](https://travis-ci.org/mcupak/avro-schema-test-base) [![GitHub license](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://raw.githubusercontent.com/mcupak/avro-schema-test-base/develop/LICENSE)

Module containing generic tests of Avro IDL schemata.

## How to build

Prerequisites: Python 2.7 (incl. Pip 7+).

Install dependencies with `pip install -r requirements.txt`. To check the test code style violations, run `flake8`.

## How to use

Install this module as a dependency in your project. You can use the following `requirements.txt` snippet:
 
```
-e git+https://github.com/mcupak/avro-schema-test-base.git@master#egg=avro-schema-test-base
avro
humanize
nose
requests
```

The master branch contains the latest release. To link to a specific release, replace `master` with the tag ID on the first line of the snippet.

Run `pip install -r requirements.txt` to process the file. The tests are installed as an editable module under `src/avro-schema-test-base`. Use `nosetests -v` to run the tests.
