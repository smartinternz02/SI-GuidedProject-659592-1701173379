"""
Created on  SEP 21:50:15  2023

@author: MYP
"""
def showall():
    sql= "SELECT * from USERS"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The user id is : ",  dictionary["userid"])
        print("The username is : ", dictionary["username"])
        print("The email is : ",  dictionary["email"])
        print("The password is : ",  dictionary["password"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(email,password):
    sql= "select * from USERS where email='{}' and password='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The user id is : ",  dictionary["userid"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The user id is : ", dictionary["username"])
        print("The Password is : ", dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,name,email,contact,address,role,branch,password):
    sql= "INSERT into USERS VALUES('{}','{}','{}','{}')".format(userid,username,email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

try:
    import ibm_db
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=mwv02817;PWD=BGu2G7vYyF7JGCrq",'','')
    print(conn)
    print("connection successful...")
    insertdb(conn,"rider2","yaseenpasha",'admin@gmail.com','123456')
    getdetails("admin@gmail.com",'123456')
    #showall()

except:
    print("Error connecting to the database")











