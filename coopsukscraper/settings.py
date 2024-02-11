import os

BOT_NAME = 'https://github.com/jarofgreen/scrape-ukcoop'

SPIDER_MODULES = ['coopsukscraper.spiders']
NEWSPIDER_MODULE = 'coopsukscraper.spiders'

USER_AGENT = 'https://github.com/jarofgreen/scrape-ukcoop'

ITEM_PIPELINES = {
    'coopsukscraper.pipelines.WriteToFilesPipeline': 300,
}
