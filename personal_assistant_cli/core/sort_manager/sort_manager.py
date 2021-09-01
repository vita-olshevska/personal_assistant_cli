from pathlib import Path

IMAGE_EXTENSIONS = ['JPEG', 'PNG', 'JPG', 'SVG', 'HEIC']
DOCUMENT_EXTENSIONS = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'TEX', 'BIB', 'CLS']
AUDIO_EXTENSIONS = ['MP3', 'OGG', 'WAV', 'AMR']
VIDEO_EXTENSIONS = ['AVI', 'MP4', 'MOV', 'MKV']
ARCHIVE_EXTENSIONS = ['ZIP', 'GZ', 'TAR', 'RAR', 'TGZ', 'FB2']


class SortManager:
    """Сортує файли у вказаній папці по категоріям (зображення, документи, відео і т.д."""
    __dir_ext: dict = None
    __another_path: Path = None

    def __setup(self, path):
        self.__dir_ext = {self.__create_dir(path, "images"): IMAGE_EXTENSIONS,
                          self.__create_dir(path, "documents"): DOCUMENT_EXTENSIONS,
                          self.__create_dir(path, "audio"): AUDIO_EXTENSIONS,
                          self.__create_dir(path, "video"): VIDEO_EXTENSIONS,
                          self.__create_dir(path, "archives"): ARCHIVE_EXTENSIONS}
        self.__another_path = self.__create_dir(path, "another")

    def sort(self, path: str) -> str:
        """Функція, що рекурсивно витягує файли із папок та визиває метод сортування файлів"""
        if not self.__validate_path(Path(path)):
            return f"Incorrect path provided: {path}"

        self.__setup(path)
        self.__sort(Path(path))
        return f"Sort done successfully by path: {path}"

    @staticmethod
    def __validate_path(path: Path):
        return path.exists() and path.is_dir()

    def __sort(self, path: Path):
        for element in path.iterdir():
            if self.__ignore(element):
                continue
            if element.is_dir():
                self.__sort(element)
            else:
                self.__transport_file(element)

    @staticmethod
    def __create_dir(path, dir_name):
        """Створює папки, куди будуть сортуватися файли відповідного типу"""
        dir_name_path = Path(str(path) + f"/{dir_name}")
        if not dir_name_path.exists():
            dir_name_path.mkdir()
        return dir_name_path

    @staticmethod
    def __get_name_extension(general_name):
        """ Розбиває ім'я файлу на 2 частини: name - головне ім'я та extension - розширення"""

        dot_position = general_name.rfind(".")
        if dot_position == -1:
            return general_name, ""

        name = general_name[:dot_position]
        extension = general_name[dot_position + 1:]
        return name, extension

    def __transport_file(self, file):
        """Переміщає файл до папки, що відповідає типу файлу"""
        file_name, file_extension = self.__get_name_extension(file.name)
        for key, val in self.__dir_ext.items():
            if file_extension.upper() in val:
                file.rename(str(key) + '/' + file.name)
                return

        file.rename(str(self.__another_path) + '/' + file.name)

    def __ignore(self, elem):
        """Ігнорує сортувальні папки, якщо вони вже існували раніше """
        for key in self.__dir_ext.keys():
            if str(elem) == str(key):
                return True
        return False
