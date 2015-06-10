from django.core.management.base import BaseCommand, CommandError
from programs.util import util
from programs.models import *

class Command(BaseCommand):
	help = 'Initializes a new DB'

	def handle(self, *args, **options):
		d1 = util.save_code(Department,'Physics')

		u1 = util.save_code(Universities,'Eastern Michigan University')
		u1.departments.add(d1)

