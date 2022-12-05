import flask_login
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from project import app, db
from project.models import Message, User
from flask import send_file
import pdfkit
import validators

kitoptions = {
    "enable-local-file-access": None
}


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
@login_required
def main():
    return render_template('main.html', output=flask_login.current_user.name_form,
                           output2=flask_login.current_user.age_form,
                           output3=flask_login.current_user.address_form,
                           output4=flask_login.current_user.email_form,
                           output5=flask_login.current_user.phone_form,
                           output6=flask_login.current_user.profession_form,
                           output7=flask_login.current_user.description_form,
                           output8=flask_login.current_user.experience_form,
                           output9=flask_login.current_user.education_form,
                           output10=flask_login.current_user.projects_form,
                           output11=flask_login.current_user.skills_form,
                           output12=flask_login.current_user.interests_form,
                           output13=flask_login.current_user.image_url_form)


@app.route('/add_message', methods=['POST'])
@login_required
def add_message():
    if request.form['age']:
        if len(request.form['age']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            age = request.form['age']
            flask_login.current_user.age_form = age
    if request.form['text']:
        if len(request.form['text']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            name = request.form['text']
            flask_login.current_user.name_form = name
    if request.form['address']:
        if len(request.form['address']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            address = request.form['address']
            flask_login.current_user.address_form = address
    if request.form['email']:
        if len(request.form['email']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            email = request.form['email']
            flask_login.current_user.email_form = email
    if request.form['phone']:
        if len(request.form['phone']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            phone = request.form['phone']
            flask_login.current_user.phone_form = phone
    if request.form['profession']:
        if len(request.form['profession']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            profession = request.form['profession']
            flask_login.current_user.profession_form = profession
    if request.form['desc']:
        if len(request.form['desc']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            desc = request.form['desc']
            flask_login.current_user.description_form = desc
    if request.form['experience']:
        if len(request.form['experience']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            experience = request.form['experience']
            flask_login.current_user.experience_form = experience
    if request.form['education']:
        if len(request.form['education']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            education = request.form['education']
            flask_login.current_user.education_form = education
    if request.form['projects']:
        if len(request.form['projects']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            projects = request.form['projects']
            flask_login.current_user.projects_form = projects
    if request.form['skills']:
        if len(request.form['skills']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            skills = request.form['skills']
            flask_login.current_user.skills_form = skills
    if request.form['interests']:
        if len(request.form['interests']) > 1024:
            flash('The limit of symbols only 1024')
        else:
            interests = request.form['interests']
            flask_login.current_user.interests_form = interests
    if request.form['image_url']:
        if validators.url(request.form['image_url']):
            if len(request.form['image_url']) > 1024:
                flash('The limit of symbols only 1024')
            else:
                image_url = request.form['image_url']
                flask_login.current_user.image_url_form = image_url
        else:
            flash('The image url is not valid')

    db.session.add(Message(flask_login.current_user.name_form, flask_login.current_user.age_form,
                           flask_login.current_user.address_form, flask_login.current_user.email_form,
                           flask_login.current_user.phone_form, flask_login.current_user.profession_form,
                           flask_login.current_user.description_form,
                           flask_login.current_user.experience_form, flask_login.current_user.education_form,
                           flask_login.current_user.projects_form,
                           flask_login.current_user.skills_form, flask_login.current_user.interests_form,
                           flask_login.current_user.image_url_form))
    db.session.commit()

    return render_template('main.html', output=flask_login.current_user.name_form,
                           output2=flask_login.current_user.age_form,
                           output3=flask_login.current_user.address_form,
                           output4=flask_login.current_user.email_form,
                           output5=flask_login.current_user.phone_form,
                           output6=flask_login.current_user.profession_form,
                           output7=flask_login.current_user.description_form,
                           output8=flask_login.current_user.experience_form,
                           output9=flask_login.current_user.education_form,
                           output10=flask_login.current_user.projects_form,
                           output11=flask_login.current_user.skills_form,
                           output12=flask_login.current_user.interests_form,
                           output13=flask_login.current_user.image_url_form)


@app.route('/make_pdf', methods=['GET', 'POST'])
@login_required
def make_pdf():
    try:
        pdf_template = render_template('make_pdf.html',
                                       image=flask_login.current_user.image_url_form,
                                       name=flask_login.current_user.name_form,
                                       age=flask_login.current_user.age_form,
                                       address=flask_login.current_user.address_form,
                                       email=flask_login.current_user.email_form,
                                       phone=flask_login.current_user.phone_form,
                                       profession=flask_login.current_user.profession_form,
                                       desc=flask_login.current_user.description_form,
                                       experience=flask_login.current_user.experience_form,
                                       education=flask_login.current_user.education_form,
                                       projects=flask_login.current_user.projects_form,
                                       skills=flask_login.current_user.skills_form,
                                       interests=flask_login.current_user.interests_form)

        pdfkit.from_string(pdf_template, f'out{flask_login.current_user}.pdf', options=kitoptions)

        return render_template('make_pdf.html',
                               image=flask_login.current_user.image_url_form,
                               name=flask_login.current_user.name_form,
                               age=flask_login.current_user.age_form,
                               address=flask_login.current_user.address_form,
                               email=flask_login.current_user.email_form,
                               phone=flask_login.current_user.phone_form,
                               profession=flask_login.current_user.profession_form,
                               desc=flask_login.current_user.description_form,
                               experience=flask_login.current_user.experience_form,
                               education=flask_login.current_user.education_form,
                               projects=flask_login.current_user.projects_form,
                               skills=flask_login.current_user.skills_form,
                               interests=flask_login.current_user.interests_form)
    except Exception as e:
        return str(e)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            # next_page = request.args.get('next')

            return redirect(url_for('main'))
            # return render_template('main.html')
        else:
            flash('Please fill correct login or password')
    # else:
    #     flash('Please fill login and password')
    return render_template('login_page.html')


@app.route('/download')
def download():
    try:
        exact_path = f'/Users/victoriakovalevskaya/PycharmProjects/flask/out{flask_login.current_user}.pdf'
        return send_file(exact_path, as_attachment=True)
    except Exception as e:
        return str(e)


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Please fill all fields')
        elif password != password2:
            flash('Passwords are not equal')
        else:
            if User.query.filter_by(login=login).first() == None:
                hash = generate_password_hash(password)
                new_user = User(login=login, password=hash)
                new_user.name_form = ''
                new_user.age_form = ''
                new_user.skills_form = ''
                new_user.email_form = ''
                new_user.phone_form = ''
                new_user.education_form = ''
                new_user.address_form = ''
                new_user.projects_form = ''
                new_user.profession_form = ''
                new_user.interests_form = ''
                new_user.experience_form = ''
                new_user.description_form = ''
                new_user.image_url_form = 'https://antiseptik.trust-import.com/img/reviews-user-photo.jpg'
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('login_page'))
                # return render_template('login_page.html')
            else:
                flash('Create another login')
    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('hello_world'))


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)
    return response
