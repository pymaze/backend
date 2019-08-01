from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class RoomsView(APIView):
    permission_classes = [IsAuthenticated]

    def index(request):
        return JsonResponse({"message": "API entrypoint.  API is stable and operating.  Please consult repository documentation for specifics on the consumption of this API.", "repository_url": "https://github.com/cs19-build-week-1/backend"})

    def get(self, request):
        return JsonResponse([

            [
                {"n": 0, "e": 0, "s": 1, "w": 0},
                {"n": 0, "e": 1, "s": 0, "w": 0},
                {"n": 0, "e": 0, "s": 1, "w": 1},
                {"n": 0, "e": 0, "s": 0, "w": 0}

            ],
            [
                {"n": 1, "e": 1, "s": 0, "w": 0},
                {"n": 0, "e": 0, "s": 1, "w": 1},
                {"n": 1, "e": 1, "s": 0, "w": 0},
                {"n": 0, "e": 0, "s": 0, "w": 1}],
            [
                {"n": 0, "e": 0, "s": 1, "w": 0},
                {"n": 1, "e": 0, "s": 1, "w": 0},
                {"n": 0, "e": 0, "s": 0, "w": 0},
                {"n": 0, "e": 0, "s": 0, "w": 0}
            ],
            [
                {"n": 1, "e": 1, "s": 0, "w": 0},
                {"n": 1, "e": 0, "s": 0, "w": 1},
                {"n": 0, "e": 1, "s": 1, "w": 0},
                {"n": 0, "e": 0, "s": 0, "w": 1}
            ]
        ], safe=False
        )
