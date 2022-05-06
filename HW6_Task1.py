"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    class Counter:
        counter = 0

        def __init__(self, ):
            Counter.counter += 1

        @classmethod
        def get_created_instances(cls):#returns the number of instances of the class created
            print(Counter.counter)
            return (Counter.counter)

        @classmethod
        def reset_instances_counter(cls):#reset instance counter, returns value before reset
            save_counter = Counter.counter
            Counter.counter = 0
            print (save_counter)
            return (save_counter)

    return Counter


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3