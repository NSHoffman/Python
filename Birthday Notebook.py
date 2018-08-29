import re
import datetime
import time

# НА ЭКРАН ВЫВОДЯТСЯ СТАРТОВЫЕ ИНСТРУКЦИИ

print('''This is the birthday notes editor!

 * Type NEW to add new note.
 * Type REMOVE to remove the exsisting note.
 * Type EDIT to edit the exsisting note.
 * Type NEXT to find out the nearest birthday.
 * Type AGE to find out an age of a certain person.
 * Type DATE to find out whether there is a person with a certain day/month/year of birth.
 * Type SHOW to see the exsisting notes.
 * Type EXIT to exit.
 ''')

# ОБЪЯВЛЕНИЕ ОСНОВНЫХ ФУНКЦИЙ

# ЗАПУСК МЕНЮ ВЫБОРА ФУНКЦИЙ
def Start():

	answerCorrect = False

	while not answerCorrect:
		answer = str(input('ACTION >> ')).upper()
		if answer in listAnswers.keys():
			for i,k in listAnswers.items():
				if answer == i:
					Confirm = False
					while not Confirm:
						AcceptConfirm = str(input('Are you sure? Y/N >> ')).lower()
						if AcceptConfirm == 'y':
							Confirm = True
							answerCorrect = True
							k()
						elif AcceptConfirm == 'n':
							Confirm = True
						else:
							print('Please answer "Y" for "Yes" / "N" for "No"!')
		else:
			print('Incorrect option! Use only key-bindings shown in the MENU.')

# СОЗДАНИЕ И ДОБАВЛЕНИЕ НОВОЙ ЗАПИСИ
def NewNote():

	CorrectName = False

	while not CorrectName:
		newName = str(input('Enter New Name >> '))
		if bool(namePattern.search(newName)) and ':' not in newName:
			if True not in [newName.lower() in i.lower().split(' : ') for i in birthdays]:
				CorrectName = True
			else:
				print('Such name already exists! Try using specific identification.')
		else:
				print('Invalid Name. Use only latin/cyrillic letters!')

	CorrectDate = False

	while not CorrectDate:
		newDate = str(input('Enter the Date of Birth (DD.MM.YYYY) >> '))
		if bool(datePattern.search(newDate)):
			try:
				NewDay = int(newDate.split('.')[0])
				NewMonth = int(newDate.split('.')[1])
				NewYear = int(newDate.split('.')[2])
				if NewDay <= 31 and NewMonth <= 12 and datetime.date(NewYear, NewMonth, NewDay) <= datetime.date.today():
					CorrectDate = True
			except ValueError:
				print('Invalid date type. Use DD.MM.YYYY format!')
		else:
			print('Invalid date type. Use DD.MM.YYYY format!')
	
	birthdays.append('{} : {}\n'.format(newName, newDate))
	with open('birthdays.txt', 'w') as update:
		for note in birthdays:
			update.write(note)
	print('{} has been successfully added with the date "{}"'.format(newName, newDate))
	
	Start()

# УДАЛЕНИЕ СУЩЕСТВУЮЩЕЙ ЗАПИСИ
def RemoveNote():

	ToDel = str(input('Enter the Name of a person you want to delete >> '))
	NoteRemoved = False

	for note in birthdays:
		if ToDel.strip().lower() == note.split(':')[0].strip().lower() and NoteRemoved == False:
			birthdays.remove(note)
			print('The note has been successfully removed!')
			with open('birthdays.txt', 'w') as update:
				for note in birthdays:
					update.write(note)
			NoteRemoved = True

	if not NoteRemoved:
		print('No name {} has been found! Check the spelling and try one more time.'.format(ToDel))		
	
	Start()

# ИЗМЕНЕНИЕ СУЩЕСТВУЮЩЕЙ ЗАПИСИ
def EditNote():

	Aim = str(input('Enter the name of the person whose data you want to change >> '))

	# ИЗМЕНЕНИЕ ИМЕНИ
	def EditName():

		CorrectName = False

		while not CorrectName:
			newName = str(input('Enter New Name >> '))
			if bool(namePattern.search(newName)) and ':' not in newName:
					CorrectName = True
			else:
					print('Invalid Name. Use only latin/cyrillic letters!')
		return newName

	# ИЗМЕНЕНИЕ ДАТЫ
	def EditDate():

		CorrectDate = False

		while not CorrectDate:
			newDate = str(input('Enter the Date of Birth (DD.MM.YYYY) >> '))
			if bool(datePattern.search(newDate)):
				try:
					NewDay = int(newDate.split('.')[0])
					NewMonth = int(newDate.split('.')[1])
					NewYear = int(newDate.split('.')[2])
					if NewDay <= 31 and NewMonth <= 12 and datetime.date(NewYear, NewMonth, NewDay) <= datetime.date.today():
						CorrectDate = True
				except ValueError:
					print('Invalid date type. Use DD.MM.YYYY format!')
			else:
				print('Invalid date type. Use DD.MM.YYYY format!')
			return newDate

	# НЕПОСРЕДСТВЕННОЕ ИЗМЕНЕНИЕ ЗАПИСИ В ЗАВИСИМОСТИ ОТ ВЫБОРА ПОЛЬЗОВАТЕЛЯ
	Found = False

	for i in range(len(birthdays)):
		if Aim.lower() == birthdays[i].split(':')[0].strip().lower():
			Found = True
			CorrectAnswer = False
			while not CorrectAnswer:
				DataToChange = str(input('What do you want to change? N/D >> '))
				if DataToChange.upper() == 'N':
					name = EditName()
					birthdays[i] = birthdays[i].replace(Aim, name)
					CorrectAnswer = True
				elif DataToChange.upper() == 'D':
					date = EditDate()
					birthdays[i] = birthdays[i].replace(birthdays[i].split(':')[1].strip(), date)
					CorrectAnswer = True
				else:
					print('Incorrect Answer!')
	
	if Found == False:
		print('{} not found.'.format(Aim))
		Start()
	
	with open('birthdays.txt', 'w') as update:
		for note in birthdays:
			update.write(note)
	
	Start() # ВОЗВРАТ К НАЧАЛУ


# ПОИСК БЛИЖАЙШЕГО ДНЯ РОЖДЕНИЯ
def FindNearest():
	
	DateHolder = []
	Deltas = []
	
	for i in birthdays:
		unitDate = i.split(':')[1].strip()
		Month = int(unitDate.split('.')[1])
		Day = int(unitDate.split('.')[0])
		if (datetime.date.today().month >= Month and datetime.date.today().day > Day) or (datetime.date.today().month > Month):
			DateHolder.append(datetime.date(datetime.date.today().year + 1, Month, Day))
		else:
			DateHolder.append(datetime.date(datetime.date.today().year, Month, Day))
	
	for i in DateHolder:
		Deltas.append(i - datetime.date.today())
	print('{} has the nearest birthday. Date of Birth : {}.'.format(birthdays[Deltas.index(min(Deltas))].split(':')[0].strip() , birthdays[Deltas.index(min(Deltas))].split(':')[1].strip()))
	
	Start()
	
# ВЫЧИСЛЕНИЕ ВОЗРАСТА
def CalcAge():
	
	BirthName = str(input('Enter the name of person whose age you want to calculate >> '))
	
	for i in birthdays:
		if BirthName.lower() == i.split(':')[0].strip().lower():
			print("{} is {} years old.".format(BirthName, int((datetime.date.today() - datetime.date(int(i.split(':')[1].strip().split('.')[2]), int(i.split(':')[1].strip().split('.')[1]), int(i.split(':')[1].strip().split('.')[0]))).days/365)))
			Start()
	print('Wrong name! Try again.')
	
	Start()

# ПОИСК ПО ДАТЕ
def FindDate():

	# ПОИСК ПО ДНЯМ (ИЗ 366)
	def search_day():

		counter = 0
		DayCorrect = False

		while not DayCorrect:
			try:
				day = int(input('Enter the day out of 366 (DDD) >> '))
				if day > 0 and day <= 366:
					DayCorrect = True
				else:
					print('Day number cannot be larger than 366!')
			except ValueError:
				print('Please enter a numeric value!')

		for data in birthdays:
			if time.strptime(data.split(':')[1].strip(), '%d.%m.%Y').tm_yday == day:
				print('{} was born that day!'.format(data.split(':')[0].strip()))
			else:
				counter += 1

		if counter == len(birthdays):
			print('There are no people born that day.')
		Start()

	# ПОИСК ПО МЕСЯЦУ
	def search_month():

		counter = 0
		MonthCorrect = False

		while not MonthCorrect:
			try:
				month = int(input('Enter the month out of 12 (MM) >> '))
				if month > 0 and month <= 12:
					MonthCorrect = True
				else:
					print('Month number cannot be larger than 12!')
			except ValueError:
				print('Please enter a numeric value!')

		for data in birthdays:
			if int(data.split(':')[1].strip().split('.')[1]) == month:
				print('{} was born that month!'.format(data.split(':')[0].strip()))
			else:
				counter += 1

		if counter == len(birthdays):
			print('There are no people born that month.')
		Start()

	# ПОИСК ПО ГОДУ
	def search_year():

		counter = 0
		YearCorrect = False

		while not YearCorrect:
			try:
				year = int(input('Enter the year (YYYY) >> '))
				if year > 0 and year <= datetime.date.today().year:
					YearCorrect = True
				else:
					print('The year cannot be larger than it is right now!')
			except ValueError:
				print('Please enter a numeric value!')

		for data in birthdays:
			if int(data.split(':')[1].strip().split('.')[2]) == year:
				print('{} was born that year!'.format(data.split(':')[0].strip()))
			else:
				counter += 1

		if counter == len(birthdays):
			print('There are no people born that year.')
		Start()

	# СКЛЕЙКА. ПОИСК ПО ВЫБРАННОМУ ПАРАМЕТРУ
	data_to_search = str(input('Search by day/month/year? >> ')).lower()
	if data_to_search == 'day':
		search_day()
	elif data_to_search == 'month':
		search_month()
	elif data_to_search == 'year':
		search_year()
	else:
		print('Incorrect Answer!')
		Start()

# ПОКАЗ ЗАПИСЕЙ
def Show():
	
	print('\n'+'*'*25)
	print('Current Notes:\n')
	with open('birthdays.txt', 'r') as bds:
		for i in bds.readlines():
			print(i, end='')
	print('\n'+'*'*25)
	
	Start()

# ВЫХОД ИЗ ПРОГРАММЫ
def Exit():
	exit()

# ОТКРЫТИЕ ТЕКСТОВОГО ФАЙЛА, ЗАПИСЬ ТЕКСТОВОЙ ИНФОРМАЦИИ ПОСТРОЧНО В СПИСОК BIRTHDAYS
with open('birthdays.txt', 'r') as bds:
	birthdays = bds.readlines()
	for i in birthdays:
		i = i.rstrip()
		i += '\n'

listAnswers = {'NEW':NewNote, 'REMOVE':RemoveNote, 'EDIT':EditNote, 'NEXT':FindNearest, 'AGE':CalcAge, 'DATE':FindDate, 'SHOW':Show, 'EXIT':Exit}	# СЛОВАРЬ, ОБЪЕДИНЯЮЩИЙ КОМАНДЫ И ФУНКЦИИ
datePattern = re.compile(r'\d{2}.\d{2}.\d{4}')	# ПАТТЕРН ДЛЯ ПРОВЕРКИ ПРАВИЛЬНОСТИ ВВЕДЕННОЙ ДАТЫ
namePattern = re.compile(r'[a-zа-я]', flags = re.IGNORECASE)	# ПАТТЕРН ДЛЯ ПРОВЕРКИ ПРАВИЛЬНОСТИ ВВЕДЕННОГО ИМЕНИ

print('\n'+'*'*25)
print('Current Notes:\n')
print(''.join(birthdays))
print('\n'+'*'*25)
Start()
