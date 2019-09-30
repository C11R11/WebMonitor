from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def tasks_list():
    #out = subprocess.run(["top", "-n", "1"], stdout=subprocess.PIPE,  universal_newlines=True)
    out = subprocess.run('top -b -n 1 | head -n 20', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    taskOutput = "<br />".join(out.stdout.split("\n"))
    return render_template('index.html', out=taskOutput)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port="6857")
    #out = subprocess.run(["top", "-n", "1"], stdout=subprocess.PIPE,  universal_newlines=True)
    #process = subprocess.Popen('top -b -n 1 | head -n 5 >> htop.txt', shell=True)
    #taskOutput = "<br />".join(out.stdout.split("\n"))
    
