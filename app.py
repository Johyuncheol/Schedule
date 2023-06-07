from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.ohmkrzr.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')


# 출력하기위한 GET 요청 부분 
@app.route("/todo", methods=["GET"])
def todo_get():
    all_todo = list(db.todo.find({"location":0},{'_id':False}))
    return jsonify({'result':all_todo})

@app.route("/running", methods=["GET"])
def running_get():
    all_running = list(db.todo.find({"location":1},{'_id':False}))
    return jsonify({'result':all_running})

@app.route("/done", methods=["GET"])
def done_get():
    all_done = list(db.todo.find({"location":2},{'_id':False}))
    return jsonify({'result':all_done})



# 맨위 인풋태그로 입력받은 값 저장 
@app.route("/add", methods=["POST"])
def add_post():
    todo_receive = request.form['todo_give']
    doc={
        'todo':todo_receive,
        'location' : 0
    }
    db.todo.insert_one(doc)
    return jsonify({'msg': '저장완료'})
    

#이동을 위한 post 부분 
#버튼눌렸을때 상태 변경

#앞으로 진행될 때
@app.route("/move", methods=["POST"])
def move():
    move_data = request.form['move_data'] 

    m_data = db.todo.find_one({'todo':move_data})
    print(m_data)
    #완료변경 1이면 완료
    if(m_data['location']==0):
        loca=m_data['location']+1
        db.todo.update_one({'todo':move_data},{'$set':{'location':loca}})
        
    elif(m_data['location']==1):
        loca=m_data['location']+1
        db.todo.update_one({'todo':move_data},{'$set':{'location':loca}})
    
    elif(m_data['location']==2):
        loca=m_data['location']+1
        db.todo.delete_one({'todo':move_data})

    return jsonify({'msg': '변경!!'})


#뒤로 진행될 때
@app.route("/move_cancel", methods=["POST"])
def move_cancel():
    move_data = request.form['move_data'] 

    m_data = db.todo.find_one({'todo':move_data})
    print(m_data)
    #완료변경 1이면 완료
    if(m_data['location']==2):
        loca=m_data['location']-1
        db.todo.update_one({'todo':move_data},{'$set':{'location':loca}})
        
    elif(m_data['location']==1):
        loca=m_data['location']-1
        db.todo.update_one({'todo':move_data},{'$set':{'location':loca}})
    
    elif(m_data['location']==0):
        loca=m_data['location']-1
        db.todo.delete_one({'todo':move_data})
        
    return jsonify({'msg': '변경!!'})

    
if __name__ == '__main__':
    app.run()