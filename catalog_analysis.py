# Задание №1
import math  #для функций и вычислений

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):  #1
    total_rating = sum(movie["rating"] for movie in movies)  #2
    return round(total_rating / len(movies), 1)  #3
    #1 вернет среднюю оценку по каталогу, округлённую до одного знака.
    #2 складывает все значения 'rating' из 'movies через переменную movie
    #3 round округляет среднее арифметическое. ', 1' - это округление до 1 знака

def catalog_age_stats(movies, current_year=2026):  #1
    ages = [current_year - movie["year"] for movie in movies]  #2
    oldest = max(ages)  #3
    newest = min(ages)  #3
    average_age = math.ceil(sum(ages) / len(ages))  #3
    return (oldest, newest, average_age)  #4
    #1 Вернёт кортеж: ( самый старый фильм, самый новый фильм, среднее)
    #2 ages - список сколько лет фильму на 2026 год
    #3 самый старый, новый фильм. И среднее через math.celi (ages - колво фильмов)
    #4 выводит кортеж по условию

def duration_in_hours(minutes):  #1
    hours = minutes // 60  #2
    remaining_minutes = minutes % 60  #3
    return f"{hours}ч {remaining_minutes}мин"  #4
    #1 Возвращает минуты в формат ч м
    #2 выделяем часы
    #3 выделчем минуты через остаток
    #4 выводит нужный формат

#Задание №2
def rating_tier(rating):  #1
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо" #2
    #1 Функция возвращает рейтинг по условию
    #2 Тернарный оператор втунтри if/elif/else

def decade_label(year):  #1
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

if __name__ == "__main__":  #блок проверки(сдвигается каждый коммит)
    print("Средняя оценка:", average_rating(movies))
    print("Статистика возраста:", catalog_age_stats(movies))

    print("\nКатегории рейтинга:")
    for rating in [9.5, 8.2, 6.0, 4.5]:
        print(f"  {rating} → {rating_tier(rating)}")

    print("\nМетки десятилетий:")
    for year in [2024, 2021, 2020, 2015, 2014, 1990]:
        print(f"  {year} → {decade_label(year)}")