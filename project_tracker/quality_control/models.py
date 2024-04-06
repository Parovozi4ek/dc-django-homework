from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from tasks.models import Project, Task

# Create your models here.

class BugReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    STATUS_CHOICES = [
        ('New', 'Новый'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершен'),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    # priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    PRIORITY_CHOICES = [
        (1, 'Очень низкий'),
        (2, 'Низкий'),
        (3, 'Средний'),
        (4, 'Высокий'),
        (5, 'Крайне высокий'),
    ]
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=3,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeatureRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    STATUS_CHOICES = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Consideration',
    )
    # priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    PRIORITY_CHOICES = [
        (1, 'Очень низкий'),
        (2, 'Низкий'),
        (3, 'Средний'),
        (4, 'Высокий'),
        (5, 'Крайне высокий'),
    ]
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=3,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
