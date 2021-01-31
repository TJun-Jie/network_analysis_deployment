
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','network_project.settings')
from faker import Faker
fakegen = Faker()
import django
django.setup()
from django.contrib.auth.models import User
def add_student(N=30):
    for entry in range(N):
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_username = fake_firstname[:2]+fake_lastname[:-2]
        fake_pass= 'Junjie2000'

        users = User.objects.create_user(username=fake_username,first_name=fake_firstname,last_name=fake_lastname, password=fake_pass)
        
if __name__ == "__main__":
    print("adding student")
    add_student(30)
    print("completed adding student")