import pyrebase

config = {
  "apiKey": "AIzaSyAlZGHRqy9ask-QB1FJfynKMFyhosNN7S0",
  "authDomain" : "simple1-flask.firebaseapp.com",
  "databaseURL" : "https://simple1-flask-default-rtdb.firebaseio.com",
  "projectId" : "simple1-flask",
  "storageBucket" : "simple1-flask.appspot.com",
  "messagingSenderId" : "275262998052",
  "appId" : "1:275262998052:web:896c55bcd308a694d17ab1",
  "measurementId" : "G-0K8ZHTF4E8"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
auth = firebase.auth()
# db.child("Information").update({"Name":"avc "}) #-------> User push information
# value = db.child("Information").child("Name").get() #-----------------> User get information
# print(value.val())
# db.child("Information").remove() #------------------------> User remove information

rQu = db.child("Qset").child("Question").get()
Qu = rQu.val()

rOp1 = db.child("Qset").child("options").child("op1").get()
Op1 = rOp1.val()
# print(Op1)

rOp2 = db.child("Qset").child("options").child("op2").get()
Op2 = rOp2.val()
# print(Op2)

rOp3 = db.child("Qset").child("options").child("op3").get()
Op3 = rOp3.val()
# print(Op3)

rOp4 = db.child("Qset").child("options").child("op4").get()
Op4 = rOp4.val()
# print(Op4)

from flask import *
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("login.html")


@app.route("/home",methods=['GET','POST'])
def uLogin():
  if request.method == 'POST':
    email = request.form['name']
    password = request.form['pass']
    try:
      auth.sign_in_with_email_and_password(email, password)
      return render_template("home.html",Qu=(db.child("Qset").child("Question").get()).val(),
      op1=(db.child("Qset").child("options").child("op1").get()).val(),
      op2 =(db.child("Qset").child("options").child("op2").get()).val(),
      op3=(db.child("Qset").child("options").child("op3").get()).val(),
      op4 = (db.child("Qset").child("options").child("op4").get()).val())
    except:
      return 'आपला ईमेल आणि पासवर्ड बरोबर टाकावा🙏🏻'
  return render_template("login.html")

@app.route("/signup",methods=['GET','POST'])
def signUp():
  if request.method == 'POST':
    email = request.form['name']
    password = request.form['pass']
    try:
      user = auth.create_user_with_email_and_password(email,password)
      print(auth.get_account_info(user['idToken']))
    except:
      return 'User different strong password'
    return render_template("login.html")
  return render_template("signUp.html")

@app.route("/thanks",methods=['GET','POST'])
def thanks():
  val = f"आपले उत्तर चुकीचे आहे."
  givenAns = int(request.form['option'])
  ans = int((db.child("Qset").child("options").child("op5").get()).val())
  if ans == givenAns:
    print("Right answer.")
    val = "🎉🎊आपले उत्तर बरोबर आहे.🎊🎉"
    return render_template("thanks.html",val1= val)
  # print(f"User ans = {givenAns} \n Right answer = {ans}")
  # print(type(givenAns))
  # print(type(ans))
  return render_template("thanks.html",val1= val)
# @app.route('/', methods=['GET', 'POST'])
# def basic():
# 	if request.method == 'POST':
# 		if request.form['submit'] == 'add':

# 			name = request.form['name']
# 			db.child("todo").push(name)
# 			todo = db.child("todo").get()
# 			to = todo.val()
# 			return render_template('index.html', t=to.values())
# 		elif request.form['submit'] == 'delete':
# 			db.child("todo").remove()
# 		return render_template('index.html')
# 	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
