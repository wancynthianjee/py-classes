class Student:
    school="AkiraChix"

    def __init__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    def greet_student(self):
        return f"Hello{self.name} from {self.country} welcome to{self.school}"
    def get_fullnames(self):
        return f" {self.first_name + ""} {self.last_name}"
    def year_of_birth(self):
        return 2023 -{self.age}
    def get_initials(self):
        return{self.f[0]}+ {self.last_name[0]}