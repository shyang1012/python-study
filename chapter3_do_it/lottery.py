import tkinter as tk
import requests
from bs4 import BeautifulSoup


class LotteryApp(tk.Frame):

    def __init__(self, master=None) -> object:
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.titleStr = tk.StringVar();
        self.titleStr.set("로또6/45 회차별 당첨번호")
        self.titleLabel = tk.Label(self, textvariable=self.titleStr)
        self.titleLabel.pack(side="top",fill="x")

        self.ent = tk.Entry(self)
        self.ent.pack()
        btn = tk.Button(self)
        btn.config(text="로또 당첨확인")
        btn.config(command=self.get_contents)
        btn.pack()
        self.contentText = tk.StringVar()
        self.contentText.set("No Data")
        self.resultLabel = tk.Label(self, textvariable=self.contentText)
        self.resultLabel.config(width=50,height=9)
        self.resultLabel.pack()

        self.tailStr = tk.StringVar();
        self.tailStr.set("Do it! 점프 투 파이썬")
        self.tailLabel = tk.Label(self, textvariable=self.tailStr)
        self.tailLabel.pack(side="bottom",anchor="e")

    def get_contents(self):
        drw_no_param = self.ent.get()
        self.contentText.set(drw_no_param)
        url = f"""https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={drw_no_param}"""
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        txt = soup.find("div", attrs={'class': 'win_result'}).text
        print(txt.split("\n"))
        drwNo = txt.split("\n")[1]
        drawNum = drwNo[0:3]
        drwDate = txt.split("\n")[2]
        num_list = txt.split("\n")[7:13]
        result_str = ''
        for drw_no_param in num_list:
            result_str += "[" + drw_no_param + "]" + " "
        bonus = txt.split("\n")[-4]

        if self.ent.get() == "":
            self.ent.insert(0, drawNum)

        print("url", url)
        print("회차", drwNo)
        print("당첨번호", num_list)
        print("회차_숫자만", drwNo[0:3])
        print("보너스번호", bonus)
        result = f"""
        {drwNo} {drwDate}
        
        {result_str}
        
        + 보너스:[{bonus}]"""
        self.contentText.set(result)
        return result


if __name__ == "__main__":
    root = tk.Tk()  # 창 생성
    root.geometry('300x200+100+100')
    root.title('로또 회차별 당첨번호')
    root.option_add("*Font", "맑은고딕 10")
    root.resizable(False,False)
    app = LotteryApp(master=root)
    app.mainloop()  # 창 실행
