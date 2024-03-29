import os
class Config:
    SECRET_KEY=os.environ.get('SECRET')
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALC')
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('EMAIL_USER')
    MAIL_PASSWORD=os.environ.get('EMAIL_PASS')