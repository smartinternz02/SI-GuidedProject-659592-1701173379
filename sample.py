from flask import * # importing all the functions

abc = Flask(__name__) # intializing the flask object

@abc.route("/") # ip address https://127.0.0.1:5000/
def home():
    return render_template("home.html")

@abc.route("/a") # ip address https://127.0.0.1:5000/
def login():
    return render_template("login.html")

@abc.route("/submit", methods = ['POST'])
def validate():
    Email = request.form['Email']
    Password = request.form['Password']
    if Email == "admin@gmail.com" and Password == "12345":
        return "Welcome to portal"
    else:
        return render_template("register.html")
    
@abc.route("/submit1", methods = ['POST'])
def register1():
    Name = request.form['Name']
    Email = request.form['Email']
    MobileNo = request.form['Mobile No']
    Password = request.form['Password']
    return render_template("login.html", UserInformation = [Name,Email,MobileNo,Password])

    

@abc.route("/b") # ip address https://127.0.0.1:5000/
def register():
    return render_template("register.html")


if __name__ == "__main__":
    abc.run(debug = True,port = 8089)


