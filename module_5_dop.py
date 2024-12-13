import time

class User:
    def __init__(self, nickname='', age=0, password=''):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __contains__(self, title):
        return title.lower() in str(self.title).lower()


class urTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = User()

    def log_in(self, nickname, password):
        for user in self.users:
            if str(user.nickname).lower() == nickname.lower():
                if user.password == hash(password):
                    self.current_user.nickname = user.nickname
                    self.current_user.age = user.age
                    self.current_user.password = user.password
                    break

    def register(self, nickname, password, age):
        inner = False
        for user in self.users:
            if str(user.nickname).lower() == nickname.lower():
                print(f'Пользователь {nickname} уже существует')
                inner = True
                break
        if not inner:
            new_user = User(nickname, age, password)
            self.current_user.nickname = nickname
            self.current_user.password = password
            self.current_user.age = age
            self.users.append(new_user)

    def log_out(self):
        self.current_user.nickname = ''
        self.current_user.age = 0
        self.current_user.password = ''

    def add(self, *args):
        for video in args:
            inner = False
            for cp in self.videos:
                if str(video.title).lower() == cp.title.lower():
                    inner = True
                    break
            if not inner:
                self.videos.append(video)

    def get_videos(self, search):
        res = []
        for video in self.videos:
            if video.__contains__(search):
                res.append(video.title)
        return res

    def watch_video(self, title):
        if len(self.current_user.nickname) != 0:
            for video in self.videos:
                if title.lower() == str(video.title).lower():
                    if (video.adult_mode and self.current_user.age >= 18) or not video.adult_mode:
                        while video.time_now < video.duration:
                            video.time_now += 1
                            print(f'{video.time_now}', end=' ')
                            time.sleep(1)
                        video.time_now = 0
                        print('Конец видео')
                        break
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = urTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)
