from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        for c in self.customers:
            if c.id == customer.id:
                return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        for t in self.trainers:
            if t.id == trainer.id:
                return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        for e in self.equipment:
            if e.id == equipment.id:
                return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        for p in self.plans:
            if p.id == plan.id:
                return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        for s in self.subscriptions:
            if s.id == subscription.id:
                return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result = ''
        result += '\n'.join([str(d) for d in self.subscriptions]) + '\n'
        result += '\n'.join([str(d) for d in self.customers])+ '\n'
        result += '\n'.join([str(d) for d in self.trainers])+ '\n'
        result += '\n'.join([str(d) for d in self.equipment])+ '\n'
        result += '\n'.join([str(d) for d in self.plans])+ '\n'




        return result