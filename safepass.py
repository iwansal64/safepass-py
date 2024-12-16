import string, random, pyperclip

run = True
while run:
	user = input("what do you want?")
	if user == "i":
		alias = input("alias? ")
		username = input("username? ")
		password = input("password? ")

		if not username:
			username = "".join([random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 8))])

		if not password:
			password = "".join([random.choice(string.printable) for i in range(random.randint(12, 24))])
		
		with open("safe.txt", "a+") as f:
			f.write(f"{alias}:\n{username}\n{password}\n\n")

		print("Stored!")
	elif user == "g":
		with open("safe.txt", "r+") as f:
			contents = f.read()
			contents = contents.split("\n\n")[:-1]

		print("\n--------------\n".join([str(i)+".\n"+content for i, content in enumerate(contents)]))

		index = input("index?")

		if index == "":
			continue
		
		item = contents[int(index)]
		items = item.split("\n")
		alias = items[0]
		username = items[1]
		password = items[2]
		
		input(username)
		pyperclip.copy(username)
		input(password)
		pyperclip.copy(password)
		input("done?")
		print("aight nice!")
	elif user == "d":
		with open("safe.txt", "r+") as f:
			contents = f.read()
			contents = contents.split("\n\n")

		print("\n-----------------\n".join([str(i)+".\n"+content for i, content in enumerate(contents)]))
		index = input("index?")

		if index == "":
			continue

		del contents[int(index)]
		with open("safe.txt", "w+") as f:
			f.write("\n\n".join(contents))

		print("done!")
	elif user == "b":
		backup_file_name = input("backup file name?")
		with open("safe.txt", "r+") as f:
			with open(backup_file_name, "w+") as b:
				b.write(f.read())
		print("done!")
	else:
		run = False
		print("Have a good day!")
