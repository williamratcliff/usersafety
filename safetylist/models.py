from django.db import models
from django.forms import ModelForm
from django.contrib.localflavor.us.models import PhoneNumberField

# Create your models here.

class Checklist(models.Model):
		name		   = models.CharField (max_length =255, blank = False)
		phone		   = models.IntegerField() # PhoneNumberField()
		emerg_contact  = models.CharField (max_length =255, blank = False)
		relationship   = models.CharField (max_length =255, blank = False)
		home_inst	   = models.CharField (max_length =255, blank = False)
		nist_contact   = models.CharField (max_length =255, blank = False)
		nist_div	   = models.CharField (max_length =255, blank = False)
		nist_ext	   = models.IntegerField() # custom validate data for 4 digit

		
		emerg_num	 = models.BooleanField()
		emerg_action = models.BooleanField()
		accid_rep 	 = models.BooleanField()
		gen_lab 	 = models.BooleanField()
		saf_info 	 = models.BooleanField()
		protective	 = models.BooleanField()
		hazacomm 	 = models.BooleanField()
		comp_reg 	 = models.BooleanField()
		inst_op 	 = models.BooleanField()
		crane_saf 	 = models.BooleanField()
		liq_handle 	 = models.BooleanField()
		gen_acid 	 = models.BooleanField()
		hyd_acid 	 = models.BooleanField()
		glove_box 	 = models.BooleanField()
		x_ray 	     = models.BooleanField()
		lab_torch 	 = models.BooleanField()
		spin_coater  = models.BooleanField()
		furnace 	 = models.BooleanField()
		lab_press 	 = models.BooleanField()
		other 	     = models.BooleanField()
#		other_text	 = models.CharField (max_length =255, blank=True null=True)

#		def	__str__(self):
#			return self.name

		
class ChecklistForm (ModelForm):
	class Meta:
		model = Checklist
		
		#reportlab to generate the PDF file