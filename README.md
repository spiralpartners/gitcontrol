*必要なもの
- CSVファイル
-- makeUsers.csv, makeRepos.csv
- リポジトリに含めたいファイル群を1つのディレクトリにまとめたもの
-- そのディレクトリ以下のファイル・ディレクトリがリポジトリとして登録される
- createUandR.py
-- サーバ側のユーザ登録及びリポジトリ登録
- pushGitRepos.sh
-- クライアント側でのリポジトリ作成及びサーバへの登録

*CSV
- makeUsers.csv
-- 作成するユーザアカウントの情報(ユーザ名，パス，フルネーム，メアド）
- makeRepos.csv
-- 作成するリポジトリの情報（ユーザ名，パス，リポジトリ名，public/private(True/False),collaborator)

*手順
- root/rootでgitbucketにログインし，rootパスをr00tに変更する
- 2つのcsvファイルを作成する
- Gitホスティングサーバ(Gitbucket)側の設定
--python createUandR.pyを実行する
--- L98のgiturlを確認する(GitBucketの初期URL）(http://gitbucket/でアクセスできるなら変更不要）
--- L103あたりのcreateUsers('makeUsers.csv')のコメントアウトを外す
--- リポジトリ作成時にアカウントでのログインが失敗することがある．その場合は失敗したindexを引数にして実行すると，続きから実施される
---- ex.「python createUandR.py 11」とするとindex11からスタートする
- Gitリポジトリ（クライアント側）の設定（配布用のファイルを学生リポジトリに登録する）
-- sh pushGitRepos.sh を実行する
--- makeRepos.csvの内容にもとづいてリポジトリの作成・サーバへの登録(push)を行う
--- L3のgiturlを確認する(http://を除いたGitBucketの初期URLに"git/"を付加したもの(リポジトリのベースURLはこのURLにユーザ名とリポジトリ名を付加したものになる））．これもhttp://gitbucket/でアクセスできるなら変更不要
--- L4のcsvファイルのファイル名を確認する
--- L6のtempRepoに指定するディレクトリ名を確認する．
---- shファイルがある場所にリポジトリとしてpushしたいファイルを含むディレクトリを置き，そのディレクトリ名をtempRepoに代入しておく


**トラブル
- ベーシック認証回避がうまくいかなかったので，現状は特定のアクセス元（IP）からのアクセスには認証をかけないことで対応
- *.gitに対しても回避設定が必要な気がするが，なくてもうまいこといってしまったのでとりあえず保留中

<Location "/">
    Satisfy Any

    AuthType Basic
    AuthName "Cloud Spiral 2017"
    AuthUserFile "/var/www/cs2016.htpasswd"
    Require user staff 2016901

    Order deny,allow
    Deny from all
    Allow from 133.1.236.160/32

</Location>
<LocationMatch /.+\.git$>
    Order allow,deny
    Allow from all
    Satisfy Any
</LocationMatch>


docker exec -it selenium bash
コンテナ内に入ったあと，下記を実行することで，python-selenium binding環境が整う
pip install --upgrade pip
pip install -U selenium pyvirtualdisplay

controlGitのために以下が必要
pip install pandas

python2系に変更する可能性がある場合
/etc/profile.d/enablepython35.sh を削除し，下記を実行すればOK
source /opt/rh/python27/enable

その後3系にする場合はrh-python35/enable をsourceすれば良い

--------
gitbucketのアカウント生成をshでゴリ押す方法

# ログインしてセッションを確保
session=$(curl -v http://$server/gitbucket/signin -X POST \
  --data "userName=$user&password=$pass" 2>&1 \
  | grep Set-Cookie --color=none \
  | perl -pe 's/^.*?(JSESSIONID.*?);.*/$1/')

# アカウント情報
u=test05
p=test05

# アカウント生成
curl -v http://$server/gitbucket/admin/users/_newuser -X POST  \
  -H "Cookie: $session" \
  --data "userName=$u&password=$p&fullName=$u&mailAddress=$u&isAdmin=false&url=&description=&fileId="

ーーーーーーーーーーー
scl enable python27 bash
scl enable rh-python35 bash


----
pip install --upgrade pip
pip install -U selenium pyvirtualdisplay
wget https://github.com/mozilla/geckodriver/releases/download/v0.15.0/geckodriver-v0.15.0-linux64.tar.gz
tar zxvf
mv /usr/local/bin

pip install wheel
pip install pandas

-----
git client側

ファイル群用意
git config --global user.name "staff"
git config --global user.email staff@softiv.info

git init
git add -A
git commit -m "1st commit"
git remote add origin http://2017001:2017001@133.1.236.160:20080/gitbucket/git/2017001/cspiral.git
git push -u origin master

git remote set-url origin http://2017002:2017002@133.1.236.160:20080/gitbucket/git/2017002/cspiral.git
git push -u origin master
繰り返し・・・