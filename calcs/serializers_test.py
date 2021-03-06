from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from calcs.models import Measure

from calcs.serializers import MeasureSerializer
from calcs.serializers import UserMeasureSerializer
from calcs.serializers import UserSerializer

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.get('/')


serializer_context = {
    'request': Request(request),
}

# python ..\manage.py shell
# exec(open('serializers_test.py').read())


'''
from django.contrib.auth.models import User
user=User.objects.create_user('vlad', password='userpassword')
user.is_superuser=False
user.is_staff=False
user.save()

User.objects.all().delete()

from django.contrib.auth.models import User
user=User.objects.create_user('staff', password='staff')
user.is_superuser=False
user.is_staff=True
user.save()

for u in User.objects.all():
    if u.is_authenticated:
        print(u)

Measure.objects.get(pk=2)
'''

admin = User.objects.get(username='vladislav')
user = User.objects.get(username='username')

Measure.objects.all().delete()
print(Measure.objects.all())


gamedatetime = timezone.make_aware(datetime.now(), timezone.get_current_timezone())


meas = Measure(date = gamedatetime, name='Grishagin', owner = user, bottom_border = 0.1, upper_border  = 2.0, r = 3.4, epsilon = 0.001)
meas.save()

meas2 = Measure(date = gamedatetime, name='Grishagin2', owner =admin, bottom_border = 0.1, upper_border  = 2.0, r = 3.4, epsilon = 0.001)
meas2.save()

'''
print(meas.pk)
print(meas.name)
print(meas.function_minimum)

print(cl.pk)
print(cl.name)
print(cl.post)

print(cl_meas.measure.pk)
print(cl_meas.measure.name)
print(cl_meas.measure.function_minimum)
'''

user_serializer = UserSerializer(instance=user, context=serializer_context)
print(user_serializer.data)

admin_serializer = UserSerializer(instance=admin, context=serializer_context)
print(admin_serializer.data)

measure_serializer = MeasureSerializer(instance=meas, context=serializer_context)
print(measure_serializer.data)

measure_serializer2 = MeasureSerializer(instance=meas2, context=serializer_context)
print(measure_serializer2.data)

'''
renderer = JSONRenderer()
rendered = renderer.render(client_measure_serializer.data)
print(rendered)'''

print(Measure.objects.all())

'''cl_meas.delete()
cl_meas2.delete()
meas.delete()
meas2.delete()
cl.delete()
'''

'''
json_string_for_new_game = '{"name":"Tomb Raider Extreme Edition","release_date":"2016-05-18T03:02:00.776594Z","game_category":"3D RPG","played":false}'
json_bytes_for_new_game = bytes(json_string_for_new_game json_game_string  , encoding="UTF-8")
stream_for_new_game = BytesIO(json_bytes_for_new_game)
parser = JSONParser()
parsed_new_game = parser.parse(stream_for_new_game)
print(parsed_new_game)

new_game_serializer = GameSerializer(data=parsed_new_game)
if new_game_serializer.is_valid():
    new_game = new_game_serializer.save()
    print(new_game.name)'''