import pytest
from scrapy.utils.test import get_crawler
from pydantic import BaseModel
from scrapy import Spider

from scrapy_spider_metadata.defaults import FromSetting
from scrapy_spider_metadata._params import Args


class Params(BaseModel):
    pages: int = FromSetting("MAX_PAGES_SETTING", default=5, getter="getint")
    lang: str = "en"


class S(Args[Params], Spider):
    name = "s"


def test_fromsetting_reads_setting():
    crawler = get_crawler(S, settings_dict={"MAX_PAGES_SETTING": 10})
    s = S()
    s._set_crawler(crawler)
    assert s.args.pages == 10
    assert s.args.lang == "en"


def test_fromsetting_uses_default_when_missing():
    crawler = get_crawler(S, settings_dict={})
    s = S()
    s._set_crawler(crawler)
    assert s.args.pages == 5
    assert s.args.lang == "en"


def test_cli_overrides_everything():
    crawler = get_crawler(S, settings_dict={"MAX_PAGES_SETTING": 10})
    s = S(pages=99)
    s._set_crawler(crawler)
    assert s.args.pages == 99
