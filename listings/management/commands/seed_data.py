from django.core.management.base import BaseCommand
from category.models import Category
from listings.models import Amenity, Detail, CategoryAmenities, CategoryDetails
  
class Command(BaseCommand):
  def handle(self, *args, **options):
    name = "seed_data"

    # CATEGORIES SEEDER

    try:
      stambene_nekretnine = Category.objects.create(name='Stambene nekretnine', description='Stambeni')
    except:  
      stambene_nekretnine = Category.objects.get(name='Stambene nekretnine', description='Stambeni')
    try:
      zemljista = Category.objects.create(name='Zemljišta', description='Zemljišta')
    except:  
      zemljista = Category.objects.get(name='Zemljišta', description='Zemljišta')
    try:
      poslovni_prostori = Category.objects.create(name='Poslovni prostori', description='Poslovni prostori')
    except:  
      poslovni_prostori = Category.objects.get(name='Poslovni prostori', description='Poslovni prostori')

    try:
      stan = Category.objects.create(parent=stambene_nekretnine, name='Stan')
    except:
      stan = Category.objects.get(parent=stambene_nekretnine, name='Stan')
    try:
      kuca = Category.objects.create(parent=stambene_nekretnine, name='Kuća')
    except:
      kuca = Category.objects.get(parent=stambene_nekretnine, name='Kuća')
    try:
      soba = Category.objects.create(parent=stambene_nekretnine, name='Soba')
    except:
      soba = Category.objects.get(parent=stambene_nekretnine, name='Soba')
    try:
      garaza = Category.objects.create(parent=stambene_nekretnine, name='Garaža')
    except:
      garaza = Category.objects.get(parent=stambene_nekretnine, name='Garaža')
    try:
      apartman = Category.objects.create(parent=stambene_nekretnine, name='Apartman')
    except:
      apartman = Category.objects.get(parent=stambene_nekretnine, name='Apartman')
    try:
      vila = Category.objects.create(parent=stambene_nekretnine, name='Vila')
    except:
      vila = Category.objects.get(parent=stambene_nekretnine, name='Vila')
    try:
      vikendica = Category.objects.create(parent=stambene_nekretnine, name='Vikendica')
    except:
      vikendica = Category.objects.get(parent=stambene_nekretnine, name='Vikendica')
    try:
      gradj_parcela = Category.objects.create(parent=zemljista, name='Građevinska parcela')
    except:
      gradj_parcela = Category.objects.get(parent=zemljista, name='Građevinska parcela')
    try:
      poljo_parcela = Category.objects.create(parent=zemljista, name='Poljoprivredna parcela')
    except:
      poljo_parcela = Category.objects.get(parent=zemljista, name='Poljoprivredna parcela')
    try:
      lokal = Category.objects.create(parent=poslovni_prostori, name='Poslovni prostor - Lokal')
    except:
      lokal = Category.objects.get(parent=poslovni_prostori, name='Poslovni prostor - Lokal')
    try:
      kancelarija = Category.objects.create(parent=poslovni_prostori, name='Poslovni prostor - Kancelarija')
    except:
      kancelarija = Category.objects.get(parent=poslovni_prostori, name='Poslovni prostor - Kancelarija')
    try:
      pos_prostor = Category.objects.create(parent=poslovni_prostori, name='Poslovni prostor')
    except:
      pos_prostor = Category.objects.get(parent=poslovni_prostori, name='Poslovni prostor')
    try:
      kom_prostor = Category.objects.create(parent=poslovni_prostori, name='Komercijalni prostor')
    except:
      kom_prostor = Category.objects.get(parent=poslovni_prostori, name='Komercijalni prostor')
    try:
      ugost_prostor = Category.objects.create(parent=poslovni_prostori, name='Ugostiteljski prostor')
    except:
      ugost_prostor = Category.objects.get(parent=poslovni_prostori, name='Ugostiteljski prostor')
    try:
      proiz_prostor = Category.objects.create(parent=poslovni_prostori, name='Proizvodni prostor')
    except:
      proiz_prostor = Category.objects.get(parent=poslovni_prostori, name='Proizvodni prostor')
    try:
      ostalo = Category.objects.create(parent=poslovni_prostori, name='Ostalo')
    except:
      ostalo = Category.objects.get(parent=poslovni_prostori, name='Ostalo')
    
    self.stdout.write(self.style.SUCCESS('Successfully seeded data for categories'))

    # ADD DETAILS AND AMENITIES and APPEND THEM TO CATEGORIES


    detailValues = ["Internet", "Kablovska", "Telefon", "Interfon", "Lift", "Garaža", "Parking u zoni", "Parking van zone", "Klima uređaj", "Lođa", "Vešernica", "Video nadzor", "Alarm", "Obezbeđenje", "Održavanje zgrade", "Prilaz za kolica", "Smart", "Dvorište", "Bašta", "Igralište", "Bazen", "Sauna", "Teretana", "Solarni panel", "Kotlarnica", "Grejanje na struju", "Centralno grejanje", "Grejanje na gas", "Čvrsta goriva", "Grejanje ostalo", "Kalorimetri", "Visina do 260cm", "Visina 260-300cm", "Visina od 300cm"]
    amenityValues = ["Kuhinja", "Frižider", "Šporet", "Rerna", "Mikrotalasna", "Sudomašina", "Veš mašina", "Garnitura", "Trpezarijski sto", "Plakar", "Krevet", "Kanc. Oprema"]



    for detail in ["Internet", "Kablovska", "Telefon", "Struja", "Voda", "Put-ulica", "Ograda"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=gradj_parcela, detail=d)
      except:
        print('exists')

    for detail in ["Internet", "Kablovska", "Telefon", "Struja", "Voda", "Put-ulica", "Ograda"]:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=poljo_parcela, detail=d)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=lokal, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=lokal, amenity=a)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=kancelarija, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=kancelarija, amenity=a)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=kom_prostor, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=kom_prostor, amenity=a)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=proiz_prostor, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=proiz_prostor, amenity=a)
      except:
        print('exists')


    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=ugost_prostor, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=ugost_prostor, amenity=a)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()
      
      try:
        CategoryDetails.objects.create(category=pos_prostor, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=pos_prostor, amenity=a)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=ostalo, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=ostalo, amenity=a)
      except:
        print('exists')


    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=stan, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=stan, amenity=a)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=kuca, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=kuca, amenity=a)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=soba, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=soba, amenity=a)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=garaza, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=garaza, amenity=a)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=apartman, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=apartman, amenity=a)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=vila, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=vila, amenity=a)
      except:
        print('exists')

    for detail in detailValues:
      try:
        d = Detail.objects.get(name=detail)
      except Detail.DoesNotExist:
        d = Detail(name=detail)
        d.save()

      try:
        CategoryDetails.objects.create(category=vikendica, detail=d)
      except:
        print('exists')

    for amenity in amenityValues:
      try:
        a = Amenity.objects.get(name=amenity)
      except Amenity.DoesNotExist:
        a = Amenity(name=amenity)
        a.save()

      try:
        CategoryAmenities.objects.create(category=vikendica, amenity=a)
      except:
        print('exists')

    self.stdout.write(self.style.SUCCESS('Successfully seeded data for amenities and details'))


