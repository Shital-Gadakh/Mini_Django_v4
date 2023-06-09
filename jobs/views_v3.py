from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Applicant
from django.contrib.auth.models import User


class Applicants(APIView):

    def get(self, request):
        applicants = Applicant.objects.all()
        # TODO - write logic to make json serializable dict and pass it to Response
        return Response(applicants)

    def post(self, request):
        # TODO - write logic to take json input from `request.body`
        # TODO - write ORM queries to create new record in database.
        pass

    def delete(self, request):
        # TODO - write logic to take json input from `request.body`
        # TODO - write ORM queries to delete record in database.
        pass


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        final = dict()
        for user in users:
            final["id"] = {"first_name": user.first_name,
                           "email": user.email}
        return Response(final)





