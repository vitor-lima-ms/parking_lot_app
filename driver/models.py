from django.db import models

# Create your models here.

class Driver(models.Model):
    driver_name = models.CharField(max_length=50)
    monthly = models.BooleanField(default=False)
    cnh = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    file_upload = models.FileField(upload_to='driver_docs/', blank=True)

    def __str__(self):
        return f'{self.driver_name} - CPF: {self.cpf}'