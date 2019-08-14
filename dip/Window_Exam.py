#-*-coding: utf-8 -*-
from tkinter import * #기본적인 윈도우를위한 import
from tkinter import ttk #label 쓰면서 import 했음 + button
from tkinter import messagebox #message import
width = 400
height = 100
win = Tk() #TK클래스 의인스턴스 를생성
def clickMe():
	messagebox.showinfo("새로운버튼윈도우제목","새로운버튼윈도우라벨")

'''
def toggle_fullscreen(self, event=None):
	win.attributes("-fullscreen", True)
	return "break"	
'''
action = ttk.Button(win, text = "버튼이름", command = clickMe)
action.grid(column = 0, row = 1)
win.title("성민이의 연습용 UI")#제목 달기
win.geometry(str(width)+ 'x' + str(height) + '+250+250')#set size
#win.attributes('-fullscreen',True)
win.resizable(0,0) #fix size
ttk.Label(win, text = "헬로우 월드").grid(column = 1, row = 0)

win.mainloop() #사용자가 윈도우를 닫아버리기 전까지 이벤트를 처리해주는 무한대기 루프

