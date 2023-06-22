from setuptools import setup, find_packages

setup(
    name="when_birthday",
    description="Script for known when birthday of employee",
    version="1.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["when_birthday = when_birthday.birthday:main"]},
)
