# https://github.com/DanceDaemon/sem5-ISR3/blob/main/README.md

class book:
  def __init__(self):
    self.guests = list()

  def add_guest(self, name):
    self.guests.append({"Name": name})
        
  def delete_guest(self, name): 
    for guest in self.guests:
      if guest.get("Name") == name:
        self.guests.remove(guest)

  def record_file(self): 
    import json
    with open("./isr/isr_1/book.json", 'a') as file: 
      data = {"Guest": self.guests }
      json.dump(data, file) 

if __name__ == '__main__':
  book = book()
  i = 0
  while i == 0:
    action = str(input("Введите действие с книгой(A = add, D = delete), чтобы закончить введите E "))
    if action == "A":
      book.add_guest(input("Введите имя гостя "))
    if action == "D":
      book.delete_guest(input("Введите имя гостя "))
    if action == "E":
      i = 1
  book.record_file()