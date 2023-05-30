  
from distutils.log import debug
from flask import Flask, render_template,request
import pandas as pd
import csv
import glob
app = Flask(__name__)
@app.route('/')
def chart():
            
    path =r'C:/Users/hi/Desktop/flask graph/attend'
    filenames = glob.glob(path + "/*.csv")
    atten=0
    count=0
    #input("Enter Name To Search : ")
    data1 = []
    for filename in filenames:
        data1.append(len(pd.read_csv(filename)))
        
                        
    data ={'Task': 'Hours per Day','Lecture 1': data1[0],'Lecture 2':  data1[1],'Lecture 3': data1[2],'Lecture 4':  data1[3],'Lecture 5': data1[4],'Lecture 6':  data1[5],}
    return render_template('index1.html',data=data)
    
if __name__ == "__main__":
    app.run(debug=True,port=1000)
    
