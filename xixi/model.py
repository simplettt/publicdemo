from sqlalchemy import create_engine

host = '120.79.19.253'
port = 3306
user = 'xy'
pas = '387e86d8-bd78-48a0-adf0-c97bc1e6da15'
dbname = 'xy'

from string import Template

dbConfig = {'host': host, 'port': port, 'user': user, 'pas': pas, 'dbname': dbname}

engine = create_engine(Template('mysql+pymysql://$user:$pas@$host:$port/$dbname').substitute(dbConfig), echo=True)




from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    users = relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, index=True)
    role_id = Column(Integer, ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username