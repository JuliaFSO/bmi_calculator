import tkinter
from tkinter import ttk
from tkinter import messagebox
from matplotlib import pyplot as plt
import tkinter.font as tkFont
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


def bmi(weight, height):
    weight = float(weight)
    height = float(height) / 100
    bmi_calc = weight / height ** 2
    if bmi_calc < 18.5:
        return 'Underweight'
    elif bmi_calc < 25:
        return 'Normal weight'
    elif bmi_calc < 30:
        return 'Overweight'
    else:
        return 'Obesity'


def get_data():
    name = nameEntry.get()
    age = agesPinBox.get()
    height = heightEntry.get()
    weight = weightEntry.get()
    try:
        res = bmi(weight, height)
        if name and age and height and weight != '':
            save_data(name, age, height, weight, res)
            bmi_result.config(text=f'BMI RESULT: {res}')
            return name, age, height, weight, res
        else:
            tkinter.messagebox.showwarning(title='Error: Missing Data', message='Please fill out the missing data.')
    except:
        tkinter.messagebox.showwarning(title='Error: Invalid data.', message='Please enter valid weight and height.')


def result():
    res = get_data()[-1]
    return res


def save_data(name, age, height, weight, res):
    print(f'Name: {name}\t Age: {age}')
    print(f'Height: {height} \tWeight: {weight}')
    print(res)
    with open('bmi_data.txt', 'a') as fwrite:
        fwrite.write(f'{name}, {age}, {height}, {weight}, {res}\n')
    print('Saved')


def show_chart():
    with open('bmi_data.txt', 'r') as bmi_data:
        info_list = []
        for line in bmi_data:
            info_list.append(line.strip())
        bmi_list = []
        for info in info_list:
            split_info = info.split(', ')
            bmi_category = split_info[-1]
            bmi_list.append(bmi_category)
    colors = ['green', 'orange', 'blue', 'red']
    counts = [
        bmi_list.count('Underweight'),
        bmi_list.count('Normal weight'),
        bmi_list.count('Overweight'),
        bmi_list.count('Obesity')
    ]

    chart_window = tkinter.Toplevel(window)
    chart_window.title('BMI Distribution Chart')

    fig, ax = plt.subplots()
    ax.pie(counts, colors=colors, autopct='%1.1f%%')
    plt.title('BMI Distribution')
    plt.legend(['Underweight', 'Normal weight', 'Overweight', 'Obesity'], loc='lower right')
    plt.show()

    canvas = FigureCanvasTkAgg(fig, master=chart_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=True)


window = tkinter.Tk()
window.title('BMI Calculator')

frame = tkinter.Frame(window)
frame.pack()

info_frame = tkinter.LabelFrame(frame, text='Information')
info_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

nameLabel = tkinter.Label(info_frame, text='Name: ')
nameLabel.grid(row=0, column=0, pady=5, padx=2, sticky='w')
nameEntry = tkinter.Entry(info_frame)
nameEntry.grid(row=0, column=1, pady=5, padx=2, sticky='ew')

ageLabel = tkinter.Label(info_frame, text='Age: ')
agesPinBox = tkinter.Spinbox(info_frame, from_=1, to=100, width=5)
ageLabel.grid(row=0, column=2, pady=5, padx=2, sticky='w')
agesPinBox.grid(row=0, column=3, pady=5, padx=2, sticky='ew')

heightLabel = tkinter.Label(info_frame, text='Height (cm): ')
heightLabel.grid(row=1, column=0, pady=0, padx=2, sticky='w')
heightEntry = tkinter.Entry(info_frame, width=7)
heightEntry.grid(row=1, column=1, pady=0, padx=2, sticky='ew')

weightLabel = tkinter.Label(info_frame, text='Weight (kg): ')
weightLabel.grid(row=1, column=2, pady=5, padx=2, sticky='w')
weightEntry = tkinter.Entry(info_frame, width=7)
weightEntry.grid(row=1, column=3, pady=5, padx=5, sticky='ew')

saveBtn = tkinter.Button(frame, text='Calculate BMI', command=get_data)
saveBtn.grid(row=2, column=0, pady=5, padx=20, sticky='w')

bmiResults = tkinter.LabelFrame(frame, text='BMI Results')
bmiResults.grid(row=3, column=0, pady=10, padx=10, sticky='nsew')

bold_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

bmi_result = tkinter.Label(bmiResults, text=f'BMI: ', font=bold_font)
bmi_result.grid(row=4, column=0, padx=20, pady=20)

showChartBtn = tkinter.Button(frame, text='Show Chart', command=show_chart)
showChartBtn.grid(row=5, column=0, pady=5, padx=20, sticky='w')

window.mainloop()
