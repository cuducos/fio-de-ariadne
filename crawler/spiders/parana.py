from datetime import date, datetime
from typing import Iterator, Union

from scrapy import Request, Spider
from scrapy.http import Response

from crawler.items import Case
from crawler.text import PARSERS
from crawler.typing import FieldValue


class ParanaSpider(Spider):
    name = "parana"
    allowed_domains = ["desaparecidosdobrasil.org"]

    def request_offset(self, offset: int) -> Request:
        base_url = "http://www.desaparecidosdobrasil.org/criancas-desaparecidas/parana/"
        url = f"{base_url}?offset={offset}"
        return Request(url, meta={"offset": offset})

    def start_requests(self) -> Iterator[Request]:
        yield self.request_offset(0)

    def parse(self, response: Response) -> Iterator[Union[Case, Request]]:
        for case in response.css("div.announcement"):

            # if we have cases, this is not the last page
            offset = response.meta.get("offset", 0)
            yield self.request_offset(offset + 1)

            # get main data from the case
            title = case.css("h4 a")
            href = title.attrib["href"]
            name = title.css("::text").get()
            if not name:
                continue

            # parse textual data from the case
            contents = tuple(
                line.strip() for line in case.css("::text").getall() if line.strip()
            )

            kwargs = {name: parser(contents) for name, parser in PARSERS.items()}
            yield Case(
                name=name,
                url=response.urljoin(href),
                full_text="\n".join(contents),
                **kwargs,
            )
