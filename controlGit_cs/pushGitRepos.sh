#!/bin/sh

giturl=gitbucket/git/
csv=makeRepos.csv
#tempRepo dir is pushed as git repository
tempRepo=csprinter

if [ -e $tempRepo/.git ]; then
  rm -rf $tempRepo/.git
fi

cd $tempRepo
git config --global user.name "staff"
git config --global user.email staff@softiv.info
git init
git add -A
git commit -m "1st commit"

username=`sed -n '2p' ../$csv | cut -d , -f 1`
password=`sed -n '2p' ../$csv | cut -d , -f 2`
reponame=`sed -n '2p' ../$csv | cut -d , -f 3`
git remote add origin http://$username:$password@$giturl$username/$reponame.git
git push -u origin master

#The first and second lines are omitted
for line in `tail -n +3 ../$csv`
do
  username=`echo ${line} | cut -d , -f 1`
  password=`echo ${line} | cut -d , -f 2`
  reponame=`echo ${line} | cut -d , -f 3`
  git remote set-url origin http://$username:$password@$giturl$username/$reponame.git
  git push -u origin master
done
