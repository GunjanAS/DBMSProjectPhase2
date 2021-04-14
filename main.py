from flask import Flask
import mariadb
import sys
from flask import flash, render_template, request, redirect
import templates


app = Flask(__name__)
app.secret_key = "secret key"

conn = mariadb.connect(
    user="root",
    password="", #netidpassword
    host="172.16.122.9",
    database="PROJECTDB")

cur = conn.cursor()
tablename=[]
columnnames=[]
@app.route('/')
def main_page():
	return render_template('main.html')

@app.route('/operation',methods=['POST'])
def operations_db():
    if (request.form['submit_button'] == 'Insert'   ):
        return render_template('showTables.html')
    if (request.form['submit_button'] == 'Delete'):
        return render_template('showTablesForDelete.html')

@app.route('/add', methods=['POST'])
def showingColumnNamesForInsertion():
    
    cur.execute("SELECT `COLUMN_NAME`  FROM `INFORMATION_SCHEMA`.`COLUMNS`  WHERE `TABLE_SCHEMA`='PROJECTDB' AND `TABLE_NAME`= '{0}';".format(request.form['submit_button']))
    tablename.append(request.form['submit_button'])
    print(tablename)
    list=[]
    for (COLUMN_NAME) in cur:
        list.append(COLUMN_NAME[0])
    for i in list:
        columnnames.append(i)
    return render_template('tablecolumns.html',value=list )

@app.route('/delete', methods=['POST'])
def showingColumnNameForDeleting():
    cur.execute("SELECT `COLUMN_NAME`  FROM `INFORMATION_SCHEMA`.`COLUMNS`  WHERE `TABLE_SCHEMA`='PROJECTDB' AND `TABLE_NAME`= '{0}';".format(request.form['submit_button']))
    tablename.append(request.form['submit_button'])
    list=[]
    for (COLUMN_NAME) in cur:
        list.append(COLUMN_NAME[0])
        break
    return render_template('tablecolumnsForDeleting.html',value=list )

@app.route('/insert', methods=['POST'])
def inserting():
    if (request.form['submit_button'] == 'INSERT'):
        result = request.form.getlist('inputtext')
        print(tablename)
        if (tablename[0]== 'COLLEGE'):
            try:
                cur.execute("INSERT INTO COLLEGE (CName,COffice, CPhone,DeanId ) VALUES (? , ?, ? ,? );",(result[0], result[1], result[2], result[3]))
                conn.commit()
                sucess()
                return redirect('/')
            except:
                failure()
                return redirect('/')
        if (tablename[0]== 'COURSE'):
            try:
                cur.execute("INSERT INTO COURSE ( CCode,Credits, CoName,Level,CDesc,DeptOffering ) VALUES (? , ?, ? ,?,?,? );",(result[0], result[1], result[2], result[3], result[4], result[5]))
                conn.commit()
                sucess()
                return redirect('/')
            except:
                failure()
                return redirect('/')
        if (tablename[0]== 'DEPARTMENT'):
            try:
                cur.execute("INSERT INTO DEPARTMENT ( DName,DCode , DOffice ,DPhone ,ChairId ,CStartDate , CollegeAdm  ) VALUES (? , ?, ? ,?,?,?,? );",(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
                conn.commit()
                sucess()
                return redirect('/')
            except:
                failure()
                return redirect('/')
        if (tablename[0]== 'INSTRUCTOR'):
            try:
                cur.execute("INSERT INTO INSTRUCTOR ( Id,Rank  , IName  ,IOffice  ,IPhone  ,DeptEmp  ) VALUES (? , ?, ? ,?,?,? );",(result[0], result[1], result[2], result[3], result[4], result[5]))
                conn.commit()
                sucess()
                return redirect('/')
            except:
                failure()
                return redirect('/')
        if (tablename[0]== 'SECTION'):
            try:
                cur.execute("INSERT INTO SECTION ( SecId,SecNo  , Sem  ,Year  ,Bldg  ,RoomNo  , DaysTime ,SecInstr ,ParentCourse   ) VALUES (? , ?, ? ,?,?,?,? );",(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))
                conn.commit()
                sucess()
                return redirect('/')
            except:
                failure()
                return redirect('/')
        if (tablename[0]== 'STUDENT'):
            try:
                cur.execute("INSERT INTO STUDENT ( SId,DOB  , FName  ,MName  ,LName  ,Addr  , Phone ,Major ,DeptName   ) VALUES (? , ?, ? ,?,?,?,? );",(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))
                conn.commit()
                sucess()
                return redirect('/')
            except:
                failure()
                return redirect('/')
        if (tablename[0]== 'TAKES'):
            try:
                cur.execute("INSERT INTO TAKES (SId,SecId , Grade ) VALUES (? , ?, ? );",(result[0], result[1], result[2]))
                conn.commit()
                sucess()
                return redirect('/')
            except:
                failure()
                return redirect('/')

@app.route('/deleting', methods=['POST'])
def deleting():
    if (request.form['submit_button'] == 'DELETE'):
        result = request.form.get('inputtext')
        if (tablename[0]== 'COLLEGE'):
            try:
                cur.execute("DELETE FROM COLLEGE WHERE CName= '{}';".format(result))
                conn.commit()
                sucess_deleting()
                return redirect('/')
            except:
                failure_deleting()
                return redirect('/')

        if( tablename[0]== 'COURSE'):
            try:
                cur.execute("DELETE FROM COURSE WHERE CCode= {};".format(result))
                conn.commit()
                sucess_deleting()
                return redirect('/')
            except:
                failure_deleting()
                return redirect('/')
        if( tablename[0]== 'DEPARTMENT'):
            try:
                cur.execute("DELETE FROM DEPARTMENT WHERE DName= '{}';".format(result))
                conn.commit()
                sucess_deleting()
                return redirect('/')
            except:
                failure_deleting()
                return redirect('/')
        if( tablename[0]== 'INSTRUCTOR'):
            try:
                cur.execute("DELETE FROM INSTRUCTOR WHERE Id= {};".format(result))
                conn.commit()
                sucess_deleting()
                return redirect('/')
            except:
                failure_deleting()
                return redirect('/')
        if( tablename[0]== 'SECTION'):
            try:
                cur.execute("DELETE FROM SECTION WHERE SecId= {};".format(result))
                conn.commit()
                sucess_deleting()
                return redirect('/')
            except:
                failure_deleting()
                return redirect('/')
        if( tablename[0]== 'STUDENT'):
            try:
                cur.execute("DELETE FROM STUDENT WHERE SId= {};".format(result))
                conn.commit()
                sucess_deleting()
                return redirect('/')
            except:
                failure_deleting()
                return redirect('/')
        if( tablename[0]== 'TAKES'):
            try:
                cur.execute("DELETE FROM TAKES WHERE SId= {};".format(result))
                conn.commit()
                sucess_deleting()
                return redirect('/')
            except:
                failure_deleting()
                return redirect('/')
        

def sucess():
    tablename.clear()
    columnnames.clear()
    flash('Insertion done successfully!!')
    

def failure():
    tablename.clear()
    columnnames.clear()
    flash('Error in inserting!!')

def sucess_deleting():
    tablename.clear()
    columnnames.clear()
    flash('Deletion done successfully!!')

def failure_deleting():
    tablename.clear()
    columnnames.clear()
    flash('Error in deleting!!')
    



        


            


if __name__ == "__main__":
    app.run()
