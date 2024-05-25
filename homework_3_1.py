
"""Рекомендації для виконання:

Імпортуйте модуль datetime.
Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
Отримайте поточну дату, використовуючи datetime.today().
Розрахуйте різницю між поточною датою та заданою датою.
Поверніть різницю у днях як ціле число."""


from datetime import datetime

def get_days_from_todays(date):

    date_dt = datetime.strptime(date, "%Y-%m-%d").date()

    current_date = datetime.today().date()
    delta_days = current_date - date_dt
    return delta_days.days


if __name__ == "__main__":
    print(get_days_from_todays("2024-05-25"))





# now = datetime.today()

# formatted_date = now.strftime("%Y-%m-%d")
# print(formatted_date)

# current_date =  
# given_date = 

# def get_days_from_today(date):
#     date = datetime.date(2021, 10, 9)
#     print(date)
