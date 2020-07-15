from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import Counter

@api_view(['POST'])
def lambda_function(request):
    data = request.data.get('question')
    try:
        for alg in data:
            if type(alg) == str:
                raise TypeError
    except TypeError:
        return Response({"solution":"wrong format"})
    
    result = []

    counter = Counter()
    for number in data:
        counter[number] += 1
    
    for number in counter.most_common():
        for _ in range(number[1]):
            result.append(number[0])

    return Response({"solution":result})

