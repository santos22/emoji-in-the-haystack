import json
import requests

from django.core.management.base import BaseCommand, CommandError

from search.models import Emoji


EMOJI_JSON_URL = 'https://raw.githubusercontent.com/iamcal/emoji-data/master/emoji.json'


class Command(BaseCommand):
    help = 'Initialize database with emoji data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            default=False)

    def execute(self, *args, **options):
        self.count = 0

        try:
            super().execute(*args, **options)
        except KeyboardInterrupt:
            self.stdout.write('')

        self.stdout.write(self.style.SUCCESS(
            'Emojis created: {}'.format(self.count)))

    def handle(self, *args, **options):
        self.dry_run = options['dry_run']

        emojis = self.get_emojis()

        for emoji in emojis:
            if not emoji.get('name'):
                continue

            code = self.handle_code(emoji)
            name = emoji['name'].lower()
            self.stdout.write(
                '{} - {}'.format(name, code))

            if not self.dry_run:
                emoji = Emoji(
                    name=name,
                    code=code)

                emoji.save()

            self.count += 1

    def get_emojis(self):
        response = requests.get(
            url=EMOJI_JSON_URL)

        emojis = json.loads(response.content)

        return emojis

    def handle_code(self, emoji):
        """
        U+1F1EC, U+1F1FE - > &#x1F1EC&#x1F1FE
        """
        unified = emoji.get('non_qualified') or emoji.get('unified')
        unified = unified.split('-')

        codes = []
        for code in unified:
            _code = '&#x' + code
            codes.append(_code)

        return ''.join(codes)