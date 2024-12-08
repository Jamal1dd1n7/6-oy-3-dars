from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Kurs nomi")
    description = models.TextField(verbose_name="Kurs tavsifi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Oxirgi tahrirlangan vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ['-created_at']


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Talaba ismi")
    email = models.EmailField(unique=True, verbose_name="Talaba email manzili")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro‘yxatdan o‘tgan vaqti")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students", verbose_name="Kurs")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"
        ordering = ['-enrolled_at']
