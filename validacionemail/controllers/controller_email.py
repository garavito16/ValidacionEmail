
from flask import render_template,redirect, request, session, flash
from validacionemail import app
from validacionemail.models.model_email import Email

@app.route('/',methods=["GET"])
def load_page():
    return render_template("index.html")

@app.route('/success',methods=["GET"])
def load_success():
    emails = Email.getEmail()
    return render_template('success.html',emails=emails)

@app.route('/add_email',methods=["POST"])
def add_email():
    email = {
        "correo_electronico" : request.form["email"]
    }
    #validate email correct
    validate = Email.validate_email(email)
    if(validate):
        #Validat repeat email
        emails = Email.getEmail()
        validate = True
        for aux in emails:
            if(aux["correo_electronico"] == email["correo_electronico"]):
                validate = False
        
        if validate:
            resultado = Email.addEmail(email)
            if(resultado > 0):
                flash("The email address you entered "+email["correo_electronico"]+" is a VALID email address! Thank you!")
                return redirect('/success')
            else:
                flash("Error registering email address")
                return redirect('/')
        else:
            flash("Email address already exists")
            return redirect('/')
    else:
        # el mensaje se envia desde el modelo
        return redirect('/')

@app.route('/delete_email',methods=["POST"])
def delete_email():
    email = {
        "id" : request.form["id"]
    }
    Email.delete_email(email)
    return redirect('/success')