from django.shortcuts import render
from datetime import date

# Create your views here.
def myview(request):
	# fetch the current datetime
	today = date.today()
	# send the current date to the template using the third argument of render
	return render(request, "index.html", {"mydate": today})
