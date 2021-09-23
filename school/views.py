from django.http import JsonResponse

def students(request):
    if request.method == 'GET':
        aluno = {
            'id':1,
            'name':'Test',
        }
        return JsonResponse(aluno)