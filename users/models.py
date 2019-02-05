from django.db import models
from django.contrib.auth.models import User
from questions.models import Question
from PIL import Image


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

    def save(self, *args, **kwargs):
        super().save()

        profile_img = Image.open(self.profile_image.path)

        if profile_img.height > 300 or profile_img.width > 300:
            output_size_profile = (300, 300)
            profile_img.thumbnail(output_size_profile)
            profile_img.save(self.profile_image.path)

        cover_img = Image.open(self.cover_image.path)

        if cover_img.height > 1200 or cover_img.width > 1200:
            output_size_cover = (1200, 1200)
            cover_img.thumbnail(output_size_cover)
            cover_img.save(self.cover_image.path)


# Model for favourite question of user
class FavouriteQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'User {self.author.id} : Question {self.question.id}'
