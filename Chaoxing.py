# -*- coding:utf-8 -*-
# author Tong-Hao time:2020/4/30
# Editor Liona Maskros <lionacc@163.com>
import requests
import re
import time
from lxml import etree
import datetime
from rich.logging import RichHandler
import logging


class Chaoxing:
    def __init__(self,
                 cookies,
                 classid,
                 courseid,
                 sleep_time=1,
                 pass_time=6) -> None:
        self.run_start_time = datetime.datetime.now()
        self.pass_time = datetime.timedelta(minutes=pass_time)
        self.run_end_time = self.run_start_time + self.pass_time

        logging.basicConfig(level="NOTSET",
                            format="%(message)s",
                            datefmt="[%X]",
                            handlers=[RichHandler(rich_tracebacks=True)])
        self.log = logging.getLogger("Chaoxing")
        self.cookies = cookies
        self.classid = classid
        self.courseid = courseid
        self.sleep_time = sleep_time
        self.headers = {
            "Cookie":
            self.cookies,
            "User-Agent":
            "Mozilla/5.0 (iPad; CPU OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ChaoXingStudy/ChaoXingStudy_3_4.3.2_ios_phone_201911291130_27 (@Kalimdor)_11391565702936108810",
            "Referer":
            "http://mooc1-1.chaoxing.com/visit/interaction?s=a23e43ba56b6a3a14a8213ef3176f159"
        }

    def fangwen(self, activeid):
        url = "https://mobilelearn.chaoxing.com/widget/pcAnswer/teaAnswer?activeId={}&classId={}&fid=23923&courseId={}".format(
            activeid, int(self.classid), int(self.courseid))
        response = requests.get(url, headers=self.headers, timeout=5)
        self.log.info(url)

    def run(self):
        self.log.info("当前时间：{}\n==========正在查看  <{}>  的活动==========".format(
            datetime.datetime.now(), '电子电路'))
        #不一定是英语，可以根据classid和courseid去更改。
        url = 'https://mobilelearn.chaoxing.com/widget/pcpick/stu/index?courseId={}&jclassId={}'.format(
            self.courseid, self.classid)
        while datetime.datetime.now() <= self.run_end_time:
            time.sleep(self.sleep_time)
            resoponse = requests.get(url, headers=self.headers, timeout=5)
            # xpath解析文本
            html = etree.HTML(resoponse.content)
            divs = html.xpath('//*[@id="startList"]/div')

            if (divs):
                for div in divs:
                    activeid = div.xpath('./div[1]/@onclick')[0]
                    active = re.findall('activeDetail\((\d+),(\d+),.*?\)',
                                        activeid)[0]

                    # activeType = 4 为抢答
                    if (int(active[1]) == 4):
                        self.fangwen(str(active[0]))
                        self.log.info('抢答成功')
                    else:
                        self.log.info("暂无抢答\n")

                self.log.info(active[1])
            else:
                self.log.info("暂无活动\n")
