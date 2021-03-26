from Chaoxing import Chaoxing
import os

# 你的Cookie信息
# 具体说明看文档
cookies = os.environ.get('COOKIE')
# ClassID
# classid = '39007569'
classid = os.environ.get("CLASSID")
# CourseID
# courseid = '208436724'
courseid = os.environ.get("COURSEID")
# 请求间隔时间,根据需要更改,单位:秒
sleep_time = os.environ.get("SLEEP_TIME")
# 程序总执行时长,单位:分钟
pass_time = os.environ.get("PASS_TIME")
# 下面无需修改
cx = Chaoxing(cookies, classid, courseid, sleep_time, pass_time)
cx.run()