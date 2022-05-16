# Team_CS180
**Team Team's CS 180 Project**  

**Contributors:**  
Pranay Sarveiya, Justin Lyu, Tommy Chhur, Chandler Mahkorn 
[Dataset: US Accidents (2016 - 2021)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)  

**If you just want to run the server using this repo, follow this instruction**  
Download the repo to a directory.  
Check if you have django installed using  

     \> py -m django --version  

Then run

     \> py manage.py runserver
     
There many be some unapplied migrations; ignore those.  
Then in your browswer, go to this link:

     http://localhost:8000/hello/
     
Done.  
  ____________________________  
  
  
**Instructions for setting up yourself**  
Python libraries used:
If pip is not installed, follow instructions [here](https://pip.pypa.io/en/stable/installation/)
matplotlib (For Creating Analyitc Graphs)

     \> pip install matplotlib
     
mpld3 (For Real-Time Graphs)

     \> pip install mpld3
     
Following [this](https://docs.djangoproject.com/en/4.0/intro/tutorial01/) loosely, check for more details  
First have django installed, check installation using:  

    \> py -m django --version
cd to directory you want to store your code, then run:  

    \> django-admin startproject mysite

this will create a mysite directory.  
Then run the dev server using:

    \> py manage.py runserver
    
Ignore the warnings about unapplied database migrations.  
Now visit http://127.0.0.1:8000/ on your web browser.  
We can add apps using this command in the same directory as the manage.py

    \> py manage.py startapp hello
    
this is the directory that will house your application. Check the instruction link for more details and examples.  
From this point, keep following the instructions from the above link using 'hello' instead of 'polls.'  
We modified hello/views.py, added and modified hello/urls.py, and modified mysite/urls.py.  
After that, we can get a dummy output by going to http://localhost:8000/hello/search
<p>
     <br>
     <br>
</p>  

**Calling Search Function:**  
http://localhost:8000/hello/search  
Then follow instructions on screen

