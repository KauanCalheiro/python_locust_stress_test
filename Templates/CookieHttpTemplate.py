import random
from Generators.CookieDataGenerator import (
    generate_unique_username,
    generate_birth_date,
    generate_foods,
)


def post_cookies(user):
    user_name = generate_unique_username()
    birth_date = generate_birth_date(18)
    gender = random.choice(["m", "f"])
    foods = generate_foods()

    payload = {"user": user_name, "birth": birth_date, "gender": gender, "foods": foods}

    with user.client.post(
        f"/cookies",
        json=payload,
        name=f"POST",
        catch_response=True,
    ) as response:
        if response.status_code == 201:
            response_json = response.json()

            check_user = response_json["user"] == user_name
            check_birth = response_json["birth"] == birth_date
            check_gender = response_json["gender"] == gender
            check_foods = response_json["foods"] == foods
            check_id = "id" in response_json

            if check_user and check_birth and check_gender and check_foods and check_id:
                response.success()

        elif response.status_code == 422:
            response_json = response.json()

            check_message = "message" in response_json
            check_errors = "errors" in response_json

            if check_message and check_errors:
                response.success()

        else:
            response.failure("Unexpected response")


def get_cookies(user):
    with user.client.get(f"/cookies", name=f"GET", catch_response=True) as response:
        if response.status_code == 200:
            response_json = response.json()

            check_cookies = ("cookies" in response_json) and (
                isinstance(response_json["cookies"], list)
            )
            check_rows = ("rows" in response_json) and (
                isinstance(response_json["rows"], int)
            )

            if check_cookies and check_rows:
                response.success()
            else:
                response.failure("Missing 'cookies' or 'rows' in response")
        else:
            response.failure("Unexpected response")


def get_cookies_by_food(user):
    food_term = generate_foods(False).pop()

    with user.client.get(
        f"/cookies?term={food_term}",
        name=f"TERM",
        catch_response=True,
    ) as response:
        if response.status_code == 200:
            response_json = response.json()

            check_cookies = ("cookies" in response_json) and (
                isinstance(response_json["cookies"], list)
            )
            check_rows = ("rows" in response_json) and (
                isinstance(response_json["rows"], int)
            )

            if check_cookies and len(response_json["cookies"]) > 0:
                check_food = food_term in response_json["cookies"][0]["foods"]
            else:
                check_food = True

            if check_cookies and check_rows and check_food:
                response.success()
            else:
                response.failure("Missing 'cookies' or 'rows' in response")
        else:
            response.failure("Unexpected response")
