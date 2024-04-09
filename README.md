# linkedin automation bot
 
 Please read this before going into the program 
 This project is sololy based on web scraping using different modules of pythons 
 to make it professional and to make it to be used for user or any organisation make sure to integrate this project with an API .


firstly before starting this project make sure you have a web driver probably the chrome driver with the version which matches with your current chrome version 
you can get this at :- https://chromedriver.chromium.org/downloads
make sure you exract this file and put the "chromedriver" in you current working directoy/ path/ location.

And make sure you update it time to time , if you get any errors or exceptions regarding the webdriver version, please download the latest version of webdriver and follow the same steps mentioned above.


""""""""linkedin cookie""""""""
Now in the code provided uses cookies to automate login, so that you don't have to login again and again and linkedin don't put an "suspicious activity detected on you".
the same code I have stored in the file "linkedin_cookie_gen.py". we have to make a file that should contain the information of you cookie you can get it through :- login to you linkedin > inspect > Application > Cookie > www.linkedin.com. and copy the attriutes of Name , Values , Domain .
make sure you store this information on the excel with .csv extension and those file should the columns name same as in the cookie that is Name , Values , Domain.

I am attaching a sample file of the cookie in this project. it should look something like that. don't copy it as it won't work properly for you.
