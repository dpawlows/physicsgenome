from django.core.management.base import BaseCommand, CommandError
from programs.util.util import *
from programs.models import *
import pdb

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

		ct1 = save_code(CourseType,'Mechanics 1')
		ct2 = save_code(CourseType,'Mechanics 2')
		ct3 = save_code(CourseType,'Mechanics 3')
		ct4 = save_code(CourseType,'Electricity and Magnetism 1')
		ct5 = save_code(CourseType,'Electricity and Magnetism 2')
		ct6 = save_code(CourseType,'Electricity and Magnetism 3')
		ct7 = save_code(CourseType,'Modern Physics 1')
		ct8 = save_code(CourseType,'Modern Physics 2')
		ct9 = save_code(CourseType,'Quantum Mechanics 1')
		ct10 = save_code(CourseType,'Quantum Mechanics 2')
		ct11 = save_code(CourseType,'Computational Physics 1')	
		ct12 = save_code(CourseType,'Computational Physics 2')	
		ct13 = save_code(CourseType,'Acoustics')
		ct12 = save_code(CourseType,'Fluid Dynamics')
		ct13 = save_code(CourseType,'Thermodynamics')
		ct14 = save_code(CourseType,'Optics')	
		ct15 = save_code(CourseType,'Mathematical Methods')
		ct16 = save_code(CourseType,'Senior Project')
		ct17 = save_code(CourseType,'Research')
		ct18 = save_code(CourseType,'Seminar')
		ct19 = save_code(CourseType,'Electronics')

		c1 = save_course(Course,u1,'PHY223',
			description='Generally 1st term calculus based mechanics',
			courseType=ct1
			)
		c2 = save_course(Course,u1,'PHY224',
			description='Intermediate level mechanics',
			courseType=ct4
			)
		c3 = save_course(Course,u1,'PHY350',
			description='Generally 1st year calculus\
			based EM',
			courseType=ct5
			)


		c1.programs.add(p1)
		c1.programs.add(p2)
		c2.programs.add(p1)
		c2.programs.add(p2)
		c3.programs.add(p1)


		con1 = save_code(Content,'Newtons Laws')
		con2 = save_code(Content,'Kinematics')
		ct1 = save_code(ContentType,'Theoretical')
		dl1 = save_code(Delivery,'Lecture')


