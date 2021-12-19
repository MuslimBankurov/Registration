#Написать приложение на flask который по адресу "signup" запрашивает следующие данные у пользователя: username, email, password, confirm_password(подтверждение пароля)! 
#Сделать валидацию данных (проверка правильности). 
#username не менее 6 символов
#email должен содержать знак @ (более подробно разберем чуть дальше)
#password - не менее 8 символов
#confirm_password - равен password
#Вся проверка делается на стороне сервера, в случае валидности данных сохранить (как вам удобнее) и вывести на странице "users"!


from os import write
from flask import Flask, render_template, request

app = Flask (__name__)


@app.route('/signup', methods = ["GET", "POST"])
def index ():
    if request.method == 'POST':
        user = request.form.get ('Username')
        email = request.form.get('email') 
        password = request.form.get('password')
        if  request.form.get('confirm_password') == password:  
            with open ('users.txt', 'w', encoding='utf-8') as f:
                f.write = (user, email, password)
    return render_template ('index.html')
    
    
if __name__  == '__main__':
    app.run(debug=True)