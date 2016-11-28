from django.db import models

# Create your models here.
class Course(models.Model):
    courseno = models.CharField(primary_key=True, max_length=10)
    coursename = models.CharField(max_length=40)
    deptname= models.CharField(max_length=20)
    credit = models.IntegerField(default=3)

    def __str__(self):
        return self.courseno

class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    year = models.IntegerField()
    gpa = models.FloatField()

    def __str__(self):
        return self.id

class Enroll(models.Model):
    class Meta:
        unique_together=(('sid', 'courseno'),)
    sid = models.ForeignKey(Student, verbose_name=('id'))
    courseno =models.ForeignKey(Course, verbose_name=('courseno'))
    grade = models.FloatField()

    def __str__(self):
        str = "%s , %s" % (self.sid, self.courseno)
        return str
