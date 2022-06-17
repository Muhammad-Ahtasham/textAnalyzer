import imp
from django.http import HttpResponse
from django.shortcuts import render

def index(reqeust):
    return render(reqeust, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    
    if removepunc== 'on':
        print(removepunc)
        print(djtext)
        punc = '''!"£$%^&*()_,{?/#'}~;'''
        analyzed = ""
        for char in djtext:
            if char not in punc:
                analyzed = analyzed+char
        
        params = {
        'purpose': 'remove puctuations',
        'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params )
    elif(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.upper()
        
        params = {
        'purpose': 'CHANGE TO UPPER CASE',
        'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params )
    
    elif(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed+char 

        params = {
        'purpose': 'Remove New line ',
        'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params ) 
    else:
        return HttpResponse("error")