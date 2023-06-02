class Transaction:
    def __init__(self, id_, date, description, from_, to_, operation_amount, state):
        self.__id = id_
        self.__date = date
        self.__description = description
        self.__from = from_
        self.__to = to_
        self.__operationAmount = operation_amount
        self.__state = state

    def __repr__(self):
        return f"Экземпляр класса 'Transaction', id операции - {self.__id}"

    @property
    def id(self):
        """Функция, возвращающая 'id' операции"""
        return self.__id

    @property
    def date(self):
        """Функция, возвращающая дату операции"""
        # делим строку исходной даты по символу 'T'
        # получаем список, где первый элемент это дата в формате 2018-03-09
        # из формата 2018-03-09 получаем список вида ['2018', '03', '09']
        __date = self.__date.split('T')[0].split('-')

        # переворачиваем список из формата ['2018', '03', '09'] в формат ['09', '03', '2018']
        __date.reverse()

        # объединяем список символом '.', получаем дату в нужном формате и возвращаем его
        return '.'.join(__date)

    @property
    def description(self):
        """Функция, возвращающая описание операции"""
        return self.__description

    @property
    def from_(self):
        """Функция, возвращающая откуда был произведён перевод операции"""
        # если отсутствует информация об источнике перевода, то возвращаем пустую строку
        if not self.__from:
            return ""

        # переводим в список с разделением по пробелам
        __from = self.__from.split(" ")

        # извлекаем номер карты. Номер карты должен быть записан без пробелов
        card_number = __from.pop()

        # формируем список по требуемому формату
        __from.extend([card_number[:4], card_number[4:8][:2] + "**", "****", card_number[12:]])

        # удаляем пустые значения в списке (пробелы между словами)
        __from = [item for item in __from if item != ""]

        # возвращаем результат
        return " ".join(__from)

    @property
    def from_to(self):
        """Функция, возвращающая откуда и куда был выполнен перевод операции"""
        return f'{self.from_} -> {self.to_}'

    @property
    def to_(self):
        """Функция, возвращающая куда был произведён перевод операции"""
        # если отсутствует информация об адресате перевода, то возвращаем пустую строку
        if not self.__to:
            return ""

        # переводим в список с разделением по пробелам
        __to = self.__to.split(' ')

        # извлекаем номер счёта, берём последние 4 цифры счёта
        account_number = f"**{__to.pop()[-4:]}"

        # добавляем в список номер счёта
        __to.append(account_number)

        # удаляем пустые значения в списке (пробелы между словами)
        __to = [item for item in __to if item != ""]

        # возвращаем результат
        return ' '.join(__to)

    @property
    def amount(self):
        """Функция, возвращающая сумму операции"""
        return f'{self.__operationAmount["amount"]} {self.__operationAmount["currency"]["name"]}'

