from flask_login import UserMixin

from project import db, manager


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_user = db.Column(db.String(1024), nullable=False)
    age = db.Column(db.String(1024), nullable=False)
    address = db.Column(db.String(1024), nullable=False)
    email = db.Column(db.String(1024), nullable=False)
    phone = db.Column(db.String(1024), nullable=False)
    profession = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    experience = db.Column(db.String(1024), nullable=False)
    education = db.Column(db.String(1024), nullable=False)
    projects = db.Column(db.String(1024), nullable=False)
    skills = db.Column(db.String(1024), nullable=False)
    interests = db.Column(db.String(1024), nullable=False)
    image_url = db.Column(db.String(1024), nullable=False)

    def __init__(self, name, age, address, email, phone, profession, description, experience, education, projects,
                 skills, interests, image):
        self.name_user = name
        self.age = age
        self.address = address
        self.email = email
        self.phone = phone
        self.profession = profession
        self.description = description
        self.experience = experience
        self.education = education
        self.projects = projects
        self.skills = skills
        self.interests = interests
        self.image_url = image



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(1024), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False)
    name_form = db.Column(db.String(1024), nullable=False)
    age_form = db.Column(db.String(1024), nullable=False)
    address_form = db.Column(db.String(1024), nullable=False)
    email_form = db.Column(db.String(1024), nullable=False)
    phone_form = db.Column(db.String(1024), nullable=False)
    profession_form = db.Column(db.String(1024), nullable=False)
    description_form = db.Column(db.String(1024), nullable=False)
    experience_form = db.Column(db.String(1024), nullable=False)
    education_form = db.Column(db.String(1024), nullable=False)
    projects_form = db.Column(db.String(1024), nullable=False)
    skills_form = db.Column(db.String(1024), nullable=False)
    interests_form = db.Column(db.String(1024), nullable=False)
    image_url_form = db.Column(db.String(1024), nullable=False)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
