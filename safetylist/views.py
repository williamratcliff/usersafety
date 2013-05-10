from safetylist.models import Checklist, ChecklistForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
import os,sys
from subprocess import Popen, PIPE
import hashlib

def addcontact(request):
	if request.method=='POST':
		form = ChecklistForm(request.POST)
		if 1:
			t=render(request,"checklist3.html", {"form":form})
			temp_html=t.content
			myfilebase=hashlib.sha1(temp_html).hexdigest()
			myfilename_html=os.path.join(r'/tmp',myfilebase+'.html')
			myfilename_pdf=os.path.join(r'/tmp',myfilebase+'.pdf')
			myfile=open(myfilename_html,'w')
			myfile.write(temp_html)
			myfile.close()	
			process=Popen(["wkhtmltopdf", 'file://'+myfilename_html, myfilename_pdf])
			#process=Popen(["wkhtmltopdf", "--disable-javascript", 'file://'+myfilename_html, myfilename_pdf])			
			print "done"		
		if form.is_valid():
			
			#form.save()
			return HttpResponseRedirect('/list/')
	else:
		form= ChecklistForm()
		if 0:
			t=render(request,"awlist.html", {"form":form})
			myfile=open(r'/tmp/outfile.html','w')
			myfile.write(t.content)
			myfile.close()	
			
			
	return render(request,"checklist3.html", {"form":form})
	
def listcontact(request):
	contact = Checklist.objects.all()
	context ={'contact': contact}
	return render(request, 'checklist2.html', context)
	
	
def detailcontact(request, pk):
		contact = Checklist.objects.get(pk=pk)
		return render(request, 'list2.html', {'user':contact})
	
