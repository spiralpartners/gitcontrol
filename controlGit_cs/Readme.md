*�K�v�Ȃ���
- CSV�t�@�C��
-- makeUsers.csv, makeRepos.csv
- ���|�W�g���Ɋ܂߂����t�@�C���Q��1�̃f�B���N�g���ɂ܂Ƃ߂�����
-- ���̃f�B���N�g���ȉ��̃t�@�C���E�f�B���N�g�������|�W�g���Ƃ��ēo�^�����
- createUandR.py
-- �T�[�o���̃��[�U�o�^�y�у��|�W�g���o�^
- pushGitRepos.sh
-- �N���C�A���g���ł̃��|�W�g���쐬�y�уT�[�o�ւ̓o�^

*CSV
- makeUsers.csv
-- �쐬���郆�[�U�A�J�E���g�̏��(���[�U���C�p�X�C�t���l�[���C���A�h�j
- makeRepos.csv
-- �쐬���郊�|�W�g���̏��i���[�U���C�p�X�C���|�W�g�����Cpublic/private(True/False),collaborator)

*�菇
- root/root��gitbucket�Ƀ��O�C�����Croot�p�X��r00t�ɕύX����
- 2��csv�t�@�C�����쐬����
- Git�z�X�e�B���O�T�[�o(Gitbucket)���̐ݒ�
--python createUandR.py�����s����
--- L98��giturl���m�F����(GitBucket�̏���URL�j(http://gitbucket/�ŃA�N�Z�X�ł���Ȃ�ύX�s�v�j
--- L103�������createUsers('makeUsers.csv')�̃R�����g�A�E�g���O��
--- ���|�W�g���쐬���ɃA�J�E���g�ł̃��O�C�������s���邱�Ƃ�����D���̏ꍇ�͎��s����index�������ɂ��Ď��s����ƁC����������{�����
---- ex.�upython createUandR.py 11�v�Ƃ����index11����X�^�[�g����
- Git���|�W�g���i�N���C�A���g���j�̐ݒ�i�z�z�p�̃t�@�C�����w�����|�W�g���ɓo�^����j
-- sh pushGitRepos.sh �����s����
--- makeRepos.csv�̓��e�ɂ��ƂÂ��ă��|�W�g���̍쐬�E�T�[�o�ւ̓o�^(push)���s��
--- L3��giturl���m�F����(http://��������GitBucket�̏���URL��"git/"��t����������(���|�W�g���̃x�[�XURL�͂���URL�Ƀ��[�U���ƃ��|�W�g������t���������̂ɂȂ�j�j�D�����http://gitbucket/�ŃA�N�Z�X�ł���Ȃ�ύX�s�v
--- L4��csv�t�@�C���̃t�@�C�������m�F����
--- L6��tempRepo�Ɏw�肷��f�B���N�g�������m�F����D
---- sh�t�@�C��������ꏊ�Ƀ��|�W�g���Ƃ���push�������t�@�C�����܂ރf�B���N�g����u���C���̃f�B���N�g������tempRepo�ɑ�����Ă���


**�g���u��
- �x�[�V�b�N�F�؉�������܂������Ȃ������̂ŁC����͓���̃A�N�Z�X���iIP�j����̃A�N�Z�X�ɂ͔F�؂������Ȃ����ƂőΉ�
- *.git�ɑ΂��Ă����ݒ肪�K�v�ȋC�����邪�C�Ȃ��Ă����܂����Ƃ����Ă��܂����̂łƂ肠�����ۗ���

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
