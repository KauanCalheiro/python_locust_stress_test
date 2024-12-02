from faker import Faker
import random

fake = Faker()


def generate_unique_username():
    return fake.user_name()


def calculate_min_birth_year(min_age):
    current_year = 2022
    return current_year - min_age


def generate_birth_date(min_age):
    min_year = calculate_min_birth_year(min_age)
    year = random.randint(min_year, 2006)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}"


def generate_foods(can_be_empty=True):
    if can_be_empty:
        foods = random.choice(
            [
                [],
                [fake.word()],
                [fake.word(), fake.word()],
                [fake.word(), fake.word(), fake.word()],
            ]
        )
    else:
        foods = random.choice(
            [
                [fake.word()],
                [fake.word(), fake.word()],
                [fake.word(), fake.word(), fake.word()],
            ]
        )
    return foods
