import requests


def get_ip(num):
    url = f"http://webapi.http.zhimacangku.com/getip?num={num}&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
    resp = requests.get(url).json()
    ip_list = []
    for i in resp['data']:
        ip = i['ip'] + ":" + str(i['port'])
        ip_list.append(ip)
    return ip_list


if __name__ == '__main__':
    pass
