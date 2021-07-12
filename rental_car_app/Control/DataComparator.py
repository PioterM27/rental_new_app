from datetime import datetime, timedelta


class DataComparator:
    def __init__(self, start_date, finish_date, rents):
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.finish_date = datetime.strptime(finish_date, "%Y-%m-%d").date()
        self.rents = rents

    def check_car_avability(self):
        list_of_cars = []
        for rent in self.rents:
            if (
                self.start_date < rent["pickUp_date"]
                and self.finish_date < rent["pickUp_date"]
            ):
                continue
            elif self.start_date > rent["return_date"]:
                continue
            else:
                list_of_cars.append(rent["car_id"])

        return list_of_cars
