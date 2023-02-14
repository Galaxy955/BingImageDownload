import requests
import re
import time
import urllib
import os

class CatchPic():
    def __init__(self):
        self.api_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

    def catch(self, save_dir):
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML,"
                                 " like Gecko) Version/16.3 Safari/605.1.15"}
        # Get the url of today's image.
        response = requests.get(url=self.api_url, headers=headers)
        get_status = response.status_code
        if get_status  != 200:
            raise RuntimeError("[Error 0001] Failed to get the url of today's image.")
        else:
            get_content = response.text
            # Debug.
            # print(get_content)
        # Extract useful information.
        image_time = re.findall(re.compile(r'"enddate":"([0-9]*?)"'), get_content)[0]
        image_url = re.findall(re.compile(r'"url":"(.*?)"'), get_content)[0]
        image_url = "https://cn.bing.com"+image_url
        # Debug.
        # print(image_time)
        # print(image_url)
        # Compare image_time with the local time.
        local_time = time.strftime("%Y%m%d", time.localtime())
        # Debug.
        # print(local_time)
        if image_time != local_time:
            raise RuntimeError("[Error 0002] The time of the image is wrong.")
        else:
            response = urllib.request.urlopen(image_url)
            get_status = response.status
            get_content = response.read()
            if get_status != 200:
                raise RuntimeError("[Error 0003] Failed to get today's image.")
            else:
                # Debug.
                # print(get_content)
                # Save the image.
                home_dir = os.path.expanduser("~")
                if save_dir:
                    if not os.path.exists(home_dir+"/"+save_dir):
                        os.makedirs(home_dir+"/"+save_dir)
                    with open(home_dir + "/" + save_dir + "/" + local_time + ".jpg", "wb") as f:
                        f.write(get_content)
                else:
                    if not os.path.exists(home_dir+"/BingImages"):
                        os.makedirs(home_dir+"/BingImages")
                    with open(home_dir+"/BingImages/"+local_time+".jpg", "wb") as f:
                        f.write(get_content)

if __name__ == "__main__":
    catch = CatchPic()
    catch.catch()
    print("Bing 今日美图已成功存储在本地。")