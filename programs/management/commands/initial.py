from django.core.management.base import BaseCommand, CommandError
from programs.util.util import *
from programs.models import *

class Command(BaseCommand):
	help = 'Initializes a new DB'

	def handle(self, *args, **options):
		d1 = save_code(Department,'Physics')
		u1 = save_code(University,'Eastern Michigan University')
		p1 = save_code(Program,'Physics Research')

		u1.departments.add(d1)

		f1 = save_code(Faculty,'Faculty')
		f2 = save_code(Faculty,'Adjunct')
		f3 = save_code(Faculty,'Lecturer')

		uhf = UniversityHasFaculty()
		uhf.university = u1
		uhf.department = d1
		uhf.faculty = f1
		uhf.number = 10
		uhf.save()