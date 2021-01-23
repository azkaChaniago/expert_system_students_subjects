from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name="Nama Jurusan")
    code = models.CharField(max_length=10, default="", verbose_name="Kode Jurusan", unique=True)
    desc = models.CharField(max_length=255, default="", verbose_name="Deskripsi Jurusan")

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name="Nama Mahasiswa")
    npm = models.CharField(max_length=10, default="", verbose_name="NPM", unique=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, verbose_name="Jurusan")
    gpa = models.FloatField(default=0.0, verbose_name="IPK")

    def __str__(self):
        return f"[{self.npm}] {self.name}"


class Semester(models.Model):
    semester = models.CharField(max_length=5, default="", verbose_name="Semester")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Mahasiswa")

    def __str__(self):
        return f"[{self.student.npm}] {self.student}"


class Subject(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name="Nama Mata Kuliah")
    code = models.CharField(max_length=100, default="", verbose_name="Kode Kuliah", unique=True)
    theory = models.IntegerField(default=0, verbose_name="Teori")
    practice = models.IntegerField(default=0, verbose_name="Praktek")
    credit = models.IntegerField(default=0, verbose_name="SKS")
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, verbose_name="Semester")
    student = models.ManyToManyField(Student, verbose_name="Mahasiswa")

    def __str__(self):
        return f"[{self.code}] {self.name}"


