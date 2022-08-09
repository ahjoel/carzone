from datetime import datetime
from ckeditor.fields import RichTextField
from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class Car(models.Model):

    state_choice = (
        ('MN', 'Minesota'),
        ('LA', 'Louisiana'),
        ('MS', 'Mississipi'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('OH', 'Ohio'),
        ('PA', 'Pennsylvania'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Audio Start/Stop', 'Audio Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    title = models.CharField(max_length=100)
    state = models.CharField(choices=state_choice, max_length=50)
    city = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=50)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices, max_length=255)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    interior = models.CharField(max_length=50)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=50)
    millage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

