Migrate videos from Youtube to Sina Weibo, a Chinese incarnation of Twitter.  Works as for 2021-07 

# Requirements

* Python 3.2+
* Pillow: for image conversion
* mouse: for native mouse control
* keyboard: for keyboard mouse control
* youtube-dl: download youtube video 
* Selenium: control web browser
* AutoIt: for native file upload selection

# Setup Before Use
* update config.py (see below for detail)
* update upload_file.au3. In the process of uploading a video and a cover picture to Weibo, there are times when we need to use a popup box from the operating system to select the file to upload. I use AutoIt to do this task, but different systems do things differently. Therefore, you need to update the AutoIt script (upload_file.au3) and re-compile. See the following link for instruction. 
https://blog.csdn.net/wuxiaobingandbob/article/details/53517074

## Configuration Setting (config.py)

### FirefoxProfileFolder

Weibo uses a two-factor authentication mechansim. As a result, we don't want to simulate login every time we run this program. Therefore, we get around this by reusing current Firefox profile ( so we can reuse login session). 

We need to find the path of the file of the current Firefox profile and then set FirefoxProfileFolder to that path
https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data

### LandingPage
Simply find the page with a tweet button and the least amount of content. 

### TimeOut
seconds to wait for web page elements to appear before killing the program. 

### InputBoxX, InputBoxY
The input box for the title of the video prevents programmatic interactions with JavaScript/DOM/Selenium. This is probably a robot prevention mechanism. Therefore, I have to literally control the mouse and keyboard to enter the title. Use the following JavaScript code to the find the coordinate of the input box on your screen because different screen has different values.  

`document.onclick=function(event) {
    var x = event.screenX ;
    var y = event.screenY;
    console.log(x, y) 
}`

and then set X and Y to InputBoxX, InputBoxY
