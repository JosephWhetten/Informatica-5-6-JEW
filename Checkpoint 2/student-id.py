def main():
	print('')
	print('Please enter the following information to create your ID Card.')
	input('Press enter to continue.')
	ask_student_info()
	display_student_info()
	
    
def ask_student_info():
	fname = input("First name = ").strip().title()
	lname = input("Last name = ").strip().upper()
	email = input("Email Address = ").strip()
	phone = input("Phone number = ")
	id = input("Student ID Number = ").strip()
	fpt = input("FPT Class = ").strip().title()
	grad = input("Expected Graduation Year = ").strip()
	fav = input("Favorite subject = ").strip().title()
	extra = input("Extracurricular Activites (Yes or No) = ").strip().title()
	yearleft = (int(grad) - 2025)
	
def display_student_info():
	global fname, lname, email, phone, id, fpt, grad, fav, extra, yearleft
	line = "-" * 45
	print(f"Your ID Card is:\n{line}\n{lname},{fname}\nStudent\nID: {id}\n\n{email},\n{phone},\n\nFPT Class: {fpt}\tFavorite Subject: {fav}\nExpected Graduation: {grad}\tYears Left: {yearleft}\n\nExtracurricular Activities: {extra}\n{line}")

main()	