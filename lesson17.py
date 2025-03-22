import json

JSON_FILE = 'cars.json'

def load_cars():
    with open(JSON_FILE, "r") as f:
        return json.load(f)

def save_cars(cars):

    with open(JSON_FILE, "w") as f:
        json.dump(cars, f, indent=4)
        print('Succesfully added to the db')

def add_car(cars): #cars = [] cars[-1]
    if cars:
        last_car = cars[-1]
        id = last_car.get('id') + 1
    else:
        id = 1

    new_car = {
        'id':id,
        'brand': input('Brand: '),
        'model': input('Model: '),
        'year': int(input('Year: ')),
        'price': float(input('Price: ')),
        'color': input('Color: ')
    }
    cars.append(new_car)
    save_cars(cars)

def get_all_cars(cars):
    if not cars:
        print('No cars in db')
        return
    for car in cars:
        print(f"ID: {car['id']}")
        print(f"Brand: {car['brand']}")
        print(f"Model: {car['model']}")
        print('-------------------------')

def get_car_by_id(cars):
    car_id = int(input('Id-ni daxil edin: '))
    for car in cars:
        if car.get('id') == car_id:
            print(f'\nCar details:')
            for key, value in car.items():
                print(f'{key.capitalize()} : {value}')
            return
    print('Car not found')

def update_car(cars):
    car_id = int(input('Id-ni daxil edin: '))
    for car in cars:
        if car.get('id') == car_id:
            car['brand'] = input(f'New brand({car.get('brand')}): ') or car['brand']
            car['model'] = input(f'New model({car.get('model')}): ') or car['model']

            year = input(f'New year({car.get('year')})')
            if year.isdigit() or year == '':
                if year == '':
                    car['year'] = car.get('year')
                else:
                    car['year'] = int(year)
            else:
                print('Dogru format daxil edilmedi')
                return

            price = input(f'New price({car.get('price')})')
            if price.isdigit() or price == '':
                if price == '':
                    car['price'] = car.get('price')
                else:
                    car['price'] = float(price)
            else:
                print('Dogru format daxil edilmedi')
                return
            
            car['color'] = input(f'New color({car.get('color')}): ') or car['color']
            save_cars(cars)
            print('Car updated successfully')
            return
    print('Car not found')

def delete_car(cars):
    car_id = int(input('Id-ni daxil edin: '))
    for index, car in enumerate(cars):
        if car.get('id') == car_id:
            del cars[index]
            save_cars(cars)
            print('Car deleted!')
            return
    print('Car not found')


while True:
    cars = load_cars()
    print("""
Choose according number:
1. Add new car
2. View all cars
3. View car details
4. Update car
5. Delete car
6. Exit
        """)
    choice = int(input("Ededi daxil edin: "))
    
    if choice == 1:
        add_car(cars)

    elif choice == 2:
        get_all_cars(cars)

    elif choice == 3:
        get_car_by_id(cars)

    elif choice == 4:
        update_car(cars)
    
    elif choice == 5:
        delete_car(cars)

    elif choice == 6:
        print('Exitted from the program')
        break

# A = ['A', 'B', 'C']
# for index, value in enumerate(A):
#     print(index, value)