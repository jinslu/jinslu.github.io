---
layout: post
title:  Solved problem cannot push to gitee
date: 2021-08-16 20:10:00
description: This post is to provide a solution when you encounter the "acess denied" problem of git push to gitee. 
categories: [Tutorials, Github]
---

<h3>Problem description</h3>
I used github account before and excute “push -u origin master” to upload my files to projects on github. Today I created a project on gitee and try to upload files from macbook to gitee according to the instructions on the gitee, as shown in below figure.

<p style="margin:0;text-align:center"><img src="gitee_comments_initiation.png" alt="gitee_comments" style="width:50%"></p>

However, when I run the comment "git push -u origin 
master", a error appeared:
>remote: Access denied <br>
>fatal: unable to access 'https://gitee.com/phylu/phylu.git/': The requested URL returned error: 403

<h3>The solution</h3>
I tried to add ssh to gitee but did not help. Then I realized that it may be due to the conflict between the two accounts of github and gitee since I used github account before. Therefore, I deleted the github account in terminal and it works. The comments which neede to be input in the terminal are:
>git credential-osxkeychain erase <br>
>host=github.com <br>
>protocol=https <br>
[press enter twice]

