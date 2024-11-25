import mysql.connector
from mysql.connector import Error
import random

class SQLHandler:
    def __init__(self, db):
        self.username = "root"
        self.hostname = "localhost"
        self.password = "12345908527"
        self.db = db
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                user=self.username,
                host=self.hostname,
                passwd=self.password,
                database=self.db
            )

            print("Connected Successfully")
        except Error as err:
            print(f"Error:{err}")

    def UD_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
        except Error as err:
            print(f"Error:{err}")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        result = []
        try:
            cursor.execute(query)
            result = cursor.fetchall()

            return result
        except Error as err:
            print(f"Error:{err}")



if __name__ == "__main__":
    connection = SQLHandler("FEU")

    active_id = "SELECT * FROM rfid_info WHERE Status = 0"

    try:
        # results = [i[1] for i in connection.execute_query(active_id)]
        # random_active_id = random.choice(results)
        #
        # insert_query = f"""
        # INSERT INTO visitors_info(RFID_NUM, FirstName, LastName, Type, Purpose, Status) VALUES
        # ('{random_active_id}','Christopher', 'Anay', 'HUMID ID', 'School', 'Pending')
        # """
        # connection.UD_query(insert_query)
        #
        # update_rfid_active = f"UPDATE rfid_info SET Status = 1 WHERE RFID_NUM = '{random_active_id}'"
        # connection.UD_query(update_rfid_active)
        # print("Available RFID", len(results))
        connection = SQLHandler("FEU")
        # data = request.get_json()
        # rfid = data.get("RFID")
        # remove_query = f"DELETE FROM visitors_info WHERE RFID_NUM = '{rfid}' "
        timeline = f"SELECT timing FROM rfid_info WHERE RFID_NUM = 'F86BA4D3D' "
        results = connection.execute_query(timeline)[0][0]
        # remove_id = f"UPDATE rfid_info SET Status = 0 WHERE RFID_NUM = '{rfid}' "
        # connection.UD_query(remove_query)
        # connection.UD_query(remove_id)
        print(results)






    except IndexError as err:
        print("No RFID Available")
    finally:
        connection.connection.close()





    # query = """INSERT INTO Visitors_Info(FirstName, LastName, Type, Purpose, Status) VALUES
    #            ('Christopher', 'Anay', 'HUMID ID', 'Accounting', 'Pending')"""

    # connection.UD_query(query)





