class Price:
    def __init__(self, pick_up, return_date, car_model, *args):
        self.pick_up = pick_up
        self.return_date = return_date
        self.car_model = car_model
        self.list_of_accessories = []
