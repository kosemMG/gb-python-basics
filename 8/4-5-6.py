class PrinterColourError(Exception):
    def __init__(self, message: str):
        self.txt = message


class InvalidParamsError(Exception):
    def __init__(self, message: str):
        self.txt = message


class Warehouse:
    __storage = {'printers': 0, 'scanners': 0, 'copiers': 0}

    def __str__(self):
        return str(self.__storage)

    def receive(self, equipment):
        for key, value in equipment.items():
            try:
                self.__storage[key] += value
            except KeyError:
                print(f'There is no {key} in the storage.')

    def transfer(self, equipment, department: str):
        for key, value in equipment.items():
            try:
                if self.__storage[key] >= value:
                    self.__storage[key] -= value
                    print(f'{value} {key} were transferred to {department} department.')
                else:
                    print(f'Not enough {key} to transfer.')
            except KeyError:
                print(f'There is no {key} in the storage.')


class OfficeEquipment:
    def __init__(self, price, model):
        self._price = price
        self._model = model

    def __str__(self):
        return str(self.__dict__)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        self._price = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: str):
        self._model = value


class Printer(OfficeEquipment):
    def __init__(self, price, model, paper_capacity, colour):
        params = Printer.validate(price, model, paper_capacity, colour)
        if not params:
            raise InvalidParamsError('Invalid params. The object not created.')
        else:
            super().__init__(params['price'], params['model'])
            self.__paper_capacity = params['capacity']
            if params['colour'] == '0':
                self.__colour = 'black & white'
            else:
                self.__colour = 'full-colour'

    def print(self):
        print('I am printing!')

    @staticmethod
    def validate(price, model, paper_capacity, colour):
        result = False
        try:
            formatted_price = float(price)
            formatted_capacity = int(paper_capacity)
            if colour != '0' and colour != '1':
                raise PrinterColourError('Invalid colour type. Please, enter 0 or 1.')
        except ValueError:
            print('Invalid price/paper capacity input. Please, enter a number.')
        except PrinterColourError as err:
            print(err)
        else:
            result = {
                'price': formatted_price,
                'model': model,
                'capacity': formatted_capacity,
                'colour': colour
            }
        finally:
            return result


class Scanner(OfficeEquipment):
    def scan(self):
        print('I am scanning!')


class Copier(OfficeEquipment):
    def __init__(self, price, model, colour):
        super().__init__(price, model)
        if colour == '0':
            self.__colour = 'black & white'
        else:
            self.__colour = 'full-colour'

    def copy(self):
        print('I am copying!')


while True:
    try:
        printer = Printer(
            input('Please, enter the printer\'s price: '),
            input('Please, enter the printer\'s model: '),
            input('Please, enter the paper capacity: '),
            input('Please, choose the printer\'s colour (0 - black & white, 1 - full-colour): ')
        )
    except InvalidParamsError as err:
        print(err)
    else:
        break

print(printer)
print()
warehouse = Warehouse()
warehouse.receive({'printers': 3, 'scanners': 2})
print(warehouse)
warehouse.transfer({'printers': 1, 'scanners': 1, 'copiers': 1}, 'IT')
print(warehouse)
