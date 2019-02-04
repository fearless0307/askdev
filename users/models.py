from django.db import models
from django.contrib.auth.models import User
from questions.models import Question
from PIL import Image


# Create your models here.
# Model for user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    profile_image = models.ImageField(default='default_profile.png',
                                      upload_to='profile_pics')
    cover_image = models.ImageField(default='default_cover.png',
                                    upload_to='cover_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)


# Model for favourite question of user
class FavouriteQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'User {self.author.id} : Question {self.question.id}'
