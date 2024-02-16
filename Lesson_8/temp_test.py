from Employee import Employee
from Company import Company

base_url = "https://x-clients-be.onrender.com"


employee_instance = Employee(base_url)
#Сразу создадим организацию и сотрудника чтобы дальше работать только с ними
company_instance = Company(base_url)

# Позитивный тест для [GET] /employee
def test_get_positive():
    # Создаём новую организацию
    new_company = company_instance.create_company(name = 'NewTestCompany', description = 'tempForTest')
    new_id = new_company["id"]
    my_params = {
        "company": new_id
    }
    # Получаем список сотрудников новой организации
    lists_employee = employee_instance.employee_list(my_params)
    assert len(lists_employee) == 0 # Проверка что для только что созданной организации список сотрудников будет пуст
    
# Негативный тест для [GET] /employee
def test_get_negative():
    # Передаем неверный параметр
    response = employee_instance.employee_list(params_to_add='A')
    assert response['statusCode'] != 200 # Ожидаем сообщение о ошибке со статусом точно не 200 ок



# Позитивный тест для [POST] /employee
def test_create_employee_positive():    
    # Создаём новую организацию
    new_company = company_instance.create_company(name = 'NewTestCompany1', description = 'tempForTest1')
    new_id = new_company["id"]
    first_name = 'Ivan'
    last_name =  'Ivanov'
    middle_name = 'Ivanovich'

    response = employee_instance.create_employee(new_id, first_name, last_name, middle_name)
    assert response is not None
    assert response['id'] != 0  # Ожидаем что id прийдёт и будет не 0

# Негативный тест для [POST] /employee
def test_create_employee_negative():
    # Передаем неверные данные
    new_id = 0
    first_name = 'Ivan'
    last_name =  'Ivanov'
    middle_name = 'Ivanovich'

    response = employee_instance.create_employee(new_id, first_name, last_name, middle_name)
    assert response['statusCode'] != 200 # Ожидаем сообщение о ошибке со статусом точно не 200 ок

# Позитивный тест для [GET] /employee/{id}
def test_get_employee_id_positive():
    # Создаём новую организацию
    new_company = company_instance.create_company(name = 'NewTestCompany', description = 'tempForTest')
    new_id = new_company["id"]
    my_params = {
        "company": new_id
    }
    
    # Создаём сотрудника
    first_name = 'Ivan'
    last_name =  'Ivanov'
    middle_name = 'Ivanovich'
    response = employee_instance.create_employee(new_id, first_name, last_name, middle_name)

    # Получаем список сотрудников новой организации
    lists_employee = employee_instance.employee_list(my_params)
    
    last_employee_id = lists_employee[-1]["id"]
    last_employee = employee_instance.get_employee_id(last_employee_id)
    first_employee_id = lists_employee[0]["id"]
    first_employee = employee_instance.get_employee_id(first_employee_id)
    if last_employee_id == first_employee_id: 
        assert last_employee == first_employee
    else: assert last_employee != first_employee # если сотрудник не один то атрибуты первого и последнего сотрудника не одинаковые


# Негативный тест для [GET] /employee/{id}
def test_get_employee_id_negative():
    list_company = company_instance.get_company_list()
    id_company = list_company[-1]["id"]
    my_params = {
        "company": id_company
    }
    lists_employee = employee_instance.employee_list(my_params)
    last_employee_id = lists_employee[-1]["id"]
    last_employee = employee_instance.get_employee_id(last_employee_id)
    assert last_employee["id"] != last_employee["companyId"] # Что ИД компании не совпадёт с ИД сотрудника



def test_change_info_employee_positive():
     # Создаём новую организацию
    new_company = company_instance.create_company(name = 'NewTestCompany', description = 'tempForTest')
    new_id = new_company["id"]
   
    # Создаём сотрудника
    first_name = 'Ivan'
    last_name =  'Ivanov'
    middle_name = 'Ivanovich'
    new_employee = employee_instance.create_employee(new_id, first_name, last_name, middle_name)

    # Изменяем информацию о последнем сотруднике
    new_id = new_employee["id"]
    response = employee_instance.change_info_employee(new_id, "Name2", "email2@mail.ru")
    
    # Проверяем, что номер телефона после изменения равен указанному
    assert response["email"] == "email2@mail.ru" # Новый email применился


# Негативный тест для [PATCH] /employee/{id}
def test_change_info_employee_negative():
     # Создаём новую организацию
    new_company = company_instance.create_company(name = 'NewTestCompany', description = 'tempForTest')
    new_id = new_company["id"]
   
    # Создаём сотрудника
    first_name = 'Ivan'
    last_name =  'Ivanov'
    middle_name = 'Ivanovich'
    new_employee = employee_instance.create_employee(new_id, first_name, last_name, middle_name)

    # Изменяем информацию о последнем сотруднике
    new_id = new_employee["id"]
    response = employee_instance.change_info_employee(new_id, "Name2", "email2@")
    
    # Проверяем, что номер телефона после изменения равен указанному
    assert response['statusCode'] == 400 # Новый email применился