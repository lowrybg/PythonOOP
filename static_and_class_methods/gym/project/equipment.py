class Equipment:
    id = 1
    def __init__(self, name):
        self.name = name
        self.id = Equipment.get_next_id()

    # def get_next_id(self):
    #     return self.equipment_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"


    @staticmethod
    def get_next_id():
        res = Equipment.id
        Equipment.id += 1
        return res










# print(Equipment._id)
# c = Equipment('mamam')
# c2 = Equipment('kdkdk')
# print(c.equipment_id)
# print(c2.equipment_id)
# print(c.get_next_id())
# print(c.get_next_id())