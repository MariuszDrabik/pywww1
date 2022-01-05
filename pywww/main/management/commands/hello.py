from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Just say hello'

    def handle(self, *args, **options):
        self.stdout.write("Hello World")
        return super().handle(*args, **options)
    
    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)
