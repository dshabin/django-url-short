from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import requests
import json

class Command(BaseCommand):
    help = 'Fetch some users from randaomuser.me API'

    def add_arguments(self, parser):
        parser.add_argument('users_count', nargs='+', type=int)

    def handle(self, *args, **options):
        url = "http://randomuser.me/api/?results=" + str((options['users_count'][0]))
        response = requests.get(url,verify=False)
        results = json.loads(response.text)['results']
        for user in results :
            username = user['login']['username']
            first_name = user['name']['first']
            last_name = user['name']['last']
            email = user['email']
            password = user['login']['password']
            date_joined = user['registered']
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,date_joined=date_joined)
        self.stdout.write("Fetch completed")
