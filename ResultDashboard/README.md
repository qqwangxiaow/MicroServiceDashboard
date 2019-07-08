### Create Local Registry

1. use command docker pull registry to pull latest registry image from dockerhub
2. docker run -d  -p 5000:5000 --privileged=true --restart=always -v /home/xhl/Volumes/docker:/var/lib/registry registry
3. add "insecure-registry":["commonNodeIP:RegistryPort"] to /etc/docker/daemon.json
4. systemctl daemon-reload
5. systemctl restart docker

### Create NFS Volume

1. ##### In CommonNode(Ubuntu temp environment,finally should be clearlinux) apt-get install nfs-kernel-server nfs-common

2. ##### sudo vim /etc/exports 

   add line /home/xhl/Volumes/result *(rw,sync,no_root_squash)

   add line /home/xhl/Volumes/config *(r,sync,no_root_squash)

   add line /home/xhl/Volumes/dockerfile *(rw,sync,no_root_squash)

3. ##### retart nfs server and export rv in common node

   1. ###### mount config

      /etc/init.d/nfs-kernel.server restart

       excute command exportfs -rv

      install ufs-util in client machine

      add below line to /etc/fstab in target node

      10.239.85.216:/home/xhl/Volumes/result /mnt nfs default 0 0

      10.239.85.216:/home/xhl/Volumes/config /mnt nfs default 0 0

      10.239.85.216:/home/xhl/Volumes/dockerfile /mnt nfs default 0 0

      mount -t nfs 10.239.85.216:/home/xhl/Volumes/result /mnt

   2. ###### unmount command

      unmount -v /mnt


4. ##### Mariadb

   1. mkdir -p /docker/mysql/data
   2. mkdir -p /docker/mysql/conf
   3. touch /doker/mysql/conf/my.cnf
   4. create config map by kubectl create configmap mysql-config --from-file=/docker/mysql/conf/my.cnf
   5. mount data and my.cnf
   6. create user 'username'@'%' identified by 'password';
   7. alter user 'username'@'%' identified with mysql_native_password by 'password';
   8. grant all privileges on *.* to 'xhl'@'%' with grant option;
   9. flush privileges;