FROM centos:centos6

MAINTAINER igaki version:0.1

RUN yum install -y wget

#wget jdk8 and localinstall
WORKDIR /opt/
RUN wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-x64.rpm";yum localinstall -y jdk-8u161-linux-x64.rpm

#Install xvfb firefox selenium
RUN yum install -y xorg-x11-server-Xvfb firefox
RUN wget -O selenium-server-standalone-3.12.0.jar https://selenium-release.storage.googleapis.com/3.12/selenium-server-standalone-3.12.0.jar
RUN yum groupinstall -y "Japanese Support"

#Install python
RUN yum install -y centos-release-scl
RUN yum install -y rh-python35 python27
ADD ./enablepython35.sh /etc/profile.d/

WORKDIR /opt
RUN wget -O geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz
RUN tar zxvf geckodriver.tar.gz
RUN mv geckodriver /usr/local/bin

RUN yum install -y git

ADD ./controlGit_cs /root/controlGit_cs/
ADD ./controlGit_test /root/controlGit_test/

COPY ./init.sh /usr/local/bin/init.sh
RUN chmod u+x /usr/local/bin/init.sh

#EXPOSE 4444
CMD ["/usr/local/bin/init.sh"]
#CMD ["/bin/bash"]      
