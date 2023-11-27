from address import Address
from mailing import Mailing


from_address = Address(756000, 'Moscow', "Pushkin", "41a", "24")
to_address = Address(724000, 'Chelyabinsk', "Kirov", "19", "4")

parcel = Mailing(from_address, to_address, 405.95, "R4563457tr4").sending_the_parcel()
