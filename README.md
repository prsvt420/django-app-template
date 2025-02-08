# Django app template

## Technologies and Tools

#### Programming Languages and Frameworks
- **Python 3.11**
- **Django 5**

### Development Tools
- **Mypy**
- **Flake8**
- **Black**
- **Isort**
- **Pre-commit**
- **Git**
- **GitHub**
- **Poetry**

### Databases
- **Redis**
- **PostgreSQL**

### Web Technologies
- **HTML**
- **CSS**
- **JavaScript**
- **JQuery**

### Server Technologies and Security
- **Gunicorn**
- **Nginx**
- **CSP**
- **HTTPS**
- **The nginx version is disabled**

### Containerization
- **Docker**
- **Docker Compose**

### Background Task Processing
- **Celery**

## Getting started

### 1. Create it .env at the root of the project:

```dotenv
# DJANGO SECRET KEY
SECRET_KEY=...

# DJANGO DEBUG
DEBUG=False

# DATABASE CONNECT SETTINGS
POSTGRES_DB=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...
POSTGRES_HOST=database# docker container name

# REDIS CONNECT SETTINGS
REDIS_LOCATION=redis://redis:6379# redis container name

# SMTP
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...
```

### 2. Add your IP and DOMAIN to the collection ALLOWED_HOSTS in setting.py and nginx/nginx.conf:
```python3.11
#  django_app_template/setting.py

ALLOWED_HOSTS: List[str] = [
    "127.0.0.1",
    "YOUR IP",
    "YOUR DOMAIN",
    "YOUR www.DOMAIN"
```

### 3. Getting a certificate (at the first launch):

```shell
sudo docker run -it --rm \
  -v "./nginx/certbot:/var/www/certbot" \
  -v "/etc/letsencrypt:/etc/letsencrypt" \
  certbot/certbot certonly \
  --webroot \
  --webroot-path=/var/www/certbot \
  -d DOMAIN \
  -d www.DOMAIN \
  --email EMAIL \
  --agree-tos \
  --no-eff-email
```

**Note:** *You can only get a certificate when the server is running.*

### 4. It is necessary to uncomment parts of the code in nginx/nginx.conf. It is necessary to uncomment parts of the code in nginx/nginx.conf. Then rebuild docker compose:

```shell
sudo docker compose up --build
```
