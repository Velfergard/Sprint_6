import random
from datetime import date, timedelta
from data import order_data


# Вспомогательные функции

def gen_phone():
    phone_base = ''
    operator_code = [
        "900", "901", "902", "903", "904", "905", "906", "908", "909", "910", "911", "912", "913", "914", "915", "916",
        "917", "918", "919", "920", "921", "922", "923", "924", "925", "926", "927", "928", "929", "930", "931", "932",
        "933", "934", "936", "937", "938", "939", "941", "942", "949", "950", "951", "952", "953", "954", "955", "956",
        "958", "959", "960", "961", "962", "963", "964", "965", "966", "967", "968", "969", "970", "971", "977", "978",
        "979", "980", "981", "982", "983", "984", "985", "986", "987", "988", "989", "990", "991", "992", "993", "994",
        "995", "996", "997", "999"
        ]
    for num in range(0, 7):
        phone_base += str(random.randint(0, 9))

    return random.choice(operator_code) + phone_base


def gen_delivery_date():
    sysdate = date.today()
    delivery_date = (sysdate + timedelta(random.randint(0, 7))).strftime("%d.%m.%Y")

    return delivery_date


def get_name():
    return random.choice(order_data.names)


def get_surname():
    return random.choice(order_data.surnames)


def get_address():
    return random.choice(order_data.addresses)


def gen_test_data_one():
    dataset_one = {
        "name": get_name(),
        "surname": get_surname(),
        "address": get_address(),
        "phone": f"+7{gen_phone()}",
        "delivery_date": gen_delivery_date(),
        "comment": "Просьба поднять самокат на 5 этаж!"
    }

    return dataset_one


def gen_test_data_two():
    dataset_two = {
        "name": get_name(),
        "surname": get_surname(),
        "address": get_address(),
        "phone": f"8{gen_phone()}",
        "delivery_date": gen_delivery_date(),
        "comment": " "
    }

    return dataset_two
