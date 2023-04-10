from celery import shared_task
import csv
from ReadCsv.models import User, UserProfile

@shared_task(bind = True)
def create_user_profiles(self):

    filepath = "uploads/files/Book5.csv" 
    with open(filepath, mode='r') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile:
            name=lines[0]
            mail = lines[1]
            username = name
            password = mail
            user = User.objects.create_user(username=username, password=password)
            user_profile = UserProfile(user=user)
            user_profile.save()
