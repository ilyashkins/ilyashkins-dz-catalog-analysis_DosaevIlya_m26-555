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

#Задание №3
print("\nФильмы НЕ-комедии: ")  #1
for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])
#1 просто ищет комедии и пропускает их, иначе - ввыводит 


print("\nПоиск первого шедевра")  #1
i = 0  #2
while i < len(movies):  #3
    if movies[i]["rating"] > 9.0:  #4
        print(f"найден: {movies[i]['title']} (рейтинг {movies[i]['rating']})")  #5
        break  #6
    i += 1  #7
else:  #8
    print("шедевров нет")
#1 просто текст перед циклом
#2 индекс/счётчик
#3 условие выхода в конце списка
#4 проверем рейтинг с 9.0 если True-шедевер,Else-дальше
#5 если тру то выводится текст 
#6 выходим из цикла
#7 если фильм не подходит добавляем +1 в индекс i и смотрим рейтинг следующего фильма
#8 если фильмы не  найдены выводим текст

def count_long_movies(movies, threshold=120):  #1
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count
#1 считает количество фильмов длиннее threshold минут

# задание №4
def normalize_title(title):  #1
    words = title.split()
    normalize_words = [word[0].upper() + word[1:].lower() for word in words]
    return " ".join(normalize_words)  #2
#1 функция разбивает название. 1знак делает заглавным, а остальные строчными.
#2 склеивает через пробел 

def make_slug(title):
    return title.lower().replace(" ", "-")  #1
#1 функция приводит все символф в нижний регистр  и заменяет пробел на "-"

def format_report_line(movie):
    title = normalize_title(movie["title"])  #1
    dur = duration_in_hours(movie["duration_min"])  #2
    genres = ", ".join(sorted(movie["genres"]))  #3
    return f'"{title}" ({movie["year"]}) - {movie["rating"]}/10, {dur}, жанры: {genres}'
#1 вытаскиваем назание из 

# задание № 5
def titles_sorted_by_rating(movie):  #1
    sorted_movie = sorted(movie, key=lambda m: m['rating'], reverse=True)  #2
    return [movie["title"] for movie in sorted_movie]  #3
#1 вернет функцию отсортированных фильмов
#2 сортирует фильмы по анонимной функции по ключу по рейтингу, от меньшего к большему
#3 возвращает новый список отсортированных фильмов 

def top_n_by_rating(movie, n=3):
    sorted_movie = sorted(movie, key=lambda m: m['rating'], reverse=True)  #1
    return [(movie["title"], movie["rating"]) for movie in sorted_movie[:n]]
#1 та же самая сортировка, что и выше
#2 возвращаем топ n с названием и рейтингом

#Задание №6
def count_by_genre(movies):
    counts = {}  #1
    for movie in movies:  #2
        for genre in movie["genres"]:  #3
            counts[genre] = counts.get(genre, 0) + 1  #4
    return counts  #5
#1 пустой словарь
#2 проходим по фильмамэ
#3 Проходим по жанрам выбранного фильма
#4 Увеличиваем счётчик
#5 вернёт кол-во по каждому жанру

def actor_filmography(movies):
    filmography = {}  #1
    for movie in movies:  #2
        title = normalize_title(movie["title"])  #3
        for actor in movie["actors"]:  #4
            filmography.setdefault(actor, []).append(title)  #5
    return filmography
#1 cписок 
#2 перебираем фильмы
#3 приводим в Вид с Заглавной буквы из функции выше
#4 перебираем актёров
#5 если актёра нет создаём список, а потом добавляем название


def top_rated_dict(movies):
    threshold = average_rating(movies)  #1
    return {  
        normalize_title(movie["title"]): movie["rating"]  #2
        for movie in movies  #3
        if movie["rating"] > threshold  #4
    }  
#1 Вычеслим средний рейтинг из функции выше 
#2 Название фильмов с Заглавной буквы
#3 Перебираем фильмы
#4 Условие при котором фильм вернётс в функцию, если выше среднего.

 #блок проверки(сдвигается каждый коммит)
 # задача №1
print('\n Задание №1')
print("Средняя оценка:", average_rating(movies))
print("\nСтатистика возраста:", catalog_age_stats(movies))

# задача №2
print('\n Задание №2')
print("Категории рейтинга:")
for rating in [9.5, 8.2, 6.0, 4.5]:
    print(f"  {rating} → {rating_tier(rating)}")

print("\nМетки десятилетий:")
for year in [2024, 2021, 2020, 2015, 2014, 1990]:
    print(f"  {year} → {decade_label(year)}")

# задача №3
print('\n Задание №3')
print("Фильмов длиннее 120 минут:", count_long_movies(movies))
print("Фильмов длиннее 100 минут:", count_long_movies(movies, 100))

# задача №4
print(f'\n Задание №4, \n{normalize_title("silent hours")}')
print(make_slug("Silent Hours"))
print(format_report_line(movies[7]))

# задача №5
print('\n Задание №5')
print("Список фильмов по убыванию рейтинга: ", titles_sorted_by_rating(movies))
print(top_n_by_rating(movies, 3))

print("\nЭтап 6. Словари:")
print("Количество по жанрам:", count_by_genre(movies))
print("\nФильмография:")
for actor, films in actor_filmography(movies).items():
    print(f"  {actor}: {films}")
print("\nФильмы выше среднего:")
for title, rating in top_rated_dict(movies).items():
    print(f"  {title}: {rating}")