class Task:
    def __init__(self, description, status="To Do"):
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.description} - Status: {self.status}"


class Employee:
    def __init__(self, name, employee_id, salary):
        if not isinstance(name, str) or not isinstance(employee_id, str):
            raise TypeError("Numele și ID-ul angajatului trebuie să fie șiruri de caractere")
        if not isinstance(salary, (int, float)):
            raise TypeError("Salariul trebuie să fie un număr.")
        if salary < 0:
            raise ValueError("Salariul trebuie să fie un număr pozitiv.")

        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        if not isinstance(department, str):
            raise TypeError("Departamentul managerului trebuie să fie un șir de caractere.")
        self.department = department
        self.team = []
        self.team_assignments = {}

    def assign_task(self, engineer, description):
        task = Task(description)

        if engineer not in self.team_assignments:
            self.team_assignments[engineer] = []

        self.team_assignments[engineer].append(task)
        engineer.tasks.append(task)

    def view_team_tasks(self):
        print(f"\nEchipa lui {self.name}:")
        for engineer in self.team:
            print(f"    {engineer.name}")

            if engineer in self.team_assignments and self.team_assignments[engineer]:
                print("    Tascurile asignate:")
                for i, task in enumerate(self.team_assignments[engineer], 1):
                    print(f"    {i}. {task.description} - Status: {task.status}")
            else:
                print("    Nicio sarcină asignată pentru acest inginer.")
            print()

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_languages=None):
        super().__init__(name, employee_id, salary)
        if not isinstance(programming_languages, list) and programming_languages is not None:
            raise TypeError("Limbajele de programare trebuie să fie o listă sau None.")
        self.tasks = []
        self.programming_languages = programming_languages or []

    def display_info(self):
        super().display_info()
        print(f"Programming Languages: {', '.join(self.programming_languages)}")

    def update_task_status(self, task_index, new_status):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].status = new_status
        else:
            print("Index de sarcină invalid.")

    def generate_progress_report(self):
        print(f"Progresul sarcinilor pentru {self.name}:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print()


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target, sales=0):
        super().__init__(name, employee_id, salary)
        if not isinstance(sales_target, (int, float)):
            raise TypeError("Target-ul de vânzări trebuie să fie un număr.")
        if sales_target < 0:
            raise ValueError("Target-ul de vânzări trebuie să fie un număr pozitiv.")
        self.sales_target = sales_target
        self.sales = sales

    def display_info(self):
        super().display_info()
        print(f"Sales Target: ${self.sales_target}")
        print(f"Sales: ${self.sales}")

    def record_sale(self, amount):
        self.sales += amount
        print(f"Vânzare înregistrată: ${amount}")


if __name__ == '__main__':
    # Creare de instanțe
    manager1 = Manager("Manager1", "M1", 80000, "Marketing")
    engineer1 = Engineer("Inginer1", "E1", 70000)
    engineer2 = Engineer("Inginer2", "E2", 60000)
    manager1.team = [engineer1, engineer2]

    manager2 = Manager("Manager2", "M2", 85000, "Development")
    engineer3 = Engineer("Inginer3", "E3", 50000)
    manager2.team = [engineer1, engineer3]

    print("-----------------------")
    manager1.display_info()

    # Asignare tascuri
    manager1.assign_task(engineer1, "Code review")
    manager1.assign_task(engineer1, "Function implementation")
    manager1.assign_task(engineer2, "Unit testing")
    manager1.view_team_tasks()

    print("---------Update tasks----------")
    engineer1.update_task_status(0, "In Progress")
    engineer1.update_task_status(1, "Done")
    manager1.view_team_tasks()

    print("-----------------------")
    manager2.display_info()
    # Managerul 2 dă sarcini inginerului 1
    manager2.assign_task(engineer1, "Alt task pt inginer1")
    manager2.view_team_tasks()

    salesperson = Salesperson("Salesperson1", "S1", 60000, 100000, 500)
    salesperson.display_info()
    salesperson.record_sale(20000)


