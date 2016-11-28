from django.shortcuts import render
# Create your views here.
# from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from .models import Guestbook


def myguestbook(requests):
    return render_to_response('myguestbook/guestbook.html')


def success(requests):
    guest = Guestbook.objects.all()
    return render_to_response('myguestbook/success.html', {'guest': guest})


@csrf_exempt
def guestbook_insert(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            g = Guestbook()
            g.savedata(request.POST.get('subject', ''), request.POST.get('email', ''), request.POST.get('message', ''))
            return HttpResponseRedirect('/success/')

    return render_to_response('myguestbook/guestbook.html',
                              {'errors': errors,
                               'subject': request.POST.get('subject', ''),
                               'message': request.POST.get('message', ''),
                               'email': request.POST.get('email', ''),
                               }
                              )

def guestbook_delete(request):
    guest = Guestbook.objects.all()
    return render_to_response('myguestbook/delete.html', {'guest' : guest})

def delete(request):
    n = request.GET['no']
    no = int(n)

    g = Guestbook.objects.all()
    t = g[no-1].title
    c = g[no-1].content
    g[no-1].delete()

    msg = '제목 : %s <br>' % t
    msg += '내용 : %s <br>' % c
    msg += "삭제되었습니다."
    msg += "<p><a href=/success> 방명록 목록 보기 </a>"
    return HttpResponse(msg)

def guestbook_update(request):
    guest = Guestbook.objects.all()
    return render_to_response('myguestbook/update.html', {'guest' : guest})
