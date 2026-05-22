from address import Address
from mailing import Mailing

address_from = Address("765345", "Омск", "Красноармейская", "21", "8")
address_to = Address("098890", "Северодвинск", "Пушкина", "7", "55")


mailing1 = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=700,
    track="RU885353535"
)


print(f"Отправление {mailing1.track} из "
      f"{mailing1.from_address.index}, {mailing1.from_address.city}, "
      f"{mailing1.from_address.street}, {mailing1.from_address.house} - {mailing1.from_address.apartment} "  # noqa: E501
      f"в {mailing1.to_address.index}, {mailing1.to_address.city}, "
      f"{mailing1.to_address.street}, {mailing1.to_address.house} - {mailing1.to_address.apartment}. "  # noqa: E501
      f"Стоимость {mailing1.cost} рублей.")
