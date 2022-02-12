import os

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Loads fixtures from fixtures dir"
    fixtures_dir = 'fixtures'
    loaddata_command = 'loaddata'

    def handle(self, *args, **options):
        for (dirpath, _, filenames) in os.walk(self.fixtures_dir):
            for fixture_filename in filenames:
                call_command(self.loaddata_command, os.path.join(dirpath, fixture_filename))
