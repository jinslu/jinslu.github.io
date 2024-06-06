---
layout: post
title:  Matlab set the properties of colorbar
date: 2021-09-01 11:00:00
description: This post is to show you how to set the properties of colorbar in Matlab, including the position, width, title, label, and value range. 
categories: [Matlab]
---

<h2>1. Set the colormap of the colorbar</h2>

```matlab
% use the colormap provided by Matlab
colormap(jet); %jet, parula, hsv, hot, etc.
```

<p style="margin:0;text-align:center"><img src="matlabcolormaplist.png" alt="" style="width:50%"></p>

```matlab
%use a custom colormap
load('RGB_Vincent.mat');
rgbvincent = flipud(RGBVincent);
colormap(rgbvincent);
```

You can generate or download some custom colormaps beyond the colormaps provided by Matlab in the following online sources. 
* [PyColormap4Matlab](https://www.mathworks.com/matlabcentral/fileexchange/68239-pycolormap4matlab)
* [jdherman github](https://jdherman.github.io/colormap/)
* [Custom Colormap](https://www.mathworks.com/matlabcentral/fileexchange/69470-custom-colormap)

<h2>2. Use colormap for the 1-D line or point plots</h2> 

```matlab
% use a colormap
jet = colormap(jet);
line_number = 20;
for ii = 1:line_number
	xx = linspace(0,2*pi,100);
	yy = sin(xx-pi*(ii-1)/(line_number-1));
	plot(xx,yy,'color',jet(floor(ii*256/line_number),:),'linewidth',1.5);
	hold on;
end
xlabel('x');
ylabel('sin(x+\phi)');
axis([0,2*pi,-1,1]);
colormap(jet);
c = colorbar;
ax = gca;
axpos = ax.Position;
c.Position(1) = 0.92;
c.Position(3) = 0.5*c.Position(3);
c.Title.String = '\phi (rad)';
set(c,'YTick',[0,1]);
set(c,'YTickLabel',{'0','\pi'});
```

<p style="margin:0;text-align:center"><img src="lineplot_withcolormap.jpg" alt="" style="width:50%"></p>

<h2>3. Set the properties of the colorbar</h2> 

<h3>3.1 set the width and position</h3>

```matlab
c = colorbar;
ax = gca;
ax.Position(3) = 0.78; %change the width-to-height ration of the figure inside the windows
axpos = ax.Position; 
c.Position(1) = 0.9; % change the position of the colorbar
c.Position(3) = 0.3*c.Position(3); %change the width of the colorbar
```

<h3>3.2 set the value range, label, and ticks</h3>

```matlab
caxis([0,1]);
c.Title.String = 'deg'; % c.Label.String = 'deg'; set label on the right
c.TickLength = 0.005;
set(c,'tickdir','out');
set(c,'YTick',[0,0.5,1]);
set(c,'YTickLabel',{'0','3','6'});
```

