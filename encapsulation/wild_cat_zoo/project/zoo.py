from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return f"Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return f"Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return f"Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if worker_name == w.name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if self.__budget < sum([x.salary for x in self.workers]):
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum([x.salary for x in self.workers])
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum_for_care = sum([x.money_for_care for x in self.animals])
        if self.__budget < sum_for_care:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= sum_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def wrap_all_animals_status(self, animal_type):
        result = ''

        animals = [str(x) for x in self.animals if x.__class__.__name__ == animal_type]
        result += f"----- {len(animals)} {animal_type}:\n"
        for a in animals:
            result += a
            result += '\n'
        return result

    def animals_status(self):
        result = ""
        result += f"You have {len(self.animals)} animals\n"

        result += self.wrap_all_animals_status('Lion')
        result += self.wrap_all_animals_status('Tiger')
        result += self.wrap_all_animals_status('Cheetah')

        return result

    def wrap_all_workers_status(self, worker_type):
        result = ''

        workers = [str(x) for x in self.workers if x.__class__.__name__ == worker_type]
        result += f"----- {len(workers)} {worker_type}:\n"
        for w in workers:
            result += w
            result += '\n'
        return result

    def workers_status(self):
        result = ""
        result += f"You have {len(self.workers)} workers\n"

        result += self.wrap_all_workers_status('Keeper')
        result += self.wrap_all_workers_status('Caretaker')
        result += self.wrap_all_workers_status('Vet')

        return result