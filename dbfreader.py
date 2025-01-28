from dbfread import DBF

table = DBF("1SCRDOC.DBF", load=True)
for record in table:
    print(record)



with open("1SCRDOC.DBF", 'r', encoding="cp1251") as f:
    b = f.readlines()