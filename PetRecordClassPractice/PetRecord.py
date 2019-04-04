class PetRecord:
    num_no_name = 0
    def __init__(self, name = 'none', age = -1, weight = -1):
        self._name = name
        self._age = age
        self._weight = weight
        if self._name == 'none':
            PetRecord.num_no_name += 1

    def print_name(self):
        print(self._name)

    def __str__(self):
        return self._name + ", " + str(self._age) + ", " + str(self._weight)


p0 = PetRecord()
p1 = PetRecord("Borf", 4, 5)
p2 = PetRecord("Dan", 4, 5)
p3 = PetRecord("Sally", 4, 5)
p4 = PetRecord("Allen", 4, 5)
p5 = PetRecord("Bobert", 4, 5)
p6 = PetRecord("Ally", 4, 5)
p7 = PetRecord("Munchkin", 4, 5)
p8 = PetRecord("Predator", 4, 5)
p9 = PetRecord("Spoof", 4, 5)


pet_list = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]

for p in pet_list:
    print(p)

print("Number of pets with no names:", p1.num_no_name)
