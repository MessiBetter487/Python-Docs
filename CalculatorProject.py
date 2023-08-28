from typing import Optional
from PySide6.QtGui import QPainter,QPixmap
from PySide6.QtWidgets import QPushButton,QHBoxLayout,QVBoxLayout,QWidget,QLabel,QLineEdit,QSizePolicy,QTextEdit,QTabWidget,QListWidget
from math import sin,cos,tan,pi,sqrt,tanh,cosh,sinh,asin,acos,atan,acosh,atanh,asinh,exp,degrees
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Calculator")
        self.setMaximumHeight(475)
        self.setMaximumWidth(325)
        self.setMinimumHeight(375)
        self.setMinimumWidth(225)
        self.background_image = QPixmap("galaxy-portrait-display-space-vertical-wallpaper-preview.jpg1") 
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background_image)
        Tabwidget=QTabWidget()
        calculatorwidget=QWidget()
        self.output=QLineEdit()
        self.output.returnPressed.connect(self.equalo)
    
        cost=QPushButton('cos(θ)')
        cost.clicked.connect(self.costo)
        tant=QPushButton('tan(θ)')
        tant.clicked.connect(self.tanto)  
        sint=QPushButton('sin(θ)')
        sint.clicked.connect(self.sinto)
        cost=QPushButton('cos(θ)')
        cost.clicked.connect(self.costo)
        tant=QPushButton('tan(θ)')
        tant.clicked.connect(self.tanto)  
        sin=QPushButton('sin(')
        sin.clicked.connect(self.sino)
        cos=QPushButton('cos(')
        cos.clicked.connect(self.coso)
        tan=QPushButton('tan(')
        tan.clicked.connect(self.tano)
        cosec=QPushButton('cosec')
        cosec.clicked.connect(self.coseco)
        sec=QPushButton('sec')
        sec.clicked.connect(self.seco)
        cot=QPushButton('cot')
        cot.clicked.connect(self.coto)
        clear=QPushButton('CE')
        clear.clicked.connect(self.clearo)
        b1=QPushButton('(')
        b1.clicked.connect(self.b1)
        b2=QPushButton(')')
        b2.clicked.connect(self.b2)
        one=QPushButton('1')
        one.clicked.connect(self.iferror)
        one.clicked.connect(self.oneo)
        two=QPushButton('2')
        two.clicked.connect(self.iferror)
        two.clicked.connect(self.twoo)
        three=QPushButton('3')
        three.clicked.connect(self.iferror)
        three.clicked.connect(self.threeo)
        four=QPushButton('4')
        four.clicked.connect(self.iferror)
        four.clicked.connect(self.fouro)
        five=QPushButton('5')
        five.clicked.connect(self.iferror)
        five.clicked.connect(self.fiveo)
        six=QPushButton('6')
        six.clicked.connect(self.iferror)
        six.clicked.connect(self.sixo)
        seven=QPushButton('7')
        seven.clicked.connect(self.iferror)
        seven.clicked.connect(self.seveno)
        eight=QPushButton('8')
        eight.clicked.connect(self.iferror)
        eight.clicked.connect(self.eighto)
        nine=QPushButton('9')
        nine.clicked.connect(self.iferror)
        nine.clicked.connect(self.nineo)
        zero=QPushButton('0')
        zero.clicked.connect(self.iferror)
        zero.clicked.connect(self.zeroo)
        point=QPushButton('.')
        point.clicked.connect(self.pointo)
        times=QPushButton('⨉')
        times.clicked.connect(self.timeso)
        divide=QPushButton('÷')
        divide.clicked.connect(self.divideo)
        divide.setCheckable(True)
        add=QPushButton('+')
        add.clicked.connect(self.addo)
        minus=QPushButton('-')
        minus.clicked.connect(self.minuso)
        equal=QPushButton('=')
        equal.clicked.connect(self.equalo)
        h1layout=QHBoxLayout()
        h1layout.addWidget(self.output)
        hlayout=QHBoxLayout()
        hlayout.addWidget(seven)
        hlayout.addWidget(eight)
        hlayout.addWidget(nine)
        hlayout.addWidget(add)
        h2layout=QHBoxLayout()
        h2layout.addWidget(four)
        h2layout.addWidget(five)
        h2layout.addWidget(six)
        h2layout.addWidget(minus)
        h3layout=QHBoxLayout()
        h3layout.addWidget(one)
        h3layout.addWidget(two)
        h3layout.addWidget(three)
        h3layout.addWidget(times)
        h4layout=QHBoxLayout()
        h4layout.addWidget(zero)
        h4layout.addWidget(point)
        h4layout.addWidget(equal)
        h4layout.addWidget(divide)
        h5layout=QHBoxLayout()
        h5layout.addWidget(clear,2)
        h5layout.addWidget(b1,0.75)
        h5layout.addWidget(b2,0.75)
        h6layout=QHBoxLayout()
        h6layout.addWidget(sin)
        h6layout.addWidget(cos)
        h6layout.addWidget(tan)
        h8layout=QHBoxLayout()
        h8layout.addWidget(cosec)
        h8layout.addWidget(sec)
        h8layout.addWidget(cot)
        h9layout=QHBoxLayout()
        h9layout.addWidget(sint)
        h9layout.addWidget(cost)
        h9layout.addWidget(tant)
        h7layout=QHBoxLayout()

        vlayout=QVBoxLayout()
        vlayout.addLayout(h1layout)
        vlayout.addLayout(h7layout)
        vlayout.addLayout(h5layout)
        vlayout.addLayout(hlayout)
        vlayout.addLayout(h2layout)
        vlayout.addLayout(h3layout)
        vlayout.addLayout(h4layout)
        vlayout.addLayout(h6layout)
        vlayout.addLayout(h9layout)
        vlayout.addLayout(h8layout)
        calculatorwidget.setLayout(vlayout)
        
        mmry=QWidget()
        self.memory=QListWidget()
        self.memory.currentItemChanged.connect(self.memoryitem)
      
        ml1=QVBoxLayout()
        ml1.addWidget(self.memory)
        mmry.setLayout(ml1)
        
        nts=QWidget()
        textedit=QTextEdit()
        lay=QVBoxLayout()
        lay.addWidget(textedit)
        nts.setLayout(lay)
        Tabwidget.addTab(calculatorwidget,'Calculator')
        Tabwidget.addTab(mmry,'History')
        Tabwidget.addTab(nts,'Notes')
    
        ML=QVBoxLayout()
        ML.addWidget(Tabwidget)
        self.setLayout(ML)
    
    def oneo(self):
        self.output.setText(self.output.text()+'1')
    def twoo(self):
        self.output.setText(self.output.text()+'2')
    def threeo(self):
        self.output.setText(self.output.text()+'3')
    def fouro(self):
        self.output.setText(self.output.text()+'4')
    def fiveo(self):
        self.output.setText(self.output.text()+'5')
    def sixo(self):
        self.output.setText(self.output.text()+'6')
    def seveno(self):
        self.output.setText(self.output.text()+'7')
    def eighto(self):
        self.output.setText(self.output.text()+'8')
    def nineo(self):
        self.output.setText(self.output.text()+'9')
    def zeroo(self):
        self.output.setText(self.output.text()+'0')
    def pointo(self):
        self.output.setText(self.output.text()+'.')
    def addo(self):
        self.output.setText(self.output.text()+'+')
    def minuso(self):
        self.output.setText(self.output.text()+'-')
    def timeso(self):
        self.output.setText(self.output.text()+'*')
    def divideo(self):
        self.output.setText(self.output.text()+'/')
    def sino(self):
        self.output.setText(self.output.text()+'sin(')
    def tano(self):
        self.output.setText(self.output.text()+'tan(')
    def coso(self):
        self.output.setText(self.output.text()+'cos(')
    def coseco(self):
        if self.output.text().rfind('+') > self.output.text().rfind('-') and self.output.text().rfind('+') > self.output.text().rfind('*') and self.output.text().rfind('+') > self.output.text().rfind('/'):
            x=self.output.text()
            c='+'
            ns=x[x.rfind(c)+1::]
            ans=1/(sin(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('-') > self.output.text().rfind('+') and self.output.text().rfind('-') > self.output.text().rfind('*') and self.output.text().rfind('-') > self.output.text().rfind('/'):
            x=self.output.text()
            c='-'
            ns=x[x.rfind(c)+1::]
            ans=1/(sin(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('*') > self.output.text().rfind('-') and self.output.text().rfind('*') > self.output.text().rfind('+') and self.output.text().rfind('*') > self.output.text().rfind('/'):
            x=self.output.text()
            c='*'
            ns=x[x.rfind(c)+1::]
            ans=1/(sin(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('/') > self.output.text().rfind('-') and self.output.text().rfind('/') > self.output.text().rfind('*') and self.output.text().rfind('/') > self.output.text().rfind('+'):
            x=self.output.text()
            c='/'
            ns=x[x.rfind(c)+1::]
            ans=1/(sin(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        else:
            x=float(self.output.text())
            ans=1/(sin(x))
            self.output.setText(str(ans))
    def coto(self):
        if self.output.text().rfind('+') > self.output.text().rfind('-') and self.output.text().rfind('+') > self.output.text().rfind('*') and self.output.text().rfind('+') > self.output.text().rfind('/'):
            x=self.output.text()
            c='+'
            ns=x[x.rfind(c)+1::]
            ans=1/(tan(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('-') > self.output.text().rfind('+') and self.output.text().rfind('-') > self.output.text().rfind('*') and self.output.text().rfind('-') > self.output.text().rfind('/'):
            x=self.output.text()
            c='-'
            ns=x[x.rfind(c)+1::]
            ans=1/(tan(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('*') > self.output.text().rfind('-') and self.output.text().rfind('*') > self.output.text().rfind('+') and self.output.text().rfind('*') > self.output.text().rfind('/'):
            x=self.output.text()
            c='*'
            ns=x[x.rfind(c)+1::]
            ans=1/(tan(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('/') > self.output.text().rfind('-') and self.output.text().rfind('/') > self.output.text().rfind('*') and self.output.text().rfind('/') > self.output.text().rfind('+'):
            x=self.output.text()
            c='/'
            ns=x[x.rfind(c)+1::]
            ans=1/(tan(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        else:
            x=float(self.output.text())
            ans=1/(tan(x))
            self.output.setText(str(ans))
    def seco(self):
        if self.output.text().rfind('+') > self.output.text().rfind('-') and self.output.text().rfind('+') > self.output.text().rfind('*') and self.output.text().rfind('+') > self.output.text().rfind('/'):
            x=self.output.text()
            c='+'
            ns=x[x.rfind(c)+1::]
            ans=1/(cos(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('-') > self.output.text().rfind('+') and self.output.text().rfind('-') > self.output.text().rfind('*') and self.output.text().rfind('-') > self.output.text().rfind('/'):
            x=self.output.text()
            c='-'
            ns=x[x.rfind(c)+1::]
            ans=1/(cos(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('*') > self.output.text().rfind('-') and self.output.text().rfind('*') > self.output.text().rfind('+') and self.output.text().rfind('*') > self.output.text().rfind('/'):
            x=self.output.text()
            c='*'
            ns=x[x.rfind(c)+1::]
            ans=1/(cos(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('/') > self.output.text().rfind('-') and self.output.text().rfind('/') > self.output.text().rfind('*') and self.output.text().rfind('/') > self.output.text().rfind('+'):
            x=self.output.text()
            c='/'
            ns=x[x.rfind(c)+1::]
            ans=1/(cos(float(ns)))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        else:
            x=float(self.output.text())
            ans=1/(sin(x))
            self.output.setText(str(ans))
    def rmo(self):
        self.output.clear()
    def sinto(self):
        if self.output.text().rfind('+') > self.output.text().rfind('-') and self.output.text().rfind('+') > self.output.text().rfind('*') and self.output.text().rfind('+') > self.output.text().rfind('/'):
            x=self.output.text()
            c='+'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=sin(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('-') > self.output.text().rfind('+') and self.output.text().rfind('-') > self.output.text().rfind('*') and self.output.text().rfind('-') > self.output.text().rfind('/'):
            x=self.output.text()
            c='-'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=sin(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('*') > self.output.text().rfind('-') and self.output.text().rfind('*') > self.output.text().rfind('+') and self.output.text().rfind('*') > self.output.text().rfind('/'):
            x=self.output.text()
            c='*'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=sin(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('/') > self.output.text().rfind('-') and self.output.text().rfind('/') > self.output.text().rfind('*') and self.output.text().rfind('/') > self.output.text().rfind('+'):
            x=self.output.text()
            c='/'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=sin(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        else:
            x=float(self.output.text())
            x=x*pi/180
            ans=sin(x)
            self.output.setText(str(ans))
    def tanto(self):
        if self.output.text().rfind('+') > self.output.text().rfind('-') and self.output.text().rfind('+') > self.output.text().rfind('*') and self.output.text().rfind('+') > self.output.text().rfind('/'):
            x=self.output.text()
            c='+'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=tan(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('-') > self.output.text().rfind('+') and self.output.text().rfind('-') > self.output.text().rfind('*') and self.output.text().rfind('-') > self.output.text().rfind('/'):
            x=self.output.text()
            c='-'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=tan(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('*') > self.output.text().rfind('-') and self.output.text().rfind('*') > self.output.text().rfind('+') and self.output.text().rfind('*') > self.output.text().rfind('/'):
            x=self.output.text()
            c='*'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=tan(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('/') > self.output.text().rfind('-') and self.output.text().rfind('/') > self.output.text().rfind('*') and self.output.text().rfind('/') > self.output.text().rfind('+'):
            x=self.output.text()
            c='/'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=tan(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        else:
            x=float(self.output.text())
            x=x*pi/180
            ans=tan(x)
            self.output.setText(str(ans))
    def costo(self):
        if self.output.text().rfind('+') > self.output.text().rfind('-') and self.output.text().rfind('+') > self.output.text().rfind('*') and self.output.text().rfind('+') > self.output.text().rfind('/'):
            x=self.output.text()
            c='+'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=cos(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('-') > self.output.text().rfind('+') and self.output.text().rfind('-') > self.output.text().rfind('*') and self.output.text().rfind('-') > self.output.text().rfind('/'):
            x=self.output.text()
            c='-'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=cos(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('*') > self.output.text().rfind('-') and self.output.text().rfind('*') > self.output.text().rfind('+') and self.output.text().rfind('*') > self.output.text().rfind('/'):
            x=self.output.text()
            c='*'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=cos(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        if self.output.text().rfind('/') > self.output.text().rfind('-') and self.output.text().rfind('/') > self.output.text().rfind('*') and self.output.text().rfind('/') > self.output.text().rfind('+'):
            x=self.output.text()
            c='/'
            ns=x[x.rfind(c)+1::]
            ns=float(ns)*pi/180
            ans=cos(float(ns))
            fs=x[:x.rfind(c)+1:]
            self.output.setText(fs+str(ans))
        else:
            x=float(self.output.text())
            x=x*pi/180
            ans=cos(x)
            self.output.setText(str(ans))
    def iferror(self):
        if 'ERROR' in self.output.text():
            self.output.setText('')
        else:
            pass
    def equalo(self):
        try:
            self.memory.addItem(str(eval((self.output.text()))))
            ans=eval(str(self.output.text()))
            self.output.setText(str(ans))
        except:       
            self.output.setText('ERROR')
    def memoryitem(self,item):
        self.output.setText(self.output.text()+str(eval((item.text()))))
    def clearo(self):
        self.output.clear()
    def b1(self):
        self.output.setText(self.output.text()+'(')
    def b2(self):
            self.output.setText(self.output.text()+')')
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background_image)



from PySide6.QtWidgets import QApplication, QWidget,QPushButton
import sys
app=QApplication(sys.argv)
win=Calculator()
win.show()
app.exec()                                            