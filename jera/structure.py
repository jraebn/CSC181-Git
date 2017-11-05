from configure import mysql


def myDbase():
    conn = mysql.connect()
    cs = conn.cursor()
    cs.execute("CREATE DATABASE IF NOT EXISTS dbase")
    cs.execute("""CREATE TABLE IF NOT EXISTS studentinfo (studentId varchar(9) NOT NULL, firstname varchar(20) NOT NULL,
    middlename varchar(20) NOT NULL, lastname varchar(20) NOT NULL, sex varchar(6) NOT NULL, course varchar(5) NOT NULL, PRIMARY KEY (studentId))""")

    cs.execute("""CREATE TABLE IF NOT EXISTS courses(
        courseId VARCHAR(4  ) NOT NULL ,
        courseDescription TEXT(200) NOT NULL,
        PRIMARY KEY (courseId))""")
    cs.close()
    conn.close()

class DB(object):
    def __init__(self, studentId, firstname, middlename, lastname, sex, course):
        self.studentId = studentId
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.sex = sex
        self.course = course

    def register(self):
        myDbase()
        conn = mysql.connect()
        cs = conn.cursor()
        cs.execute("""INSERT INTO studentinfo(studentId, firstname, middlename, lastname, sex, course) 
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""" % (self.studentId,self.firstname,self.middlename,self.lastname, self.sex,self.course))
        conn.commit()
        cs.close()
        conn.close()

def search(data):
    datas = '%'+data+'%'
    myDbase()
    conn = mysql.connect()
    cs = conn.cursor()
    cs1 = conn.cursor()
    cs2 = conn.cursor()
    cs3 = conn.cursor()
    cs4 = conn.cursor()
    cs5 = conn.cursor()
    cs.execute("SELECT * FROM studentinfo WHERE studentId = '%s'" %(data))
    res = cs.fetchall()
    cs1.execute("SELECT * FROM studentinfo WHERE firstname LIKE '%s'"%(datas))
    res1 = cs1.fetchall()
    cs2.execute("SELECT * FROM studentinfo WHERE middlename LIKE '%s'"%(datas))
    res2 = cs2.fetchall()
    cs3.execute("SELECT * FROM studentinfo WHERE lastname = '%s'" %(datas))
    res3 = cs3.fetchall()
    cs4.execute("SELECT * FROM studentinfo WHERE sex LIKE '%s'"%(datas))
    res4 = cs4.fetchall()
    cs5.execute("SELECT * FROM studentinfo WHERE course LIKE '%s'"%(datas))
    res5 = cs5.fetchall()
    return res+res1+res2+res3+res4+res5

def delete(idnumber):
    myDbase()
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM studentinfo WHERE studentId = '%s'" %(idnumber))
    conn.commit()
    cur.close()
    conn.close()

def update(copy, idnum, firstname, middlename, lastname, sex, course):
    myDbase()
    conn = mysql.connect()
    cs = conn.cursor()
    cs1 = conn.cursor()
    cs2 = conn.cursor()
    cs3 = conn.cursor()
    cs4 = conn.cursor()
    cs5 = conn.cursor()
    cs.execute("UPDATE studentinfo SET studentId= '%s' WHERE studentId= '%s'" %(idnum, copy))
    cs1.execute("UPDATE studentinfo SET firstname= '%s' WHERE studentId= '%s'" % (firstname, copy))
    cs2.execute("UPDATE studentinfo SET middlename= '%s' WHERE studentId= '%s'" % (middlename, copy))
    cs3.execute("UPDATE studentinfo SET lastname= '%s' WHERE studentId= '%s'" % (lastname, copy))
    cs4.execute("UPDATE studentinfo SET sex= '%s' WHERE studentId= '%s'" % (sex, copy))
    cs5.execute("UPDATE studentinfo SET course= '%s' WHERE studentId= '%s'" % (course, copy))
    conn.commit()
    cs.close()
    cs1.close()
    cs2.close()
    cs3.close()
    cs4.close()
    cs5.close()


def all():
    myDbase()
    conn = mysql.connect()
    cs = conn.cursor()
    cs.execute("""SELECT * FROM studentinfo JOIN courses ON studentinfo.course = courses.courseId""")
    result = cs.fetchall()
    return result


