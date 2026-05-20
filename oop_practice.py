# ==============================================================================
# Task 1. Python Classes Foundation (Blueprint and Object Creation)
# ==============================================================================

class ClientProfile:
    name = ''
    city = ''
    is_active = False

client_one = ClientProfile()

client_one.name = 'Alex'
client_one.city = 'Warsaw'
client_one.is_active = True

print(f'Client {client_one.name} lives in {client_one.city}. Status: {client_one.is_active}')