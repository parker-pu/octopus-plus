import json
import os

import scrapy

from scrapy.utils.project import get_project_settings


class SrcSpider(scrapy.Spider):
    name = 'src'

    def start_requests(self):
        """ 打开相关文件,读取Json,把Json变为请求
        :return:
        """
        setting = get_project_settings()
        for file_path, _, _files in os.walk("{}/agent/data/60/".format(setting.get("BASE_DIR"))):
            for _file in _files:
                file_suffix = os.path.splitext(_file)[-1]
                if file_suffix not in [".json"]:
                    continue
                with open("{}/{}".format(file_path, _file), 'r') as load_f:
                    json_data = json.load(load_f)
                    if json_data.get("request_type", "") != "GET":
                        continue

                    # 增加相关请求参数
                    header, data, meta = {}, {}, {}
                    header.update(json_data.get("header"))
                    data.update(json_data.get("data"))
                    meta.update(json_data.get("meta"))

                    # 发送请求
                    yield scrapy.Request(
                        url=json_data.get("url"),
                        headers=header,
                        body=data,
                        meta=meta,
                        dont_filter=True,  # 不过滤
                        callback=self.parse,
                    )

    def parse(self, response):
        print(response.text)
        pass
