import psycopg2
import random
import time
from config import config

def import_to_db(year, conn, cur, test_fall_chance):
	with open("log.txt") as log_file:
		log = log_file.readline()
		if (log == ""):
			cluster_num = 0
		else:
			line = log.split(";")
			if (int(year)<int(line[1])):
				return 1
			else:
				cluster_num = int(line[0])
	duration = float(time.time())
	with open('Odata' + year + 'File.csv') as csvfile:
		csvfile.readline()
		n = 0
		ider = 0
		while (n < cluster_num*50):
			n += 1
			csvfile.readline()
		for line in csvfile:
			arg_lst = []
			line = line.split(";")
			OutID = ("'" + str(line[0].replace('"','')) + "_" + year + "'")
			arg_lst.append(OutID)
			arg_lst.append(line[33].replace('"',"'"))
			arg_lst.append(line[29].replace(',','.'))
			arg_lst.append(line[28].replace('"',"'"))
			arg_lst.append(year)
			cur.execute(command_insert % (", ".join(arg_lst)))
			#f = open("uploaded.txt", "a")
			#f.write(str(n) + (", ".join(arg_lst)) + "\n")
			#f.close()

			n+=1
			if ((n > 0)&((n % 50) == 0)):			
				conn.commit()
				cluster_num+=1
				log_file = open("log.txt", "w")
				log_file.write(str(cluster_num) + ";" + year)
				log_file.close()
			if (random.randint(0, test_fall_chance) == 1):
				print("Потеряно соединение с базой данных")
				conn.close()
		duration = round((float(time.time()) - duration), 4)
		with open('upload_time.txt','a') as upload_time:
			upload_time.write('Data from Odata' + year + 'File.csv uploaded in ' + str(duration) + ' seconds\n')
	return 0	

command_drop = "DROP TABLE hist_results;"
command_create = """
CREATE TABLE public."hist_results"
(
	"OutID" text COLLATE pg_catalog."default" NOT NULL,
    "Region" text COLLATE pg_catalog."default",
    "Score" real,
    "Status" text COLLATE pg_catalog."default",
    "Year" integer NOT NULL,
    CONSTRAINT "Hist_results_pkey" PRIMARY KEY ("OutID")
)
"""

command_select = '''SELECT "Region", min("Score"), "Year" FROM public.hist_results
	WHERE "Status" = 'Зараховано'
	GROUP BY "Region", "Year"
	ORDER BY "Region", "Year";'''

command_insert = "INSERT INTO Hist_results VALUES(%s)"





try:
	f = open("log.txt")
	f.close()
except FileNotFoundError:
	f = open("log.txt","w")
	f.close()


years = ['2019', '2020']

test_fall = input("Желеете протестировать сценарий 'падения' базы данных? (y/n)")
if (test_fall == "y"):
	test_fall_chance = int(input("Пожалуйста введите n (вероятность падения базы данных после анализа строчки - 1/n): "))
else:
	test_fall_chance = 0
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()
cur.execute("select exists(select * from information_schema.tables where table_name='hist_results')")
if (cur.fetchone()[0]):
	drop = input("Желеете удалить базу данных? (y/n)")
	if (drop == "y"):
		cur.execute(command_drop)
cur.execute("select exists(select * from information_schema.tables where table_name='hist_results')")
if (not (cur.fetchone()[0])):
	cur.execute(command_create)
for year in years:
	import_to_db(year, conn, cur, test_fall_chance)

clear = open("log.txt","w")
clear.write("")
clear.close()

select_list = []
cur.execute(command_select)
result = cur.fetchone()
select_list.append(list(result)[:2])
while (result != None):
	result = cur.fetchone()
	if (result != None):		
		if (result[0] == select_list[-1][0]):
			(select_list[-1]).append(result[1])
		else:
			select_list.append(list(result)[:2])

cur.close()
conn.commit()
conn.close()
csv_data = [";".join([str(y) for y in x]) for x in select_list]

with open("Result.csv", "w") as result_f:
	result_f.write("Регіон;Найнижчий бал в 2019;Найнижчий бал в 2020")
	for item in csv_data:
		result_f.write("\n")
		result_f.write(item)
