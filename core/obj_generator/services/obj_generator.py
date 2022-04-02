import datetime
import logging
import random
from string import ascii_lowercase, digits
from collections import Counter

logger = logging.getLogger(__name__)


class ObjGenerator:
    def __init__(self):
        self.objects_list = list()

    @staticmethod
    def _generate_object(data):
        generate_object = ''
        for _ in range(random.randint(5, 15)):
            generate_object += random.choice(data)
        return generate_object

    def _generate_real_number(self):
        return random.random() * random.randint(100, 200)

    def _generate_alphanumerics(self):
        alphanumerics = list(ascii_lowercase + digits)
        random.shuffle(alphanumerics)
        alphanumerics = ''.join(alphanumerics)
        return self._generate_object(alphanumerics)

    def _generate_alpha_string(self):
        return self._generate_object(ascii_lowercase)

    def _generate_integers(self):
        return self._generate_object(digits)

    def get_object(self):
        try:
            object_type = ["string", "real_number", "integers", "alphanumerics"]
            object_type_dict = {
                "string": self._generate_alpha_string(),
                "real_number": self._generate_real_number(),
                "integers": self._generate_integers(),
                "alphanumerics": self._generate_alphanumerics()
            }
            selected_obj = random.choice(object_type)
            self.objects_list.append(selected_obj)
            return object_type_dict.get(selected_obj)
        except Exception as e:
            logger.error(f"{e}. Time: {datetime.datetime.now()}")
            return ''

    def generate_report(self):
        return dict(Counter(self.objects_list))


# generator = ObjGenerator()
# object_str = str(generator.get_object())
# while len(object_str.encode('utf-8')) <= 20000:
#     object_str += ', ' + str(generator.get_object())
