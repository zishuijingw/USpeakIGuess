from django.shortcuts import render
from django.http import HttpResponseRedirect
from AuthorIdentification.inputoutput import input_output  #test tmp

# Create your views here.
def AuthorIdView(request):
    #test tmp import
    user_input_test=""
    IdentifyResult="before test"
    if request.POST:
        user_input_test=request.POST.get('user_input_test', '')
        #test tmp import
        IdentifyResult=input_output(user_input_test)
    return render(request, 'AuthorIdentification.html', {'resp': IdentifyResult, 'user_input_test':user_input_test})

def Identify(request):
    # new_test_item = AuthorIditem(content=test_item)
    # new_test_item.save()
    # return HttpResponseRedirect('/AuthorIdentification/')
    #test tmp import
    # user_input_test=""
    # IdentifyResult="before test"
    # if request.POST:
    #     user_input_test=request.POST.get('user_input_test', '')
    #     #test tmp import
    #     IdentifyResult=input_output(user_input_test)
    # return render(request, 'AuthorIdentification.html', {'resp': IdentifyResult, 'user_input_test':user_input_test})
    return HttpResponseRedirect('/AuthorIdentification/')

def Backhome(request):
    return HttpResponseRedirect('/home/')