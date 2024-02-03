from django.db import models

class Profile(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact = models.CharField(max_length=11)
    user_id = models.CharField(max_length=255, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"

class PlantCareGuide(models.Model):
    plant_name = models.CharField(max_length=255)
    description = models.TextField()
    seasonal = models.CharField(max_length=255)
    guide = models.TextField()
    admin_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='plant_photos/', null=True, blank=True, default='default_photo.jpg')
    status = models.CharField(max_length=255, default='none')
    def __str__(self):
        return self.plant_name

class Category(models.Model):
    plant_id = models.CharField(max_length=255, unique=True)
    plant_name = models.CharField(max_length=255)

    def __str__(self):
        return self.plant_name

class CategoryBridge(models.Model):
    plant_care_guide = models.ForeignKey(PlantCareGuide, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Collection(models.Model):
    plant_care_guide = models.ForeignKey(PlantCareGuide, on_delete=models.CASCADE)
    review = models.TextField()

    def __str__(self):
        return f"{self.plant_care_guide.plant_name} - {self.plant_care_guide.id}"

    def get_plant_image_url(self):
        return self.plant_care_guide.plant_image.url if self.plant_care_guide.plant_image else ''
