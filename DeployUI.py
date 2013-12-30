from Tkinter import Tk, mainloop
import sys
import os
import tkFileDialog
from helper.DeployHelper import DeployHelper
from helper.UIHelper import UIHelper

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class DeployUI(object):

    def buildBaseUI(self):
        self.root.title("Wordpress Deployment tool!")
        self.root.configure(background='white')
        self.root.resizable(width=False, height=False)

        self.uiHelper.buildEntryFieldsAndLabelsForUI(self)
        self.uiHelper.buildDBAndWordpressDirectoryFields(self)
        self.uiHelper.buildFinishButtons(self)

        mainloop()
        
    def onWordpressDirectorySelected(self):
        self.wordpressDirectory = tkFileDialog.askdirectory(initialdir='.')
        self.wordpressEntryString.set(self.wordpressDirectory)
    
    def onDatabaseFileSelected(self):
        self.databaseFile = tkFileDialog.askopenfile("r",initialdir='.',filetypes=[('SQL database files', '.sql')])
        self.dbEntryString.set(self.databaseFile.name)
        
    def onDeploymentStarted(self):
        self.transferVariablesToDeployHelper()
        self.deployHelper.startDeployment()

    def __init__(self):
        self.root = Tk()
        self.deployHelper = DeployHelper()
        self.uiHelper = UIHelper()

    def transferVariablesToDeployHelper(self):
        self.deployHelper.setValuesWithUIBuilderSource(self)
        print "transfered values"
