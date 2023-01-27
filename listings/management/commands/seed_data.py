from django.core.management.base import BaseCommand
from category.models import Category
from listings.models import Amenity, Detail, CategoryAmenities, CategoryDetails
  
class Command(BaseCommand):
  def handle(self, *args, **options):
    name = "seed_data"

    # CATEGORIES SEEDER

    stambene_nekretnine = Category.objects.create(name='Stambene nekretnine', description='Stambeni')
    zemljista = Category.objects.create(name='Zemljišta', description='Zemljišta')
    poslovni_prostori = Category.objects.create(name='Poslovni prostori', description='Poslovni prostori')

    stan = Category.objects.create(parent=stambene_nekretnine, name='Stan')
    kuca = Category.objects.create(parent=stambene_nekretnine, name='Kuća')
    soba = Category.objects.create(parent=stambene_nekretnine, name='Soba')
    garaza = Category.objects.create(parent=stambene_nekretnine, name='Garaža')
    apartman = Category.objects.create(parent=stambene_nekretnine, name='Apartman')
    vila = Category.objects.create(parent=stambene_nekretnine, name='Vila')
    vikendica = Category.objects.create(parent=stambene_nekretnine, name='Vikendica')

    gradj_parcela = Category.objects.create(parent=zemljista, name='Građevinska parcela')
    poljo_parcela = Category.objects.create(parent=zemljista, name='Poljoprivredna parcela')

    lokal = Category.objects.create(parent=poslovni_prostori, name='Poslovni prostor - Lokal')
    kancelarija = Category.objects.create(parent=poslovni_prostori, name='Poslovni prostor - Kancelarija')
    pos_prostor = Category.objects.create(parent=poslovni_prostori, name='Poslovni prostor')
    kom_prostor = Category.objects.create(parent=poslovni_prostori, name='Komercijalni prostor')
    ugost_prostor = Category.objects.create(parent=poslovni_prostori, name='Ugostiteljski prostor')
    proiz_prostor = Category.objects.create(parent=poslovni_prostori, name='Proizvodni prostor')
    ostalo = Category.objects.create(parent=poslovni_prostori, name='Ostalo')
    
    self.stdout.write(self.style.SUCCESS('Successfully seeded data for categories'))

    # ADD DETAILS AND AMENITIES and APPEND THEM TO CATEGORIES

    for detail in ["Internet", "Kablovska", "Telefon", "Struja", "Voda", "Put-ulica", "Ograda"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=gradj_parcela, detail=d)

    for detail in ["Internet", "Kablovska", "Telefon", "Struja", "Voda", "Put-ulica", "Ograda"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=poljo_parcela, detail=d)

    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=lokal, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Kanc. nameštaj"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=lokal, amenity=a)

    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=kancelarija, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Kanc. nameštaj"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=kancelarija, amenity=a)

    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Vešernica", "Kotlarnica", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=kom_prostor, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Kanc. nameštaj"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=kom_prostor, amenity=a)

    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Vešernica", "Kotlarnica", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=proiz_prostor, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Kanc. nameštaj"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=proiz_prostor, amenity=a)

    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Vešernica", "Kotlarnica", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri", "Ostalo"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=ostalo, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Kanc. nameštaj"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=ostalo, amenity=a)


    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Vešernica", "Kotlarnica", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=stan, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Trpezarijski set", "Krevet"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=stan, amenity=a)

    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Vešernica", "Kotlarnica", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=kuca, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Trpezarijski set", "Krevet"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=kuca, amenity=a)

    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Vešernica", "Kotlarnica", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=soba, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Trpezarijski set", "Krevet"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=soba, amenity=a)

    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Vešernica", "Kotlarnica", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=garaza, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Trpezarijski set", "Krevet"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=garaza, amenity=a)

    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Vešernica", "Kotlarnica", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=apartman, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Trpezarijski set", "Krevet"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=apartman, amenity=a)

    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Vešernica", "Kotlarnica", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=vila, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Trpezarijski set", "Krevet"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=vila, amenity=a)

    for detail in ["Internet", "Kablovska", "Telefon", "Klima uređaj", "Terasa", "Lođa", "Ostava", "Podrum", "Garaža", "Parking u zoni", "Parking van zone", "Video nadzor", "Alarm", "Obezbeđenje", "Lift", "Energetski pasoš", "Smart", "Solarni panel", "Prilaz za kolica", "Održavanje zgrade", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Vešernica", "Kotlarnica", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      CategoryDetails.objects.create(category=vikendica, detail=d)

    for amenity in ["Kuhinja", "Sudomašina", "Veš mašina", "Plakar", "TV", "Garnitura", "Trpezarijski set", "Krevet"]:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      CategoryAmenities.objects.create(category=vikendica, amenity=a)

    self.stdout.write(self.style.SUCCESS('Successfully seeded data for amenities and details'))


