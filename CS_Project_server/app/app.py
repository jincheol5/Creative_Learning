from flask import Flask,jsonify,request
from config import db
import pymysql
import json


def create_app():
  app=Flask(__name__)
  app.config['JSON_AS_ASCII'] = False #한글 출력을 위해 ascii 인코딩 false
  
  def db_connect(): #db 연결 변수 리턴 함수 
    connect=pymysql.connect(host=db['host'],user=db['user'],password=db['pw'],db=db['database'],charset='utf8')
    return connect
  
  @app.route('/',methods=['GET'])
  def hello_world():
    print(request.remote_addr)
    return 'os = return_os_quiz, cs = return_cs_quiz'

  @app.route('/return_os_quiz',methods=['GET'])
  def return_os_quiz():
    con=db_connect()
    
    cur=con.cursor(pymysql.cursors.DictCursor)
    
    cur.execute('select * from os_quiz order by rand() limit 10')
    #cur.execute('select * from os_quiz where id=1')   
    
    data=cur.fetchall() #rows = dic
    
    con.close() #db 연결 끊기 
    
    return jsonify(data) #json 형태로 변환해서 반환 
  
  @app.route('/return_cs_quiz',methods=['GET'])
  def return_cs_quiz():
    con=db_connect()
    
    cur=con.cursor(pymysql.cursors.DictCursor)
    
    cur.execute('select * from cs_quiz order by rand() limit 10')
    #cur.execute('select * from os_quiz where id=1')   
    
    data=cur.fetchall() #rows = dic
    
    con.close() #db 연결 끊기 
    
    return jsonify(data) #json 형태로 변환해서 반환 

  @app.route('/return_all_quiz',methods=['GET'])
  def return_all_quiz():
    con=db_connect()
    
    cur=con.cursor(pymysql.cursors.DictCursor)
    
    cur.execute('select * from all_quiz order by rand() limit 10')
    #cur.execute('select * from os_quiz where id=1')   
    
    data=cur.fetchall() #rows = dic
    
    con.close() #db 연결 끊기 
    
    return jsonify(data) #json 형태로 변환해서 반환 
  
  
  return app