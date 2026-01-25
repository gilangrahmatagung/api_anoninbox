

LINK:
Customize built-in user model: https://testdriven.io/blog/django-custom-user-model/
Cookie-based auth in DRF: https://medium.com/@michal.drozdze/django-rest-framework-authentication-permissions-5b81da9d0364

https://yoongkang.com/blog/cookie-based-authentication-spa-django/


Tentang cookie-based auth + csrf token:
- sessionid itu HTTPOnly tapi CSRF cookie bisa diakses Javascript
- untuk melakukan unsafe method (POST/PUT/PATCH/DELETE) user harus kirim X-CSRFToken di HTTP Header yg dia dapat dari csrftoken (yg ini dihandle otomatis). Artinya harus di set X-CSRFToken == get(csrftoken).


