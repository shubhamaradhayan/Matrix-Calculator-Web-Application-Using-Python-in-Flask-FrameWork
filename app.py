# from urllib import request
from flask import Flask,render_template,redirect,request
import numpy as np


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# for two matrix multiplication

@app.route("/multiplication")
def multiplication():
    return render_template("twomatrixrowcol.html", act='table-multiplication', m1='readonly', o='Multiplication') 

@app.route("/table-multiplication", methods=['GET', 'POST'])
def multiplication_table():
    if request.method=='POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        r2=int(request.form['c1'])
        c2=int(request.form['c2'])


        return render_template("twomatrix.html", act='cal-multiplication', r1=r1, c1=c1, r2=r2, c2=c2, o='Multiplication' ) 

@app.route("/cal-multiplication",methods=['GET', 'POST'])
def cal_multiplication():
    a=[]
    b=[]
    r=[]
    if request.method == 'POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        r2=int(request.form['c1'])
        c2=int(request.form['c2'])

        for i in range(r1):
            a.append([])
        for i in range(r1):
            for j in range(c1):
                a[i].append(0)    
        for i in range(r2):
            b.append([])
        for i in range(r2):
            for j in range(c2):
                b[i].append(0)    
        for i in range(r1):
            r.append([])
        for i in range(r1):
            for j in range(c2):
                r[i].append(0) 

        for i in range(r1):
            for j in range(c1):
                a[i][j] += int(request.form[f'A[{i}][{j}]'])           
        for i in range(r2):
            for j in range(c2):
                b[i][j] += int(request.form[f'B[{i}][{j}]'])           
        for i in range(r1):
            for j in range(c1):
                for k in range(c2):
                    r[i][k] += a[i][j]*b[j][k]            

        return render_template("result.html",a=a,b=b, r=r, o='Multiplication' ) 

# add of two mtrx 

@app.route("/summation")
def summation():
    return render_template("twomatrixrowcol.html", act='table-summation', m1='readonly',m2='readonly',o='addition') 

@app.route("/table-summation", methods=['GET', 'POST'])
def summation_table():
    if request.method=='POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        r2=int(request.form['r1'])
        c2=int(request.form['c1'])


        return render_template("twomatrix.html", act='cal-summation', r1=r1, c1=c1, r2=r2, c2=c2,o='addition' ) 

@app.route("/cal-summation",methods=['GET', 'POST'])
def cal_summation():
    a=[]
    b=[]
    r=[]
    if request.method == 'POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        r2=int(request.form['r1'])
        c2=int(request.form['c1'])

        for i in range(r1):
            a.append([])
        for i in range(r1):
            for j in range(c1):
                a[i].append(0)    
        for i in range(r2):
            b.append([])
        for i in range(r2):
            for j in range(c2):
                b[i].append(0)    
        for i in range(r1):
            r.append([])
        for i in range(r1):
            for j in range(c2):
                r[i].append(0) 

        for i in range(r1):
            for j in range(c1):
                a[i][j] += int(request.form[f'A[{i}][{j}]'])           
        for i in range(r1):
            for j in range(c1):
                b[i][j] += int(request.form[f'B[{i}][{j}]'])           
        for i in range(r1):
            for j in range(c1):    
                r[i][j] += a[i][j]+b[i][j]            

        return render_template("result.html", a=a,b=b,r=r,o='addition' ) 


# sub of two mtrx 

@app.route("/substraction")
def substraction():
    return render_template("twomatrixrowcol.html", act='table-substraction', m1='readonly',m2='readonly', o='substration' ) 

@app.route("/table-substraction", methods=['GET', 'POST'])
def substraction_table():
    if request.method=='POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        r2=int(request.form['r1'])
        c2=int(request.form['c1'])


        return render_template("twomatrix.html", act='cal-substraction', r1=r1, c1=c1, r2=r2, c2=c2, o='substration'  ) 

@app.route("/cal-substraction",methods=['GET', 'POST'])
def cal_substraction():
    a=[]
    b=[]
    r=[]
    if request.method == 'POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        r2=int(request.form['r1'])
        c2=int(request.form['c1'])

        for i in range(r1):
            a.append([])
        for i in range(r1):
            for j in range(c1):
                a[i].append(0)    
        for i in range(r2):
            b.append([])
        for i in range(r2):
            for j in range(c2):
                b[i].append(0)    
        for i in range(r1):
            r.append([])
        for i in range(r1):
            for j in range(c2):
                r[i].append(0) 

        for i in range(r1):
            for j in range(c1):
                a[i][j] += int(request.form[f'A[{i}][{j}]'])           
        for i in range(r1):
            for j in range(c1):
                b[i][j] += int(request.form[f'B[{i}][{j}]'])           
        for i in range(r1):
            for j in range(c1):    
                r[i][j] += a[i][j]-b[i][j]            

        return render_template("result.html",a=a,b=b, r=r, o='substration' ) 



# sclar multiplication of  mtrx 

@app.route("/scalarmultiplication")
def scalarmultiplication():
    return render_template("matrixrowcol.html", act='table-scalar-multiplication', o='Scalar Multiplication') 

@app.route("/table-scalar-multiplication", methods=['GET', 'POST'])
def table_scalar_multiplication():
    if request.method=='POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        


        return render_template("scalarmatrix.html", act='cal-scalar-multiplication', r1=r1, c1=c1, o='Scalar Multiplication' ) 

@app.route("/cal-scalar-multiplication",methods=['GET', 'POST'])
def cal_scalar_multiplication():
    a=[]
    r=[]
    if request.method == 'POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        n=int(request.form['n'])
        
      

        for i in range(r1):
            a.append([])
        for i in range(r1):
            for j in range(c1):
                a[i].append(0)    
            
        for i in range(r1):
            r.append([])
        for i in range(r1):
            for j in range(c1):
                r[i].append(0) 

        for i in range(r1):
            for j in range(c1):
                a[i][j] += int(request.form[f'A[{i}][{j}]'])           
        for i in range(r1):
            for j in range(c1):    
                r[i][j] += a[i][j]*n            

        return render_template("result.html",b=a, r=r, n=n, o='Scalar Multiplication' ) 




# sclar addition of  mtrx 

@app.route("/scalarsum")
def scalarsum():
    return render_template("matrixrowcol.html", act='table-scalarsum', o='Scalar Summation') 

@app.route("/table-scalarsum", methods=['GET', 'POST'])
def table_scalarsum():
    if request.method=='POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        


        return render_template("scalarmatrix.html", act='cal-scalar-sum', r1=r1, c1=c1, o='Scalar Summation' ) 

@app.route("/cal-scalar-sum",methods=['GET', 'POST'])
def cal_scalar_sum():
    a=[]
    r=[]
    if request.method == 'POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        n=int(request.form['n'])
        
      

        for i in range(r1):
            a.append([])
        for i in range(r1):
            for j in range(c1):
                a[i].append(0)    
            
        for i in range(r1):
            r.append([])
        for i in range(r1):
            for j in range(c1):
                r[i].append(0) 

        for i in range(r1):
            for j in range(c1):
                a[i][j] += int(request.form[f'A[{i}][{j}]'])           
        for i in range(r1):
            for j in range(c1):    
                r[i][j] += a[i][j]+n            

        return render_template("result.html",b=a, r=r, n=n, o='Scalar Summation' ) 




# sclar subs of  mtrx 

@app.route("/scalarsubstraction")
def scalarsubstraction():
    return render_template("matrixrowcol.html", act='table-scalar-sub', o='Scalar Substraction') 

@app.route("/table-scalar-sub", methods=['GET', 'POST'])
def table_scalar_sub():
    if request.method=='POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        


        return render_template("scalarmatrix.html", act='cal-scalar-sub', r1=r1, c1=c1, o='Scalar Substraction' ) 

@app.route("/cal-scalar-sub",methods=['GET', 'POST'])
def cal_scalar_sub():
    a=[]
    r=[]
    if request.method == 'POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        n=int(request.form['n'])
        
      

        for i in range(r1):
            a.append([])
        for i in range(r1):
            for j in range(c1):
                a[i].append(0)    
            
        for i in range(r1):
            r.append([])
        for i in range(r1):
            for j in range(c1):
                r[i].append(0) 

        for i in range(r1):
            for j in range(c1):
                a[i][j] += int(request.form[f'A[{i}][{j}]'])           
        for i in range(r1):
            for j in range(c1):    
                r[i][j] += a[i][j]-n            

        return render_template("result.html",b=a, r=r, n=n, o='Scalar Substraction' ) 




# n Power of  mtrx 

@app.route("/power")
def power():
    return render_template("matrixrowcol.html", act='table-n-power', o='n Power Of Matrix') 

@app.route("/table-n-power", methods=['GET', 'POST'])
def table_n_power():
    if request.method=='POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        


        return render_template("scalarmatrix.html", act='cal-n-power', r1=r1, c1=c1, o='n Power Of Matrix' ) 

def mtrx_mlt(a,b):
    m=len(a)
    n=len(a[0])
    p=len(b)
    q=len(b[0])
    l=[]
    for i in range(m):
        l.append([])
    for i in range(m):
        for j in range(n):
            l[i].append(0)
    for i in range(m):
        for j in range(n):
            for k in range(q):
                l[i][k] += a[i][j]*b[j][k]
    return l                        


@app.route("/cal-n-power",methods=['GET', 'POST'])
def cal_n_power():
    a=[]
    r=[]
    if request.method == 'POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        n=int(request.form['n'])
        
      

        for i in range(r1):
            a.append([])
        for i in range(r1):
            for j in range(c1):
                a[i].append(0)    
      

        

        for i in range(r1):
            for j in range(c1):
                a[i][j] += int(request.form[f'A[{i}][{j}]']) 

        r=a

        for i in range(n-1):
            r = mtrx_mlt(r,a)                  
       

        return render_template("result.html",b=a, r=r, n=n, o='n Power Of Matrix' ) 





# det of  mtrx 

@app.route("/determinant")
def det():
    return render_template("matrixrowcol.html", act='table-det', o='Determinant Of Matrix') 

@app.route("/table-det", methods=['GET', 'POST'])
def table_det():
    if request.method=='POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        


        return render_template("matrix.html", act='cal-det', r1=r1, c1=c1,o='Determinant Of Matrix' ) 


@app.route("/cal-det",methods=['GET', 'POST'])
def cal_det():
    a=[]
    # r=[]
    if request.method == 'POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        
        
      

        for i in range(r1):
            a.append([])
        for i in range(r1):
            for j in range(c1):
                a[i].append(0)    
        

        for i in range(r1):
            for j in range(c1):
                a[i][j] += int(request.form[f'A[{i}][{j}]']) 

        det = np.linalg.det(a)
        r=round(det)                  
       

        return render_template("result.html",a=a, t=r, o='Determinant Of Matrix' ) 





# transpose of  mtrx 

@app.route("/transpose")
def transpose():
    return render_template("matrixrowcol.html", act='table-transpose') 

@app.route("/table-transpose", methods=['GET', 'POST'])
def table_transpose():
    if request.method=='POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        


        return render_template("matrix.html", act='cal-transpose', r1=r1, c1=c1 ) 


@app.route("/cal-transpose",methods=['GET', 'POST'])
def cal_transpose():
    a=[]
    r=[]
    if request.method == 'POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        n=int(request.form['n'])
        
      

        for i in range(r1):
            a.append([])
        for i in range(r1):
            for j in range(c1):
                a[i].append(0) 

        for i in range(r1):
            r.append([])
        for i in range(r1):
            for j in range(c1):
                r[i].append(0)    
      

        

        for i in range(r1):
            for j in range(c1):
                a[i][j] += int(request.form[f'A[{i}][{j}]']) 

        

        for i in range(r1):
            for j in range(c1):
                r[j][i] = a[i][j]                  
       

        return render_template("result.html",b=a, r=r, n=n, o='Transpose Of Matrix' ) 





# inverse of  mtrx 

@app.route("/inverse")
def inverse():
    return render_template("matrixrowcol.html", act='table-inverse') 

@app.route("/table-inverse", methods=['GET', 'POST'])
def table_inverse():
    if request.method=='POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        


        return render_template("matrix.html", act='cal-inverse', r1=r1, c1=c1 ) 



@app.route("/cal-inverse",methods=['GET', 'POST'])
def cal_inverse():
    a=[]
    r=[]
    if request.method == 'POST':
        r1=int(request.form['r1'])
        c1=int(request.form['c1'])
        n=int(request.form['n'])
        
      

        for i in range(r1):
            a.append([])
        for i in range(r1):
            for j in range(c1):
                a[i].append(0)    
           

        for i in range(r1):
            for j in range(c1):
                a[i][j] += int(request.form[f'A[{i}][{j}]']) 

        r=np.linalg.inv(a)

        return render_template("result.html",b=a, r=r, n=n, o='Inverse Of Matrix' ) 











app.run(debug=True)    
    
 