LINK:
Customize built-in user model: https://testdriven.io/blog/django-custom-user-model/
Cookie-based auth in DRF: https://medium.com/@michal.drozdze/django-rest-framework-authentication-permissions-5b81da9d0364
https://medium.com/@altafkhan_24475/guide-to-session-authentication-in-django-rest-framework-b079d2452d9d

https://yoongkang.com/blog/cookie-based-authentication-spa-django/


Tentang cookie-based auth + csrf token:
- sessionid itu HTTPOnly tapi CSRF cookie bisa diakses Javascript
- untuk melakukan unsafe method (POST/PUT/PATCH/DELETE) user harus kirim X-CSRFToken di HTTP Header yg dia dapat dari csrftoken (yg ini dihandle otomatis). Artinya harus di set X-CSRFToken == get(csrftoken).

Apa sih yg perlu dites ketika API testing?
- dengan/tanpa auth API
- sesuai/tidak sesuai schema JSON body

AUTH:
- permission beda dengan authentication. Auth dulu baru permission
- ternyata django default sessionauth, itu nyimpan session di DB. Stateful!
- CSRF Token skemanya double submit. Jadi client get csrf token, trus masukin ke header. Lihat topik sebelumnya.

- CORS itu whitelist siapa saja origin (origin of browser, alias aplikasi frontend) yang boleh akses data via JS. Tidak mencegah request, hanya mencegah JS baca response. Ini browser policy.


