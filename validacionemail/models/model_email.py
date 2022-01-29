
from validacionemail.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    name_db = "esquema_email"
    

    def __init__(self,id,correo_electronico,created_at):
        self.id = id
        self.correo_electronico = correo_electronico
        self.created_at = created_at

    @classmethod
    def getEmail(cls):
        query = "SELECT * FROM email"
        resultado = connectToMySQL(cls.name_db).query_db(query)
        return resultado

    @classmethod
    def addEmail(cls,data):
        query = "INSERT INTO email (correo_electronico,created_at) VALUES (%(correo_electronico)s,now());"
        resultado = connectToMySQL(cls.name_db).query_db(query,data)
        return resultado
    
    @classmethod
    def validate_email(cls,data):
        is_valid = True
        if not EMAIL_REGEX.match(data["correo_electronico"]):
            flash("Invalid email address")
            is_valid = False
        return is_valid
    
    @classmethod
    def delete_email(cls,data):
        query = "DELETE FROM email WHERE id = %(id)s"
        resultado = connectToMySQL(cls.name_db).query_db(query,data)
        return resultado