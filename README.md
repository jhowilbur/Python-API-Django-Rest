# Python API REST
Api Rest about school DATA using DJANGO. 

------------

# Commands to start project - zero from hero
- to get all dependencies
```
pip install pipreqs 
pip install -r requirements.txt
```

- to start django project in a like "root" folder for manage.py
```
django-admin startproject apirest .
```
- to create an app inside project
```
python manage.py startapp school
```
- to run your app
```
python manage.py runserver
```
- to make changes in DB when you change/include objects in admin.py (inside your app folder)
```
python manage.py makemigrations
python manage.py migrate
```
- to see help
```
python manage.py help
```

# Steps inside code
### to Make models/data in DB
- Enter in your startapp created
- Create class in models.py
- Include that's new object on admin.py 
- Run commands to make migrations
--------------
### to give resources/endpoints in URL in JSON format for CRUD operations
- Enter in your startapp created
- Going to serializing.py and include new META
- Include in views.py your new META
- Enter in your startproject folder created in beginning of project
- inside urls.py include new router
--------------
### to give resources in endpoints with special formats
- Just enter in serializing.py and insert new modules (like ListRegisterStudentSerializer)
- Normally after step is insert new serializing in views.py that's right, inside class you just insert generics.ListAPIView (like ListRegisterStudent)
- And don't forget to insert new URL (urlpatterns) in urls.py with path(INSER_NEW_URL_FORMAT) like path('student/<int:pk>/registers')
--------------
### to protect with Authentication our resources in endpoints
- in views.py insert inside a class for example *ViewSet a BasicAuthentication and IsAuthenticated 
- if you can, just insert in all class inside views.py (like StudentViewSet)