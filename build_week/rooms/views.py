from django.http import JsonResponse


def all_rooms(request):
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