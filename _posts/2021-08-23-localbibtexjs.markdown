---
layout: post
title: Use bibtexjs as a local app
date: 2021-08-23 11:53:00
description: This post is to solve the problem of requring VPN to acess google when using the bibtex-js. 
categories: [Tutorials, Website]
---

<h3>Problem description</h3>
When you use [bibtex-js](https://github.com/pcooksey/bibtex-js) to generate the publication list in your website as the instruction given by the author, you will find it requires two js files obtained in an online way:<br>
* `<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/pcooksey/bibtex-js@1.0.0/src/bibtex_js.min.js"></script>`
* `jq.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'`

The first file (bibtex_js.min.js) is required in your publication.md which is used to generate the pulication list page in your website. In the meantime, the the second file (jquery.min.js) is required inside the first file. 
As you can see, if you access the second file in an online way, you will need a VPN to access the googleapis first. If you are in China, it will be a problem to visit google.

<h3>The solution</h3>
It requires two steps (please download the two files,bibtex_js.min.js and jquery.min.js, and put them in your publication folder):

1. In your publication.md, change
<br>
`<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/pcooksey/bibtex-js@1.0.0/src/bibtex_js.min.js"></script>`
<br>
to be
<br>
`<script type="text/javascript" async src="/publications/bibtex_js.min.js"></script>`
2. In the bibtex_js.min.js file, change <br>
`jq.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'`
<br>
to be 
<br>
`jq.src = 'jquery.min.js'`