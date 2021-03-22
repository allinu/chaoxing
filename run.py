from Chaoxing import Chaoxing

# 填写你的Cookie信息
cookies = ""
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