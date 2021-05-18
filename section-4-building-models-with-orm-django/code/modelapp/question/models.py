# from django.db import models
#
#
# # Create your models here.
# class Question(models.Model):
#     title = models.CharField(max_length=10)
#
#
# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
#     answer = models.TextField()
#     reply = models.ForeignKey(
#         'self', on_delete=models.CASCADE,
#         blank=True,
#         null=True, related_name='replies'
#     )
#
#
# class Person(models.Model):
#     name = models.CharField(max_length=128)
#
#     def __str__(self):
#         return self.name
#
#
# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')
#
#     def __str__(self):
#         return self.name
#
#
# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class School(models.Model):
    school_name = models.CharField(max_length=64)
    school_address = models.CharField(max_length=200)
    school_phone = models.CharField(max_length=15)
    is_favorite = models.BooleanField(default=False)
    policy = models.TextField()
    time_open = models.TimeField()
    time_close = models.TimeField()

    def __str__(self):
        return self.school_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=64)
    user_email = models.EmailField(max_length=64)
    user_phone = models.CharField(max_length=13)
    user_address = models.CharField(max_length=200)
    user_flat = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    children = models.ManyToManyField('Children', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user_name


class Lesson(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.CharField(max_length=15)
    slot = models.PositiveIntegerField()
    slot_available = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(null=True, blank=True)
    time_start = models.TimeField()
    time_end = models.TimeField()
    last_in_minute = models.CharField(max_length=32, default="")

    def __str__(self):
        return self.lesson_name


class Children(models.Model):
    prefer_subject = models.ManyToManyField(Lesson, on_delete=models.CASCADE)
    children_firstname = models.CharField(max_length=32)
    children_lastname = models.CharField(max_length=32)
    children_birthday = models.DateField()
    children_gender = models.CharField(max_length=5)

    def __str__(self):
        return  self.children_firstname


class Comment(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    comment_content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_rating = models.PositiveIntegerField()

    def __str__(self):
        return str(self.user_id) + " | " + str(self.comment_content)[:100]