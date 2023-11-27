class Address:

    def __init__(self, index: int, city: str, street: str, building: str, apartment: str):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment

    def from_address(self):
        return f"{self.index}, {self.city}, {self.street}, {self.building}, {self.apartment}"

    def to_address(self):
        return f"{self.index}, {self.city}, {self.street}, {self.building}, {self.apartment}"
