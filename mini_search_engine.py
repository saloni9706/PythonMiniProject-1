import urllib.request
from urllib.error import URLError
import re
import pymysql
import mysql.connector


def crawl_all_url(url, domain):
    global url_crawler

    con = pymysql.connect(host ="localhost",user = "root",password="root",db ="python_search_engine")
    cur = con.cursor()


    if(url in url_crawler and url_crawler[url]==1):
        return
    else:
        url_crawler[url] = 1

    try:
        # print(url)
        page = urllib.request.urlopen(url)
        code = page.getcode()
        if(code==200):
            content=page.read()
            content_string=content.decode("utf-8")
            # print(content_string)
            reg_title=re.compile('<title>(?P<title>(.*))</title>')
            reg_Keywords=re.compile('<meta name="Keywords" content="(?P<Keywords>(.*))" />')
            reg_keywords=re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
            reg_description=re.compile('<meta name="Description" content="(?P<Description>(.*))" />')

            next_url=re.compile("https?://\w*"+domain+"[/\w+]*")

            result=reg_title.search(content_string, re.IGNORECASE)
            if result:
                title=result.group("title")
                print(title)
            else:
                title="NULL"
			
            result = reg_keywords.search(content_string, re.IGNORECASE)

            if result:
                keywords=result.group("keywords")
                print(keywords)
            else:
                result_1 = reg_Keywords.search(content_string, re.IGNORECASE)
                if result_1:
                    keywords=result_1.group("Keywords")
                    print(keywords)
                else:
                    keywords="NULL"
            result = reg_description.search(content_string, re.IGNORECASE)
            
            if result:
                description=result.group("Description")
                print(description)
            else:
                description="NULL"
            
            
            table_name="crawler"
            query="insert into "+table_name+" values ('"+title+"','"+keywords+"','"+url+"','"+description+"')"

            try:
                cur.execute(query)
                con.commit()
            except Exception as e:
                print(e)

            for (urls) in re.findall(next_url, content_string):
                if(urls  not in url_crawler or url_crawler[urls] != 1):
                    url_crawler[urls] = 0
                    crawl_all_url(urls, domain)
    

        
    except URLError as e:
        print("error")

url_crawler={}  
seed = "http://www.newhaven.edu/"
url_crawler[seed]=0
crawl_all_url(seed, "\.newhaven\.edu")
