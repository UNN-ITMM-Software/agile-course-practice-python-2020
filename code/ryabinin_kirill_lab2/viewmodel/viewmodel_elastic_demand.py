from re import split

from ryabinin_kirill_lab2.model.model_elastic_of_demand import ElasticOfDemand


class ViewModelElasticOfDemand:
    def __init__(self):
        self.start_demand = ''
        self.end_demand = ''
        self.start_price = ''
        self.end_price = ''
        self.start_salary = ''
        self.end_salary = ''
        self.type_price = ''
        self.type_salary = ''

    def set_arguments_from_array(self, array):
        self.start_demand = array[0]
        self.end_demand = array[1]
        self.start_price = array[2]
        self.end_price = array[3]
        self.start_salary = array[4]
        self.end_salary = array[5]

    def get_arguments_array(self):
        return [self.start_demand, self.end_demand, self.start_price,
                self.end_price, self.start_salary, self.end_salary]

    def get_type_price(self):
        return self.type_price

    def get_type_salary(self):
        return self.type_salary

    def calc_by_price(self):
        sd = int(split(r'\n', self.start_demand)[0]) if self.start_demand != '\n' else None
        ed = int(split(r'\n', self.end_demand)[0]) if self.end_demand != '\n' else None
        sp = int(split(r'\n', self.start_price)[0]) if self.start_price != '\n' else None
        ep = int(split(r'\n', self.end_price)[0]) if self.end_price != '\n' else None
        demand = ElasticOfDemand(start_demand=sd, end_demand=ed, start_price=sp, end_price=ep)
        self.type_price, _ = demand.by_price()

    def calc_by_salary(self):
        sd = int(split(r'\n', self.start_demand)[0]) if self.start_demand != '\n' else None
        ed = int(split(r'\n', self.end_demand)[0]) if self.end_demand != '\n' else None
        ss = int(split(r'\n', self.start_salary)[0]) if self.start_salary != '\n' else None
        es = int(split(r'\n', self.end_salary)[0]) if self.end_salary != '\n' else None
        demand = ElasticOfDemand(start_demand=sd, end_demand=ed, start_salary=ss, end_salary=es)
        self.type_salary, _ = demand.by_salary()
