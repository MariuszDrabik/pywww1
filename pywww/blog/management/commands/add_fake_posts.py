from django.core.management.base import BaseCommand
from blog.utils import create_posts


class Command(BaseCommand):
    help = 'adding fake post'

    def handle(self, *args, **options):
        n = options.get("number", 10)
        create_posts(n)

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--number',
            type=int, default=10, dest="number", help='Amount of post',
        )
