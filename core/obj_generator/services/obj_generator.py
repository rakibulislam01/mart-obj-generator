import datetime
import logging
import random
from string import ascii_lowercase, digits
from collections import Counter

from .output import generate_file, generate_report, erase_file

logger = logging.getLogger(__name__)
TWO_MB = 1900000


class ObjGenerator:
    def __init__(self):
        self.objects_list = list()

    @staticmethod
    def _generate_object(data):
        generate_object = ''
        for _ in range(random.randint(5, 15)):
            generate_object += random.choice(data)
        return generate_object

    def generate_real_number(self):
        return random.random() * random.randint(100, 200)

    def generate_alphanumerics(self):
        alphanumerics = list(ascii_lowercase + digits)
        random.shuffle(alphanumerics)
        alphanumerics = ''.join(alphanumerics)
        return self._generate_object(alphanumerics)

    def generate_alpha_string(self):
        return self._generate_object(ascii_lowercase)

    def generate_integers(self):
        return self._generate_object(digits)

    def get_object(self):
        try:
            object_type = ["string", "real_number", "integers", "alphanumerics"]
            object_type_dict = {
                "string": self.generate_alpha_string(),
                "real_number": self.generate_real_number(),
                "integers": self.generate_integers(),
                "alphanumerics": self.generate_alphanumerics()
            }
            selected_obj = random.choice(object_type)
            self.objects_list.append(selected_obj)
            return object_type_dict.get(selected_obj)
        except Exception as e:
            logger.error(f"{e}. Time: {datetime.datetime.now()}")
            return ''

    def generate_report(self):
        return dict(Counter(self.objects_list))

    def generate_obj_process(self):
        erase_file()
        object_string = str(self.get_object())
        while len(object_string.encode('utf-8')) <= TWO_MB:
            object_string += ', ' + str(self.get_object())
        generate_file(object_string)
        generate_report(self.generate_report())
        return ''
