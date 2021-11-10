class Order:
    def __init__(self, name, surname):
        if not isinstance(name, str) or not isinstance(surname, str):
            raise
        self.name = name
        self.surname = surname

        self.commodities = []
        self.summ = 0

    def orders(self, commodity, price):
        if price < 0:
            raise
        self.commodities.append(commodity)
        self.summ += price

    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\n' \
               f'Order price: {self.summ}₴\n' \
               'Order: ' + ', '.join(self.commodities)

    def __iter__(self):
        return OrderIterator(self.commodities)

    def __getitem__(self, index):
        if isinstance(index, slice):
            if index.start < 0 or index.stop > len(self.commodities):
                raise IndexError
            else:
                result = []
                start = 0 if index.start is None else index.start
                stop = len(self.commodities) - 1 if index.stop is None else index.stop
                step = 1 if index.step is None else index.step

                for i in range(start, stop, step):
                    result.append(self.commodities[i])
                return result

        if isinstance(index, int):
            if index < len(self.commodities):
                return self.commodities[index]
            else:
                raise IndexError
        raise TypeError()


class OrderIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index = self.index + 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


customer = Order('Ivan', 'Ivanov')
customer.orders('Garnet', 39.95)
customer.orders('Pineapple', 45.99)
customer.orders('Orange', 41.95)
print(customer)
for order in customer[0:3]:
    print(order)
print(customer[1])