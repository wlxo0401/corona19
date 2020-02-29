# 라이브러리를 불러온다.
import datetime
import tkinter
from bs4 import BeautifulSoup
from urllib.request import urlopen
import tkinter.font
import tkinter.messagebox
import threading
def MsgBox1():
    tkinter.messagebox.showinfo('메시지상자','테스트입니다.\n데스트세트트테스트')




window = tkinter.Tk()

# 윈도우 창의 제목 설정
window.title("Corona")
# 너비x높이+x좌표+y좌표
window.geometry("640x400+100+100")
# 상하 좌우 크기 조절 여부
window.resizable(False,False)


#시계는 반복해주어야 합니다.
now = datetime.datetime.now()
font=tkinter.font.Font(family="맑은 고딕", size=15, slant="italic")
size = tkinter.font.Font(size=10)
intro = tkinter.Label(window, text = '안녕하세요 저는 프로그램을 연습하려고 이 것을 만들었습니다.',width=100, height=5, fg="red",font=font, relief="solid")
now = datetime.datetime.now()
nowtime = tkinter.Label(window, text="%s년 %s월 %s일 %s시 %s분" %(now.year, now.month, now.day, now.hour, now.minute),font=font)
button = tkinter.Button(window, overrelief="solid", width=15, command = MsgBox1, repeatdelay=1000, repeatinterval=100)

intro.pack()
nowtime.pack()
button.pack()
window.mainloop()


