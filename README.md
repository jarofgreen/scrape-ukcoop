# Scrape Co‑operatives UK

Scrapes data from https://www.uk.coop
And makes it available as machine readable data at https://jarofgreen.github.io/scrape-ukcoop

This is for the purposes of promoting co-ops around the internet.

We have to scrape data because the official website does not make this available as open data.
Please, Co‑operatives UK, add open data feeds to your own website and then we wouldn't have to do this!
We just want to help you promote co-ops :-)

## Configure

To configure, open the Pages settings of your repository, and select GitHub Actions as the Source for your pages.

## To develop locally

To run scraper:

    scrapy crawl coopsukevents

To build:

    python -m datatig.cli build --staticsiteoutput _site .

