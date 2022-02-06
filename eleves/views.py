from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime

from .forms import ClasseForm
# Create your views here.





def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Ibou Sarr"
    month = month.capitalize()
    # concert month to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    # current year
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M')
    # the calendar

    cal = HTMLCalendar().formatmonth(year, month_number)

    return render(request, 'eleves/home.html', {
        'name': name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "current_year": current_year,
        "time": time,
        "cal": cal
        })


def addClasse(request):

    form = ClasseForm()
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context = {
        'form': form
    }

    return render(request, 'eleves/add_student.html', context)