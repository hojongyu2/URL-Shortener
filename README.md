# URL-Shortener
Introduction: URL shortening service using Django and Python.

Prerequisites:
  - Python
  - asgiref==3.6.0
  - Django==4.2.1
  - djangorestframework==3.14.0
  - psycopg2==2.9.6
  - python-dotenv==1.0.0
  - pytz==2023.3
  - sqlparse==0.4.4
  - POSTMAN

Installation and Setup:

1. Clone my repo using this link: https://github.com/hojongyu2/URL-Shortener.git
2. Create a virtual environment within the project folder (optional but recommended).
3. Make sure to create a .env file and add your own DJANGO_SECRET_KEY inside the .env file.
4. Install all of the dependencies. Use requirements.txt or, in your terminal, use `pip install -r requirements.txt`.
5. Run the Python server with `python3 manage.py runserver`.
6. Download POSTMAN from here: [https://www.postman.com/](https://www.postman.com/downloads/) or open POSTMAN if you already have it installed.
7. Send a POST request using POSTMAN. Make sure you send the right URL. You can check your URL from your terminal when you start your Python server. The default is http://127.0.0.1:8000.
8. Make sure to include `X-CSRFToken` within Headers. Inside the header in POSTMAN, you will find your csrf_token value next to the Cookie. Copy that csrf_token and paste it as a value next to `X-CSRFToken` you just created.
9. Send a POST request to http://127.0.0.1:8000/encode/. Make sure to include in your body `original_url` as a key and your URL as a value.
10. If everything is properly set up, you will see a JSON response in the body with `shortened_url` as `'shortened_url': <your_shortened_url>`.
11. Copy the shortened_url value.
12. Change your link to the decode URL http://127.0.0.1:8000/decode/ and send a POST request with `shortened_url` as the key and the copied shortened_url from the previous request as the value.
13. If everything is properly set up, you should see your original URL as a JSON response in the body as `'original_url': <your_original_url>`.
