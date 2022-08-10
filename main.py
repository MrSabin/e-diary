from datacenter.models import Schoolkid, Mark

def fix_marks(schoolkid):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    points = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
    for record in points:
        record.points = 5
        record.save()


fix_marks("Фролов Иван")
