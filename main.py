import sys, getopt
from you_get import common as you_get
from multiprocessing import Pool

directory = './'

base_url = ''

bv_id = ''

thread_num = 8

download_num = 1

def get_urls_by_url(base_url, number):
    urls = []
    for i in range(1, number + 1):
        url = base_url + '?p=' + str(i)
        urls.append(url)
    return urls

def get_urls_by_bv(bv_id, number):
    urls = []
    for i in range(1, number + 1):
        url = 'https://www.bilibili.com/video/' + bv_id + '?p=' + str(i)
        urls.append(url)
    return urls

def download_func(urls):
    sys.argv = ['you-get','-o',directory,'--no-caption',urls]
    you_get.main()
    
def print_help_info():
    print('\t-h(--help) : help info')
    print('\t-o(--opath) : Specify the output folder, default value is \'./\'')
    print('\t-u(--url) : bilibili video url, u must give one of the param between url and bv-id')
    print('\t-b(--bv) : bilibili video bv-id, u must give one of the param between url and bv-id')
    print('\t-t(--tread_num) : download thread number, default value is 8')
    print('\t-n(--number) : download \'number\' of the videos in the playlist, default value is 1')
    
def get_params(argv):
    global directory, base_url, bv_id, thread_num, download_num
    try:
        opts, _ = getopt.getopt(argv, '-h-o:-u:-b:-t:-n:', ['help', 'opath=', 'url=', 'bv=', 'tread_num=', 'number='])
    except getopt.GetoptError:
        print_help_info()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print_help_info()
            sys.exit(2)
        elif opt in ('-o', '--opath'):
            directory = arg
        elif opt in ('-u', '--url'):
            base_url = arg
        elif opt in ('-b', '--bv'):
            bv_id = arg
        elif opt in ('-t', '--tread_num'):
            thread_num = int(arg)
        elif opt in ('-n', '--number'):
            download_num = int(arg)
        else:
            print('can\'t handle param %s' % opt)
            
def judge_param():
    if base_url == '' and bv_id == '':
        print('u must give one of the param between url and bv-id')
        print('please give the video url or the bv-number')
        print('param -h to get more info')
        sys.exit(2)

def download(argv):
    get_params(argv)
    judge_param()
    
    if base_url != '':
        urls = get_urls_by_url(base_url, download_num)
    elif bv_id != '':
        urls = get_urls_by_bv(bv_id, download_num)
    try:
        pool = Pool(thread_num)
        pool.map(download_func, urls)
        pool.close()
        pool.join()
    except:
        pool.terminate()
        print('stop all the tasks')
    
if __name__ == '__main__':
    download(sys.argv[1:])
    
