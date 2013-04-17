from django.db import models
from django.forms import ModelForm
# Create your models here.

class Checklist(models.Model):
		name		   = models.CharField (max_length =255, blank = False)
		phone		   = models.IntegerField()
		emerg_contact  = models.CharField (max_length =255, blank = False)
		relationship   = models.CharField (max_length =255, blank = False)
		home_inst	   = models.CharField (max_length =255, blank = False)
		nist_contact   = models.CharField (max_length =255, blank = False)
		nist_div	   = models.CharField (max_length =255, blank = False)
		nist_ext	   = models.IntegerField()

		
		emerg_num	 = models.CharField (max_length =2, blank=False)
		emerg_action = models.CharField (max_length =2, blank=False)
		accid_rep 	 = models.CharField (max_length =2, blank=False)
		gen_lab 	 = models.CharField (max_length =2, blank=False)
		saf_info 	 = models.CharField (max_length =2, blank=False)
		protective	 = models.CharField (max_length =2, blank=False)
		hazacomm 	 = models.CharField (max_length =2, blank=False)
		comp_reg 	 = models.CharField (max_length =2, blank=False)
		inst_op 	 = models.CharField (max_length =2, blank=False)
		crane_saf 	 = models.CharField (max_length =2, blank=False)
		liq_handle 	 = models.CharField (max_length =2, blank=False)
		gen_acid 	 = models.CharField (max_length =2, blank=False)
		hyd_acid 	 = models.CharField (max_length =2, blank=False)
		glove_box 	 = models.CharField (max_length =2, blank=False)
		x_ray 	     = models.CharField (max_length =2, blank=False)
		lab_torch 	 = models.CharField (max_length =2, blank=False)
		spin_coater  = models.CharField (max_length =2, blank=False)
		furnace 	 = models.CharField (max_length =2, blank=False)
		lab_press 	 = models.CharField (max_length =2, blank=False)
		other 	     = models.CharField (max_length =2, blank=False)
#		other_text	 = models.CharField (max_length =255, blank=True null=True)

#		def	__str__(self):
#			return self.name

		
class ChecklistForm (ModelForm):
	class Meta:
		model = Checklist