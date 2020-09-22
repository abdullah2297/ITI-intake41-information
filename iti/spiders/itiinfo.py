import scrapy


class ItiinfoSpider(scrapy.Spider):
    name = 'itiinfo'
    start_urls = ['http://www.iti.gov.eg/Admission/PTPprogram/intake41']

    def parse(self, response):
        links = response.css(".track a::attr(href)").extract()
        for link in links:
            link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.parse_info)

    def parse_info(self, response):
        yield {
            'page': response.url,
            'track':response.css("#Main_ctrl_Name_lbl_TrackName::text").extract(),
            'courses':response.css("#owl1 span::text").extract(),
            'branchs':response.css(".branchName span::text").extract(),
            'staff': response.css("h5 a span::text").extract(),
            'track_purpose':response.css("#Main_ctrl_Description_lbl_TrackPurpose::text").extract(),
            'track_opportunities':response.css("#viewOpportunitiesContent a span::text").extract()
        }
