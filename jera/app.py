from flask import Flask, render_template, request
from form import RegistrationForms
import structure

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForms(request.form)
    if(form.validate_on_submit()):
        try:
            user = structure.DB(form.idnum.data, form.firstname.data, form.middlename.data, form.lastname.data, form.sex.data, form.course.data)
            user.register()
            return render_template("added.html")
        except:
            return 'Registration Error: User has already existed'
    return render_template("register.html", form=form)

@app.route('/search', methods=["GET", "POST"])
def search():
    if(request.method == "POST"):
        info = request.form['searcher']
        result = structure.search(info)
        return render_template('result.html', result=result)
    return render_template("back-to-home.html")

@app.route('/delete', methods=["GET", "POST"])
def delete():
    if (request.method == "POST"):
        info = request.form['idnum']
        structure.delete(info)
        return render_template('deleted.html')
    return render_template("delete.html")

@app.route('/update', methods=['GET','POST'])
def update():
    try:
        copy = request.form['copy']
        idnum = request.form['idnum']
        firstname = request.form['firstname']
        middlename = request.form['middlename']
        lastname = request.form['lastname']
        sex = request.form['sex']
        course = request.form['course']
        structure.update(copy, idnum, firstname, middlename, lastname, sex, course)
        return render_template('updated.html')
    except:
        return 'Error!'

@app.route('/displayall', methods=['GET', 'POST'])
def all():
    cs = structure.all()
    return render_template('allTables.html',cs=cs)


if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(debug=True)
