from flask import Flask, render_template, jsonify, request
import easyocr
from PIL import Image
import io
import numpy as np
from APPSql import SQLHandler
app = Flask(__name__)

reader = easyocr.Reader(['en'], gpu=False)


def lastRFIDNum():
    connection = SQLHandler("FEU")
    query = "SELECT * FROM rfid_info WHERE Status = 0 ORDER BY ID LIMIT 1"
    results = connection.execute_query(query)
    rfid_num = results[0][1]
    update_query = f"UPDATE rfid_info SET Status = 1 WHERE RFID_NUM = '{rfid_num}'"
    connection.UD_query(update_query)
    return rfid_num



@app.route("/remove", methods=["POST"])
def testAPI2():
    connection = SQLHandler("FEU")
    data = request.get_json()
    rfid = data.get("RFID")
    remove_query = f"DELETE FROM visitors_info WHERE RFID_NUM = '{rfid}' "
    timeline = f"SELECT timing FROM rfid_info WHERE RFID_NUM = '{rfid}'"
    results = connection.execute_query(timeline)[0][0]
    remove_id = f"UPDATE rfid_info SET Status = 0 WHERE RFID_NUM = '{rfid}' "
    connection.UD_query(remove_query)
    connection.UD_query(remove_id)
    print(results)
    return jsonify({"Success": results})


@app.route("/image", methods=["POST"])
def testAPI():
    connection = SQLHandler("FEU")
    rfid = ""
    timing = ''
    if 'file' not in request.files:
        return jsonify({"error": "No File Part"}), 400
    file = request.files['file']
    try:
        image = Image.open(io.BytesIO(file.read()))
        image = image.convert('RGB')
        image_np = np.array(image)
        results = reader.readtext(image_np)
        text = [text.title() for (bbox, text, prob) in results]
        count = "SELECT COUNT(*) AS COUNT FROM visitors_info"
        results = connection.execute_query(count)
        total_count = results[0][0]
        print(text)
        if total_count <= 15:
            if " ".join(text).__contains__("Philippine Identification"):
                print("run")
                surname = text[6]
                firstname = text[8]
                print(surname, firstname)
                card = "Philippine Identification Card"
                purpose = "School"
                rfid = lastRFIDNum()
                insert_query = f"""INSERT INTO visitors_info(RFID_NUM, FirstName, LastName, Type, Purpose, Status) VALUES
                ('{rfid}', '{firstname}', '{surname}', '{card}', '{purpose}', 'Pending') """
                connection.UD_query(insert_query)
                timing = f"SELECT timing from rfid_info WHERE RFID_NUM = '{rfid}'"
                results = connection.execute_query(timing)[0][0]
                return jsonify({'result': f"card,{results}"})

            elif " ".join(text).__contains__("Department Of Transportation"):
                full_name = text[6].replace(",", "").split(" ")
                firstname = full_name[1]
                surname = full_name[0]
                card = "Drivers License"
                purpose = "School"
                rfid = lastRFIDNum()
                insert_query = f"""INSERT INTO visitors_info(RFID_NUM, FirstName, LastName, Type, Purpose, Status) VALUES 
                ('{rfid}', '{firstname}', '{surname}', '{card}', '{purpose}', 'Pending') """
                connection.UD_query(insert_query)
                timing = f"SELECT timing from rfid_info WHERE RFID_NUM = '{rfid}'"
                results = connection.execute_query(timing)[0][0]
                return jsonify({'result': f"card,{results}"})
            elif " ".join(text).__contains__("Unified Multi-Purpose Id") or " ".join(text).__contains__("'Unified Multi-Purpose Id") or " ".join(text):
                surname = text[5]
                firstname = text[6]
                card = "HUMID"
                purpose = "School"
                rfid = lastRFIDNum()
                insert_query = f"""INSERT INTO visitors_info(RFID_NUM, FirstName, LastName, Type, Purpose, Status) VALUES 
                ('{rfid}', '{firstname}', '{surname}', '{card}', '{purpose}', 'Pending') """
                connection.UD_query(insert_query)
                timing = f"SELECT timing from rfid_info WHERE RFID_NUM = '{rfid}'"
                results = connection.execute_query(timing)[0][0]
                return jsonify({'result': f"card,{results}"})
    except Exception as e:
        return jsonify({"text": str(e)}), 500

@app.route("/image2", methods=["POST"])
def testAPI3():
    connection = SQLHandler("FEU")
    rfid = ""
    timing = ''
    if 'file' not in request.files:
        return jsonify({"error": "No File Part"}), 400
    file = request.files['file']
    try:
        image = Image.open(io.BytesIO(file.read()))
        image = image.convert('RGB')
        image_np = np.array(image)
        results = reader.readtext(image_np)
        text = [text.title() for (bbox, text, prob) in results]
        count = "SELECT COUNT(*) AS COUNT FROM visitors_info"
        results = connection.execute_query(count)
        total_count = results[0][0]
        print(text)
        if total_count <= 15:
            if " ".join(text).__contains__("Philippine Identification"):
                print("run")
                surname = text[6]
                firstname = text[8]
                print(surname, firstname)
                card = "Philippine Identification Card"
                purpose = "School"
                rfid = lastRFIDNum()
                insert_query = f"""INSERT INTO visitors_info(RFID_NUM, FirstName, LastName, Type, Purpose, Status) VALUES
                ('{rfid}', '{firstname}', '{surname}', '{card}', '{purpose}', 'Pending') """
                connection.UD_query(insert_query)
                timing = f"SELECT timing from rfid_info WHERE RFID_NUM = '{rfid}'"
                results = connection.execute_query(timing)[0][0]
                return jsonify({'result': f"card,{results}"})

            elif " ".join(text).__contains__("Department Of Transportation"):
                full_name = text[6].replace(",", "").split(" ")
                firstname = full_name[1]
                surname = full_name[0]
                card = "Drivers License"
                purpose = "School"
                rfid = lastRFIDNum()
                insert_query = f"""INSERT INTO visitors_info(RFID_NUM, FirstName, LastName, Type, Purpose, Status) VALUES 
                ('{rfid}', '{firstname}', '{surname}', '{card}', '{purpose}', 'Pending') """
                connection.UD_query(insert_query)
                timing = f"SELECT timing from rfid_info WHERE RFID_NUM = '{rfid}'"
                results = connection.execute_query(timing)[0][0]
                return jsonify({'result': f"card,{results}"})
            elif " ".join(text).__contains__("Unified Multi-Purpose Id") or " ".join(text).__contains__("'Unified Multi-Purpose Id") or " ".join(text):
                surname = text[5]
                firstname = text[6]
                card = "HUMID"
                purpose = "School"
                rfid = lastRFIDNum()
                insert_query = f"""INSERT INTO visitors_info(RFID_NUM, FirstName, LastName, Type, Purpose, Status) VALUES 
                ('{rfid}', '{firstname}', '{surname}', '{card}', '{purpose}', 'Pending') """
                connection.UD_query(insert_query)
                timing = f"SELECT timing from rfid_info WHERE RFID_NUM = '{rfid}'"
                results = connection.execute_query(timing)[0][0]
                return jsonify({'result': f"card,{results}"})
    except Exception as e:
        return jsonify({"text": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

