from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KL", "KIWI"),
        ("PL", "PLAIN"),
        ("EL", "ELACHI"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.SmallIntegerField(default=10.00)

    def __str__(self):
        return self.name
    


# One to Many

class ChaiReview(models.Model):
    CHAI_RATINGS = [
        ("0", "Very Bad"),
        ("1", "Bad"),
        ("2", "Not Bad"),
        ("3", "Average"),
        ("4", "Good"),
        ("5", "Very Good"),
    ]


    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, choices=CHAI_RATINGS)
    comment = models.TextField()
    dateAdded = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'



# Many to Many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')


    def __str__(self):
        return self.name
    



# One to One 

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=10)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()


    def __str__(self):
        return f'certificate of {self.chai.name}'
