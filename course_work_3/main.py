from operator import itemgetter
from course_work_3.get_data import read_local_json
from course_work_3.transaction import Transaction


def last_operations(file_name, count):
    """Функция, которая выводит последние 'count' операций из файла"""
    # список последних 'count' операций
    transactions = []

    # если количество операций <= 0, то ничего не выдаём
    if count <= 0:
        return []

    # считыванием данные с файла JSON
    operations = read_local_json(file_name)

    # перебираем список словарей и удаляем пустые словари
    operations = [operate for operate in operations if operate != {}]

    # сортируем полученный список по дате и времени
    operations = sorted(operations, key=itemgetter('date'), reverse=True)

    # получаем последние 'count' выполненных записей
    operations = [operate for operate in operations if operate["state"] == "EXECUTED"][:count]

    # формируем список классов последних 'count' операций
    for operate in operations:
        transactions.append(Transaction(
            id_=operate.get("id"),
            date=operate.get("date"),
            description=operate.get("description"),
            from_=operate.get("from"),
            to_=operate.get("to"),
            operation_amount=operate.get("operationAmount"),
            state=operate.get("state")
        ))

    # возвращаем список классов последних 'count' операций
    return transactions


def main():
    # строка последних 'count' операций
    last_operations_str = ""

    # получаем список последних 5 операций
    transactions = last_operations("operations.json", 5)

    # проходим по последним 5 операциям и выводим информацию
    for transaction in transactions:
        last_operations_str += f"{transaction.date} {transaction.description}\n"
        last_operations_str += transaction.from_to + "\n"
        last_operations_str += transaction.amount + "\n\n"

    print(last_operations_str)


# вызываем главную функцию
main()

