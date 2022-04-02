import datetime
import json
import logging

from django.conf import settings

# Get an instance of a logger
logger = logging.getLogger(__name__)


def get_report():
    try:
        with open(f"{settings.BASE_DIR}/media/data/report.json", 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        logger.error(f"{e}. Time: {datetime.datetime.now()}")
        return {'integers': 0, 'alphanumerics': 0, 'string': 0, 'real_number': 0}


def generate_file(result: str):
    try:
        f = open(f"{settings.BASE_DIR}/media/data/objects.txt", 'w')
        f.write(result)
        f.close()
    except IOError as e:
        logger.error(f"{e}. Time: {datetime.datetime.now()}")
        return {'integers': 0, 'alphanumerics': 0, 'string': 0, 'real_number': 0}


def generate_report(result: dict):
    try:
        report_file = open(f"{settings.BASE_DIR}/media/data/report.json", 'w')
        json.dump(result, report_file, indent=4)
        report_file.close()
    except IOError as e:
        logger.error(f"{e}. Time: {datetime.datetime.now()}")
        return {'integers': 0, 'alphanumerics': 0, 'string': 0, 'real_number': 0}
