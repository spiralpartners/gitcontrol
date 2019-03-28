#!/bin/sh

first(){
    echo "The following procedure is invoked only once"
    cp -a /root/controlGit_cs/ /data/
    cp -a /root/controlGit_aibic/ /data/
    source /opt/rh/rh-python35/enable
    pip install --upgrade pip
    pip install -U selenium pyvirtualdisplay
    pip install pandas
}
init(){
    echo "The following procedure is always invoked"
    echo "container start" >> /var/log/docker_container
    date >> /var/log/docker_container
}

if [ ! -r /var/log/docker_container ] ; then
    first
fi

init

cat <<EOF >>~/.bashrc
function TERMINATE {
    echo "container terminate" >> /var/log/docker_container
    date >> /var/log/docker_container
}
trap 'TERMINATE; exit 0' TERM
EOF
exec /bin/bash

