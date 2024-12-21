# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
# Задание "Свой YouTube"
from time import sleep


class User:
    """
    Класс для создания объекта Пользователь с аттрибутами:
    nickname - имя пользователя
    password - захешированный пароль пользователя
    age - возраст пользователя
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self): return f'Пользователь: {self.nickname}, Возраст: {self.age}'
    def __repr__(self): return f"('{self.nickname}', {self.age})"


class Video:
    """
    Класс для создания объекта Видео с аттрибутами:
    title - название видео
    duration - продолжительность видео
    adult_mode - возрастное ограничение
    time_now - время, на котором приостановился просмотр
    """
    def __init__(self, title, duration, *, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self): return f'Видео "{self.title}", длительностью {self.duration} сек'
    def __repr__(self): return f"('{self.title}', {self.duration}, {self.adult_mode})"


class UrTube:
    """
    Класс, который управляет логикой работы сервиса UrbanTube с аттрибутом
    current_user - текущий пользователь
    """
    users = []
    videos = []

    def __init__(self, current_user=None): self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                break
        else:
            return print(f'Пользователь {nickname} не найден')
        self.current_user = nickname
        print(f'{nickname}, добро пожаловать, на UrbanTube! Приятного просмотра')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                return print(f'Пользователь {nickname} уже существует')
        h_password = hash(password)
        self.users.append(User(nickname, h_password, age))
        print(f'Пользователь {nickname} успешно зарегестрирован')
        self.log_in(nickname, password)

    def log_out(self):
        if self.current_user:
            print(f'Всего доброго, {self.current_user}, будем ждать Вас снова!')
            self.current_user = None
        else:
            print('В данный момент никто не авторизован')

    def add(self, *args):
        for v in args:
            if not isinstance(v, Video):
                print(f'ОШИБКА: не является объектом класса Video - "{v}"')
                continue
            if v.title in list(map(lambda x: x.title, self.videos)):
                print(f'ОШИБКА: Видео с таким названием уже существует - "{v.title}"')
                continue
            self.videos.append(v)
            print(f'УСПЕХ: Видео успешно загружено - "{v.title}"')

    def get_videos(self, title_search):
        success_search = []
        for title in list(map(lambda x: x.title, self.videos)):
            if title_search.lower() in title.lower():
                success_search.append(title)
        return print(success_search if success_search else 'Ничего не найдено')

    def watch_video(self, title):

        if not self.current_user:
            return print('Войдите в аккаунт что бы смотреть видео!')

        if self.users[list(map(lambda x: x.nickname, self.users)).index(self.current_user)].age < 18:
            return print('Вам нем 18 лет, пожалуйста покиньте страницу')

        if title not in list(map(lambda x: x.title, self.videos)):
            return print('Видео не найдено, попробуйте ещё раз')

        print('Запуск видео:', title)
        for i in range(1, self.videos[list(map(lambda x: x.title, self.videos)).index(title)].duration + 1):
            sleep(1)
            print(i, end=" ")
        else:
            print(' Конец видео')

    def __str__(self):
        return \
            f'Авторизованный пользователь: {self.current_user}' \
            if self.current_user \
            else 'Пользователь не авторизован'


print()
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
print()

# Проверка поиска
ur.get_videos('лучший')
ur.get_videos('ПРОГ')
print()

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
print()
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
print()
ur.watch_video('Для чего девушкам парень программист?')
print()
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
print()
ur.watch_video('Для чего девушкам парень программист?')
print()

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print()
print(ur.current_user)
# или
print(ur)
print()

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
