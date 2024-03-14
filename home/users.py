from bank import MiniMbank

islam_mbank = MiniMbank('Isa', 19, 20_000_000_000, 5555)

print(islam_mbank.name)
islam_mbank.name = 'Islam'
print(islam_mbank.name)

print(islam_mbank.age)
islam_mbank.age = 20
print(islam_mbank.age)

print(islam_mbank.money)
islam_mbank.money = 20_000_000
print(islam_mbank.money)

print(islam_mbank.key)
islam_mbank.key = 4444
print(islam_mbank.key)