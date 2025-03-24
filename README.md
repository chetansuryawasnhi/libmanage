As per given assignment i created this repo
To use this repositry or project follow the steps

1.Run this commands on shell or dolwnlaod this zip in your pc
  - git clone https://ggithub.com/chetansuryawasnhi/libmanage.git
  - libmanage.git
2. after dowanloading you have to donload the python
  - link -https://www.python.org/downloads/
  - version 3.12
3. after that insatll the pacages from requirement.txt
  - open the downloaded folder 
  - open the terminal in file by right clciking 
  - hit command pip install -r requirements.txt
4. now open the all folder in the ide ex vs code

5. open tour mysql database ex.. mysql workbench
   - create a database
   - create database your_db_name
  
6. now go to the file and open settings.py form
 libmanage\settings.py
    and do this changes
  - DATABASES = {
  -  'default': {
  -     'ENGINE': 'django.db.backends.mysql',
  -      'NAME': 'your_db_name', // here add your databse name which you created just
  -      'USER': 'your_db_user', // here add your user
  -     'PASSWORD': 'your_db_password', // your password
  -      'HOST': 'localhost',
  -     'PORT': '3306',
  -    }
  - }

7. after that open the new terminal from your open filed location
   - Run the following commands to set up the database tables:
   - python manage.py makemigrations
   - python manage.py migrate

8. all the setup is done now you have to start the server by using commnad in terminal
  - python manage.py runserver

9. now you can use the applications like postman to use api

10. Register the uer by using api

 - POST http://127.0.0.1:8000/api/register/

  Request Body (JSON Format):
  
  {
      "username": "newuser",
      "email": "newuser@example.com",
      "password": "securepassword",
      "password2": "securepassword"
  }

 - make sure password" ==== "password2" matches

 - If successful, you'll receive a response like:

    {
        "username": "newuser",
        "email": "newuser@example.com"
    }


11. login user by api
    - POST http://127.0.0.1:8000/api/login/
        Request Body (JSON Format):
      
      {
          "username": "newuser",
          "password": "securepassword"
      }

    - if succesful you will recive a response like
     {
    access_toekn "_________________________________"
    refresh_toek "_________________________________"

     }

    - this token are very userful to do the crud opertions copy the access_toekn
    - this toekn will update at certain time
  
  12. now to add a new book
      ![image](https://github.com/user-attachments/assets/a4ebf533-9b3a-448e-9ef9-e1d948295ff8)

      - at this time the acces toekn is we have to proivde in header
      - Bearer access_toekn
      - ex using a postman go to header and chooce authorization and in next column past "Bearer acces_toekn"
      - like this image

    


  
      - use api endpoint
      - POST http://127.0.0.1:8000/api/book_create/
     {
         "id ": book id ex 123
        "title": "title of book",
        "author": "author of book",
        "description": "description of book",
        "isbn": "1234",
        "available": true or false
    },
13 .  read the book 
       -follow same mathod of accesS token from login which you get
       - use this api endpoint
      
         GET  http://127.0.0.1:8000/api/read/
      
        - Bearer access_toekn in header 
        - ex using a postman go to header and chooce authorization and in next column past "Bearer acces_toekn"
      
      
      14.update the book
      PUT  http://127.0.0.1:8000/api/book_update/provide_the_book_id_here/
      ex PUT http://127.0.0.1:8000/api/book_update/123/
      Bearer access_toekn in header 
      
      here what you want ot update provide in key:vlaue
      eg..
      {
       "title": "python",
      }

14. delete the book 
    DELETE  http://127.0.0.1:8000/api/book_delete/provide_the_book_id_here/
    eg.. DELETE http://127.0.0.1:8000/api/book_update/123/

15 . For student view ther is ui

- http://127.0.0.1:8000/student/
- to paste it in your browser you will get a student wiew
  ![image](https://github.com/user-attachments/assets/05e43036-b339-4d16-8bf6-6051b991f14d)


so all about the assignment
- thanks for the project 


