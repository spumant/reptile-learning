import requests

url = "https://pearvideo.com/video_1769717"

VideoStatus = "https://pearvideo.com/videoStatus.jsp?contId=1769717&mrd=0.09998069021775358"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    # 防盗链：溯源，当前本次请求的上一级
    "Referer": url
}

contId = url.split("_")[1]
resp = requests.get(VideoStatus, headers=headers)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
print(srcUrl)

# 下载视频
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
print("视频爬取完毕")
