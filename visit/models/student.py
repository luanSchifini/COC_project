from  django.db import models


class Student(models.Model):
    registration = models.IntegerField(null=True)
    student_name = models.CharField(max_length=50)
    anosemestre = models.IntegerField(null=True)
    student_class =models.CharField(max_length=10, null=True)

    def get_visits(self):
        visits = self.my_visits.count()

        return visits

    def __str__(self) -> str:
        return f'{self.registration} -> {self.student_name} -> {self.get_visits()} visitas'
    

