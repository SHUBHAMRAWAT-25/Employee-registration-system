from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import matplotlib.pyplot as plt
import re

def f1():
	root.withdraw()
	aw.deiconify()

def f2():
	aw.withdraw()
	root.deiconify()

def f3():
	root.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0,END)
	con=None
	try:
		con=connect("kc.db")
		cursor=con.cursor()
		sql="select * from employee order by id"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info=info+"id:" + str(d[0]) + "  name:" + str(d[1]) + "  sal:" + str(d[2]) +"\n"
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()

def f4():
	vw.withdraw()
	root.deiconify()

def f5():
	con=None
	try:
		con=connect("kc.db")
		cursor=con.cursor()
		sql="insert into employee values('%d','%s','%f')"		
		id2=aw_ent_id.get()
		id=id2
		query = "SELECT * FROM employee WHERE id = ?"
		cursor.execute(query, (id,))
		if cursor.fetchone():
			showerror("Issue", "id already exists")
		else:
			if id2.isnumeric():
				id=int(id2)
				if id<=0:			
					raise ValueError("id should be positive integer")
			else:
				raise ValueError("id should be positive integer")

			name1=aw_ent_name.get()	
			# if bool(re.match("^[A-Za-z ]+$",name)):
			if name1.isalpha():
				if name1.strip() == "":
					showerror("Issue", "Name should contain only alphabets 1")
				else:
					if len(name1)>=2:	
						name=name1
					else:
						showerror("Issue", "Minimum length of name should be two")

			else:
				raise ValueError("Name should contain only alphabets")	
	
			salary2=aw_ent_salary.get()
			if salary2.isdigit():
				salary=float(salary2)
				if salary<8000.0:
					raise ValueError("Minimum salary should be 8000")
			else:
				raise ValueError("Salary should be number")
			cursor.execute(sql%(id,name,salary))
			if cursor.rowcount==1:
				con.commit()
				showinfo("Success", "Record Created")
		
	except ValueError as e:
		showerror("Issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		aw_ent_id.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_salary.delete(0,END)
		aw_ent_id.focus()

def f6():
	root.withdraw()
	uw.deiconify()

def f7():
	uw.withdraw()
	root.deiconify()

def f8():
	root.withdraw()
	dw.deiconify()

def f9():
	dw.withdraw()
	root.deiconify()

def f10():
	con=None
	try:		
		con=connect("kc.db")
		cursor=con.cursor()
		sql="update employee set name='%s',salary='%f' where id='%d'"
	
		id2=uw_ent_id.get()
		if not id2.isalpha():	
			if id2.isnumeric():
				id=int(id2)
				if id<=0:			
					raise ValueError("id should be positive integer")
			else:
				raise ValueError("id should be integer")	 	
		else:
			raise ValueError("id should be integer")

		id=int(id2)
		query = "SELECT * FROM employee WHERE id = ?"
		cursor.execute(query, (id,))
		if cursor.fetchone():	
			name1=uw_ent_name.get()	
			if name1.isalpha():
				if name1.strip() == "":
					showerror("Issue", "Name should contain only alphabets 1")
				else:
					if len(name1)>2:	
						name=name1
					else:
						showerror("Issue", "Minimum length of name should be two")

			else:
				raise ValueError("Name should contain only alphabets")	
	
			salary2=uw_ent_salary.get()
			if not salary2.isalpha():
				if salary2.isdigit():
					salary=float(salary2)
					if salary<8000.0:
						raise ValueError("Minimum salary should be 8000")
				else:
					raise ValueError("Salary should be number")
			else:	
				raise ValueError("Salary should be number")	
			cursor.execute(sql%(name,salary,id))
			if cursor.rowcount==1:
				con.commit()
				showinfo("Success", "Record updated")
		else:
			showerror("Issue", "id does not exists")
	except ValueError as e:
		con.rollback()
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
		uw_ent_id.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_salary.delete(0,END)
		uw_ent_id.focus()

def f11():
	con=None
	try:		
		con=connect("kc.db")
		cursor=con.cursor()
		sql="delete from employee where id='%d'"

		id2=dw_ent_id.get()
		if not id2.isalpha():	
			if id2.isnumeric():
				id=int(id2)
				if id<=0:			
					raise ValueError("id should be positive integer")
			else:
				raise ValueError("id should be integer")	 	
		else:
			raise ValueError("id should be integer")
		
		id=int(id2)
		query = "SELECT * FROM employee WHERE id = ?"
		cursor.execute(query, (id,))
		if cursor.fetchone():
			cursor.execute(sql%(id))
			if cursor.rowcount==1:
				con.commit()
				showinfo("Success", "Record deleted")
		else:
			showerror("Issue", "id does not exists")
	except ValueError as e:
		con.rollback()
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
		dw_ent_id.delete(0,END)
		dw_ent_id.focus()

def f12():
	root.withdraw()
	con=None
	try:
		con=connect("kc.db")
		cursor=con.cursor()
		sql="select salary, name from employee order by salary desc limit 5"
		cursor.execute(sql)
		result=cursor.fetchall()
		data1=[row[0] for row in result]		
		data2=[row[1] for row in result]		
		plt.bar(data2,data1,width=0.5)
		plt.xlabel("Employee")
		plt.ylabel("Salary")
		plt.title("Top 5 Salaried Employee")
		plt.show()
		
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
	


root=Tk()
root.title("E.M.S")
root.geometry("900x700+50+50")
root.configure(bg="pale green")
f=("Simsun", 30, "bold")

try:
	wa1="https://ipinfo.io/"
	res1=requests.get(wa1)	
	data3=res1.json()
	city=data3["city"]

	a1 = "https://api.openweathermap.org/data/2.5/weather?"
	a2 = "q=" + city
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	a4 = "&units=" + "metric"	
	wa2=a1+a2+a3+a4
	res2=requests.get(wa2)
	data4=res2.json()
	temp=data4["main"]["temp"]

except Exception as e:
	print("issue", e)
	
btn_add=Button(root,text="Add",font=f,width=15,command=f1)
btn_add.pack(pady=20)
btn_view=Button(root,text="View",font=f,width=15,command=f3)
btn_view.pack(pady=20)
btn_update=Button(root,text="Update",font=f,width=15,command=f6)
btn_update.pack(pady=20)
btn_delete=Button(root,text="Delete",font=f,width=15,command=f8)
btn_delete.pack(pady=20)
btn_charts=Button(root,text="Charts",font=f,width=15,command=f12)
btn_charts.pack(pady=20)

lab_location=Label(root,text="Location:"+ city,font=f,bg="pale green")
lab_location.place(x=50,y=600)

lab_temp=Label(root,text="Temp:"+ str(temp),font=f,bg="pale green")
lab_temp.place(x=600,y=600)

aw=Toplevel(root)
aw.title("Add Employee")
aw.geometry("900x700+50+50")
aw.configure(bg="light sky blue")

aw_lab_id=Label(aw,text="Enter id",font=f,bg="light sky blue")
aw_ent_id=Entry(aw,font=f,bd=2)
aw_lab_name=Label(aw,text="Enter name",font=f,bg="light sky blue")
aw_ent_name=Entry(aw,font=f,bd=2)
aw_lab_salary=Label(aw,text="Enter salary",font=f,bg="light sky blue")
aw_ent_salary=Entry(aw,font=f,bd=2)
aw_btn_save=Button(aw,text="Save",font=f,command=f5)
aw_btn_back=Button(aw,text="Back",font=f,command=f2)
aw_lab_id.pack(pady=10)
aw_ent_id.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lab_salary.pack(pady=10)
aw_ent_salary.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)

aw.withdraw()

f2=("Simsun", 25, "bold")
vw=Toplevel(root)
vw.title("View Employee")
vw.geometry("900x700+50+50")
vw.configure(bg="light yellow")
vw_st_data=ScrolledText(vw,width=40,height=15,font=f2,bg="light yellow")
vw_btn_back=Button(vw,text="Back",font=f,command=f4)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()

uw=Toplevel(root)
uw.title("Update Employee")
uw.geometry("900x700+50+50")
uw.configure(bg="light salmon")
uw_lab_id=Label(uw,text="Enter id",font=f,bg="light salmon")
uw_ent_id=Entry(uw,font=f,bd=2)
uw_lab_name=Label(uw,text="Enter name",font=f,bg="light salmon")
uw_ent_name=Entry(uw,font=f,bd=2)
uw_lab_salary=Label(uw,text="Enter salary",font=f,bg="light salmon")
uw_ent_salary=Entry(uw,font=f,bd=2)
uw_btn_save=Button(uw,text="Save",font=f,command=f10)
uw_btn_back=Button(uw,text="Back",font=f,command=f7)
uw_lab_id.pack(pady=10)
uw_ent_id.pack(pady=10)
uw_lab_name.pack(pady=10)
uw_ent_name.pack(pady=10)
uw_lab_salary.pack(pady=10)
uw_ent_salary.pack(pady=10)
uw_btn_save.pack(pady=10)
uw_btn_back.pack(pady=10)

uw.withdraw()

dw=Toplevel(root)
dw.title("Delete Employee")
dw.geometry("900x700+50+50")
dw.configure(bg="light cyan")
dw_lab_id=Label(dw,text="Enter id",font=f,bg="light cyan")
dw_ent_id=Entry(dw,font=f,bd=2)
dw_lab_id.pack(pady=10)
dw_ent_id.pack(pady=10)
dw_btn_save=Button(dw,text="Save",font=f,command=f11)
dw_btn_back=Button(dw,text="Back",font=f,command=f9)
dw_btn_save.pack(pady=10)
dw_btn_back.pack(pady=10)

dw.withdraw()

def f13():
	answer=askyesno(title='Confirmation',message='Are you sure you want to exit?')
	if answer:
		root.destroy()
root.protocol("WM_DELETE_WINDOW", f13)
root.mainloop()