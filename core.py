
import cookielib
import urllib2, urllib
import time
import re
import traceback

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'),
                     ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'), 
                     ('Accept-Encoding', 'gzip,deflate,sdch'), 
                     ('Accept-Language', 'zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4'), 
                     ('Cache-Control:', 'max-age=0'),
                     ('Connection', 'keep-alive'),
                     ('Host', '42.62.10.213:20000'),
                     #('Cookie', 'JSESSIONID=7786B6BF86273AE0F8600355EB81C799; cod=15.17; csd=151'),
                     ]


def get_page(url, data=None):
    resp = None
    n = 0
    while n < 5:
        n = n + 1
        try:
            resp = opener.open(url, data)
            page = resp.read()
            return page
        except:
            traceback.print_exc()
            print "Will try after 2 seconds ..."
            time.sleep(2.0)
            continue
        break
    return "Null"



LOGIN_URL = "http://42.62.10.213:20000/userlogin.jsp"
MANAGE_URL = "http://42.62.10.213:20000/manage.jsp"
QUERY_URL= "http://42.62.10.213:20000/sms_kf/QueryMo2.jsp"


username = "gd84"
passwd = "123456"
mobile = "13556373414"
startdate = "2014/07/27"
enddate = "2014/07/28"


def get_rnum(mobile, startdate, enddate):

    formData = urllib.urlencode({'username' : username,
                                 'passwd' : passwd,
                                 })
    p = get_page(LOGIN_URL, formData)

    #p = get_page(MANAGE_URL)
    #assert 'parent.location.href="/index.jsp"' not in p, "Login failed!"

    query_url = "%s?mobile=%s&startdate=%s&enddate=%s" % (QUERY_URL, mobile, startdate, enddate) 
    print query_url
    p = get_page(query_url)

    rs = re.findall("\xb9\xb2(.*)\xcc\xf5", p)
    if rs:
        rnum = rs[0]
    else:
        rnum = "0"

    print rnum

    return rnum


if __name__ == "__main__":
    print get_rnum(mobile, startdate, enddate)
