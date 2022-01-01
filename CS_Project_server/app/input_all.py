
from flask import Flask,jsonify,request
from config import db
import pymysql
import json
import os


#question 리턴하는 함수
def return_os_q(id):
  #문제 id
  id_str=str(id)
  path="app/os_data/os_q/os-"+id_str+".txt"
  file=open(path,'r',encoding='utf-8')
  
  question=file.readline().rstrip()#끝에 '\n'제거
  
  file.close()
  
  return question

def return_cs_q(id):
  #문제 id
  id_str=str(id)
  path="app/cs_data/cs_q/ca-"+id_str+".txt"
  file=open(path,'r',encoding='utf-8')
  
  question=file.readline().rstrip()#끝에 '\n'제거
  
  file.close()
  
  return question


#ans,ans_list 담긴 dic 리턴
def return_os_ans_list(id):
  
  dic={}
  #문제 id
  id_str=str(id)
  path="app/os_data/os_ans/os-"+id_str+"-a.txt"
  file=open(path,'r',encoding='utf-8')
  
  ans_list=file.readline().split(',')
  ans_list[3]=ans_list[3].rstrip()#끝에 '\n'제거
  
  ans=file.readline().rstrip() #끝에 '\n'제거
  
  dic['ans']=ans
  dic['ans_list']=ans_list
  
  return dic

def return_cs_ans_list(id):
  
  dic={}
  #문제 id
  id_str=str(id)
  path="app/cs_data/cs_ans/ca-"+id_str+"-a.txt"
  file=open(path,'r',encoding='utf-8')
  
  ans_list=file.readline().split(',')
  ans_list[3]=ans_list[3].rstrip()#끝에 '\n'제거
  
  ans=file.readline().rstrip() #끝에 '\n'제거
  
  dic['ans']=ans
  dic['ans_list']=ans_list
  
  return dic

    
def db_connect(): #db 연결 변수 리턴 함수 
  connect=pymysql.connect(host=db['host'],user=db['user'],password=db['pw'],db=db['database'],charset='utf8')
  return connect
  
print(os.getcwd())

con=db_connect()
    
cur=con.cursor(pymysql.cursors.DictCursor)


question=""

ans=""

for i in range(1,31):
  id=str(i)
  question=return_os_q(i)
  dic=return_os_ans_list(i)
  ans_list=dic['ans_list']
  ans=dic['ans']
  sql="insert into all_quiz values("+id+",'"+question+"','"+ans_list[0]+"','"+ans_list[1]+"','"+ans_list[2]+"','"+ans_list[3]+"','"+ans+"')"
  cur.execute(sql)
  con.commit()
  print(sql)

for i in range(1,28):
  id=str(i+30)
  question=return_cs_q(i)
  dic=return_cs_ans_list(i)
  ans_list=dic['ans_list']
  ans=dic['ans']
  sql="insert into all_quiz values("+id+",'"+question+"','"+ans_list[0]+"','"+ans_list[1]+"','"+ans_list[2]+"','"+ans_list[3]+"','"+ans+"')"
  cur.execute(sql)
  con.commit()
  print(sql)



con.close() #db 연결 끊기 