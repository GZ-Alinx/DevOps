#!/bin/bash

cd /etc/yum.repos.d/ && mkdir bak && mv ./* bak


echo  "yum 源配置"

echo "[base]" >> /etc/yum.repos.d/Centos.repo
echo "name=CentOS-$releasever - Base - mirrors.aliyun.com" >> /etc/yum.repos.d/Centos.repo
echo "failovermethod=priority" >> /etc/yum.repos.d/Centos.repo
echo "baseurl=http://mirrors.aliyun.com/centos/$releasever/os/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "        http://mirrors.aliyuncs.com/centos/$releasever/os/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "        http://mirrors.cloud.aliyuncs.com/centos/$releasever/os/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "gpgcheck=1" >> /etc/yum.repos.d/Centos.repo
echo "gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7" >> /etc/yum.repos.d/Centos.repo
echo " " >> /etc/yum.repos.d/Centos.repo
echo "#released updates " >> /etc/yum.repos.d/Centos.repo
echo "[updates]" >> /etc/yum.repos.d/Centos.repo
echo "name=CentOS-$releasever - Updates - mirrors.aliyun.com" >> /etc/yum.repos.d/Centos.repo
echo "failovermethod=priority" >> /etc/yum.repos.d/Centos.repo
echo "baseurl=http://mirrors.aliyun.com/centos/$releasever/updates/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "        http://mirrors.aliyuncs.com/centos/$releasever/updates/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "        http://mirrors.cloud.aliyuncs.com/centos/$releasever/updates/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "gpgcheck=1" >> /etc/yum.repos.d/Centos.repo
echo "gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7" >> /etc/yum.repos.d/Centos.repo
echo " " >> /etc/yum.repos.d/Centos.repo
echo "#additional packages that may be useful" >> /etc/yum.repos.d/Centos.repo
echo "[extras]" >> /etc/yum.repos.d/Centos.repo
echo "name=CentOS-$releasever - Extras - mirrors.aliyun.com" >> /etc/yum.repos.d/Centos.repo
echo "failovermethod=priority" >> /etc/yum.repos.d/Centos.repo
echo "baseurl=http://mirrors.aliyun.com/centos/$releasever/extras/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "        http://mirrors.aliyuncs.com/centos/$releasever/extras/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "        http://mirrors.cloud.aliyuncs.com/centos/$releasever/extras/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "gpgcheck=1" >> /etc/yum.repos.d/Centos.repo
echo "gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7" >> /etc/yum.repos.d/Centos.repo
echo " " >> /etc/yum.repos.d/Centos.repo
echo "#additional packages that extend functionality of existing packages" >> /etc/yum.repos.d/Centos.repo
echo "[centosplus]" >> /etc/yum.repos.d/Centos.repo
echo "name=CentOS-$releasever - Plus - mirrors.aliyun.com" >> /etc/yum.repos.d/Centos.repo
echo "failovermethod=priority" >> /etc/yum.repos.d/Centos.repo
echo "baseurl=http://mirrors.aliyun.com/centos/$releasever/centosplus/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "        http://mirrors.aliyuncs.com/centos/$releasever/centosplus/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "        http://mirrors.cloud.aliyuncs.com/centos/$releasever/centosplus/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "gpgcheck=1" >> /etc/yum.repos.d/Centos.repo
echo "enabled=0" >> /etc/yum.repos.d/Centos.repo
echo "gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7" >> /etc/yum.repos.d/Centos.repo
echo " " >> /etc/yum.repos.d/Centos.repo
echo "#contrib - packages by Centos Users" >> /etc/yum.repos.d/Centos.repo
echo "[contrib]" >> /etc/yum.repos.d/Centos.repo
echo "name=CentOS-$releasever - Contrib - mirrors.aliyun.com" >> /etc/yum.repos.d/Centos.repo
echo "failovermethod=priority" >> /etc/yum.repos.d/Centos.repo
echo "baseurl=http://mirrors.aliyun.com/centos/$releasever/contrib/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "        http://mirrors.aliyuncs.com/centos/$releasever/contrib/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "        http://mirrors.cloud.aliyuncs.com/centos/$releasever/contrib/$basearch/" >> /etc/yum.repos.d/Centos.repo
echo "gpgcheck=1" >> /etc/yum.repos.d/Centos.repo
echo "enabled=0" >> /etc/yum.repos.d/Centos.repo
echo "gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7" >> /etc/yum.repos.d/Centos.repo


echo "yum install"
yum clean all
yum makecache
yum repolist

yum install -y vim wget lrzsz* gcc*
if [ $? -eq 0 ];
	echo "System yum Source images Install Success~"
else
	echo "Install Faild...."
fi

