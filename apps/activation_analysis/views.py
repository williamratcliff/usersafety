# Create your views here.

import hashlib,os
import types
import tempfile

import random
from numpy import NaN
from numpy import array
import numpy as np
import hmac

from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.utils import simplejson
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #paging for lists
from django.core.exceptions import ObjectDoesNotExist
import cStringIO, gzip
from django.db import transaction
from django.core.mail import send_mail

## models
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.conf import settings
from django.template import RequestContext, loader
import periodictable
from periodictable import activation

class ActivationForm(forms.Form):
    #like_website = forms.TypedChoiceField(
        #label = "Do you like this website?",
        #choices = ((1, "Yes"), (0, "No")),
        #coerce = lambda x: bool(int(x)),
        #widget = forms.RadioSelect,
        #initial = '1',
        #required = True,
    #)

    chemical_formula = forms.CharField(
        label = "Chemical Formula",
        max_length = 80,
        required = True,
    )

    mass = forms.IntegerField(
        label = "Mass (g)",
        #max_length = 80,
        required = True,
    )

    time_on = forms.DecimalField(
        label = "Time on Beam (hours)",
        required = True,
    )
    
    time_off = forms.DecimalField(
            label = "Time off Beam (hours)",
            required = True,
        )  
    
    flux = forms.DecimalField(
           label = "Instrument Flux (n/cm^2/s)",
           #max_length = 80,
           required = True,
       )    

    #notes = forms.CharField(
        #label = "Additional notes or feedback",
        #required = False,
    #)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-activationForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        #self.helper.form_action = 'submit_calculation'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(ActivationForm, self).__init__(*args, **kwargs)    



#@login_required()
def activation_view(request):
    
    #redirect_url = request.GET.get('next')

    # Form handling logic
    #[...]
    print 'reached'
    #if redirect_url is not None:
    #    activation_form.helper.form_action = reverse('submit_calculation') + '?next=' + redirectUrl
    if request.method == 'POST':
        print 'posting'
        activation_form = ActivationForm(request.POST)
        if activation_form.is_valid():
            cleaned_data=activation_form.cleaned_data
            print 'valid'
            
            #activation.load_table()
            fast_ratio=50
            Cd_ratio=70
            fluence=float(cleaned_data['flux'])
            mass=cleaned_data['mass']
            chemical_formula=cleaned_data['chemical_formula']
            exposure=float(cleaned_data['time_on'])
            rest_times=[0,1,24,360,float(cleaned_data['time_off'])]
            env = activation.ActivationEnvironment(fluence=fluence,Cd_ratio=Cd_ratio,
                                                           fast_ratio=fast_ratio,location="BT-2")
            sample = activation.Sample(chemical_formula, mass)
            sample.calculate_activation(env, exposure=exposure, rest_times=rest_times)
            sample.show_table()   
            total = [0]*len(sample.rest_times)
            rows = []
            for el,activity_el in activation._sorted_activity(sample.activity.items()):
                total = [t+a for t,a in zip(total,activity_el)]
                rows.append([el.isotope,el.daughter,el.reaction,el.Thalf_str]+activity_el)
        
            result = { 
                'success': True,
                'sample': chemical_formula,
                'mass': mass,
                'flux': fluence,
                'fast': fast_ratio,
                'Cd': Cd_ratio,
                'exposure': exposure,
                'rest': rest_times,
                'activity': rows, 
                'total': total,
            }
            return HttpResponse(simplejson.dumps(result))
            #return HttpResponseRedirect("/results/")
    else:
        activation_form=ActivationForm()
    return render_to_response("activation.html", {'activation_form': activation_form}, context_instance=RequestContext(request))