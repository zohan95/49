from django.db import models
from django.contrib.auth.models import User

# class Token(models.Model):
#     token = models.UUIDField(verbose_name='Token', default=uuid4)
#     user = models.ForeignKey('auth.User', related_name='registration_tokens',
#                              verbose_name='User', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.token)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    about = models.TextField(max_length=500, blank=True, null=True, verbose_name='О себе')
    git_hub = models.URLField(null=True, blank=True, verbose_name='Github')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'