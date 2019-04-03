import urllib.request
import urllib.parse
import json


def get_data(words):
    data = {}
    data["type"] = "AUTO"
    data["i"] = words
    data["doctype"] = "json"
    data["xmlVersion"] = "1.8"
    data["keyfrom:fanyi"] = "web"
    data["ue"] = "UTF-8"
    data["action"] = "FY_BY_CLICKBUTTON"
    data["typoResult"] = "true"
    data = urllib.parse.urlencode(data).encode('utf-8')
    return data


def url_open(url, data):
    req = urllib.request.Request(url, data)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1")

    response = urllib.request.urlopen(req)

    html = response.read()
    html = html.decode("utf-8")
    return html


def get_json_data(html):
    result = json.loads(html)
    result = result['translateResult']
    result = result[0][0]['tgt']
    return result


def main():
    words = input("please input words: ")
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict.top"

    data = get_data(words)
    print(data)
    html = url_open(url, data)
    print(html)
    result = get_json_data(html)
    print(result)
    print("The result: %s" % result)


if __name__ == "__main__":
    while True:
        main()