

from tkinter import *
import requestMethod


def printtext():
    doc = entry.get()
    output = ''
    if doc == '':
        output = requestMethod.get()
    else:
        dictionary = {'disease': doc}
        output = requestMethod.post(dictionary)

################################## second window opens#######################################
    searchbutton.place_forget()
    lable.place_forget()
    lable2.place_forget()
    entry.place_forget()

    scrollbar = Scrollbar(main_window)
    scrollbar.pack(side=RIGHT, fill=Y)
    area = Text(main_window, yscrollcommand=scrollbar.set,
                font=('Courier New', 11))
    area.pack(expand=True, fill='both')
    scrollbar.config(command=area.yview)
    print(output)
    for x in output:
        area.insert(INSERT, x['disease'])
        area.insert(INSERT, "\n\n")

    area.config(state=DISABLED)


############################## Start up window ###################################
main_window = Tk()
main_window.geometry('1100x650+50+100')
main_window.title('D-Checker')

entry = Entry(main_window, bd=2, relief='raised', width=60)
entry.place(x=340, y=250)
lable = Label(
    main_window, text='This is a medical search engine.', font='times 30')
lable.place(x=320, y=300)
lable2 = Label(main_window, text='D-Checker', fg='green', font='times 110')
lable2.place(x=280, y=80)

searchbutton = Button(main_window, text='search', width=12,
                      height=1, bd=3, relief='raised', command=printtext)
searchbutton.place(x=760, y=246)


main_window.mainloop()
