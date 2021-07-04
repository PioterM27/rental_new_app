from datetime import datetime, timedelta


class PriceCounter:
    def __init__(self, pick_up, return_date, price, *args):
        self.pick_up = pick_up
        self.return_date = return_date
        self.price = price
        self.list_of_accessories = []

    def count_number_of_days(self):
        first_date = datetime.strptime(self.pick_up, "%Y-%m-%d")
        second_date = datetime.strptime(self.return_date, "%Y-%m-%d")
        overall_days = second_date - first_date
        return overall_days.days

    def count_price(self):
        overall_price = self.price * int(str(self.count_number_of_days()))
        return overall_price
