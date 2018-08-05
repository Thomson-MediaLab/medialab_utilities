import csv
import os.path
import datetime
from datetime import timedelta

batch_List = r"N:\EDP\1000668775\TSD-198-19608\LUCA Reports\batch_List.csv"
with open(batch_List) as batch_csvfile:
	batch_start = datetime.datetime.now()
	batch_totalfilecount = 0
	batch_missingfiles = 0
	OPTfile_count = 0
	batch_OutputDir = r"N:\EDP\1000668775\TSD-198-19608\LUCA Reports\\"
	batch_BaseDir = r"N:\EDP\1000668775\TSD-198-19608\Aegis Drive\D\\"
	batch_Report_file = batch_OutputDir +  '_Batch_Report.csv'
	batch_Report = open(batch_Report_file, 'a+')
	batch_Report.writelines('Count, OPT Filename, Base Directory, Total File Count, Missing File Count, Report Start, Report End, Elapsed Time (Minutes), Missing Files Report')
	batch_Report.writelines('\n')
	batch_Report.close()
	batch_reader = csv.DictReader(batch_csvfile, delimiter=',', fieldnames=['OPTfile', 'OPTname', 'BaseDir'])
	for file in batch_reader:
		start = datetime.datetime.now()
		#logs start time of current OPT file
		#print('\n', file)
		OPTfile = file['OPTfile']
		#print(OPTfile)
		#Enable above to show fullpath of OPT file on the screen
		Opticon = file['OPTname']
		print(Opticon)
		#Enable above to show the current OPT file on the screen
		BaseDir = file['BaseDir']
		print(BaseDir)
		#Enable above to show the base directory on the screen
		totalfilecount = 0
		#resets totalfilecount per OPT file
		missingfiles = 0
		#resets missingfiles per OPT file
		OPTfile_count = OPTfile_count + 1
		#counts each OPT file
		with open(OPTfile) as csvfile:
			reader = csv.DictReader(csvfile, delimiter=',', fieldnames=['PageID', 'Volume', 'Filename', 'DocMarker', 'Box', 'Folder', 'PageCount'])
			for row in reader:
				totalfilecount = totalfilecount + 1
				imagefile = BaseDir  + row['Filename']
				#print(row)
				#Enable above to show current line of OPT file on the screen
				#print(imagefile)
				#Enable above to show current full filepath of the image file on the screen
				if os.path.isfile(imagefile) == False:
					missingfiles = missingfiles + 1
					MissingFilesReport = batch_OutputDir + Opticon + '_MissingFilesReport.csv'
					missing = open(MissingFilesReport, 'a+')
					missing.writelines(row['PageID'] + ',' + row['Filename'] + '\n')
					missing.close()
					Batch_MissingFilesReport = batch_OutputDir +  '__BatchMissingFilesReport.csv'
					batch_missing = open(Batch_MissingFilesReport, 'a+')
					batch_missing.writelines(Opticon + ', ' + row['PageID'] + ', ' + row['Filename'] + '\n')
					batch_missing.close()
		#Starts the individual OPT file summary
		end = datetime.datetime.now()
		#logs end time
		time_difference = end - start
		#calculates elapsed time
		time_difference_in_minutes = time_difference / timedelta(minutes=1)
		#converts elapsed time into minutes
		print('Start time: ', start)
		print('End time: ', end)
		print('Elapsed time: ', round(time_difference_in_minutes, 2))
		print(Opticon + ' contains ' + str(missingfiles) + ' missing files.' '\n')
		batch_missingfiles = batch_missingfiles + missingfiles
		#Adds missingfile count to the batch tally
		batch_totalfilecount = batch_totalfilecount + totalfilecount
		#Add totalfile count to the batch tally
		batch_Report = open(batch_Report_file, 'a')
		batch_Report.writelines(str(OPTfile_count)  + ', ' + Opticon + ', ' + BaseDir + ', ' + str(totalfilecount) + ', '  + str(missingfiles) + ', ' + str(start)  + ', ' + str(end) + ',' + str(round(time_difference_in_minutes, 2))  + ', '  + MissingFilesReport +  '\n')
		batch_Report.close()
batch_end = datetime.datetime.now()
batch_time_difference = batch_end - batch_start
batch_time_difference_in_minutes = batch_time_difference / timedelta(minutes=1)
print('\n')
print('Batch start time: ', batch_start)
print('Batch end time: ', batch_end)
print('Batch elapsed time: ', str(round(batch_time_difference_in_minutes, 2)))
print('Batch contains ' + str(OPTfile_count) + ' with ' + str(batch_totalfilecount) + ' files and ' + str(batch_missingfiles) + '  missing files')
