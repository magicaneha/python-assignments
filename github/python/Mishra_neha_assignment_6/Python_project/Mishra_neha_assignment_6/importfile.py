import csv
import datetime



################Creating csv file of addressbook at current time ################################
def currentTimeString():
	time = datetime.datetime.now()
	currentTimeStr = str(time.date()) + "_" + str(time.hour) + "_" + str(time.minute) + "_" + str(time.second)
	return currentTimeStr

def createBasicCSV(dataList = (), header=('first_nm', 'last_nm', 'address1', 'address2', 'city', 'state', 'zip', 'phone')):
	fileName = currentTimeString() + '.csv'
	print fileName

	try:
		with open(fileName, 'w') as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow(header)
			for row in dataList:
				wr.writerow(row)
			myfile.close()
	except:
		print "error in making csv"
		return None
	return fileName
