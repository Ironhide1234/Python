import sys
from datetime import date, datetime
import os
import json
import uuid


class Pizza:
    def __init__(self):
        with open("pizza_storage.json") as file:
            self.pizza_day = json.load(file)

    def get_pizza_price(self):
        return self.pizza_day[self.__class__.__name__[:-5]]["price"]

    def get_pizza_ingr(self):
        return self.pizza_day[self.__class__.__name__[:-5]]["ingredients"]

    def get_pizza_name(self):
        return self.pizza_day[self.__class__.__name__[:-5]]["name"]


class MondayPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_day = self.pizza_day[0]


class TuesPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_day = self.pizza_day[1]


class WednesdayPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_day = self.pizza_day[2]


class ThursdayPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_day = self.pizza_day[3]


class FridayPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_day = self.pizza_day[4]


class SaturdayPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_day = self.pizza_day[5]


class SundayPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_day = self.pizza_day[6]


class Customer:
    def __init__(self, name, surname):
        if not (isinstance(name, str) and isinstance(surname, str)):
            raise TypeError("Name and Surname fields must contain only letters")
        self.name = name
        self.surname = surname

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @staticmethod
    def __check_value(value):
        if not isinstance(value, str):
            raise TypeError("Wrong type of value")
        if not value:
            raise ValueError("Wrong Value")
        return True

    @name.setter
    def name(self, value):
        if Customer.__check_value(value):
            self.__name = value

    @surname.setter
    def surname(self, value):
        if Customer.__check_value(value):
            self.__surname = value

    def __str__(self):
        return f"Customer info:\nName:{self.__name}\nSurname:{self.__surname}"


class Order:
    def __init__(self, cust):
        if not isinstance(cust, Customer):
            raise TypeError("Wrong type")
        self.customer = cust
        self._id = uuid.uuid1()

    def check_day(buy_date):
        return buy_date.strftime("%A")

    def additional_ingr(self, add_ingr: dict):
        if not os.path.exists("additional_ingr.json"):
            raise FileNotFoundError
        if not isinstance(add_ingr, dict):
            raise TypeError("Wrong type of ingredients")
        with open("additional_ingr.json") as file:
            additional_ingredients = json.load(file)
        for ingredient in add_ingr:
            if not additional_ingredients.get(ingredient):
                raise ValueError("No such ingredient in the list")
            if not (
                isinstance(ingredient, str) and isinstance(add_ingr[ingredient], int)
            ):
                raise ValueError(
                    "Wrong data value(ingredient must be string and quantity must be int)"
                )

        if additional_ingredients[ingredient] - add_ingr[ingredient] < 0:
            raise ValueError(f"Not enough quantity of {ingredient}")
        additional_ingredients[ingredient] -= add_ingr[
            ingredient
        ]  # we subrtract from the orig list needed quant
        with open("additional_ingr.json", "w") as file:
            json.dump(additional_ingredients, file)
        return add_ingr

    def get_pizza_to_day(self, day):
        pizza_to_day = {
            "Monday": MondayPizza(),
            "Tuesday": TuesPizza(),
            "Wednesday": WednesdayPizza(),
            "Thursday": ThursdayPizza(),
            "Friday": FridayPizza(),
            "Saturday": SaturdayPizza(),
            "Sunday": SundayPizza(),
        }
        return pizza_to_day[day]

    def construct_pizza_data(self, buydate, pizza, addit_prod):
        storage = {}
        storage[str(self._id)] = {}
        storage[str(self._id)]["name"] = self.customer.name
        storage[str(self._id)]["surname"] = self.customer.surname
        storage[str(self._id)]["name_of_the pizza"] = pizza.get_pizza_name()
        storage[str(self._id)]["ingredients"] = pizza.get_pizza_ingr()
        storage[str(self._id)]["aditional_ingredients"] = addit_prod
        storage[str(self._id)]["price"] = pizza.get_pizza_price()
        storage[str(self._id)]["purchase day"] = buydate
        return storage

    def buy(self, addit_prod={}):
        order_date = Order.check_day(date.today())
        pizza = self.get_pizza_to_day(order_date)
        checked_prod = self.additional_ingr(addit_prod)

        with open("orders.json", "r") as file:
            strg = json.load(file)
            strg.append(self.construct_pizza_data(order_date, pizza, checked_prod))
        with open("orders.json", "w") as file:
            json.dump(strg, file)


customer = Customer("Arseniy", "Mets")
order = Order(customer)
order.buy({"pineapple pieces": 100})
