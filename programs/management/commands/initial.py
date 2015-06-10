from django.core.management.base import BaseCommand, CommandError
from programs.util import util
from programs.models import *

class Command(BaseCommand):
	help = 'Initializes a new DB'

	def handle(self, *args, **options):
		d1 = util.save_code(Department,'Physics')
		u1 = util.save_code(University,'Eastern Michigan University',department=d1)
		
		p1 = util.save_code(Program,'Physics Research')

		
