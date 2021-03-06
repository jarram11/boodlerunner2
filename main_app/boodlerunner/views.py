from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse
from .forms import LoginForm
from .forms import boodleReceiverForm
from .forms import boodleRunnerForm


def welcome(request):
    return render(request, 'boodlerunner/welcome.html', {})
    #form = boodleReceiverForm()
    #return render(request, 'boodlerunner/welcome.html','boodleReceiverInfo': receiverInfo, 'forms':form)

def menu(request):
	return render(request, 'boodlerunner/menu.html', {})

def order(request):
	form = boodleReceiverForm(request.POST  or None)
	if form.is_valid():
		receiverInfo  = boodleReceiver(name = forms.cleaned_data['name'],
										phoneNumber  = forms.cleaned_data['phone number'],
										barracks =   forms.cleaned_data['barracks'],
										roomNumber =   forms.cleaned_data['room number'],
										restaurant =   forms.cleaned_data['restaurant'],
										timeOfArrival =   forms.cleaned_data['time of arrival'],
										additionalInstruction =   forms.cleaned_data['additional instruction'],
										receiverCompany = forms.cleaned_data['company'],)
		receiverInfo.save()
	return render(request,'boodlerunner/order.html',{'form': form})


def updateRunner(request):
	form = boodleRunnerForm(request.POST  or None)
	if form.is_valid():
		runnerInfo  = boodleRunner(name = forms.cleaned_data['name'],
										phoneNumber  = forms.cleaned_data['phone number'],
										barracks =   forms.cleaned_data['barracks'],
										runnerCompany = forms.cleaned_data['company'],)
		runnerInfo.save()
	return render(request,'boodlerunner/runner.html',{'form': form})

def signup(request):
    form = UserCreationForm()
    return render(request, 'boodlerunner/signup.html', {'form': form})

def loginPage(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			if user is not None:
				if user.is_active:
					login(request, user)
					return render(request, 'boodlerunner/order.html', {'form':form})

				else:
					print("disabled")
			else:
				print('incorrect')
	else:
		form =LoginForm()
		return render(request, 'boodlerunner/order.html',{'form':form})



def receipt(request):
	return render(request, 'boodlerunner/receipt.html', {})

def get_order(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = boodleReceiverForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['name']
            phoneNumber = form.cleaned_data['phoneNumber']
            barracks =   form.cleaned_data['barracks']
            roomNumber =  form.cleaned_data['roomNumber']
            restaurant =  form.cleaned_data['restaurant']
            timeOfArrival =   form.cleaned_data['timeOfArrival']
            additionalInstruction =   form.cleaned_data['additionalInstruction']
            receiverCompany =   form.cleaned_data['receiverCompany']
            context = {'name':name , 'phoneNumber':phoneNumber , 'barracks':barracks , 'roomNumber':roomNumber , 'restaurant':restaurant , 'timeOfArrival':timeOfArrival, 'additionalInstruction':additionalInstruction, 'receiverCompany':receiverCompany }
            print('form is validd')
            return render(request, 'boodlerunner/receipt.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = boodleReceiverForm()

    return render(request, 'boodlerunner/receipt.html', {'form': form})

#def post_boodleReceiverInfo(request):
#	form = boodleReceiverForm(request.POST)
#	if form.is_valid():
#		receiverInfo  = boodleReceiver(name = forms.cleaned_data['name'],
#										phoneNumber  = forms.cleaned_data['phone number'],
#										barracks =  = forms.cleaned_data['barracks'],
#										roomNumber =  = forms.cleaned_data['room number'],
#										restaurant =  = forms.cleaned_data['restaurant'],
#										timeOfArrival =  = forms.cleaned_data['time of arrival'],
#										additionalInstruction =  = forms.cleaned_data['additional instruction'],
#										receiverCompany = f = forms.cleaned_data['company'],)
#		receiverInfo.save()
#	return HttpResponseRedirect('boodlerunner/welcome.html')