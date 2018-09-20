class worker:
    raise_pay = 1.05
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def pay_raise(self):
        self.pay = int (self.pay * self.raise_pay)
    def all_of_them(self):
        return '{}, {}'.format(self.name, self.pay)
worker_one = worker ('Kimani', 10000)
worker_two = worker ('Obaga', 5000)
print(worker_one.all_of_them())
print(worker_two.all_of_them())
   #or
print(worker_one.raise_pay)
worker_one.pay_raise
print(worker_one.raise_pay)
   #or
print(worker_two.raise_pay)
worker_two.pay_raise
print(worker_two.raise_pay)
   #or
print(worker_one.pay)
worker_one.pay_raise()
print(worker_one.pay)
   #or
print(worker_two.pay)
worker_two.pay_raise()
print(worker_two.pay)