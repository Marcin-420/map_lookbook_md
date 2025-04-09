users: list = [
    {'name': 'Julia', 'location': 'Ząbki', 'posts': 10},
]

print(users)


def add_user(users_data: list) -> None:
    new_name: str = input('podaj imie nowego znajomego: ')
    new_location: str = input('podaj nazwę lokalizacji: ')
    new_posts: int = int(input('podaj liczbe postów: '))
    users.append({'name': new_name, 'location': new_location, 'posts': new_posts})


add_user(users)
print(users)
