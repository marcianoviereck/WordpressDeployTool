WordpressDeployTool
===================

A Python tool to make deployment of wordpress sites easier

This tool can be used for free and can also be improved.

Some improvements that I can think of:

* Make the database migration better/easier
* Make the tool start up by user, instead of through command line/IDE

**How to use :**

1. Have a wordpress site/project somewhere locally.
2. Download/Export the database which belongs to the wordpress site/project (.sql file).
3. Start up tool through IDE/command line 'python main.py'
4. Fill in the information and don't use a trailing '/' at the 'old(current) wordpress site URL'
5. Don't use a trailing '/' at the new wordpress site URL
6. Press 'Deploy!' and wait