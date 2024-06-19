class Employee:
  def __init__(self,name,roll_no):
    self.name=name
    self.roll_no=roll_no
  def ShowDetails(self):
        print(f"Enter the Employee Details : {self.name} is {self.roll_no}")


e=Employee("Mrunali",4)
e.ShowDetails()



