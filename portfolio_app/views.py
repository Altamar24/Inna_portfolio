from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact, Price, Photo, Question
from .forms import ContactForm

def home(request):
    contacts = Contact.objects.first()
    photos = Photo.objects.all()
    return render(request, 'portfolio_app/index.html', {'current_page': 'home', 'contacts': contacts, 'photos': photos})

def information(request):
    price_ids = [1, 2, 3, 4, 5, 6, 7]
    prices = Price.objects.filter(pk__in=price_ids).in_bulk()
    
    context = {
        'current_page': 'information',
        'price_1': prices.get(1),
        'price_2': prices.get(2),
        'price_3': prices.get(3),
        'price_4': prices.get(4),
        'price_5': prices.get(5),
        'price_6': prices.get(6),
        'price_7': prices.get(7),
    }
    return render(request, 'portfolio_app/information.html', context)

def portfolio(request):
    return render(request, 'portfolio_app/portfolio.html', {'current_page': 'portfolio'})

def faqs(request):
    questions = Question.objects.all()
    return render(request, 'portfolio_app/faqs.html', {'current_page': 'faqs', 'questions': questions})

def contact(request):
    success = False
    contacts = Contact.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"""
            Имя: {name}
            Email: {email}
            Телефон: {phone}
            Тип услуги: {subject}
            Сообщение:
            {message}
            """

            send_mail(
                subject=f"Новое сообщение с сайта: {subject}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],  # или ваш email для получения
                fail_silently=False,
            )
            success = True
            form = ContactForm()  # очистить форму после отправки
    else:
        form = ContactForm()
    return render(request, 'portfolio_app/contact.html', {'form': form, 'success': success, 'current_page': 'contact', 'contacts': contacts})
