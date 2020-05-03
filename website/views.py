from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
	if request.method == 'POST':
		client_email = request.POST['client_email']

		send_mail(
			'Sign up new follower',
			f"Hi, You have new follower, let's go:{client_email}" ,
			client_email,
			['chrispan456@gmail.com']
			)
		return render(request, 'website/index.html')
	else:

		return render(request, 'website/index.html')

def contact(request):
	if request.method =='POST':
		message_FN = request.POST['message_FN']
		message_LN = request.POST['message_LN']
		message_email = request.POST['message_email']
		message = request.POST['message']
		
		send_mail(
			message_FN, #subject
			message_LN, #message
			message_email, #from email
			['chrispan456@gmail.com'], #to email

			)


		return render(request, 'website/contact.html', {"message_FN": message_FN, "message_LN": message_LN})

	else:
		
		return render(request, 'website/contact.html', {})

def about(request):
	return render(request, 'website/about.html')

def gallery(request):
	return render(request, 'website/gallery.html')


def packages(request):
	return render(request, 'website/packages.html')


def pricing(request):
	return render(request, 'website/pricing.html')