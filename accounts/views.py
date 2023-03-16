from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from oglasi_app import settings
from oglasi_app.mail import send_mailgun_mail
from accounts.models import Account
from django.urls import reverse

from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        terms = request.POST.get('terms')
        privacy = request.POST.get('privacy')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number', '')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        type = request.POST.get('type')
        identification_number = request.POST.get('identification_number', '')
        tax_id = request.POST.get('tax_id', '')
        newsletter_subscribed = True if request.POST.get('newsletter_subscribed') else False
        address = request.POST.get('address')

        try:
            if type == "1":
                if not identification_number or not tax_id:
                    raise ValueError('PIB i Matični broj obavezni')
                
                if not address:
                    raise ValueError('Adresa je obavezan podatak')

            if password != confirm_password:
                raise ValueError('Lozinke se ne poklapaju')
            
            if not terms or not privacy:
                raise ValueError('Molimo prihvatite pravila i uslove korištenja')
            
            emailExists = Account.objects.filter(email=email)
            usernameExists = Account.objects.filter(username=username)

            if emailExists or usernameExists:
                raise ValueError('Email ili korisničko ime zauzeto')

            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                phone_number=phone_number,
                type=type,
                identification_number=identification_number,
                tax_id=tax_id,
                newsletter_subscribed=newsletter_subscribed,
                address=address
            )
            user.save()
            response_data = {'success': True}
        
            
            # User activation
            current_site = get_current_site(request)
            full_name = first_name + ' ' + last_name
            activate_url = reverse('activate', kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)), 'token': default_token_generator.make_token(user)})
            link = f"https://{current_site}{activate_url}"
            data = {
                "first_name": first_name,
                "link": link
            }
            send_mailgun_mail(email, full_name, 'Verifikujte vaš nalog', 'email_verification', data)
        
        except Exception as e:
            response_data = {'success': False, 'error': str(e)} 

        return JsonResponse(response_data, safe=False)

    else:
        return render(request, 'account_pages/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'You are now logged in.')
            return JsonResponse({ "success": True}, safe=False)
        else:
            return JsonResponse({ "success": False}, safe=False)

    return render(request, 'account_pages/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('home')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations, you have successfully activated your account')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


def forgot_password(request):
    if request.method == 'POST':
        email_address = request.POST['email']

        if Account.objects.filter(email=email_address).exists():
            user = Account.objects.filter(email__icontains=email_address).first()
            current_site = get_current_site(request)
            activate_url = reverse('reset_password_valited', kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)), 'token': default_token_generator.make_token(user)})
            link = f"https://{current_site}{activate_url}"
            data = {
                "first_name": user.first_name,
                "link": link
            }
            send_mailgun_mail(user.email, user.first_name, 'Izmenite vašu lozinku', 'forgot_password', data)
            messages.success(request, 'Password reset email has been sent to your email address')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist.')
            return redirect('forgot_password')

    return render(request, 'account_pages/forgot_password.html')


def reset_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request, 'This link expired')
        return redirect('login')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password changed!')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('reset_password')

    return render(request, 'account_pages/reset_password.html')
