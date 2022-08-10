from datacenter.models import Schoolkid, Mark, Chastisement

def fix_marks(schoolkid):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    points = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
    for record in points:
        record.points = 5
        record.save()


def remove_chastisements(schoolkid):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    all_chastisements = Chastisement.objects.filter(schoolkid=child)
    all_chastisements.delete()


remove_chastisements("Голубев Феофан")
