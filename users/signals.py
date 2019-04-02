# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-04-01 08:40:39
# @Last Modified by:   gvishal
# @Last Modified time: 2019-04-01 08:51:34
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()