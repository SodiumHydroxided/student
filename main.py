import tkinter as tk
from tkinter import messagebox as mes
import easygui as e
import os
class login:
    def __init__(self, main: tk.Tk):
        self.setting=['名字',"班级","学籍号"]
        self.yonhu=os.listdir(r"./user")
        self.root = main
        self.root.title('登陆')
        self.root.geometry('420x300')
        #self.root.iconbitmap(tk.PhotoImage(r'D:\114.514\test\twitch.png'))
        self.login_page = tk.Frame(self.root)
        self.password = tk.StringVar()
        self.user = tk.StringVar()
        self.open_page()
    def windows(self):
        self.a=os.listdir(r"./user")
    def make(self):
        a=e.multenterbox('请填写信息','新建信息',['账号',"密码"])
        if a[0]=="" or a[1]=="":
            mes.showwarning(title='警告', message="请检查账号或密码是否为空")
        else:
            if a[0] in self.yonhu:
                mes.showwarning(title='警告',message='此账号已存在')
            else:
                os.mkdir(r"./user/" + a[0])
                open(r"./user/" + a[0] + "/mima", "w").write(a[1])
                open(r"./user/" + a[0] + "/flei", "w", encoding="GBK").close()
                mes.showinfo(title='提示',message='已成功新建，重启后生效')
    def open_page(self):
        tk.Label(self.login_page, text='账户:').grid(column=2, row=1)
        tk.Entry(self.login_page,textvariable=self.user).grid(column=3, row=1)
        tk.Label(self.login_page, text='密码:').grid(column=2, row=2)
        tk.Entry(self.login_page,show="#",textvariable=self.password).grid(column=3, row=2)
        tk.Button(self.login_page,text='登陆',command=self.match).grid(column=2,row=4)
        tk.Button(self.login_page, text='新建',command=self.make).grid(column=3, row=4)
        self.login_page.pack()
        self.login_page.update()
    def student(self):
        a = e.multenterbox('请填写信息', '新建信息', ['学生姓名', "班级","学籍号"])
        if a[0]=="" or a[1]=="" or a[2]=="":
            mes.showwarning(title='警告',message="请检查输入是否有空")
        else:
            for i in a:
                open(r"./user/" + self.user1 + "/flei", "a", encoding='GBK').write(i+"        ")
            open(r"./user/" + self.user1 + "/flei", "a", encoding='GBK').write("\n")
            b=a[0]+"        "+a[1]+"         "+a[2]
            c = open(r"./user/" + self.user.get() + "/flei", "r", encoding='GBK').readlines()
            ##del c[0]
            if c[0] == "\n" and c[1] == "\n":
                del c[0]
                del c[1]
            self.LB.insert("end",b)
    def remove(self):
        a=[]
        b=mes.askokcancel(title='删除',message='你确定删除吗')
        if b:
            for i in self.LB.curselection():
                a.append(self.LB.get(i))
            self.LB.delete(self.LB.index(tk.ANCHOR))
            b=open(r"./user/" + self.user.get() + "/flei", "r", encoding='GBK').readlines()
            del b[self.LB.index(tk.ANCHOR)]
            open(r"./user/" + self.user.get() + "/flei", "w", encoding='GBK').close()
            for i in range(len(b)):
                if b[i]=="\n":
                    del b[i]
            for j in range(len(b)):
                b[j]=b[j].rstrip('\n')
            for i in b:
                open(r"./user/" + self.user.get() + "/flei", "w", encoding='GBK').write(i+"\n")
            #print(open(r"./user/" + self.user.get() + "/flei", "r", encoding='GBK').readlines())
            b.clear()
        else:
            pass
    def kk(self, user):
        self.window = tk.Tk()
        self.window.title('系统')
        self.window.geometry("400x300")
        tk.Label(self.window,text=self.setting[0]).place(x=0,y=0)
        tk.Label(self.window,text=self.setting[1]).place(x=57,y=0)
        tk.Label(self.window, text=self.setting[2]).place(x=114, y=0)
        self.flie=open(r"./user/"+user+"/flei","r",encoding='GBK')
        # 创建一个空列表
        self.LB = tk.Listbox(self.window,width='300')
        self.LB.place(x=0,y=20)
        tk.Button(self.window, text="删除", command=lambda: self.remove()).place(x=50,y=200)
        tk.Button(self.window, text='添加',command=self.student).place(x=100,y=200)
        # 往列表里添加数据
        for item in self.flie:
            self.LB.insert("end", item)
        #print(self.LB.get())
    def match(self):
        if self.user.get() in self.yonhu:
            b=open(r"./user/"+self.user.get()+"/mima",'r').read()
            if self.password.get()==b:
                mes.showinfo(title='欢迎',message='欢迎管理员')
                self.user1=self.user.get()
                #self.root.destroy()
                self.kk(self.user.get())
                self.windows()

        else:
            if self.user.get() not in self.yonhu:
                mes.showwarning(title='警告',message='用户名不存在')
            else:
                mes.showerror(title='失败',message='身份验证失败')
if __name__ == '__main__':
    e.msgbox(title='警告',msg='未经作者允许禁止商用',ok_button='我知道了')
    try:
        os.mkdir(r"./user")
    except:
        pass
    root = tk.Tk()
    login(root)
    root.mainloop()