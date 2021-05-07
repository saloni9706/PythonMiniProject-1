import pymysql
import mysql.connector
import json
import time

start=time.time()
con = pymysql.connect(host ="localhost",user = "root",password="root",db ="python_search_engine")
cur = con.cursor()

search_keyword=input("Enter keyword for search : ")

table_name="crawler"
param="%"
get_data="select * from "+table_name+" where Title LIKE '"+param+search_keyword+param+"' OR Content LIKE '"+param+search_keyword+param+"'"
# print(get_data)
json_string = '{"search_content":[],"execution_details":[]}'
cur.execute(get_data)
total_count=0
try:
    con.commit()
    for i in cur:
        output={}
        execution_details={}
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
        total_count+=1
    execution_time=time.time()-start

    execution_details["total_count"]=total_count
    execution_details["execution_time"]=execution_time
    json_dict['execution_details'].append(execution_details)
    # json_dict['time_to_execute'].append(execution_time)
    json_string = json.dumps(json_dict,indent=2)


    print(json_string)  
except Exception as e:
    print(e)


