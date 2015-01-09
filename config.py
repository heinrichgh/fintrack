__author__ = 'heinrich'
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SECRET_KEY = "D_^14)2*#J}_NRr41IV~Xb;Qv1)aG{HU6.o;4XuuFmCB^(2ofsQ8w-y@[>:+?Bi"