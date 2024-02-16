import requests
from Company import Company

class Employee:
    base_url = "https://x-clients-be.onrender.com"
    company = Company(base_url)

    def __init__(self, base_url=None):
        pass          
    
    #Получить список сотрудников для компании
    def employee_list(self, params_to_add= None):
        lists = requests.get(self.base_url+"/employee", params= params_to_add)
        return lists.json()

    #Создать нового сотрудника
    def create_employee(self, id_company, first_name, last_name, middle_name, phone = "89991234567", url = ""):
        dictionary_new_employee = {
            "companyId": id_company,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "phone": phone,
            "url": url
        }
        company = Company(self.base_url)
        my_token = {}
        my_token["x-client-token"] = company.get_token()
        new_employee = requests.post(self.base_url+"/employee", json=dictionary_new_employee, headers=my_token)
        return new_employee.json()
    
    #Получить сотрудника по ИД 
    def get_employee_id(self, id):
        employee = requests.get(self.base_url+"/employee/"+str(id))
        return employee.json()
    
    # #Изменить информацию о сотруднике
    # def change_info_employee(self, id, info):

    #     my_token = {}
    #     my_token["x-client-token"] = self.company.get_token()

    #     change_info = requests.patch(self.base_url+"/employee/"+str(id), json=info, headers=my_token)
    #     return change_info.json()

    #Изменить информацию о сотруднике
    def change_info_employee(self, id, last_name, email):
        info = {
            "lastName": last_name,
            "email": email,
            "isActive": True
        }
        company = Company(self.base_url)
        my_token = {}
        my_token["x-client-token"] = company.get_token()

        change_info = requests.patch(self.base_url+"/employee/"+str(id), json=info, headers=my_token)
        return change_info.json()
