# ==============================================================================
# Task 1. Python Classes Foundation (Blueprint and Object Creation)
# ==============================================================================

# class ClientProfile:
#     name = ''
#     city = ''
#     is_active = False

# client_one = ClientProfile()

# client_one.name = 'Alex'
# client_one.city = 'Warsaw'
# client_one.is_active = True

# print(f'Client {client_one.name} lives in {client_one.city}. Status: {client_one.is_active}')

# client_two = ClientProfile()

# client_two.name = 'Alena'
# client_two.city = 'Gdansk'
# client_two.is_active = False

# print(f'Client {client_two.name} lives in {client_two.city}. Status: {client_two.is_active}')

# ==============================================================================
# Task 2. Modern Object Initialization (Keyword Arguments Entry)
# ==============================================================================

from dataclasses import dataclass

@dataclass
class ClientProfile:
    name: str
    city: str
    is_active: bool

client_one = ClientProfile(name='Alex', city='Warsaw', is_active=True)
print(f'Client {client_one.name} lives in {client_one.city}. Status: {client_one.is_active}')

client_two = ClientProfile(name='Alena', city='Gdansk', is_active=False)
print(f'Client {client_two.name} lives in {client_two.city}. Status: {client_two.is_active}')