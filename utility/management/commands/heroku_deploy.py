import os

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    '''
    This management command will automatically migrate the project apps
    as well as flush the data in the database.
    '''
    help = 'Clean database and migrate automatically.'

    def migrate_project_apps(self):
        project_app_names = settings.DRF_LOGGER_PROJECT_APPS
        for app_name in project_app_names:
            try:
                call_command('makemigrations', app_name)
                call_command('migrate', app_name)
            except CommandError as ex:
                print('MIGRATION ERROR: {0}'.format(ex.message))

    def reset_database(self):
        call_command('flush', '--no-input')

    def handle(self, *args, **options):
        self.reset_database()
        # self.migrate_project_apps()
