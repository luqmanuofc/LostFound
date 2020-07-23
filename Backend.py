import mysql.connector
mydb = mysql.connector.connect(host= "localhost", user= 'root', passwd= 'Simaan@18', database = 'Lost')

desc = input('Enter the Description of the Lost Item:')
email = input('Enter your email:')
cate = input('Please Select Category:')
keyw = input('Please Enter the KeyWord:')

item = (desc,email,cate,keyw)

def add_lost_item(item):
    mycursor = mydb.cursor()
    sqlFormula = "INSERT INTO lost (Description, Email, Category, Keyword) VALUES (%s, %s,%s,%s)"
    mycursor.execute(sqlFormula, item)
    mydb.commit()


def find_item(item):
    
