from Chaoxing import Chaoxing
import os

# 你的Cookie信息,环境变量自动获取! 请不要更改! 更改无效!
# 具体说明看文档
cookies = os.environ.get('COOKIE')
# ClassID
classid = '39007569'
# CourseID
courseid = '208436724'
# 请求间隔时间,根据需要更改,单位:秒
sleep_time = 0.5
# 程序总执行时长,单位:分钟
pass_time = 6
# 下面无需修改
cx = Chaoxing(cookies, classid, courseid, sleep_time, pass_time)
cx.run()