from safetylist.models import Checklist, ChecklistForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
import os,sys
from subprocess import Popen, PIPE
import hashlib
from django.core.mail import send_mail, EmailMessage
import logging

logger=logging.getLogger(__name__)

def addcontact(request):
    if request.method=='POST':
        form = ChecklistForm(request.POST)
        if form.is_valid():
#            t=render(request,"checklist.html", {"form":form})
            signature=form.data['output']
            t=render(request,"checklist.html", {"form":form, "signature":signature})
            temp_html=t.content
            logger.error("template_html "+temp_html)
#            myfile=open(r'/tmp/outfile.html','w')
            myfilebase=hashlib.sha1(temp_html).hexdigest()
            logger.error("myfilebase "+myfilebase)
            myfilename_html=os.path.join(r'/tmp/',myfilebase+'.html')
            myfilename_pdf=os.path.join(r'/tmp/',myfilebase+'.pdf')
            #myfilename_pdf=os.path.join(r'/tmp/','abc.pdf')
            myfile=open(myfilename_html,'w')
            myfile.write(temp_html)
            myfile.close()	
#            process=Popen(["/Applications/wkhtmltopdf.app/Contents/MacOS/wkhtmltopdf", 'file://'+myfilename_html, myfilename_pdf])
#            process=Popen(["/Applications/wkhtmltopdf.app/Contents/MacOS/wkhtmltopdf", "/tmp/outfile.html", "outfile.pdf"])
            process=Popen(["wkhtmltopdf", "--disable-javascript", 'file://'+myfilename_html, myfilename_pdf])			
#            if form.is_valid():
#            signature=form.cleaned_data["signature"]
            form.save()
            if 0:
                email = EmailMessage("Safety Check form","Safety Check form is attached","patrick8100@gmail.com",["patrick8100@gmail.com"])
                #email.attach_file('outfile.pdf')
                email.attach_file(myfilename_pdf)
                email.send()
            return HttpResponseRedirect('/thanks/')
    else:
        form= ChecklistForm()
#		if 0:
#			t=render(request,"awlist.html", {"form":form, "signature":signature})
#			myfile=open(r'/tmp/outfile.html','w')
#			myfile.write(t.content)
#			myfile.close()	
    try:
        signature=form.data['output']
    except:
        signature=''
    return render(request,"checklist.html", {"form":form,"signature":signature})

def listcontact(request):
    contact = Checklist.objects.all()
    context ={'contact': contact}
    return render(request, 'checklist2.html', context)

def thanks(request):
    return render(request,'thanks.html')

def detailcontact(request, pk):
    contact = Checklist.objects.get(pk=pk)
    return render(request, 'list2.html', {'user':contact})
