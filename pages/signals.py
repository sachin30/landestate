from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group


def assign_group_to_user(sender, instance , created, **kwargs):
    if created:
        group= Group.objects.get(name="usergroup")    
        instance.groups.add(group)
    print("User is assigned to usergroup via signal functionality")

post_save.connect(assign_group_to_user,sender=User)