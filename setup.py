import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="avro-schema-test-base",
    version="0.1.0",
    author="Miro Cupak",
    author_email="mirocupak@gmail.com",
    description="Base for tests of Avro IDL schemas",
    url="https://github.com/mcupak/avro-schema-test-base",
    license="Apache 2",
    packages=['tests'],
    classifiers=[
        "License :: OSI Approved :: Apache 2 License",
    ]
)
