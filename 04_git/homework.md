# 04. Git - домашнее задание

## Part1

- сделать git clone репозитория `git@github.com:alsigna/python2024-01-git-hw.git`
- найти commit c описанием "update sw"
- удалить этот коммит и все изменения после него включительно (коммит с описанием “update sw” так же удаляем)
- определить версию ПО для платформы "ASR920 Series" из файла sw.csv (запишем на бумажке)

```bash
modemfux@python-vm:~/n4e/python2024-01-git-hw [master|✔]> git log --oneline
7c85b13 (HEAD -> master, origin/master, origin/HEAD) Merge pull request #1 from alexigna843/master
95dcff9 Update README.md
6c171a3 update nb40 notes
03fa8b9 update nb40 notes
b54f069 update nb40 notes
7c01096 nb40 notes
82d6141 update sw
c5a9f76 delete ntp server
122a122 add more git notes
e58cfa9 add more git notes
f7f0ad8 add git notes
49ba941 correct loopback interface
1ec0c39 add servers to log stats
0ab7525 reduce logo size
620c7cd add cisco logo
199cddf add sw versions
964953b fix load-interval
e8fc568 add uplink config
712369f add log_stats
baae044 add readme
9c7f415 add tunnel template
modemfux@python-vm:~/n4e/python2024-01-git-hw [master|✔]> git reset --hard HEAD~6
HEAD is now at c5a9f76 delete ntp server
modemfux@python-vm:~/n4e/python2024-01-git-hw [master ↓·7|✔]> git log --oneline
c5a9f76 (HEAD -> master) delete ntp server
122a122 add more git notes
e58cfa9 add more git notes
f7f0ad8 add git notes
49ba941 correct loopback interface
1ec0c39 add servers to log stats
0ab7525 reduce logo size
620c7cd add cisco logo
199cddf add sw versions
964953b fix load-interval
e8fc568 add uplink config
712369f add log_stats
baae044 add readme
9c7f415 add tunnel template
modemfux@python-vm:~/n4e/python2024-01-git-hw [master ↓·7|✔]> ls
dmvpn-tunnel-template.j2  git_commands.txt  logo.png  log_stats.csv  README.md  sw.csv  uplink.cfg
modemfux@python-vm:~/n4e/python2024-01-git-hw [master ↓·7|✔]> cat sw.csv | grep "ASR920"
ASR920 Series,,3.16.5S
modemfux@python-vm:~/n4e/python2024-01-git-hw [master ↓·7|✔]>
```

## Part2

- сделать fork репозитория `git@github.com:alsigna/python2024-01-git-hw.git`
- найти netbox-token NB_TOKEN

```bash
modemfux@python-vm:~/n4e/python2024-01-git-hw [master|✔]> git log origin/master HEAD --full-diff -p | grep NB
-NB_URL=http://netbox.org
-NB_TOKEN=9fc9b897abec9ada2da54321dbc34596293c9cb9
+NB_URL=http://netbox.org
+NB_TOKEN=9fc9b897abec9ada2da54321dbc34596293c9cb9
modemfux@python-vm:~/n4e/python2024-01-git-hw [master|✔]>
```

## Part3

- создать файл в корне вашего форкнутого репозитории с именем, равным вашему имени git пользователя
- записать в этот файл версию ПО из part1 и netbox token из part2
- сделать commit/push в свой форкнутый репозиторий на github
- сделать pull request вашего форка в alsigna/python2024-01-git-hw.git с созданным файлом, тем самым я увижу его

```bash
modemfux@python-vm:~/n4e/python2024-01-git-hw [master|✔]> echo "ASR920 Series,,3.16.5S" > modemfux
modemfux@python-vm:~/n4e/python2024-01-git-hw [master| …1]> echo "NB_TOKEN=9fc9b897abec9ada2da54321dbc34596293c9cb9" >> modemfux
modemfux@python-vm:~/n4e/python2024-01-git-hw [master| …1]> git add modemfux
modemfux@python-vm:~/n4e/python2024-01-git-hw [master|●1]> git commit -m "Add solution for 04_git_homework"
[master e911389] Add solution for 04_git_homework
 1 file changed, 2 insertions(+)
 create mode 100644 modemfux
modemfux@python-vm:~/n4e/python2024-01-git-hw [master ↑·1|✔]> git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 363 bytes | 363.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:modemfux/python2024-01-git-hw.git
   7c85b13..e911389  master -> master
modemfux@python-vm:~/n4e/python2024-01-git-hw [master|✔]>
```
