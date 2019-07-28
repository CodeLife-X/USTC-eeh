from flask import render_template
from app import app
from app.models import List


@app.route('/')
@app.route('/index')
def index():
    dirl = List().Dir
    return render_template('index.html',
                           dir=dirl)


@app.route('/File/introduce')
def intro():
    dirl = List().Dir
    return render_template('File/logisim.html',
                           dir=dirl)


@app.route('/File/logisim')
def logisim():
    dirl = List().Dir
    return render_template('File/logisim.html',
                           dir=dirl)


@app.route('/File/verilog')
def verilog():
    dirl = List().Dir
    return render_template('File/verilog.html',
                           dir=dirl)


@app.route('/File/fpga')
def fpga():
    dirl = List().Dir
    return render_template('File/fpga.html',
                           dir=dirl)


@app.route('/File/IO')
def IO():
    dirl = List().Dir
    return render_template('File/IO.html',
                           dir=dirl)


@app.route('/File/vivado')
def vivado():
    dirl = List().Dir
    return render_template('File/verilog.html',
                           dir=dirl)


@app.route('/File/testbench')
def testbench():
    dirl = List().Dir
    return render_template('File/verilog.html',
                           dir=dirl)


@app.route('/File/basic')
def basic():
    dirl = List().Dir
    return render_template('File/basic.html',
                           dir=dirl)


@app.route('/File/SLC')
def SLC():
    dirl = List().Dir
    return render_template('File/SLC.html',
                           dir=dirl)


@app.route('/File/CLC')
def CLC():
    dirl = List().Dir
    return render_template('File/CLC.html',
                           dir=dirl)


@app.route('/File/STC')
def STC():
    dirl = List().Dir
    return render_template('File/STC.html',
                           dir=dirl)


@app.route('/File/CTC')
def CTC():
    dirl = List().Dir
    return render_template('File/CTC.html',
                           dir=dirl)


@app.route('/File/memory')
def memory():
    dirl = List().Dir
    return render_template('File/memory.html',
                           dir=dirl)


@app.route('/File/FSM')
def FSM():
    dirl = List().Dir
    return render_template('File/FSM.html',
                           dir=dirl)
















