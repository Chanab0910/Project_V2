import tkinter as tk
from tkinter import ttk
from project_code.analyse_results import Analyse
import project_code


class GUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        '''self.geometry("1239x697")'''

        self.Argentina = tk.PhotoImage(file="../img/Argentina.png")
        self.Australia = tk.PhotoImage(file="../img/Australia.png")
        self.Austria = tk.PhotoImage(file="../img/Austria.png")
        self.Belgium = tk.PhotoImage(file="../img/Belgium.png")
        self.Canada = tk.PhotoImage(file="../img/Canada.png")
        self.Croatia = tk.PhotoImage(file="../img/Croatia.png")
        self.Czech = tk.PhotoImage(file="../img/Czech.png")
        self.Denmark = tk.PhotoImage(file="../img/Denmark.png")
        self.England = tk.PhotoImage(file="../img/England.png")
        self.Finland = tk.PhotoImage(file="../img/Finland.png")
        self.France = tk.PhotoImage(file="../img/France.png")
        self.Germany = tk.PhotoImage(file="../img/Germany.png")
        self.Hungary = tk.PhotoImage(file="../img/Hungary.png")
        self.Iceland = tk.PhotoImage(file="../img/Iceland.png")
        self.Ireland = tk.PhotoImage(file="../img/Ireland.png")
        self.Italy = tk.PhotoImage(file="../img/Italy.png")
        self.Mexico = tk.PhotoImage(file="../img/Mexico.png")
        self.Ghana = tk.PhotoImage(file="../img/Ghana.png")
        self.Netherlands = tk.PhotoImage(file="../img/Netherlands.png")
        self.Morocco = tk.PhotoImage(file="../img/Morocco.png")
        self.Norway = tk.PhotoImage(file="../img/Norway.png")
        self.Poland = tk.PhotoImage(file="../img/Poland.png")
        self.Portugal = tk.PhotoImage(file="../img/Portugal.png")
        self.Romania = tk.PhotoImage(file="../img/Romania.png")
        self.Scotland = tk.PhotoImage(file="../img/Scotland.png")
        self.Spain = tk.PhotoImage(file="../img/Spain.png")
        self.Sweden = tk.PhotoImage(file="../img/Sweden.png")
        self.Ukraine = tk.PhotoImage(file="../img/Ukraine.png")
        self.USA = tk.PhotoImage(file="../img/USA.png")
        self.Wales = tk.PhotoImage(file="../img/Wales.png")
        self.Japan = tk.PhotoImage(file="../img/Japan.png")
        self.China = tk.PhotoImage(file="../img/China.png")



        self.Argentina_button = tk.Button(self, image=self.Argentina, width=220, height=140)
        self.Australia_button = tk.Button(self, image=self.Australia, width=220, height=140)
        self.Austria_button = tk.Button(self, image=self.Austria, width=220, height=140, padx=50)
        self.Belgium_button = tk.Button(self, image=self.Belgium, width=220, height=140)
        self.Canada_button = tk.Button(self, image=self.Canada, width=220, height=140)
        self.Croatia_button = tk.Button(self, image=self.Croatia, width=220, height=140)
        self.Czech_button = tk.Button(self, image=self.Czech, width=220, height=140)
        self.Denmark_button = tk.Button(self, image=self.Denmark, width=220, height=140)
        self.England_button = tk.Button(self, image=self.England, width=220, height=140, command=self.get_country_stats)
        self.Finland_button = tk.Button(self, image=self.Finland, width=220, height=140)
        self.France_button = tk.Button(self, image=self.France, width=220, height=140)
        self.Germany_button = tk.Button(self, image=self.Germany, width=220, height=140)
        self.Hungary_button = tk.Button(self, image=self.Hungary, width=220, height=140)
        self.Iceland_button = tk.Button(self, image=self.Iceland, width=220, height=140)
        self.Ireland_button = tk.Button(self, image=self.Ireland, width=220, height=140)
        self.Italy_button = tk.Button(self, image=self.Italy, width=220, height=140)
        self.Mexico_button = tk.Button(self, image=self.Mexico, width=220, height=140)
        self.Ghana_button = tk.Button(self, image=self.Ghana, width=220, height=140)
        self.Netherlands_button = tk.Button(self, image=self.Netherlands, width=220, height=140)
        self.Morocco_button = tk.Button(self, image=self.Morocco, width=220, height=140)
        self.Norway_button = tk.Button(self, image=self.Norway, width=220, height=140)
        self.Poland_button = tk.Button(self, image=self.Poland, width=220, height=140)
        self.Portugal_button = tk.Button(self, image=self.Portugal, width=220, height=140)
        self.Romania_button = tk.Button(self, image=self.Romania, width=220, height=140)
        self.Scotland_button = tk.Button(self, image=self.Scotland, width=220, height=140)
        self.Spain_button = tk.Button(self, image=self.Spain, width=220, height=140)
        self.Sweden_button = tk.Button(self, image=self.Sweden, width=220, height=140)
        self.Ukraine_button = tk.Button(self, image=self.Ukraine, width=220, height=140)
        self.USA_button = tk.Button(self, image=self.USA, width=220, height=140)
        self.Wales_button = tk.Button(self, image=self.Wales, width=220, height=140)
        self.Japan_button = tk.Button(self, image=self.Japan, width=220, height=140)
        self.China_button = tk.Button(self, image=self.China, width=220, height=140)

        self.title = tk.Label(self, text='Select the country whoms stats you would like to see',
                              font='FuturaStd-Medium 50')
        self.Argentina_label = tk.Label(self, text='Argentina', font='FuturaStd-Medium 20')
        self.Australia_label = tk.Label(self, text='Australia', font='FuturaStd-Medium 20')
        self.Austria_label = tk.Label(self, text='Austria', font='FuturaStd-Medium 20')
        self.Belgium_label = tk.Label(self, text='Belgium', font='FuturaStd-Medium 20')
        self.Canada_label = tk.Label(self, text='Canada', font='FuturaStd-Medium 20')
        self.Croatia_label = tk.Label(self, text='Croatia', font='FuturaStd-Medium 20')
        self.Czech_label = tk.Label(self, text='Czech Republic', font='FuturaStd-Medium 20')
        self.Denmark_label = tk.Label(self, text='Denmark', font='FuturaStd-Medium 20')
        self.England_label = tk.Label(self, text='England', font='FuturaStd-Medium 20')
        self.Finland_label = tk.Label(self, text='Finland', font='FuturaStd-Medium 20')
        self.France_label = tk.Label(self, text='France', font='FuturaStd-Medium 20')
        self.Germany_label = tk.Label(self, text='Germany', font='FuturaStd-Medium 20')
        self.Hungary_label = tk.Label(self, text='Hungary', font='FuturaStd-Medium 20')
        self.Iceland_label = tk.Label(self, text='Iceland', font='FuturaStd-Medium 20')
        self.Ireland_label = tk.Label(self, text='Ireland', font='FuturaStd-Medium 20')
        self.Italy_label = tk.Label(self, text='Italy', font='FuturaStd-Medium 20')
        self.Mexico_label = tk.Label(self, text='Mexico', font='FuturaStd-Medium 20')
        self.Ghana_label = tk.Label(self, text='Ghana', font='FuturaStd-Medium 20')
        self.Netherlands_label = tk.Label(self, text='Netherlands', font='FuturaStd-Medium 20')
        self.Morocco_label = tk.Label(self, text='Morocco', font='FuturaStd-Medium 20')
        self.Norway_label = tk.Label(self, text='Norway', font='FuturaStd-Medium 20')
        self.Poland_label = tk.Label(self, text='Poland', font='FuturaStd-Medium 20')
        self.Portugal_label = tk.Label(self, text='Portugal', font='FuturaStd-Medium 20')
        self.Romania_label = tk.Label(self, text='Romania', font='FuturaStd-Medium 20')
        self.Scotland_label = tk.Label(self, text='Scotland', font='FuturaStd-Medium 20')
        self.Spain_label = tk.Label(self, text='Spain', font='FuturaStd-Medium 20')
        self.Sweden_label = tk.Label(self, text='Sweden', font='FuturaStd-Medium 20')
        self.Ukraine_label = tk.Label(self, text='Ukraine', font='FuturaStd-Medium 20')
        self.USA_label = tk.Label(self, text='USA', font='FuturaStd-Medium 20')
        self.Wales_label = tk.Label(self, text='Wales', font='FuturaStd-Medium 20')
        self.Japan_label = tk.Label(self, text='Japan', font='FuturaStd-Medium 20')
        self.China_label = tk.Label(self, text='China', font='FuturaStd-Medium 20')

        self.place_widgets()

    def place_widgets(self):
        # This project_code creates the widgets and grids them
        '''self.background.grid()'''
        self.title.grid(columnspan=8, row=0, pady=10)

        self.Argentina_button.grid(column=0, row=1, padx=10)
        self.Australia_button.grid(column=1, row=1, padx=10)
        self.Austria_button.grid(column=2, row=1, padx=10)
        self.Belgium_button.grid(column=3, row=1, padx=10)
        self.Canada_button.grid(column=4, row=1, padx=10)
        self.Croatia_button.grid(column=5, row=1, padx=10)
        self.Czech_button.grid(column=6, row=1, padx=10)
        self.Denmark_button.grid(column=7, row=1, padx=10)

        self.Argentina_label.place(x=78, y=236)
        self.Australia_label.place(x=332, y=236)
        self.Austria_label.place(x=583, y=236)
        self.Belgium_label.place(x=832, y=236)
        self.Canada_label.place(x=1082, y=236)
        self.Croatia_label.place(x=1331, y=236)
        self.Czech_label.place(x=1541, y=236)
        self.Denmark_label.place(x=1823, y=236)

        self.England_button.grid(column=0, row=2, padx=10, pady=40)
        self.Finland_button.grid(column=1, row=2, padx=10, pady=40)
        self.France_button.grid(column=2, row=2, padx=10, pady=40)
        self.Germany_button.grid(column=3, row=2, padx=10, pady=40)
        self.Hungary_button.grid(column=4, row=2, padx=10, pady=40)
        self.Iceland_button.grid(column=5, row=2, padx=10, pady=40)
        self.Ireland_button.grid(column=6, row=2, padx=10, pady=40)
        self.Italy_button.grid(column=7, row=2, padx=10, pady=40)

        self.England_label.place(x=85, y=425)
        self.Finland_label.place(x=338, y=425)
        self.France_label.place(x=588, y=425)
        self.Germany_label.place(x=828, y=425)
        self.Hungary_label.place(x=1078, y=425)
        self.Iceland_label.place(x=1328, y=425)
        self.Ireland_label.place(x=1581, y=425)
        self.Italy_label.place(x=1840, y=425)

        self.Mexico_button.grid(column=0, row=3, padx=10, )
        self.Ghana_button.grid(column=1, row=3, padx=10, )
        self.Netherlands_button.grid(column=2, row=3, padx=10, )
        self.Morocco_button.grid(column=3, row=3, padx=10, )
        self.Norway_button.grid(column=4, row=3, padx=10, )
        self.Poland_button.grid(column=5, row=3, padx=10, )
        self.Portugal_button.grid(column=6, row=3, padx=10, )
        self.Romania_button.grid(column=7, row=3, padx=10, )

        self.Mexico_label.place(x=89, y=614)
        self.Ghana_label.place(x=338, y=614)
        self.Netherlands_label.place(x=568, y=614)
        self.Morocco_label.place(x=828, y=614)
        self.Norway_label.place(x=1080, y=614)
        self.Poland_label.place(x=1328, y=614)
        self.Portugal_label.place(x=1571, y=614)
        self.Romania_label.place(x=1822, y=614)

        self.Scotland_button.grid(column=0, row=4, padx=10, pady=40)
        self.Spain_button.grid(column=1, row=4, padx=10, pady=40)
        self.Sweden_button.grid(column=2, row=4, padx=10, pady=40)
        self.Ukraine_button.grid(column=3, row=4, padx=10, pady=40)
        self.USA_button.grid(column=4, row=4, padx=10, pady=40)
        self.Wales_button.grid(column=5, row=4, padx=10, pady=40)
        self.Japan_button.grid(column=6, row=4, padx=10, pady=40)
        self.China_button.grid(column=7, row=4, padx=10, pady=40)

        self.Scotland_label.place(x=82, y=803)
        self.Spain_label.place(x=338, y=803)
        self.Sweden_label.place(x=573, y=803)
        self.Ukraine_label.place(x=829, y=803)
        self.USA_label.place(x=1091, y=803)
        self.Wales_label.place(x=1334, y=803)
        self.Japan_label.place(x=1584, y=803)
        self.China_label.place(x=1838, y=803)

    def get_country_stats(self):
        analyse = Analyse()
        print(analyse.controller('England'))


if __name__ == '__main__':
    root = GUI()
    root.mainloop()
