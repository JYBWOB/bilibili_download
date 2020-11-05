import sys
from you_get import common as you_get
from multiprocessing import Pool

directory = 'C:/Users/Administrator/Desktop/bilibili'

base_url = 'https://www.bilibili.com/video/BV1Yt411q7K1'

def get_urls(base_url, number):
    urls = []
    for i in range(1, number + 1):
        url = base_url + '?p=' + str(i)
        urls.append(url)
    return urls

def download(urls):
    sys.argv = ['you-get','-o',directory,'--no-caption',urls]
    you_get.main()
    
if __name__ == '__main__':
    urls = get_urls(base_url, 18)
    pool = Pool(10)
    pool.map(download, urls)
    pool.close()
    pool.join()