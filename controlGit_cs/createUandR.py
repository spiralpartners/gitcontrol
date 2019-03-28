from pyvirtualdisplay import Display
from selenium import webdriver
import time
import pandas as pd
import math
import sys

#Check whether browser control is succeeded or not
def isSucceed(start, end):
    if start == end:
        return False
    else:
        return True

#Sign in
def signIn(user="root", password="r00t"):
    driver.get(giturl+'signout')
    driver.get(giturl+"signin?redirect=%2F")
    stitle = driver.title
    print(stitle,flush=True)
    entry = driver.find_element_by_id("userName")
    entry.send_keys(user)
    entry = driver.find_element_by_id("password")
    entry.send_keys(password)
    btn = driver.find_element_by_class_name('btn-success')
    btn.click()
    #driver.implicitly_wait(0.5)
    time.sleep(1)
    if isSucceed(stitle,driver.title) == False:
        sys.exit()
    print(user+" signIn:"+str(isSucceed(stitle,driver.title)),flush=True)

#Create repository (requires signIn)
def createRepo(reponame, isPublic=False):
    driver.get(giturl+'new')
    repotitle = driver.title
    print(repotitle,flush=True)
    entRepo = driver.find_element_by_id("name")
    entRepo.send_keys(reponame)

    if isPublic==True:
        #public
        entRepoRadio = driver.find_element_by_xpath('//*[@id="form"]/fieldset[3]/label[1]/input')
    else:
        #private
        entRepoRadio = driver.find_element_by_xpath('//*[@id="form"]/fieldset[3]/label[2]/input')
    entRepoRadio.click()
    entRepoBtn = driver.find_element_by_xpath('//*[@id="form"]/fieldset[5]/input')
    entRepoBtn.click()
    time.sleep(1)
    print(isSucceed(repotitle,driver.title),flush=True)

#Create user (requires signIn(root,root))
def createUser(name,password,fullName,mail):
    driver.get(giturl + 'admin/users/_newuser')
    ctitle = driver.title
    print(ctitle,flush=True)
    entry = driver.find_element_by_id("userName")
    entry.send_keys(name)
    entry = driver.find_element_by_id("password")
    entry.send_keys(password)
    entry = driver.find_element_by_id("fullName")
    entry.send_keys(fullName)
    entry = driver.find_element_by_id("mailAddress")
    entry.send_keys(mail)
    driver.find_element_by_xpath('//*[@id="userType_Normal"]').click()
    driver.find_element_by_xpath('/html/body/div/div[2]/div/form/fieldset/input').click()
    time.sleep(1)
    print(isSucceed(ctitle,driver.title),flush=True)

def createUsers(csv):
    signIn()
    df = pd.read_csv(csv)
    for i,row in df.iterrows():
        print(i)
        createUser(row['username'],row['password'],row['fullname'],row['mail'])


#add Collaborator (requires signIn(root,root) or signIn(name,pass))
def addCollaborator(name,repo,collaborator):
    driver.get(giturl + str(name) + '/' + str(repo) + '/settings/collaborators')
    atitle = driver.title
    print(atitle,flush=True)
    entry = driver.find_element_by_id("userName-collaborator")
    entry.send_keys(collaborator)
    driver.find_element_by_id("addCollaborator").click()
    driver.find_element_by_xpath('//*[@id="form"]/div[3]/input[2]').click() #apply Changes
    time.sleep(0.5)

#setup repository(createRepo and addCollaborator)
#deprecate
def setupRepo(username,password,reponame,repoIsPublic,collaborator):
    signIn(username,password)
    createRepo(reponame,repoIsPublic)
    addCollaborator(username,reponame,collaborator)

#setup multiple repositories by file
#if index is specified, signIn process is executed after index.
def setupReposByFile(csv,index=0):
    df = pd.read_csv(csv)
    for i,row in df.iterrows():
        if i < index:
            continue
        print(i,flush=True)
        signIn(row['username'],row['password'])
        createRepo(row['reponame'],row['repoIsPublic'])
        for j in range(1,7):
            collabo = row['collaborator'+str(j)]
            if collabo is not None:
                if isinstance(collabo,float) == True and math.isnan(collabo) == False:
                    collabo = int(collabo)
                    print(collabo)
                elif isinstance(collabo,float) == True and math.isnan(collabo) == True:
                    break

                print(row['username'],row['reponame'],collabo)
                addCollaborator(row['username'],row['reponame'],collabo)

giturl='http://gitbucket/'
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Firefox()

def main(args):

    createUsers('makeUsers.csv')
    
    #If signIn is terminated, add index value as argv(ex. python createUandR.py 5)
    if len(args) == 1:
        index = 0
    elif len(args) == 2:
        index = int(args[1])
    setupReposByFile('makeRepos.csv',index)

    #df = pd.read_csv('makeRepos.csv')
    #for i,row in df.iterrows():
        #print(i,flush=True)
        #if len(args) == 1 or i >= int(args[1]):
            #signIn(row['username'],row['password'])

    driver.close()
    display.stop()

if __name__ == '__main__':
    main(sys.argv)
