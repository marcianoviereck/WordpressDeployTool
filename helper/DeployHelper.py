import datetime
import shutil
import os
import re
from shutil import ignore_patterns
import tkMessageBox

class DeployHelper(object):

    currentWordpressDirectory = ""
    deploymentSubdirectory = "Deployment" + os.sep
    databaseSubdirectory = "Database" + os.sep
    #os.path.join()
    newWordpressDirectory = ""
    
    #user values
    databaseName = ""
    databaseUser = ""
    databasePassword = ""
    
    #database values
    databaseFile = ""
    databaseFileName = ""
    newAbsoluteDatabaseDirectory = ""
    
    #site urls
    oldSiteUrl = ""
    newSiteUrl = ""
    
    def createDatabaseDirectoryAndCopyDBFile(self):
        newDatabaseDirectory = self.newWordpressDirectory + self.databaseSubdirectory
        os.mkdir(newDatabaseDirectory)
        self.newAbsoluteDatabaseDirectory = newDatabaseDirectory
    
    def copyOldDirectoryToNewDirectory(self):
        shutil.copytree(self.currentWordpressDirectory, self.newWordpressDirectory, False, ignore=ignore_patterns('Deployment*'))

    def initializeDeploymentDirectory(self):
        if not self.currentWordpressDirectory.endswith(os.sep):
            self.currentWordpressDirectory += os.sep

        self.newWordpressDirectory = self.currentWordpressDirectory + self.deploymentSubdirectory + self.getDateTimeString() + os.sep
        
    def getDateTimeString(self):
        dateTimeString = str(datetime.datetime.now())
        
        dateTimeString = re.sub(r"(\s+)","",dateTimeString)
        dateTimeString = re.sub(r"\:","_",dateTimeString)
    
        if "." in dateTimeString:
            dateTimeString = re.split(r"\.", dateTimeString)[0]
    
        return dateTimeString
    
    def writeCredentialToFile(self, credential, currentLine, output_file):
        lineSegments = re.split(",", currentLine)
        toInsertLine = re.sub(r"(\'(\w+)\')|(\'\')",
                                "'"+credential+"'",
                                str(lineSegments[1]))
        output_file.write(str(lineSegments[0])+","+toInsertLine)
                
    def insertUserCredentialsAndMoveWPConfig(self):
        wpConfig = open(self.newWordpressDirectory + "wp-config.php",'r+')
        temporaryWpConfig = open("wp-config-temp.php",'w')
        
        for line in wpConfig:
            if re.search(r"DB_NAME", line):
                self.writeCredentialToFile(self.databaseName, line, temporaryWpConfig)
       
            elif re.search(r"DB_USER",line):
                self.writeCredentialToFile(self.databaseUser, line, temporaryWpConfig)
                
            elif re.search(r"DB_PASSWORD",line):
                self.writeCredentialToFile(self.databasePassword, line, temporaryWpConfig)
            else:
                temporaryWpConfig.write(line)
    
        wpConfig.close()
        temporaryWpConfig.close()
        
        shutil.copyfile("wp-config-temp.php", 
                        self.newWordpressDirectory + "wp-config.php")
        os.remove("wp-config-temp.php")
        
        print "done writing and stuff"
        
    def modifyDatabaseFile(self):
        databaseFile = open(self.databaseFile.name,'r')
        temporaryDatabaseFile = open("database-temp.sql",'w')
        
        for line in databaseFile:
            if self.oldSiteUrl in line:
                lineToWrite = re.sub(self.oldSiteUrl, self.newSiteUrl, line)
                temporaryDatabaseFile.write(lineToWrite)
            else:
                temporaryDatabaseFile.write(line)
        
        databaseFile.close()
        temporaryDatabaseFile.close()
        
        shutil.copyfile("database-temp.sql", 
                       self.newAbsoluteDatabaseDirectory+"database_file.sql")
        
        os.remove("database-temp.sql")

    def startDeployment(self):
        self.initializeDeploymentDirectory()
        
        self.copyOldDirectoryToNewDirectory()

        self.createDatabaseDirectoryAndCopyDBFile()
        self.modifyDatabaseFile()
        self.insertUserCredentialsAndMoveWPConfig()
        
        tkMessageBox.showinfo("Deployment complete!", "The deployment has completed!")
        
        
    def setValuesWithUIBuilderSource(self, UIBuilder):
        self.databaseName = UIBuilder.newDBEntryString.get()
        self.databaseUser = UIBuilder.newUsernameEntryString.get()
        self.databasePassword = UIBuilder.newPasswordEntryString.get()
        
        self.oldSiteUrl = UIBuilder.oldSiteEntryString.get()
        self.newSiteUrl = UIBuilder.newSiteEntryString.get()
        
        self.databaseFile = UIBuilder.databaseFile
        self.currentWordpressDirectory = UIBuilder.wordpressEntryString.get()
