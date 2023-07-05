import sys
import json
from curl_cffi import requests
from bs4 import BeautifulSoup


def get_dm_bp(url, num):
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception("获取网页失败,请检查url是否正确")
    soup = BeautifulSoup(resp.content, "html.parser")
    info = soup.find_all("div", id="dataDefault")[-1]  # div标签 id='dataDefault
    # 去掉<div id="dataDefault" style="display: none"> 和 </div>
    info = (
        str(info)
        .replace('<div id="dataDefault" style="display: none">', "")
        .replace("</div>", "")
    )
    info = json.loads(info)

    # 提取itemId和skuId
    for item in info["performBases"]:
        print(
            "选票链接: {}{}/detail/sku.html?id={}".format(
                BASE_URL, dm, item["performs"][-1]["itemId"]
            )
        )
        for perform in item["performs"]:
            print("场次时间: ", perform["performName"], "最大购买数量: ", perform["singleLimit"])
            itemId = perform["itemId"]
            for sku in perform["skuList"]:
                print(
                    "场次座位: ",
                    sku["skuName"],
                    "bp链接: ",
                    f"{BASE_URL}{dm}/cyclops/scan.html?url={BASE_URL}app/dmfe/h5-ultron-buy/index.html?buyParam={itemId}_{num}_{sku['skuId']}&buyNow=true&exParams=%257B%2522channel%2522%253A%2522{dm}_app%2522%252C%2522{dm}%2522%253A%25222%2522%252C%2522umpChannel%2522%253A%2522100041005%2522%252C%2522subChannel%2522%253A%2522{dm}%2540{dm}h5_h5%2522%252C%2522atomSplit%2522%253A1%257D&spm=a2o71.project.sku.dbuy&sqm=dianying.h5.unknown.value",
                )


if __name__ == "__main__":
    BASE_URL = bytes.fromhex("68747470733a2f2f6d2e64616d61692e636e2f").decode()
    dm = bytes.fromhex("64616d6169").decode()
    args = sys.argv
    get_dm_bp(args[1], args[2])
    # python3 dm.py link num
