# 🚀 超星学习通

上课抢答脚本

> 有些学校上课使用学习通抢答问题,进行加分, 故产生了本脚本


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [🚀 超星学习通](#超星学习通)
  - [🥢使用方法](#使用方法)
  - [⚠️注意事项](#️注意事项)
    - [Cookies 获取](#cookies-获取)
    - [Class ID 和 Course ID](#class-id-和-course-id)
    - [💡 Github Action:自动运行](#github-action自动运行)

<!-- /code_chunk_output -->



## 🥢使用方法

1. Clone本仓库代码到本地

    ```shell
    git clone https://github.com/allinu/chaoxing
    ```

2. 创建虚拟环境

    ```shell
    # 需要提前安装 virtualenv
    # pip install virtualenv
    cd chaoxing
    virtualenv venv
    ```

3. 安装相关依赖

    ```shell
    pip install -r requirements.txt
    ```

4. 修改配置,请看 - [⚠️注意事项](#注意事项)

    - 添加cookie
    - 添加`classid`,`courseid`

5. 运行脚本

    ```shell
    # 只提供类Unix系统的激活虚拟环境的方法
    # Windows用户请百度
    source ./venv/bin/activate
    ```


## ⚠️注意事项

### Cookies 获取

    - 打开[这个链接](http://mooc1-1.chaoxing.com/visit/interaction): 如果需要登录的话请登录后重试
    - 在页面右键 -> 审查元素, 或者摁下<kbd>F12</kbd>,打开`开发者窗口`
    - 在打开`开发者窗口`的状态下,刷新页面<kbd>F5</kbd>
    - ![](https://i0.hdslb.com/bfs/album/55c3551bffe943703b814b33c96c540f0abd2591.png)

### Class ID 和 Course ID
    - 关闭`开发者窗口`
    - 选择需要抢答的课程并点击
    - 等待页面跳转完毕
    - 复制地址栏的内容,大概这样:
    `https://mooc1-1.chaoxing.com/mycourse/studentcourse?courseId=4324234&clazzid=432423432&xxxxxxxxxxxxxxxxxxxx`
    - 将里面的`courseId=`后面到`&classId`之前的复制到`run.py`文件中的`courseid`,
    - 将里面的`classid=`后面到`&`之前的复制到`run.py`文件中的`classid`

### 💡 Github Action:自动运行
- 本项目提供了Github action 来提供自动运行,主要需要修改的就是`.github/workflows/sign-action.yml`中第11行的`cron`,具体的cron使用方法请百度,或者在issuse中的`课表计算`中提出来
    ⚠️ **请把你的课表时间减去8个小时**
    ⚠️ **请把你的课表时间减去8个小时**
    ⚠️ **请把你的课表时间减去8个小时**
- 这个功能的主要功能就是,我举个🌰:
    > 我每周一有一节电子电路的课程,我们8:00上课,总时长2h,所以,我可以设置一个定时器,让程序每周一的上午八点执行,程序的执行时间在run.py中可以更改,单位为分钟,默认为6分钟,支持小数,github action默认每隔5分钟执行,理论上就可以一直执行了,同时可以解决如果报错的情况,如果报错,也没关系,下一轮会重新执行,这样就可以在上课的时段内一直运行了

    > (具体是机智,还是翻车只能等下周测试了😢)

    **自己给自己点赞也可以触发执行**
    **自己更改代码上传也会触发执行**
    **自己手动触发执行也可以运行**
