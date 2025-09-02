"""
Django settings for mysite project.
"""

from pathlib import Path

# Базова директорія проєкту (де лежить manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent


# Секретний ключ для шифрування (зберігає cookies, токени)
SECRET_KEY = 'django-insecure-vr9++r1i66)tua#ccu(cm4edl^vug80748l45fyoi(d2qpb^$p'

# Режим налагодження: True → показує детальні помилки (лише для розробки)
DEBUG = True

# Дозволені хости (домени/айпі з яких можна відкривати сайт)
ALLOWED_HOSTS = []


# Додатки Django, які увімкнені у проєкті
INSTALLED_APPS = [
    'django.contrib.admin',        # Панель адміністратора
    'django.contrib.auth',         # Аутентифікація користувачів
    'django.contrib.contenttypes', # Підтримка моделей різних типів
    'django.contrib.sessions',     # Сесії користувачів
    'django.contrib.messages',     # Flash-повідомлення
    'django.contrib.staticfiles',  # Статичні файли (CSS, JS, картинки)
]

# Обробники запитів між сервером і додатком
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',           # Захист і HTTPS
    'django.contrib.sessions.middleware.SessionMiddleware',    # Сесії
    'django.middleware.common.CommonMiddleware',               # Загальні функції
    'django.middleware.csrf.CsrfViewMiddleware',               # Захист від CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Авторизація
    'django.contrib.messages.middleware.MessageMiddleware',    # Повідомлення
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Захист від Clickjacking
]

# Файл з маршрутами (urls.py)
ROOT_URLCONF = 'mysite.urls'

# Налаштування шаблонів (HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # Використання шаблонізатора Django
        'DIRS': [],        # Список папок з власними шаблонами
        'APP_DIRS': True,  # Шукати шаблони у кожному app
        'OPTIONS': {
            'context_processors': [ # Автоматично передавати в шаблони:
                'django.template.context_processors.request', # Об’єкт request
                'django.contrib.auth.context_processors.auth', # Інформація про користувача
                'django.contrib.messages.context_processors.messages', # Повідомлення
            ],
        },
    },
]

# Точка входу WSGI для запуску сайту на сервері
WSGI_APPLICATION = 'mysite.wsgi.application'


# База даних (за замовчуванням SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Яка БД використовується
        'NAME': BASE_DIR / 'db.sqlite3',        # Файл з базою даних
    }
}


# Валідація паролів (перевірка складності)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # Пароль не схожий на ім’я
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # Мінімальна довжина
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # Заборона простих паролів
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # Заборона лише цифрових паролів
    },
]


# Інтернаціоналізація (мова і час)
LANGUAGE_CODE = 'en-us'  # Мова сайту
TIME_ZONE = 'UTC'        # Часовий пояс
USE_I18N = True          # Використання перекладу
USE_TZ = True            # Використання часових поясів


# Статичні файли (CSS, JS, зображення)
STATIC_URL = 'static/'

# Тип первинного ключа за замовчуванням для моделей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
