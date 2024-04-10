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
make sure you store this information on the excel with "linkedin_cookie.csv" extension and those file should the columns name same as in the cookie that is Name , Values , Domain.

I am attaching a sample file of the cookie in this project. it should look something like that. don't copy it as it won't work properly for you.

i have added the same piece of code in the part1.py and part2.py for the same you don't have to repeat the same procedure again . but make sure you have created a CSV file "linkedin_cookie.csv" and it is in your current working directory.




""""""""Part 1""""""""

In the part one, what actually the code is doing is that it is retreiving the information of the particular individual who satisfy no. of attributes you will provide accordingly . 
you can specify the no. of attributes the individual should have at line no. 37 "search_query = "Java "   #seach query " make sure to replace the value of search_query according to your need.

then this will ask how many pages should be need to exract , its up to you . and this will exract the information and stored it in a CSV file name "output20.csv".
I have shared an examplary ouput of the same in which i have stored the information of only one page.


""""""""Part 2""""""""

the second part is the actual part of the whole project in which you are actually sending the followin request and a custom message to make a connection with the respective peoples.
at line no. 69 you can customize the message you want to send . your process may get interrupted because their are peoples who want differnet setting on their linekedin which may differ from others.
you can either skip it or can again start the same process again . 


make sure you have a proper internet connection to run up this code 
and you can edit the time.sleep() function accordingly to your needs