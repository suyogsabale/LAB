def add_apt(apts):
	apt_id = input("Enter apt ID: ")
	name = input("Enter name: ")
	status="waiting"
	apts.append({"Id":apt_id,"Name":name,"Status":status})
	print("apt added")

def view_apt(apts):
	if not apts:
		print("Noapt found")
		return
	else:
		print("Apts are :-")
		for apt in apts:
			print("ID :",apt["Id"])
			print("Name :",apt["Name"])
			print("Status :",apt["Status"])
			print("------------------")

def update_apt(apts):
	apt_id=input("Enter apt id to update :-")
	status=input("enter new status :-")
	for apt in apts:
		if apt["Id"]==apt_id:
			apt["Status"]=status
			print("status updated successfully.")
			return
	print("Ticket not found.")

def del_apt(apts):
	apt_id=input("Enter apt id to delete :-")
	for apt in apts:
		if apt["Id"]==apt_id:
			apts.remove(apt)
			print("status delted successfully.")
			return
	print("Ticket not found.")
			
		


def main():
	apts=[]
	while True:
		print("\n--- Helpdesk Management System ---")
		print("1. Create a appointment")
		print("2. View all aptms=nts")
		print("3. Update aptmnt status")
		print("4. Delete a aptmnt")
		print("5. Exit")
		
		ch = input("Enter your choice (1-5): ")
		if ch == "1":
			add_apt(apts)
		elif ch == "2":
			view_apt(apts)
		elif ch == "3":
			update_apt(apts)
		elif ch == "4":
			del_apt(apts)
		elif ch == "5":
			print("Exiting the program...")
			break
		else:
			print("Invalid choice. Please try again.")




if __name__=="__main__":
	main()