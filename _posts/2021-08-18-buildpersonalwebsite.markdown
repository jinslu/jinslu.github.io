---
layout: post
title:  Build a personal academic website using Github and jekyll
date: 2021-08-18 11:10:00
description: This post is a detailed step-by-step tutorial to show how to build a personal academic website based on github page. 
categories: [Tutorials, Website]
---

<h1>Step 1: Github or Gitee</h1>

### 1. Create an account
First, you need to have a [Github](https://github.com/) or [Gitee](https://gitee.com/) account, and your website will be deployed on it. Gitee is a something like a China version of Github. Their functions are almost the same. But if your website is deployed on Github, it will be very slow to visit your website or sometimes your website cannot be accessed in China. It will be a good choice to use Gitee if you hope your website can be accessed in a easy and convenient way in China. Don't worry, you can also access your website deployed on Gitee in other countries (e.g. U.S.A). If you do not have an github or gitee account yet, you can try to choose a good user name for your account when you creating it, because your website url name will be related to your user name and be something like "https://username.github.io". 

### 2. Create an repository
After you have a Github or Gitee account and log in, new repository first (taking Github for example).

<p style="margin:0;text-align:center"><img src="github_newrepo_1.png" alt="github_newrepo_1" style="width:30%"></p>
Then you will need to input your repository name. I strongly suggest you give the repository name (e.g. jinslu) the same as your user name (e.g. jinslu). Choose "private" if you do not want your repository (i.e. your source files) to be found on the Internet by others. Click "create repository".

<p style="margin:0;text-align:center"><img src="github_newrepo_2.png" alt="github_newrepo_2" style="width:50%"></p>

### 3. Upload files to you repository
You can use [Git tool](https://git-scm.com/downloads) and command line shown below to upload files (html, css, jave scripts, images, pdfs, and so on) from your computer to your new repository or use web-based Github file uploade interface in the Github to do it. You can also find a lot of tutorials (e.g. [khan academy](https://www.khanacademy.org/computing/computer-programming/html-css/web-development-tools/a/hosting-your-website-on-github)) on the internet to show you creat a Github account and repository.
<p style="margin:0;text-align:center"><img src="github_newrepo_3.png" alt="github_newrepo_3" style="width:100%"></p>

### 4. Github page
Previously, you need to turn on the Github page in your repository. It seems now you just need to add ".github.io" to your repository name to have this function. After that, your repository name will be something like "jinslu.github.io". 

### 5. Use templates to build your website
There are a lot of nice personal website template on the Github. Here are some examples:
* [Github repository 1](https://github.com/ys1998/academic-portfolio): https://github.com/ys1998/academic-portfolio
* [Personal website 1](https://ys1998.github.io/academic-portfolio/): https://ys1998.github.io/academic-portfolio/
* [Github repository 2](https://github.com/academicpages/academicpages.github.io): https://github.com/academicpages/academicpages.github.io
* [Personal website 2](https://academicpages.github.io/publications/): https://academicpages.github.io/publications/
* [Github repository 3](https://github.com/qzhang95/qzhang95.github.io): https://github.com/qzhang95/qzhang95.github.io
* [Personal website 3](https://qzhang95.github.io/): https://qzhang95.github.io/
* [Github Page theme with jekyll](https://jekyllthemes.io/github-pages-themes): https://jekyllthemes.io/github-pages-themes

<h1>Step 2: jekyll</h1>
### 1. jekyll installation on Mac
It is very easy to install jekyll on Macbook. Just open terminal and input:`sudo  gem install jekyll`

### 2. jekyll usage
* If there is no jekyll project on your computer, open terminal and create one `jekyll new project_name` 
* You can download the jekyll project from [Github Page theme with jekyll](https://jekyllthemes.io/github-pages-themes) as shown in above, open terminal and cd to the project folder. Input command `jekyll server` and it is without error if you see these messages as shown below:
<p style="margin:0;text-align:center"><img src="jekyll_server_message.png" alt="jekyll_server_message" style="width:50%"></p>
* Open your browser and use http://127.0.0.1:4000 as your url. You can preview the website in this way. 
* Try to change the content of the files in the project, for example, change the index.html file, to see what will be changed in the website (http://127.0.0.1:4000). You can understand the html, css, java scripts, and markdown by this way little by little. 

<h1>Step 3: bibtex-js: generate your publication list automatically</h1>

You can install the bibtex-js on your website from this [Github project](https://github.com/pcooksey/bibtex-js): https://github.com/pcooksey/bibtex-js
Here is my modified html scripts (the content in between the "---" are for markdown, if you use html, please delete this part and start from "<script type="):
```
---
layout: page
permalink: /publications/
title: Publications
---

<script type="text/javascript" async src="https://cdn.jsdelivr.net/gh/pcooksey/bibtex-js@1.0.0/src/bibtex_js.min.js"></script>

<bibtex src="/publications/jinsheng.bib"></bibtex>

<div class="bibtex_structure">
  <div class="group year" extra="DESC number">
      <div style="padding-bottom:10px;"></div>
      <div class="sort journal" extra="DESC string">
        <div class="templates"></div>
      </div>
  </div>
</div>

<div id="bibtex_display">
  <div class="bibtex_template">
    <ul><li>
      <div class="if title">
        <a class="url"><strong><span class="title"></span></strong></a>
      </div>
      <div class="if author">
        <span class="author"></span>
      </div>
      <span class="if journal"><em><span class="journal"></span></em>,</span>
      <span class="if booktitle"><em><span class="booktitle"></span></em>,</span>
      <span class="if volume">vol. <span class="volume"></span>,</span>
      <span class="if journal number">(<span class="number"></span>),</span>
      <span class="if pages"> pp. <span class="pages"></span>,</span>
      <span class="if year"><span class="year"></span>.</span>
      <span class="if editorsuggestion">Editors' Suggestion.</span>
      <span class="if cover">
        <a class="cover">Cover Paper.</a>
      </span>
      <span class="if news">
        <a class="news">Featured News.</a>
      </span>
      <span class="if file">
        <a class="file">
          <div class="color-button">PDF</div>
        </a>
      </span> 
      <p style="margin:0">   
        <button class="accordion">Abstract</button>  
        <div class="panel" style="background-color: #f5f5f5;text-align: justify;">
        <span class="if abstract">
            <span class="abstract"></span>
        </span>
        </div>
      </p>       
      <script> 
        var acc = document.getElementsByClassName("accordion");
        var i;
        for (i = 0; i < acc.length; i++) {
            acc[i].onclick = function(){
                this.classList.toggle("active");
                this.parentNode.nextElementSibling.classList.toggle("show");
          }
        }
      </script>
    </li></ul>
  </div>
</div>
```
You can download my <a href="/publications/jinsheng.bib">bib file</a> here.

<h1>Step 4: automatical images slider in your home page</h1>
You can use this script to automatically switch between multiple images in your home page.
```
---
layout: default
---

<!--
<p style="margin:0;text-align:center;"><img src="/projects/cover_2017PRL.png" onmouseover="imagefun()" id="getImage" style="width:100%"></p>

<script>
function imagefun() {
    var Image_Id = document.getElementById('getImage');
    if (Image_Id.src.match("/projects/cover_2017PRL.png")) {
        Image_Id.src = "/projects/newscover_2019SA.png";
    }
    else {
        Image_Id.src = "/projects/cover_2017PRL.png";
    }
}        
</script>
-->

<html lang="en">

<style>
    *{
        margin: 0px;
        padding: 0px;
    }
    .pic1{
        width: 100%;
        height: auto;
        
    }
</style>

<!-- ------------- CSS Ends here -->
<body>

    <!-- Slider Code -->
    <div class="slider">
        <img src="/projects/cover_2017PRL.png" alt="light-induced pulling and pushing" class="pic1">
        <img src="/projects/newscover_2019SA.png" alt="Optical motors" class="pic1">
        <img src="/projects/onchipopticaltweezers.png" alt="On-chip optical tweezers" class="pic1">
    </div>


</body>
    <script>
        var index=0;
        Carousel();
        function Carousel()
        {
            var i;

            var x = document.getElementsByClassName('pic1');
            for(i=0; i<x.length; i++)
            {
                if(i==index)
                {
                    x[i].style.display = "block";
                }
                else{
                    x[i].style.display = "none";
                }
            }
            index++;
            if(index>=x.length)
            {
                index = 0;
            }
            setTimeout(Carousel,3000);
        }

    </script>

</html> 
```
or use [this script](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_slideshow_auto):
```
---
layout: default
---

<html>

<style>

.mySlides {display: none;}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* The dots/bullets/indicators */
.dot {
  height: 10px;
  width: 10px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  /*top: 0;*/
  bottom: 0;
}
.active {
  background-color: #717171;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 2s;
  animation-name: fade;
  animation-duration: 2s;
}

@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

</style>


<body>

<div class="slideshow-container">

<div class="mySlides fade">
  <!--<div class="numbertext">1 / 3</div>-->
  <img src="/projects/cover_2017PRL.png" style="width:100%">
  <div class="text">Light-induced pulling and pushing</div>
</div>

<div class="mySlides fade">
  <!--<div class="numbertext">2 / 3</div>-->
  <img src="/projects/newscover_2019SA.png" style="width:100%">
  <div class="text">Optical motor in the dry adhesive regime</div>
</div>

<div class="mySlides fade">
  <!--<div class="numbertext">3 / 3</div>-->
  <img src="/projects/onchipopticaltweezers.png" style="width:100%">
  <div class="text">On-chip optical tweezer based on freeform optics</div>
</div>

</div>

<div style="text-align:center">
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
</div>

<script>
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 4000);
}
</script>

</body>
</html> 
```