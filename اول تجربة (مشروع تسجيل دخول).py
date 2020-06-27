import webbrowser # استدعيناه كي ينقلنا الى اليوتيوب عند الضغط على تسجيل
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * #استخدمنا منه QPixmap
from PyQt5.QtCore import Qt
a=QApplication(sys.argv)
w=QWidget()
w.setWindowTitle('اهلا وسهلا ') # اسم النافذة التي سنسجل الدخول اليها
#w.setGeometry(20,20,300,200)
lab=QLabel(w) # عرفناه كي نضع فيه الصورة
pic=QPixmap('ss.png') # الصورة طبعا هي موجودة في نفس ملف البرنامج لذلك اضفنا اليه فقط اسمها وامتدادها
lab.setPixmap(pic)
w.resize(pic.width(),pic.height()) # جعلنا النافذة w تاخذ عرض و طول الصورة
"""---------------------------------------------------------------"""
b=('انشاء حساب جديد','لدي حساب') # قائمة عرفناها كي نعرضها في مربع الحوار
d1=QInputDialog.getItem(w,'اهلا','الاجابة لطفا',b,1,False) # مربع الحوارDialogItem والذي من خلاله سنختار  ان كان لدينا حساب او ننشئ حساب جديد
if d1==('انشاء حساب جديد', False) or d1==('لدي حساب', False) : #هذه الدالة اذا ضغطنا cancel في Dialog Item سيخرج من البرنامج كما موضح فيه
       w.destroy(sys.exit())

elif d1 ==('انشاء حساب جديد', True) : # اذا اخترنا انشاء حساب سينفذ هذه الدالة وسننشئ فيها نافذة كاملة
      z1=QLabel('اسم المستخدم',w)
      z1.move(30,10)
      z2=QLineEdit(w)
      z2.setGeometry(120,10,150,20)
      x1=QLabel('الرقم السري',w)
      x1.move(30,50)
      x2=QLineEdit(w)
      x2.setGeometry(120,50,150,20)
      def p1f():#اذا ضغطنا على زر حفظ
          user=open("user.txt", "w") # فتحنا الملف اللي اسمه user بمود الكتابة
          z22=z2.text()# قرانا من QLineEdit مال اسم المستخدم
          user.write(str(z22)) ##  ملاحظة ان الملف لن يقبل سوى نص(string) لذلك كتبنا قبله نوع Type string
          print(user)
          password=open("pass.txt","w") #الباسوورد مثل عملية اليوزر نيم user name
          x22=x2.text()
          password.write(str(x22)) #  ملاحظة ان الملف لن يقبل سوى نص(string) لذلك كتبنا قبله نوع Type string
          print(password)
          w.destroy(sys.exit()) # عند التسجيل سيخرج من النافذة او نستطيع ارساله لاي مكان بعدها نريد
      def p2f():#اذا ضغطنا على زر الغاء
          w.destroy(sys.exit())
      p1=QPushButton('حفظ',w)
      p1.move(200,100)
      p1.clicked.connect(p1f) # ربط
      p2=QPushButton('الغاء',w)
      p2.move(280,100)
      p2.clicked.connect(p2f) # ربط
else: # هنا خيار لدي حساب
    z1 = QLabel('اسم المستخدم', w)
    z1.move(30, 10)
    z2 = QLineEdit(w)
    z2.setGeometry(120, 10, 150, 20)
    x1 = QLabel('الرقم السري', w)
    x1.move(30, 50)
    x2 = QLineEdit(w)
    x2.setGeometry(120, 50, 150, 20)


    def p1f():# عند الضغط على زر تشغيل
        user=open('user.txt','r') # نقرأ من الملف
        luser=[] # عرفنا مصفوفة او list كي نقرا من الملف لان الملف يرجع قيم على شكل مصفوفة
        for l in user:
            luser.append(l) # هذه الفور هي طريقة القراءة من اي ملف
        password=open('pass.txt','r')
        lpass=[]
        for i in password:
            lpass.append(i)
        z22=z2.text()
        lz=[str(z22)]
        x22=x2.text()
        lx=[str(x22)]
        if lz==luser and lx==lpass : # هذه الدالة اذا ضغطنا على تسجيل وكانت النتائج صحيحة سيسجل الدخول ويدخل لليوتيوب
            print('Done')
            webbrowser.open('https://www.youtube.com/watch?v=d_TuTzx0U1Y')
            w.destroy(sys.exit()) # هنا سيتخلص من النافذة ليبقى فقط اليوتيوب
        else: # اذا كانت معلومات التسجيل خاطئة سيظهر سؤال باستخدام QMessage Box
            b=QMessageBox.question(w,'خطأ','لديك خطأ في تسجيل الدخول هل تريد المحاولة من جديد؟؟؟',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if b==QMessageBox.Yes: # اذا اخترنا نعم
                p1f #نفذلي الدخول مجددا
            else:#اذا اخترنا لا
                w.destroy(sys.exit()) #سيخرج من النافذة



    def p2f(): # اذا اخترنا الغاء من النافذة W
        w.destroy(sys.exit()) # يخرج من النافذة w


    p1 = QPushButton('تسجيل', w)
    p1.move(200, 100)
    p1.clicked.connect(p1f)
    p2 = QPushButton('الغاء', w)
    p2.move(280, 100)
    p2.clicked.connect(p2f)

w.show()
sys.exit(a.exec_())