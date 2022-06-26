# Alegrosz

## New django feature implementation algorithm

1. Do we need create new django app?
   - ```bash python manage.py startapp <name>```
   - add app to settings.py (INSTALLED_APP section) - ```python '<app_name>.apps.<class_name>```
2. Do we need data for feature? Go to models.py
   - ```bash python manage.py makemigrations <app_name>```
   - ```bash python manage.py migrate <app_name>```
3. Do we need add support to CMS(content management system) - Admin
   - admin.py ```python admin.site.register(<Model>)```
4. Do we need forms?
   - forms.py
5. Create views -> views.py
6. Create templates -> <app_name>/templates/<app_name>/<file_name>.html
7. Create local router -> urls.py -> urlspattern
8. Add local router to global router -> config/urls.py
9. Add link to html.