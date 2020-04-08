

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display=('category_id','area','category_name')
	class meta:
		model=Categorie
admin.site.register(Categorie,CategoryAdmin)

class Sub_CategoryAdmin(admin.ModelAdmin):
	list_display=('sub_category_id','sub_category_name','category')
	class meta:
		model=Sub_categorie
admin.site.register(Sub_categorie,Sub_CategoryAdmin)

class QuestionAdmin(admin.ModelAdmin):
	list_display=('question','qtype','option_1','option_2','option_3','option_4','answer','category_name','sub_category_name')
	class meta:
		model=Question
admin.site.register(Question,QuestionAdmin)

class CandidateAdmin(admin.ModelAdmin):
	list_display=('candidate_id','name','email','level_of_expertise','area_of_expertise')
	class meta:
		model=Candidate
admin.site.register(Candidate,CandidateAdmin)
