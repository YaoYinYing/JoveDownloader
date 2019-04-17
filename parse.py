#coding: utf-8
import urllib
import sys

#控制台版本进度条
def bar(name, pos, total):
    sys.stdout.write('   \r')
    sys.stdout.flush()
    pos_scale = float(pos) / float(total) * 50
    pos_percent = int(pos * total / 100)
    bar_text = ""
    bar_text = name + "[" + "*"*int(pos_scale) + " "*(50 - int(pos_scale)) + "]" + str(pos_percent) + "%"
    sys.stdout.write(bar_text)

def bar2(name, pos, total):
    pos_scale = float(pos) / float(total) * 50
    pos_percent = int(pos * total / 100)
    bar_text = ""
    bar_text = name + "[" + "*"*int(pos_scale) + " "*(50 - int(pos_scale)) + "]" + str(pos_percent) + "%"
    return bar_text
#下载网页代码
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#解析文章名字
def getPaperName(url):
    names = url.split('/')
    paper_name = names[-1]
    paper_name = paper_name.replace("-"," ")
    paper_name = paper_name.title()
    print (paper_name)
    return paper_name

#解析视频文件名
def getVideoName(url):
    page = getHtml(url)
    lines = page.split('\n')
    video_name = ""
    for i, item in enumerate(lines):
        if item.find("mp4") != -1:
            video_name = item[0:item.find("mp4") + 3]
            video_name = video_name.split("/")
            video_name = video_name[len(video_name) - 1]
            break
    print (video_name)
    return (video_name)

def getVideoFullName(url):
    video_fullname = "http://ecsource.jove.com/CDNSource/protected/"
    video_name = getVideoName(url)
    return video_fullname + video_name

# 下载回调函数
def schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    bar("下载进度:", per, 100)

def downloadVideo(url, dir = "./"):
    video_fullname = "http://ecsource.jove.com/CDNSource/protected/"
    dir = dir.rstrip('/') + '/'
    paper_name = dir + getPaperName(url) + ".mp4"
    video_name = getVideoName(url)
    if video_name == "":
        return
    video_fullname = video_fullname + video_name
    urllib.urlretrieve(video_fullname, paper_name, schedule)

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print ("请输入视频网址...")
        exit()
    url = sys.argv[1]
    # url = "https://www.jove.com/video/57188/isolation-protocol-mouse-monocyte-derived-dendritic-cells-their"
    downloadVideo(url)




