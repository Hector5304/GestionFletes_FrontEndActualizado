from django.contrib.auth import get_user_model

User = get_user_model()

username = 'demo_user'
email = 'demo@example.com'
password = 'DemoPass123!'

if not User.objects.filter(username=username).exists():
    User.objects.create_user(username=username, email=email, password=password)
    print(f"Usuario '{username}' creado con contraseña '{password}'")
else:
    print(f"Usuario '{username}' ya existe")
