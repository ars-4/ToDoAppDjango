from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Notes
from core.serializers import NotesSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/core/',
            'method': 'GET',
            'body': None,
            'description': 'Returns Array Of Notes'
        },
        {
            'Endpoint': '/core/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns A Single Note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Notes.objects.all()
    serializer = NotesSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Notes.objects.get(id=pk)
    serializer = NotesSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Notes.objects.create(
        title = data['title'],
        body = data['body']
    )
    serializer = NotesSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Notes.objects.get(id=pk)
    serializer = NotesSerializer(note, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Notes.objects.get(id=pk)
    note.delete()
    return Response("You just deleted a Note")