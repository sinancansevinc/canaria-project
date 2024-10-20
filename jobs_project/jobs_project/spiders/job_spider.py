import json
import scrapy
from jobs_project.items import JobsProjectItem

class JobSpider(scrapy.Spider):
    name = 'job_spider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'jobs_project.pipelines.JobsProjectPipeline': 300,
        },
    }

    def start_requests(self):
        yield scrapy.Request(
            url='file:///app/s01.json',
            callback=self.parse_page,
            meta={'file_index': 1}
        )

    def parse_page(self, response):
        data = json.loads(response.text)
        for job in data.get('jobs', []):
            job_data = job.get('data', {})
            item = JobsProjectItem()
            
            for field in item.fields:
                try:
                    item[field] = job_data.get(field, None)
                    if isinstance(item[field], (dict, list)):
                        item[field] = json.dumps(item[field])
                except Exception as e:
                    print(f"Error processing field '{field}': {e}")
            
            yield item
        
        if response.meta['file_index'] == 1:
            yield scrapy.Request(
                url='file:///app/s02.json',
                callback=self.parse_page,
                meta={'file_index': 2}
            )
