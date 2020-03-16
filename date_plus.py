from subprocess import Popen
from subprocess import PIPE


def get_date():
    date_prc = Popen("date /t", shell=True, stdout=PIPE)
    text_date, error_date = date_prc.communicate()
    if error_date:
        text_date_d = "Произошла ошибка, дата неизвестно"
    else:
        text_date_d = text_date.decode("utf-8")
    return text_date_d


def visoknechnost(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 1
    else:
        return 0


month31 = 1, 3, 5, 7, 8, 10, 12
month30 = 4, 6, 9, 11


def date_finish():
    date_start = get_date()
    year_start = int(date_start[6:10])
    month_start = int(date_start[3:5])
    day_start = int(date_start[0:2])
    if month_start in month31:
        day_count = 31
    elif month_start in month30:
        day_count = 30
    elif visoknechnost(year_start) == 1:
        day_count = 29
    elif visoknechnost(year_start) == 0:
        day_count = 28
    day_finish = day_start + day_count
    month_finish = month_start
    year_finish = year_start
    if day_finish > day_count:
        day_finish = day_count - day_start
        month_finish = month_start + 1
        if month_finish > 12:
            year_finish = year_start + 1
    if month_finish < 10:
        date_finish_upd = '{}-0{}-{}'.format(year_finish, month_finish, day_finish)
    elif day_finish < 10:
        date_finish_upd = '{}-{}-0{}'.format(year_finish, month_finish, day_finish)
    elif month_finish < 10 and day_finish < 10:
        date_finish_upd = '{}-0{}-0{}'.format(year_finish, month_finish, day_finish)
    return date_finish_upd
















