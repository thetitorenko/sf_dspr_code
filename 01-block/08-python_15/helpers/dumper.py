import pickle
from datetime import datetime
from os import path


# Класс для сохранения и загрузки данных
class Dumper():
    pass

    def __init__(self, archive_dir='archive/'):
        self.archive_dir = archive_dir

    # Сохраняем данные в файл
    def dump(self, data):
        with open(self.get_file_name(), 'wb') as file:
            pickle.dump(data, file)

    # Читаем данные из файла
    def load_for_day(self, day):
        file_name = path.join(self.archive_dir, day + '.pkl')
        with open(file_name, 'rb') as file:
            sets = pickle.load(file)
        return sets

    # Получаем имя файла для сохранения данных
    def get_file_name(self):
        today = datetime.now().strftime('%Y-%m-%d')
        return path.join(self.archive_dir, today + '.pkl')