(env) PS C:\Users\me\projects\Oat> git push origin master
remote: Permission to app-generator/django-dashboard-light-blue.git denied to techcure.
fatal: unable to access 'https://github.com/app-generator/django-dashboard-light-blue.git/': The requested URL returned error: 403
(env) PS C:\Users\me\projects\Oat> git init https://github.com/techcure/dashboard.git
fatal: cannot mkdir https://github.com/techcure/dashboard.git: Invalid argument
(env) PS C:\Users\me\projects\Oat> git remote add origin https://github.com/techcure/dashboard.git
fatal: remote origin already exists.
(env) PS C:\Users\me\projects\Oat> git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/app-generator/django-dashboard-light-blue.git'
(env) PS C:\Users\me\projects\Oat> git remote set-url --add --push origin https://github.com/techcure/dashboard.git
(env) PS C:\Users\me\projects\Oat> git init
Reinitialized existing Git repository in C:/Users/me/Projects/Oat/.git/
(env) PS C:\Users\me\projects\Oat> git add .
(env) PS C:\Users\me\projects\Oat> git commit -m "added"
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
(env) PS C:\Users\me\projects\Oat> git  status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
(env) PS C:\Users\me\projects\Oat> git push origin master
Enumerating objects: 1596, done.
Counting objects: 100% (1596/1596), done.
Delta compression using up to 4 threads
Compressing objects: 100% (1099/1099), done.
Writing objects: 100% (1596/1596), 8.40 MiB | 1.58 MiB/s, done.
Total 1596 (delta 438), reused 1537 (delta 414), pack-reused 0
remote: Resolving deltas: 100% (438/438), done.
To https://github.com/techcure/dashboard.git
 * [new branch]      master -> master
(env) PS C:\Users\me\projects\Oat> git  status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   app/views.py

no changes added to commit (use "git add" and/or "git commit -a")
(env) PS C:\Users\me\projects\Oat> git add apps/views.py
fatal: pathspec 'apps/views.py' did not match any files
(env) PS C:\Users\me\projects\Oat>  git init
Reinitialized existing Git repository in C:/Users/me/Projects/Oat/.git/
(env) PS C:\Users\me\projects\Oat> git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   app/views.py

no changes added to commit (use "git add" and/or "git commit -a")
(env) PS C:\Users\me\projects\Oat> git add app/views.py
(env) PS C:\Users\me\projects\Oat> git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   app/views.py

(env) PS C:\Users\me\projects\Oat> git commit -m "Added"
[master 33878dc] Added
 1 file changed, 1 insertion(+)
(env) PS C:\Users\me\projects\Oat> git branch
* master
(env) PS C:\Users\me\projects\Oat> git push origin master                                                                                                                                       Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 355 bytes | 355.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/techcure/dashboard.git
   76d0cc1..33878dc  master -> master
(env) PS C:\Users\me\projects\Oat>