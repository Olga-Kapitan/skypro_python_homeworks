from address import Address
from mailing import Mailing

to_address = Address('137000', 'Moscow', 'Gromova', '50', '7')
from_address = Address('236000', 'Kaliningrad', 'Leninskiy', '30A', '25')
delivery1 = Mailing(to_address, from_address, 1000, 'P123LOK456789')

print(f'Отправление {delivery1.track} из {delivery1.from_address.index}, '
      f'{delivery1.from_address.city}, {delivery1.from_address.street}, '
      f'{delivery1.from_address.home} - {delivery1.from_address.flat} '
      f'в {delivery1.to_address.index}, {delivery1.to_address.city}, '
      f'{delivery1.to_address.street}, {delivery1.to_address.home} - '
      f'{delivery1.to_address.flat}. Стоимость {delivery1.cost} рублей.')
