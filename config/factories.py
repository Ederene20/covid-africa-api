from orator.orm import Factory
from app.User import User
from app.Country import Country

from random import randrange
factory = Factory()


def users_factory(faker):
    return {
        'name': faker.name(),
        'email': faker.email(),
        'password': '$2b$12$WMgb5Re1NqUr.uSRfQmPQeeGWudk/8/aNbVMpD1dR.Et83vfL8WAu',  # == 'secret'
    }


def countries_factory(faker):
    return {
        'name': faker.country(),
        'case_number': randrange(1, 100),
        'case_death': randrange(1, 100),
        'case_recovered': randrange(1, 100)
    }


factory.register(User, users_factory)
factory.register(Country, countries_factory)
