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
