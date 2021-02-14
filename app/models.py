from django.db import models

# Create your models here.


class Major(models.Model):
    name = models.CharField(
        max_length=100,
        default="",
        verbose_name="Nama Jurusan")
    code = models.CharField(
        max_length=10,
        default="",
        verbose_name="Kode Jurusan",
        unique=True)
    desc = models.CharField(
        max_length=255,
        default="",
        verbose_name="Deskripsi Jurusan")

    def __str__(self):
        return self.name


class MajorConcentration(models.Model):
    name = models.CharField(
        max_length=50,
        default='',
        verbose_name="Konsentrasi Jurusan")
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    STUDENT_STATE = (
        ('active', 'Aktif'),
        ('inactive', 'Cuti'),
        ('graduate', 'Lulus'),
        ('drop', 'Drop Out')
    )

    name = models.CharField(
        max_length=100,
        default="",
        verbose_name="Nama Mahasiswa")
    npm = models.CharField(
        max_length=10,
        default="",
        verbose_name="NPM",
        unique=True)
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        verbose_name="Jurusan")
    concentration = models.ForeignKey(
        MajorConcentration,
        on_delete=models.CASCADE,
        verbose_name="Konsentrasi",
        null=True,
        blank=True
    )
    gpa = models.FloatField(default=0.0, verbose_name="IPK")
    status = models.CharField(
        max_length=15,
        choices=STUDENT_STATE,
        default="active",
        verbose_name="Status Mahasiswa")

    def __str__(self):
        return f"[{self.npm}] {self.name}"


class Subject(models.Model):
    name = models.CharField(
        max_length=100,
        default="",
        verbose_name="Nama Mata Kuliah")
    code = models.CharField(
        max_length=100, default="", verbose_name="Kode Kuliah", unique=True
    )
    theory = models.IntegerField(default=0, verbose_name="Teori")
    practice = models.IntegerField(default=0, verbose_name="Praktek")
    credit = models.IntegerField(default=0, verbose_name="SKS")
    major = models.ManyToManyField(Major, blank=True, verbose_name="Jurusan")
    concentration = models.ManyToManyField(
        MajorConcentration, blank=True, verbose_name="Konsentrasi"
    )

    def __str__(self):
        return f"[{self.code}] {self.name}"


class Semester(models.Model):
    semester = models.CharField(
        max_length=5,
        default="",
        verbose_name="Semester")
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Mahasiswa")
    subject = models.ManyToManyField(Subject, verbose_name="Mata Kuliah")

    def __str__(self):
        return f"[{self.student.npm}] {self.student}"
