from abc import ABC, abstractmethod


class SalaryManager:

    def __init__(self, salary_profession_handler):
        self.salary_profession_handler = salary_profession_handler

    def calculate_salary(self):
        return self.salary_profession_handler.salary(self)

    def __repr__(self):
        return '  '.join([str(self.salary_profession_handler.__class__), str(self.calculate_salary())])


class SalaryProfessionHandler(ABC):

    @abstractmethod
    def salary(self, salary_manager):
        """get salary"""


class WorkerSalaryHandler(SalaryProfessionHandler):

    def salary(self, salary_manager):
        return 10.0


class ChiefSalaryHandler(SalaryProfessionHandler):

    def salary(self, salary_manager):
        return 13.0


class TopManagerSalaryHandler(SalaryProfessionHandler):

    def salary(self, salary_manager):
        return 20.0


worker = WorkerSalaryHandler()
sm1 = SalaryManager(worker)
print(sm1)

worker = TopManagerSalaryHandler()
sm2 = SalaryManager(worker)
print(sm2)
