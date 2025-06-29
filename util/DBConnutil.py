import mysql.connector
from util.PropertyUtil import PropertyUtil


class DBConnUtil:
    connection = None
    @staticmethod
    def get_connection():
        try:
            props = PropertyUtil.get_property("config/db.properties")
            connection = mysql.connector.connect(
                host = props["host"],
                user = props["user"],
                password = props["password"],
                database = props["database"]
            )
            return connection
        except mysql.connector.Error as e:
            print("Error while connecting to the database:", e)
            return None

if __name__=="__main__":
    conn = DBConnUtil.get_connection()
    if conn:
        print("Connection is successful")
    else:
        print("Connection failed")