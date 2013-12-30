from Tkconstants import DISABLED, W
from Tkinter import Label, Entry, StringVar, Button

class UIHelper(object):
    def buildEntryFieldsAndLabelsForUI(self, deployerUI):
        deployerUI.newDBLabel = Label(deployerUI.root,text="Please insert your new database name",bg="white").grid(row=0,column=0,sticky=W)
        deployerUI.newDBEntryString = StringVar()
        deployerUI.newDBEntry = Entry(deployerUI.root,textvariable=deployerUI.newDBEntryString).grid(row=0, column=1,sticky=W)

        deployerUI.newUsernameLabel = Label(deployerUI.root,text="Please insert your new database username",bg="white").grid(row=1,column=0,sticky=W)
        deployerUI.newUsernameEntryString = StringVar()
        deployerUI.newUsernameEntry = Entry(deployerUI.root,textvariable=deployerUI.newUsernameEntryString).grid(row=1,column=1)

        deployerUI.newPasswordLabel = Label(deployerUI.root,text="Please insert your new database password",bg="white").grid(row=2,column=0,sticky=W)
        deployerUI.newPasswordEntryString = StringVar()
        deployerUI.newPasswordEntry = Entry(deployerUI.root,show="*",textvariable=deployerUI.newPasswordEntryString).grid(row=2,column=1,sticky=W)

        deployerUI.oldSiteLabel = Label(deployerUI.root,text="Please insert your old(current) wordpress site URL",bg="white").grid(row=3,column=0,sticky=W)
        deployerUI.oldSiteEntryString = StringVar()
        deployerUI.oldSiteEntry = Entry(deployerUI.root,textvariable=deployerUI.oldSiteEntryString).grid(row=3,column=1,sticky=W)

        deployerUI.newSiteLabel = Label(deployerUI.root,text="Please insert your new wordpress site URL",bg="white").grid(row=4, column=0, sticky=W)
        deployerUI.newSiteEntryString = StringVar()
        deployerUI.newSiteEntry = Entry(deployerUI.root,textvariable=deployerUI.newSiteEntryString).grid(row=4, column=1, sticky=W)

    def buildDBAndWordpressDirectoryFields(self, deployerUI):
        deployerUI.wordpressDirectoryLabel = Label(deployerUI.root,text="Please select the wordpress directory to deploy",bg="white").grid(row=5,column=0,sticky=W)

        deployerUI.wordpressEntryString = StringVar()
        deployerUI.wordpressDirectoryEntry = Entry(deployerUI.root,state=DISABLED,textvariable=deployerUI.wordpressEntryString).grid(row=6,column=0)

        deployerUI.wordpressDirectoryBytton = Button(deployerUI.root,text="Select wordpress dir",command=deployerUI.onWordpressDirectorySelected).grid(row=6,column=1,sticky=W)
        deployerUI.dbDirectoryLabel = Label(deployerUI.root,text="Please select databse .sql file",bg="white").grid(row=7,column=0,sticky=W)

        deployerUI.dbEntryString = StringVar()
        deployerUI.dbDirectoryEntry = Entry(deployerUI.root,state=DISABLED,textvariable=deployerUI.dbEntryString).grid(row=8,column=0)

        deployerUI.dbDirectoryBytton = Button(deployerUI.root,text="Select database .sql file",command=deployerUI.onDatabaseFileSelected).grid(row=8,column=1,sticky=W)

    def buildFinishButtons(self, deployerUI):
        deployerUI.deploymentString = StringVar()
        deployerUI.deploymentString.set("Deploy!")

        deployerUI.startDeployment = Button(deployerUI.root,text="Deploy!",command=deployerUI.onDeploymentStarted,textvariable=deployerUI.deploymentString).grid(row=10,column=0)
