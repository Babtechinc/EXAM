from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from rest_framework import status
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import examserial
# Create your views here.
from  .models import exam

@api_view(['GET'])
def api(response):
    api_url= {
        'List': '/exam_list/',
        'Detail View': '/examdetail/<str:pk>',
        'Create': '/examcreate/',
        'Update': '/examupdate/<str:pk>/',
        'Delete': '/examdelete/<str:pk>/',

    }
    return Response(api_url)
@api_view(['GET'])
def examlist(response):
    examque = exam.objects.all()
    examqueserial = examserial(examque,many=True)
    return Response(examqueserial.data)

@api_view(['GET'])
def examdetail(response,pk):
    examque = exam.objects.get(id=pk)
    examqueserial = examserial(examque,many=False)
    return Response(examqueserial.data)
@api_view(['POST'])
def examcreate(response):
    examqueserial = examserial(data=response.data)
    if examqueserial.is_valid():
        examqueserial.save()
    return Response(examqueserial.data)


@api_view(['POST'])
def examupdate(response,pk):
    examque = exam.objects.get(id=pk)
    examqueserial = examserial(instance=examque,data=response.data)
    if examqueserial.is_valid():
        examqueserial.save()
    return Response(examqueserial.data)

@api_view(['DELETE'])
def examdelete(response,pk):
    examque = exam.objects.get(id=pk)
    examque.delete()

    return Response("deleted")

#

def examque2(response):
    page_obj = exam.objects.all()
    dict_answer = {

    }
    if response.method == 'POST':
        for key,val in response.POST.items():
            dict_answer.update({key: val})
    examNo = page_obj.count()
    dict_id={}
    for key in range(1,examNo+1):

        dict_id.update({key:key})

    print(dict_answer)
    print(dict_id)
    print('hIi')

    pickId=zip(page_obj,dict_id)

    dict_Q ={'page_obj':page_obj,'Number':examNo,'selectedi':dict_answer,'dict_id':pickId }


    return render(response,'[AJAX]exam.html',context=dict_Q)


def examque(response):
    examlist = exam.objects.all()
    paginator = Paginator(examlist, 1)  # Show 25 contacts per page.
    page_number = response.GET.get('page')
    page_obj = paginator.get_page(page_number)
    examNo =examlist.count()
    if response.method == 'POST':
    # form = NameForm(request.POST)
        print(response.POST)
        dict_selected = response.POST.get('1', False);
        print(dict_selected)
    dict_Q ={'page_obj':page_obj,'Number':examNo,'key':"1950s"}
    print(dict_Q)

    return render(response,'',context=dict_Q)


def get_mark(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        redirect("summit")
    # form = NameForm(request.POST)
        print(request.POST)
        print('iam hehr')
    return HttpResponse('summit')