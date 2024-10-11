# import easyocr
# import random
# from APPSql import SQLHandler
# reader = easyocr.Reader(['en'])
# result = reader.readtext("Photo/drivers2.jpg")
# type = [text.title() for (bbox, text, prob) in result]
#
# print(type)
# #
# # 'Republic Of The Philippines', 'Department Of Transportation',
# # 'Land Transportation Office', "Non-Professional Driver'$ License",
# # 'Last Wamne: Fist Maine: Middle Mama', 'Labrador, John Paul Plastina', 'Hationality', 'Sex', 'Date 0I Buth', 'Meighi (Ke)', 'Hetehtltn)', 'Phl', 'M', '2000/09/09', '103', '.81', 'Addree:', '817 L4 Pacific Hill Palo Alto Calamba', 'Laguna', 'Liccnae No.', 'Expirabon Dale', 'Aecngy Code', 'D22-18-007916', '2023/09/09', '022', 'Bcod My', 'Eues Celo', 'Adosd', '8 .', 'Brown', 'Raelnuona', 'Candition:', 'None', 'Edgar Cagalvahie', 'Siknatare 0F Licenscd', 'Nhsuay Sccretary', 'Surct']
#
# if "Philippine Identification Card" in type:
#     connection = SQLHandler("FEU")
#     active_id = "SELECT * FROM rfid_info WHERE Status = 0"
#
#     try:
#         results = [i[1] for i in connection.execute_query(active_id)]
#         random_active_id = random.choice(results)
#
#         id_type = result[3][1]
#         last_name = str(result[6][1]).title()
#         first_name = str(result[8][1]).title()
#
#         print(id_type)
#         print(last_name)
#         print(first_name)
#
#         query = f"""INSERT INTO visitors_info(RFID_NUM, FirstName, LastName, Type, Purpose, Status) VALUES
#                          ('{random_active_id}', '{first_name}', '{last_name}', '{id_type}', 'School', 'Pending')"""
#         connection.UD_query(query)
#
#         update_rfid_active = f"UPDATE rfid_info SET Status = 1 WHERE RFID_NUM = '{random_active_id}'"
#         connection.UD_query(update_rfid_active)
#     except IndexError as err:
#         print("No RFID Available")
#     finally:
#         connection.connection.close()
#
#
#
# elif "Unified Multi-Purpose Id" in type:
#     connection = SQLHandler("FEU")
#     active_id = "SELECT * FROM rfid_info WHERE Status = 0"
#     try:
#         results = [i[1] for i in connection.execute_query(active_id)]
#         random_active_id = random.choice(results)
#         id_type = type[4]
#         last_name = str(type[8]).title()
#         first_name = str(type[10]).title()
#         print(id_type)
#         print(last_name)
#         print(first_name)
#         query = f"""INSERT INTO visitors_info(RFID_NUM, FirstName, LastName, Type, Purpose, Status) VALUES
#                        ('{random_active_id}','{first_name}', '{last_name}', '{id_type}', 'School', 'Pending')"""
#         connection.UD_query(query)
#         update_rfid_active = f"UPDATE rfid_info SET Status = 1 WHERE RFID_NUM = '{random_active_id}'"
#         connection.UD_query(update_rfid_active)
#     except IndexError as err:
#         print(f"Error:{err}")
#     finally:
#         connection.connection.close()
#
#
# elif "Department Of Transportation" in type or "Land Transportation Office" in type:
#     connection = SQLHandler("FEU")
#     active_id = "SELECT * FROM rfid_info WHERE Status = 0"
#     if not str(type[3]).__contains__("Professional"):
#         try:
#             results = [i[1] for i in connection.execute_query(active_id)]
#             random_active_id = random.choice(results)
#             id_type = 'Drivers License'
#             full_name = str(type[4]).replace(";", "").replace(",", "").split(" ")
#             first_name = full_name[1]
#             last_name = full_name[0]
#             print(id_type)
#             print(last_name)
#             print(first_name)
#             query = f"""INSERT INTO visitors_info(RFID_NUM, FirstName, LastName, Type, Purpose, Status) VALUES
#                               ('{random_active_id}', '{first_name}', '{last_name}', '{id_type}', 'School', 'Pending')"""
#             connection.UD_query(query)
#             update_rfid_active = f"UPDATE rfid_info SET Status = 1 WHERE RFID_NUM = '{random_active_id}'"
#             connection.UD_query(update_rfid_active)
#
#         except IndexError as err:
#             print(f"Error:{err}")
#         finally:
#             connection.connection.close()
#
#     elif str(type[3]).__contains__("Professional"):
#         try:
#             results = [i[1] for i in connection.execute_query(active_id)]
#             random_active_id = random.choice(results)
#             id_type = "Drivers License"
#             full_name = str(type[5]).replace(";", "").replace(",", "").split(" ")
#             last_name = full_name[0]
#             first_name = full_name[1]
#             print(id_type)
#             print(last_name)
#             print(first_name)
#             query = f"""INSERT INTO visitors_info(RFID_NUM, FirstName, LastName, Type, Purpose, Status) VALUES
#                                     ('{random_active_id}','{first_name}', '{last_name}', '{id_type}', 'School', 'Pending')"""
#             connection.UD_query(query)
#             update_rfid_active = f"UPDATE rfid_info SET Status = 1 WHERE RFID_NUM = '{random_active_id}'"
#             connection.UD_query(update_rfid_active)
#         except IndexError as err:
#             print(f"Error:{err}")
#         finally:
#             connection.connection.close()



import requests

api_key = 'K87010546188957'
image_path = 'Photo/drivers2.jpg'
with open(image_path, 'rb') as image_file:
    response = requests.post(
        'https://api.ocr.space/parse/image',
        files={'file': image_file},
        data={'apikey': api_key}
    )
    result = response.json()
    text = result.get('ParsedResults', [{}])[0].get('ParsedText', '')
    print(text)
