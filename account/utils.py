from django.core.mail import send_mail

def send_activation_email(email, activation_code, is_password):
    activation_url = f'http://localhost:8000/api/v1/account/activate/{activation_code}'
    if not is_password:
        message = f'Thank you for registration!\nTo activate your account, please, click link here {activation_url}'
    else:
        message = activation_code
    send_mail('StackOVewFlow Activation', message, 'insan@insan.com', [email, ], fail_silently=False)