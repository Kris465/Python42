import requests


def get_vacancies(keyword, area='113'):

    # URL для запроса вакансий
    url = 'https://api.hh.ru/vacancies'

    # Параметры запроса
    params = {
        'text': keyword,  # Поисковый запрос
        'area': area,     # ID региона (например, 113 - Москва)
        'per_page': 20,   # Количество вакансий на странице
        'page': 0         # Номер страницы
    }

    # Выполнение GET-запроса
    response = requests.get(url, params=params)

    # Проверка успешности запроса
    if response.status_code == 200:
        data = response.json()  # Получение данных в формате JSON
        return data['items']     # Возвращаем список вакансий
    else:
        print(f"Ошибка: {response.status_code}")
        return []


def main():
    keyword = input("Введите ключевое слово для поиска вакансий: ")
    vacancies = get_vacancies(keyword)

    if vacancies:
        print(f"\nНайдено {len(vacancies)} вакансий:\n")
        for vacancy in vacancies:
            print(f"Название: {vacancy['name']}")
            print(f"Ссылка: {vacancy['alternate_url']}")
            print("-" * 40)
    else:
        print("Вакансии не найдены.")

if __name__ == "__main__":
    main()
