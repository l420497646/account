from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/post/reg',methods=['POST'])
def post_reg():
    print(request.form)
    user = request.form.get("uu")
    password = request.form.get("pp")
    gender = request.form.get("gender")
    hobby_list = request.form.getlist("hobby")
    city = request.form.get("city")
    skill = request.form.getlist("skill")
    more = request.form.get("more")
    return "注册成功"

@app.route('/mi',methods=['get'])
def get_mi():
    return render_template('mi.html')

if __name__ == "__main__":
    app.run()