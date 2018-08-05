import csv
import os.path
import datetime
from datetime import timedelta

start = datetime.datetime.now()
#logs start time
BaseDir = r"N:\EDP\1000668775\TSD-198-19608\Aegis Drive\D\TAK013"
#Enter the base directory (a.k.a. the folders before the OPT file's relative path entries.
#print(BaseDir)
#Enable above to show the base directory on the screen
OutputDir = r"N:\EDP\1000668775\TSD-198-19608\LUCA Reports\\"
#Enter the output directory for the reports [use r"<enter fullpath to output directory>"]  If the output directory is the same as the base directory use: OutputDir = BaseDir 
Opticon = r"\TAK013_Edited.OPT"
#Enter the Opticon filename above.  If using backslashes preceed with r"\<opticon file>"  i.e.  Opticon = r"\TAK013_Edited.OPT"
OPTfile = BaseDir + Opticon
#print(OPTfile)
#Enable above to show fullpath of OPT file on the screen
missingfiles = 0
with open(OPTfile) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', fieldnames=['PageID', 'Volume', 'Filename', 'DocMarker', 'Box', 'Folder', 'PageCount'])
    for row in reader:
        imagefile = BaseDir  + row['Filename']
        #print(row)
        #Enable above to show current line of OPT file on the screen
        print(imagefile)
        #Enable above to show current full filepath of the image file on the screen
        #print(os.path.isfile(imagefile))
        #Enable above to show True/False of the file validater  on the screen [True if found...False if missing]
        if os.path.isfile(imagefile) == False:
            missingfiles = missingfiles + 1
            MissingFilesReport = OutputDir + row['Volume'] + '_MissingFilesReport.txt'
            missing = open(MissingFilesReport, 'a+')
            missing.writelines(row['Filename'] + '\n')
            missing.close()
        if os.path.isfile(imagefile) == True:
            ValidatedFilesReport = OutputDir + row['Volume'] + '_ValidatedFilesReport.txt'
            validated = open(ValidatedFilesReport, 'a+')
            validated.writelines(row['Filename'] + '\n')
            validated.close()
end = datetime.datetime.now()
#logs end time
time_difference = end - start
#calculates elapsed time
time_difference_in_minutes = time_difference / timedelta(minutes=1)
#converts elapsed time into minutes
print('Start time: ', start)
print('End time: ', end)
print('Elapsed time: ', time_difference_in_minutes)
print(Opticon + ' contains ' + str(missingfiles) + ' missing files.')
