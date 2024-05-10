class My_List:
    def __init__(self):
        self.mylist = []

    def add_numbers(self, numbers):
        self.mylist.extend(numbers)

    def find_pairs(self, target):
        for i in range(len(self.mylist)):
            for j in range(i+1, len(self.mylist)):
                if self.mylist[i] + self.mylist[j] == target:
                    return (i, j)
        return -1

# Example usage:
my_list = My_List()
my_list.add_numbers([1, 2, 3, 4, 5])
target_number = int(input("Reqem daxil et: "))
result = my_list.find_pairs(target_number)
print(f"Pairs for target number {target_number}: {result}")
