import datetime
import logging

from django.views.generic import TemplateView
from rest_framework import views
from rest_framework.response import Response

from .services.obj_generator import ObjGenerator
from .services.output import generate_file, generate_report, get_report

TWO_MB = 2000000
logger = logging.getLogger(__name__)


class GenerateObjAPIView(views.APIView):
    """
    API endpoint that allows users to generate objs file.
    """
    def get(self, request):
        try:
            generator = ObjGenerator()
            object_string = str(generator.get_object())
            while len(object_string.encode('utf-8')) <= TWO_MB:
                object_string += ', ' + str(generator.get_object())
            generate_file(object_string)
            generate_report(generator.generate_report())
            return Response({
                "file_link": request.build_absolute_uri('/media/data/objects.txt')
            })
        except Exception as e:
            logger.error(f"{e}. Time: {datetime.datetime.now()}")
            return Response(str(e))


class ReportAPIView(views.APIView):
    """
    API endpoint that allows users to show reports.
    """
    def get(self, request):
        try:
            data = get_report()
            return Response(data)
        except Exception as e:
            logger.error(f"{e}. Time: {datetime.datetime.now()}")
            return Response(str(e))


class HomeView(TemplateView):
    template_name = 'obj_generator/home.html'
