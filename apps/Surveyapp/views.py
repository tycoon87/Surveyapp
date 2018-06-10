from django.shortcuts import render, HttpResponse, redirect



def index (request):
    return render (request, 'Surveyapp/index.html')

def addinfo (request):
    if request.method == "POST":
        request.session['FirstName'] = request.POST['FirstName']
        request.session['LastName'] = request.POST['LastName']
        request.session['Location'] = request.POST['Location']
        request.session['Favorate'] = request.POST['Favorate']
        request.session['comments'] = request.POST['comments']
        request.session['formcount'] = 0
        request.session['formcount'] =+ 1
        print request.session['formcount']
        return render (request, 'Surveyapp/info.html')
    else:
        return redirect('/')

def clearsession (request):
    request.session.clear()
    return redirect('/')