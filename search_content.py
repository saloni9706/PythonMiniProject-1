import pymysql
import mysql.connector
import json

con = pymysql.connect(host ="localhost",user = "root",password="root",db ="python_search_engine")
cur = con.cursor()

search_keyword=input("Enter keyword for search : ")

table_name="crawler"
param="%"
get_data="select * from "+table_name+" where Title LIKE '"+param+search_keyword+param+"'"
print(get_data)
json_string = '{"search_content":[]}'
cur.execute(get_data)
try:
    con.commit()
    for i in cur:
        output={}
        output["Title"]=i[0]
        output["Keywords"]=i[1]
        output["Url"]=i[2]
        output["Content"]=i[3]
        
        # convert it to a python dictionary
        json_dict = json.loads(json_string)
        # append your data as {key:value}
        json_dict['search_content'].append(output)
        # convert it back to string
        json_string = json.dumps(json_dict,indent=2)

    print(json_string)  
except Exception as e:
    print(e)


