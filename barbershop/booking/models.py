from django.db import models

class Master(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='photos/services/', blank=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.master.name} - {self.date}"

class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client_name} - {self.service.name} ({self.date} {self.time})"


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    video_url = models.URLField()

    def __str__(self):
        return self.title

