from safetylist.models import Checklist, ChecklistForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404

def addcontact(request):
	form = ChecklistForm(request.POST)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/list/')
#	else:
#		formset = ContactForm ()
	return render(request,"awlist.html", {"form":form})
	
def listcontact(request):
	contact = Checklist.objects.all()
	context ={'contact': contact}
	return render(request, 'checklist2.html', context)
	
	
def detailcontact(request, pk):
		contact = Checklist.objects.get(pk=pk)
		return render(request, 'list2.html', {'user':contact})
	
