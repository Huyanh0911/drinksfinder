from flask import Flask, render_template,request,redirect
app = Flask(__name__)
from models.data import cafe_ndt

@app.route('/all_cafe')
def cafe():
    all_cafe=cafe_ndt.find()
    return render_template('allcafe.html',all_cafe=all_cafe)
@app.route('/')
def index():
    return render_template('home.html') 
    
    
       
    
@app.route('/find',methods=["GET","POST"])
def find():
    if request.method =='GET':
        return render_template('index.html')
    elif request.method == 'POST':
        form = request.form
        a=(form["add"])
 
        
        findcafe=cafe_ndt.find({"Quan":a})

    
        
        return render_template('list1.html',findcafe=findcafe)

    


    


if __name__ == '__main__':
    app.run(debug=True)
 