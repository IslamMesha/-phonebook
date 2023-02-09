from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from contacts.models import Contact


def index(request):
    contacts = Contact.objects.all()
    return render(request, "contact_list.html", {"contacts": contacts})


def detail(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, "contact_detail.html", {"contact": contact})


def edit(request, contact_id):
    contact = Contact.objects.get(id=contact_id)

    if request.method == 'POST':
        contact.name = request.POST.get('name', contact.name)
        contact.phone = request.POST.get('phone', contact.phone)
        contact.email = request.POST.get('email', contact.email)
        contact.address = request.POST.get('address', contact.address)
        contact.save()
        return redirect(reverse('contact_detail', args=[str(contact.id)]))
    return render(request, 'contact_edit.html', {'contact': contact})


def delete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    contacts = Contact.objects.all()
    return redirect(reverse("contact_list"), {"contacts": contacts})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact = Contact(name=name, phone=phone, email=email, address=address, user=User.objects.first())
        contact.save()
        return redirect(reverse('contact_list'))
    return render(request, 'add_contact.html')
