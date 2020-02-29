from django.core.management.base import BaseCommand
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

from crawler.spiders.parana import ParanaSpider
from web.core.models import Kid


class Command(BaseCommand):
    help = "Crawls data from Paraná and saves it to the database"

    def add_arguments(self, parser):
        help = "Cleans the database before importing new data."
        parser.add_argument("--drop-all", action="store_true", help=help)

    def echo(self, text, style=None):
        self.stdout.write(style(text) if style else text)

    def warn(self, text):
        return self.echo(text, self.style.WARNING)

    def success(self, text):
        return self.echo(text, self.style.SUCCESS)

    @staticmethod
    def serialize(kid):
        return Kid(**kid)

    def save(self, signal, sender, item, response, spider):
        if Kid.objects.filter(name=item["name"]).exists():
            self.warn(f"Caso já existe: {item['name']}")
            return

        kid = self.serialize(item)
        kid.save()

    def handle(self, *args, **options):
        if options.get("drop_all"):
            self.warn("Dropping existing records...")
            Kid.objects.all().delete()

        dispatcher.connect(self.save, signal=signals.item_passed)
        process = CrawlerProcess(settings={"LOG_LEVEL": "INFO"})
        process.crawl(ParanaSpider)
        process.start()
        self.success("Done!")
