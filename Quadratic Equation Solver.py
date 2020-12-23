from tkinter import *
from helper import EntryWithPlaceholder
from main import solve, calculate_det

WIDTH = 700
HEIGHT = 600



#----------------------------------------------------------#
#                  		FUNCTIONS                          #
#----------------------------------------------------------#


def get_solution():
	try:
		error_label['text'] = ''
		a, b, c = float(a_entry.get()), float(b_entry.get()), float(c_entry.get())
		if int(a) == a: a = int(a)
		if int(b) == b: b = int(b)
		if int(c) == c: c = int(c)
		equation_label['text'] = f'{a} * x^2 + {b} * x + {c} = 0'
		delta = calculate_det(a, b, c)
		delta_label['text'] = f'Δ = ({b})^2 - 4 * ({a}) * ({c}) = {delta}'
		if delta < 0:
			interpretation_label['text'] = 'Δ < 0  =>  This equation admits 0 solution in IR'
			solution1['text'] = ''
			solution2['text'] = ''
			final_solutions['text'] = f'Solutions : {None}'
		elif delta == 0:
			x = solve(a, b, c)
			if int(x) == x: x = int(x)
			interpretation_label['text'] = 'Δ = 0  =>  This equation admits 1 solution in IR'
			solution1['text'] = f'x1 = x2 = x = -{b} / 2 * {a} = {x}'
			solution2['text'] = ''
			final_solutions['text'] = f'Solutions : {x}'
		else:
			solutions = [int(x) for x in solve(a, b, c) if int(x)==x]
			x1, x2 = solutions[0], solutions[1]
			interpretation_label['text'] = 'Δ > 0  =>  This equation admits 2 solutions in IR'
			solution1['text'] = f'x1 = (-{b} + √{delta} ) / 2 * {a} = {x1}'
			solution2['text'] = f'x2 = (-{b} - √{delta} ) / 2 * {a} = {x2}'
			final_solutions['text'] = f'Solutions : {x1}, {x2}'
	except ValueError:
		error_label['text'] = 'a, b and c should be numbers !'
		equation_label['text'] = ''
		interpretation_label['text'] = ''
		delta_label['text'] = ''
		solution1['text'] = ''
		solution2['text'] = ''
		final_solutions['text'] = ''
	finally:
		a_entry.put_placeholder()
		b_entry.put_placeholder()
		c_entry.put_placeholder()


def key_pressed(event):
	if event.keysym == 'Return':
		get_solution()

#----------------------------------------------------------#
#                  		INITIALIZATION                     #
#----------------------------------------------------------#


root = Tk()
root.bind("<Key>",key_pressed)
canvas = Canvas(root, width=WIDTH,height=HEIGHT)
root.iconbitmap('./icon.ico')
root.title('Quadratic Equations Solver')
canvas.pack()


#----------------------------------------------------------#
#                  		  GUI                              #
#----------------------------------------------------------#


#-----------Frames-----------#


bg_frame = Frame(root, bg='red')
bg_frame.place(relwidth=1, relheight=1, relx=0, rely=0)


holder_frame = Frame(root, bg='black')
holder_frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)


entry_frame = Frame(holder_frame, bg='black')
entry_frame.place(relwidth=0.8, relheight=0.1, relx=0.2, rely=0.15)


solution_frame = Frame(holder_frame)
solution_frame.place(relwidth=0.8, relheight=0.55, relx=0.1, rely=0.3)


#-----------Entries and Labesl-----------#


a_entry = EntryWithPlaceholder(entry_frame, 'a')
a_entry.place(relx = 0, rely = 0.1, relwidth=0.1)

x2_label = Label(entry_frame, text='x^2  +', font=('Helvetica', 14), fg='white', bg = 'black')
x2_label.place(relx = 0.11, rely = 0.07)


b_entry = EntryWithPlaceholder(entry_frame, 'b')
b_entry.place(relx = 0.28, rely = 0.1, relwidth=0.1)

x1_label = Label(entry_frame, text='x  +', font=('Helvetica', 14), fg='white', bg = 'black')
x1_label.place(relx = 0.39, rely = 0.07)


c_entry = EntryWithPlaceholder(entry_frame, 'c')
c_entry.place(relx = 0.51, rely = 0.1, relwidth=0.1)

equal0_label = Label(entry_frame, text='=  0', font=('Helvetica', 14), fg='white', bg = 'black')
equal0_label.place(relx = 0.63, rely = 0.07)

equation_label = Label(solution_frame, text='a * x^2 + b * x + c = 0', font=('Helvetica', 13))
equation_label.pack()

delta_label = Label(solution_frame, text='Δ = b^2 - 4 * a * c', font=('Helvetica', 13))
delta_label.place(relx=0.05, rely=0.2)

interpretation_label = Label(solution_frame, text='', font = ('Helvetica', 13))
interpretation_label.place(relx=0.05, rely=0.35)

solution1 = Label(solution_frame, text='x1 = (-b + √Δ )/2a', font=('Helvetica', 13))
solution1.place(relx=0.15, rely=0.5)

solution2 = Label(solution_frame, text='x2 = (-b - √Δ )/2a', font=('Helvetica', 13)) 
solution2.place(relx=0.15, rely=0.65)

final_solutions = Label(solution_frame, text='',font=('Helvetica', 14), fg='red')
final_solutions.place(relx=0.35, rely=0.8)

error_label = Label(solution_frame, text='',font=('Helvetica', 16), fg ='red')
error_label.place(relx = 0.23, rely=0.41)

madeby_label = Label(bg_frame, text='Made by Abdellah Essordo', font='Helvetica 13 bold', fg='black', bg='red')
madeby_label.place(relx=0.05, rely=0.955)



#-----------Buttons-----------#


solve_BTN = Button(holder_frame, text = 'Solve', font=('Helvetica', 12), command=lambda:get_solution())
solve_BTN.place(relx =0.4 , rely =0.9 , relwidth =0.2 , relheight = 0.05)



#----------------------------------------------------------#
#                  		  EXECUTION                        #
#----------------------------------------------------------#

if __name__ == '__main__':
	root.mainloop()