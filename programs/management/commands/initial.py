from django.core.management.base import BaseCommand, CommandError
from programs.util.util import *
from programs.models import *

class Command(BaseCommand):
	help = 'Initializes a new DB'

	def handle(self, *args, **options):
		u1 = save_code(University,'Eastern Michigan University')
		u2 = save_code(University, 'Michigan State University')

		d1 = save_code(Department,'Physics',universities=u1)

		p1 = save_code(Program,'Physics Research',departments=d1)
		p2 = save_code(Program,'Physics',departments=d1)
		



		f1 = save_code(Faculty,'Faculty')
		f2 = save_code(Faculty,'Adjunct')
		f3 = save_code(Faculty,'Lecturer')


		c1 = save_code(Course,'Mechanics 1',description='Generally 1st term calculus based mechanics')
		c2 = save_code(Course,'Mechanics 2',description='Intermediate level mechanics')
		c3 = save_code(Course,'Electricity and Magnetism 1',description='Generally 1st year calculus\
			based EM')

		p1.courses.add(c1)
		p1.courses.add(c2)
		p1.courses.add(c3)
		p2.courses.add(c1)
		p2.courses.add(c2)


		con1 = save_code(Content,'Newtons Laws')
		con2 = save_code(Content,'Kinematics')
		ct1 = save_code(ContentType,'Theoretical')
		dl1 = save_code(Delivery,'Lecture')


