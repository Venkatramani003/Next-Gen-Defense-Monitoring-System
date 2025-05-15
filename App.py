from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
import mysql.connector
import base64, os, sys

app = Flask(__name__)
app.secret_key = 'a'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/AdminLogin')
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route('/OfficerLogin')
def OfficerLogin():
    return render_template('OfficerLogin.html')


@app.route('/UserLogin')
def UserLogin():
    return render_template('UserLogin.html')


@app.route('/NewOfficer')
def NewOfficer():
    return render_template('NewOfficer.html')


@app.route('/NewUser')
def NewUser():
    return render_template('NewUser.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM officertb ")
            data = cur.fetchall()

            return render_template('AdminHome.html', data=data)

        else:
            flash('Username or Password is wrong')
            return render_template('AdminLogin.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM officertb ")
    data = cur.fetchall()

    return render_template('AdminHome.html', data=data)


@app.route("/AUserInfo")
def AUserInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()
    return render_template('AUserInfo.html', data=data)


@app.route('/SFileInfo')
def SFileInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb ")
    data1 = cur.fetchall()
    return render_template('SFileInfo.html', data=data1)


@app.route('/AActivityInfo')
def AActivityInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM activitytb ORDER BY id ")
    data1 = cur.fetchall()
    return render_template('AActivityInfo.html', data=data1)


@app.route("/newofficer", methods=['GET', 'POST'])
def newofficer():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from officertb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO officertb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "')")
            conn.commit()
            conn.close()

            flash('Record Saved!')
            return render_template('NewOfficer.html')
        else:
            flash('Already Register This  Officer Name!')
            return render_template('NewOwner.html')


@app.route("/officerlogin", methods=['GET', 'POST'])
def officerlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        session['oname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from officertb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('OfficerLogin.html')

        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                           database='1smartdefensedb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM officertb where username='" + session['oname'] + "'")
            data1 = cur.fetchall()
            return render_template('OfficerHome.html', data=data1)


@app.route('/OfficerHome')
def OfficerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM officertb where username='" + session['oname'] + "'")
    data1 = cur.fetchall()
    return render_template('OfficerHome.html', data=data1)


@app.route('/OUserInfo')
def OUserInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status !='waiting'")
    data1 = cur.fetchall()
    return render_template('OUserInfo.html', data=data, data1=data1)


@app.route("/Approved")
def Approved():
    id = request.args.get('lid')
    email = request.args.get('email')
    mob  = request.args.get('mob')
    import random
    loginkey = random.randint(1111, 9999)
    message = "Your Defense  Login Key :" + str(loginkey)



    sendmail(email, message)
    sendmsg(mob,message)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cursor = conn.cursor()
    cursor.execute("Update regtb set Status='Active',LoginKey='" + str(loginkey) + "' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status !='waiting'")
    data1 = cur.fetchall()

    return render_template('OUserInfo.html', data=data, data1=data1)


@app.route("/Reject")
def Reject():
    id = request.args.get('lid')
    email = request.args.get('email')

    message = "Your Request  Rejected"

    sendmail(email, message)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cursor = conn.cursor()
    cursor.execute("Update regtb set Status='reject' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status !='waiting'")
    data1 = cur.fetchall()

    return render_template('OUserInfo.html', data=data, data1=data1)


@app.route('/OActivityInfo')
def OActivityInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM activitytb ORDER BY id ")
    data1 = cur.fetchall()
    return render_template('OActivityInfo.html', data=data1)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']

        outFileName = 'static/user/' + username + '.jpg'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO regtb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" +
                username + "','" + password + "','waiting','','" + outFileName + "')")
            conn.commit()
            conn.close()

            flash('Record Saved!')
            import LiveRecognition as liv
            liv.att()

            del sys.modules["LiveRecognition"]

            return render_template('NewUser.html')
        else:
            flash('Already Register This  UserName!')
            return render_template('NewUser.html')


import hmac
import hashlib
import binascii


def create_sha256_signature(key, message):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()


def blockchainstor(username, activity):
    import random
    import datetime
    import time
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM activitytb ")
    data2 = cursor.fetchone()

    if data2:

        conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
        cursor1 = conn1.cursor()
        cursor1.execute("select max(id) from activitytb")
        da = cursor1.fetchone()
        if da:
            d = da[0]
            print(d)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM activitytb where  id ='" + str(d) + "'   ")
        data1 = cursor.fetchone()
        if data1:
            hash1 = data1[6]
            num1 = random.randrange(1111, 9999)
            hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))

            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                           database='1smartdefensedb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO activitytb VALUES ('','" + username + "','" + str(date) + "','" + str(
                    timeStamp) + "','" + activity + "','" +
                hash1 + "','" + hash2 + "')")
            conn.commit()
            conn.close()


    else:

        hash1 = '0'
        num1 = random.randrange(1111, 9999)
        hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO activitytb VALUES ('','" + username + "','" + str(date) + "','" + str(
                timeStamp) + "','" + activity + "','" +
            hash1 + "','" + hash2 + "')")
        conn.commit()
        conn.close()


@app.route("/Download")
def Download():
    fid = request.args.get('lid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:

        fname = data[3]

    else:
        return 'Incorrect username / password !'

    filepath = "./static/upload/" + fname

    return send_file(filepath, as_attachment=True)


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        loginkey = request.form['loginkey']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')

        else:

            Status = data[7]
            lkey = data[8]
            session['lkey'] = data[8]

            if Status == "waiting":

                flash('Waiting For Server Approved!')
                return render_template('UserLogin.html')

            else:

                if lkey == loginkey:

                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='1smartdefensedb')
                    cursor = conn.cursor()
                    cursor.execute("truncate table temptb ")
                    conn.commit()
                    conn.close()

                    import LiveRecognition1
                    #del sys.modules["LiveRecognition1"]
                    return facelogin()
                    #return render_template('UserHome.html')





                else:
                    flash('Login Key Incorrect')
                    return render_template('UserLogin.html')


def loginvales1():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM regtb where username='" + uname + "'")
    data = cursor.fetchone()

    if data:
        Email = data[3]
        Phone = data[2]


    else:
        return 'Incorrect username / password !'

    return uname, Email, Phone


@app.route("/facelogin")
def facelogin():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cursor = conn.cursor()
    cursor.execute("SELECT * from temptb where username='" + uname + "' ")
    data = cursor.fetchone()
    if data is None:

        flash('Face Wrong..!')
        return render_template('UserLogin.html')


    else:

        blockchainstor(session['uname'], "Login")

        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='1smartdefensedb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM regtb where username='" + session['uname'] + "'")
        data1 = cur.fetchall()
        flash('Login Successfully')
        return render_template('UserHome.html', data=data1)


@app.route('/UserHome')
def UserHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM UserHome where OwnerName='" + session['uname'] + "'")
    data1 = cur.fetchall()
    return render_template('UserHome.html', data=data1)


@app.route('/UploadFile')
def UploadFile():
    oname = session['uname']
    return render_template('UploadFile.html', uname=oname)


@app.route("/owfileupload", methods=['GET', 'POST'])
def owfileupload():
    if request.method == 'POST':
        oname = session['uname']
        info = request.form['info']
        file = request.files['file']
        import random
        fnew = random.randint(111, 999)
        savename = str(fnew) + file.filename
        file.save("static/upload/" + savename)
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='1smartdefensedb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO filetb VALUES ('','" + oname + "','" + info + "','" + savename + "','" + oname + "')")
        conn.commit()
        conn.close()
        flash('File Upload Successfully ')
        blockchainstor(session['uname'], "File Upload FileName:" + savename)
        return render_template('UploadFile.html', oname=oname)


@app.route('/ShareFile')
def ShareFile():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where UserName='" + session['uname'] + "'")
    data1 = cur.fetchall()
    return render_template('ShareFile.html', data=data1)


@app.route("/sharef")
def sharef():
    lid = request.args.get('lid')
    session['fid'] = lid

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT UserName   FROM regtb ")
    data1 = cur.fetchall()
    return render_template('share.html',data=data1)


@app.route("/fshares", methods=['GET', 'POST'])
def fshares():
    if request.method == 'POST':
        oname = session['uname']

        suname = request.form['suname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM  filetb where id='" + session['fid'] + "'")
        data = cursor.fetchone()

        if data:
            info = data[3]
            ffile = data[3]

        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='1smartdefensedb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO filetb VALUES ('','" + oname + "','" + info + "','" + ffile + "','" + suname + "')")
        conn.commit()
        conn.close()
        flash('File Share Successfully ')
        blockchainstor(session['uname'], "File Share to" + suname + "FileName:" + ffile)
        return ShareFile()


@app.route("/FileInfo")
def FileInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where UserName='" + uname + "'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1smartdefensedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where shareName='" + uname + "'")
    data1 = cur.fetchall()

    return render_template('UFileInfo.html', data=data, data1=data1)




@app.route('/ULogout')
def ULogout():
    blockchainstor(session['uname'], 'Logout')
    return render_template('index.html')


def sendmail(Mailid, message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "projectmailm@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "qmgn xecl bkqv musr")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


def sendmsg(targetno,message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True, port=5000)
    app.run(debug=True, use_reloader=True)
