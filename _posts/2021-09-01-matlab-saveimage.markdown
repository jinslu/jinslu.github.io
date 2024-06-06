---
layout: post
title:  Matlab save image
date: 2021-09-01 11:00:00
description: This post is to show you how to save images with good quality in Matlab. 
categories: [Matlab]
---

Use below codes to show and save high quality or vector images with defined figures size

```matlab
%set the width and height of the figure windows
width = 6;
height = 3;

%set the size of figure window to be displayed
figure('unit','inch','position',[1,1,width,height]);

%plot your figure here

%set the size of figure to be saved
set(gcf,'InvertHardcopy','on');
set(gcf,'PaperUnits', 'inches');
papersize = get(gcf, 'PaperSize');
left = (papersize(1)- width)/2;
bottom = (papersize(2)- height)/2;
myfiguresize = [left, bottom, width, height];
set(gcf,'PaperPosition', myfiguresize);

%save your figure
print('myfigure','-djpeg','-r600'); %resolution 600 dpi
%or save your figure to pdf
print('myfigure','-dpdf');
%or save your figure to svg
print('myfigure','-dsvg');
```

Matlab image format used in print function
<p style="margin:0;text-align:center"><img src="matlabimageformatlist.png" alt="" style="width:90%"></p>

Matlab vector image format used in print function
<p style="margin:0;text-align:center"><img src="matlabvectorimageformatlist.png" alt="" style="width:90%"></p>

