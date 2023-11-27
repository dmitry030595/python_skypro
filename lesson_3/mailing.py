from address import Address


class Mailing:

    def __init__(self, from_address: Address, to_address: Address, cost: float, track: str):
        self.from_address = from_address
        self.to_address = to_address
        self.cost = cost
        self.track = track

    def sending_the_parcel(self):
        print(f"Отправление {self.track} из {self.from_address.from_address()} в {self.to_address.to_address()}. "
              f"Стоимость {self.cost} рублей")
