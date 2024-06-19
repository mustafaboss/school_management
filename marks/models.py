from django.db import models
from students.models import Student
from classes.models import Class
from courses.models import Course
from teachers.models import Teacher

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    mark = models.FloatField()

    def __str__(self):
        return f'{self.student} - {self.course} - {self.mark}'
