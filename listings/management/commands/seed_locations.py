from django.core.management.base import BaseCommand
from listings.models import Location
  
class Command(BaseCommand):
  def handle(self, *args, **options):
    name = "seed_locations"

    # CATEGORIES SEEDER

    locations = [
    {
        "grad": "Beograd",
        "opstina": "Beograd",
        "lokacija": "Beograd"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Arnajevo"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Barajevo"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Baćevac"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Bela Reka"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Beljina"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Boždarevac"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Veliki Borak"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Vitkovica"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Vranić"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Gaj"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Glumčevo Brdo"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Guncati"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Dražanovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Dubrave"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Ibarska Magistrala"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Karaula"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Lipovica"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Lipovička Šuma"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Lisović"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Manić"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Meljak"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Nenadovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Pajšuma"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Ravni Gaj"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Rašića Kraj"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Rožanci"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Srednji Kraj"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Stara Lipovica"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Suva Šuma"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Taraiš"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Trebež"
    },
    {
        "grad": "Beograd",
        "opstina": "Barajevo",
        "lokacija": "Šiljakovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Autokomanda"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Avala"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Banjica"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Banjica 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Banjička Šuma"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Beli Potok"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Bioskop Voždovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Braće Jerković 1"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Braće Jerković 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Braće Jerković 3"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Bubanj Potok"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Bulevar Oslobođenja"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Vitanovačka"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Voždovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Voždovac Centar"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Voždovačka Crkva"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Vojvode Vlahovića"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Vojvode Stepe"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Vojislava Ilića"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Gaj"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Gornji Voždovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Darvinova Pošta"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Donji Voždovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Dušanovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Zaplanjska"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Zuce"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Jajinci"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Jove Ilića"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Konjarnik 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Kumodraž 1"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Kumodraž 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Kumodraž Staro Selo"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Kumodraška"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Mala Utrina"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Marinkova Bara"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Medaković 1"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Medaković 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Medaković 3"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Medaković Padina"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Mitrovo Brdo"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Pašino (Lekino) Brdo"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Pinosava"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Prnjavor"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Ripanj"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Saobraćajni Fakultet"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Selo Rakovica"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Siva Stena"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Spomen Park Jajinci"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Stepa Stepanović"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Stepin Lug"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Topovske Šupe"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Torlak"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Trošarina"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "TC Stadion"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Ustanička"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Farmaceutski fakultet"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "FON"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Franš"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Hotel M"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Činovnička Kolonija"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Šumice"
    },
    {
        "grad": "Beograd",
        "opstina": "Voždovac",
        "lokacija": "Šuplja Stena"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Beogradska"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Bulevar Kralja Aleksandra"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Vračar"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Gospodara Vučića"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "gradić Pejton"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Englezovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Istočni Vračar"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Južni Bulevar"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Kalenić Pijaca"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Karađorđev Park"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Krunska"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Krunski Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Maksima Gorkog"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Neimar"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Pravni Fakultet"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Savinac"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Slavija"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "SC Vračar"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Hram Svetog Save"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Centar"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Crveni Krst"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Cvetni Trg"
    },
    {
        "grad": "Beograd",
        "opstina": "Vračar",
        "lokacija": "Čubura"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Avala"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Begaljica"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Boleč"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Brestovik"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Vinča"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Vrčin"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Grocka"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Dražanj"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Živkovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Zaklopača"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Kaluđerica"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Kamendol"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Leštane"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Leštane Novo Naselje"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Plavinci"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Pudarci"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Radmilovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Ritopek"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Smederevski Put"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Strnjike"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Umčari"
    },
    {
        "grad": "Beograd",
        "opstina": "Grocka",
        "lokacija": "Šuplja Stena"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Bulbuder"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Bulevar Kralja Aleksandra"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Veliki Mokri Lug"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Vukov Spomenik"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "gradska Bolnica"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Denkova Bašta"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Dimitrija Tucovića"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Đeram Pijaca"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Zvezdara"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Zvezdara 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Zvezdara 3"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Zvezdarska Padina"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Zvezdarska Šuma"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Zeleno Brdo"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Kluz"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Konjarnik"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Konjarnik 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Konjarnik 3"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Lion"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Lipov Lad"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Mali Mokri Lug"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Mirijevo"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Mirijevo 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Mirijevo 3"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Mirijevo 4"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Novo Groblje"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Novo Mirijevo"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Olimp"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Orlovsko Naselje"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Rudo"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Severni Bulevar"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Slavujev Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Smederevski Put"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Stari Đeram"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Učiteljsko Naselje"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Cvetanova Ćuprija"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Cvetkova pijaca"
    },
    {
        "grad": "Beograd",
        "opstina": "Zvezdara",
        "lokacija": "Crveni Krst"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Altina"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Autoput za Zagreb"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Autoput za Novi Sad"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Bački Ilovik"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Batajnica"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Batajnički Drum"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Cara Dušana"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Centar"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Ćukovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Gardoš"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Gornji grad"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Goveđi Brod"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Jelovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Kalvarija"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Kamendin"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Karađorđev Trg"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Kej"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Kolonija Zmaj"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Lido"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Mala Pruga"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Marija Bursać"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Meandri"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Muhar"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Naselje Sveti Sava"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Novi grad"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Plavi Horizonti"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Pregrevica"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Prvomajska"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Retenzija"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Save Kovačevića"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Sutjeska"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Tošin Bunar"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Ugrinovačka"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Ugrinovci"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Vojni put"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Zelena Avenija"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Zemun"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Zemun Bačka"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Zemun Polje"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Zemunske Kapije"
    },
    {
        "grad": "Beograd",
        "opstina": "Zemun",
        "lokacija": "Železnička Kolonija"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Arapovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Baroševac"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Barzilovica"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Bistrica"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Brajkovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Burovo"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Cvetovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Čibutkovica"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Ćelije"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Dren"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Dudovica"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Junkovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Ibarska Magistrala"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Kruševica"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Lazarevac"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Leskovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Lukavica"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Mali Crljeni"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Medoševac"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Mirosaljci"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Petka"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Prkosava"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Rudovci"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Sakulja"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Sokolovo"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Stepojevac"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Strmovo"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Stubica"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Šopić"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Šušnjar"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Trbušnica"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Veliki Crljeni"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Vrbovno"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Vreoci"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Zeoke"
    },
    {
        "grad": "Beograd",
        "opstina": "Lazarevac",
        "lokacija": "Županjac"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "25. Maj"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Amerić"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Bataševo"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Beluće"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Beljevac"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Velika Ivanča"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Velika Krsna"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Vlaška"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Vrbovno"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Granice"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Drapšin"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Dubona"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Jagnjilo"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Kovačevac"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Koraćica"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Kosmaj"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Mala Vrbica"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Markovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Međulužje"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Mladenovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Mladenovac (varoš)"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Mladenovac (selo)"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Pružatovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Rabrovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Rajkovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Selters Banja"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Senaja"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Crkvine"
    },
    {
        "grad": "Beograd",
        "opstina": "Mladenovac",
        "lokacija": "Šepšin"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Ada Međica"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Bežanijska Kosa 1"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Bežanijska Kosa 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Bežanijska Kosa 3"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 1 - Fontana"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 3"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 4"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 5"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 6"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 7 - Paviljoni"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 7a - Paviljoni"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 8 - Paviljoni"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 8a - Paviljoni"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 9"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 9a"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 11a"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 11b"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 11c"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 18 - Staro Sajmište"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 19 - Sava Centar"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 19a"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 20 - Hyatt"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 21"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 22"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 23"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 24"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 25 - Arena"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 26"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 28"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 29"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 30"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 31 - opstina"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 32"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 33 - Geneks"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 34"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 35"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 37"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 38"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 39"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 40"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 41"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 41a"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 42"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 43"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 44 - TC Piramida"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 45"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 53 - Kvantaš"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 58"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 60"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 61"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 62"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 63"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 64"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 65 - WEST 65"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 66"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 66a"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 67 - Belville"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 67 - A Blok"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 68"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 69"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 70 - Kineski TC"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 70a"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 71"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Blok 72"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Dr Ivana Ribara"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Fontana"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Hotel Hyatt"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Hotel Jugoslavija"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Ledine"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Novi Beograd"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Novi Merkator"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "opstina"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Paviljoni"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Sava Centar"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Savski Nasip"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Stara Bežanija"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Tošin Bunar"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Trešnjinog Cveta"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "Ušće"
    },
    {
        "grad": "Beograd",
        "opstina": "Novi Beograd",
        "lokacija": "YUBC"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Baljevac"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Barič"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Belo Polje"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Brgulice"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Brović"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Veliko Polje"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Vukićevica"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Grabovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Draževac"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Dren"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Zabrežje"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Zvečka"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Jasenak"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Konatice"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Krtinska"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Ljubinić"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Mala Moštanica"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Mislođin"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Obrenovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Orašac"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Piroman"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Poljane"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Ratari"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Rvati"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Rojkovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Skela"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Stočnjak Novo Naselje"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Stubline"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Trstenica"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Urovci"
    },
    {
        "grad": "Beograd",
        "opstina": "Obrenovac",
        "lokacija": "Ušće"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "27. Marta"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Ada Huja"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Bela Stena"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Bogoslovija"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - 1"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - 3"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - 4 i 5"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - Atovi"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - Crvenka"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - Greda"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - Mali Zbeg"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - Nova Borča"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - Popova Bara"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - Pretok"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - Sebeš Borčanski"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Borča - Stara Borča"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Botanička Bašta"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Bulevar Despota Stefana"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Centar"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Cvijićeva"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Ćalije"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Dalmatinska"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Hadžipopovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Hala Pionir"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Karaburma"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Karaburma 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Karaburma Stara"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Kotež"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Kovilovo"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Kožara"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Krnjača"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Krnjača - Braća Marić"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Krnjača - Branko Momirov"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Krnjača - Grga Andrijanović"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Krnjača - Sava Kovačević"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Krnjača - Sutjeska"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Krnjača - Zaga Malivuk"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Krnjača - Dunavski Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Krnjača - Mika Alas"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Krnjača - Partizanski Put"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Krnjača - Partizanski Blok"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Lešće"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Mašinski fakultet"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Ovča"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Padinska Skela"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Padinska Skela - Besni Fok"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Padinska Skela - Dunavac"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Padinska Skela - Glogonjski Rit"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Padinska Skela - Jabučki Rit"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Padinska Skela - Tovilište"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Padinska Skela - Vrbovsko"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Palilula"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Palilulska pijaca"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Pančevački put"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Pančevački most"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Poštanska Štedionica"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Profesorska Kolonija"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Rospi Ćuprija"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Ruzveltova"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Slanci"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Tašmajdan"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Veliko Selo"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Viline Vode"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Višnjica"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Višnjička Banja"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Višnjičko Polje"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Zira"
    },
    {
        "grad": "Beograd",
        "opstina": "Palilula",
        "lokacija": "Zrenjaninski Put"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Vidikovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Vidikovačka Padina"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Ibarska Magistrala"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Jelezovac"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Kanarevo Brdo"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Kijevo"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Kneževac"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Labudovo Brdo"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Miljakovac 1"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Miljakovac 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Miljakovac 3"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Petlovo Brdo"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Rakovica"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Rakovica - Centar"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Rakovica 2"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Resnik"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Selo Rakovica"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Skojevsko Naselje"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Stari Košutnjak"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Straževica"
    },
    {
        "grad": "Beograd",
        "opstina": "Rakovica",
        "lokacija": "Sunčani Breg"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Autokomanda"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Balkanska"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Banjica"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Bara Venecija"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Beograd na Vodi"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Beograd na Vodi - Bristol Park"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Beograd na Vodi - Savska Ulica"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Beograđanka"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Brankova"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Višegradska"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "VMA"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Gavrila Principa"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Dedinje"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Dedinje - Diplomatska Kolonija"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Ekonomski Fakultet"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Zeleni Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Jatagan Mala"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Karađorđeva"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Klinički Centar"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Kneza Miloša"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Kraljice Natalije"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Lisičji Potok"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Mostarska Petlja"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Nemanjina"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Palata Pravde"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Park Manjež"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Prokop"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Resavska"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Savamala"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Savamala - Bolnica Narodni Front"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Savamala - Finansijski Park"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Savski Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Savski Trg - Pristanište"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Sajam"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Sarajevska - Hajduk-Veljkov Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Sarajevska"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Svetozara Markovića"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Senjak"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Senjak - Gospodarska Mehana"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Stadion Partizana"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Stadion Crvene Zvezde"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Topčider"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Topčicer - Topčidersko Brdo"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Humska"
    },
    {
        "grad": "Beograd",
        "opstina": "Savski Venac",
        "lokacija": "Centar"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Avala"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Babe"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Guberevac"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Drlupa"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Dučina"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Đurinci"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Kosmaj"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Mala Ivanča"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Mali Popović"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Mali Požarevac"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Nemenikuće"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Parcani"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Popović"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Ralja"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Rogača"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Ropočevo"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Sibnica"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Slatina"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Sopot"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Sopot (mesto)"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Stojnik"
    },
    {
        "grad": "Beograd",
        "opstina": "Sopot",
        "lokacija": "Trešnja"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "25. Maj"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Andrićev Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Andrićev Venac - Devojački Park"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Atelje 212"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Bajlonijeva Pijaca"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Beograd Centar"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Gundulićev Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Dom Omladine"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Dorćol"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Dorćol - Donji Dorćol"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Dorćol - Gornji Dorćol"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Dunavski Kej"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Zeleni Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Kalemegdan"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "K - District"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Knez Mihailova"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Kopitareva gradina"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Kosančićev Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Kralja Milana"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Kralja Petra"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "London"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Obilićev Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Politika"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Savamala"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Skadarlija"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Skupština"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Stari grad"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Studentski Trg"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Takovska"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Terazije"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Terazije - Pionirski Park"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Terazije - Terazijska Terasa"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Topličin Venac"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Trg Nikole Pašića"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Trg Republike"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Francuska"
    },
    {
        "grad": "Beograd",
        "opstina": "Stari grad",
        "lokacija": "Cara Dušana"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Bečmen"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Boljevci"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Dobanovci"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Jakovo"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Ključ"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Ledine"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Petrovčić"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Progar"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Radiofar"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Stremen"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Surčin"
    },
    {
        "grad": "Beograd",
        "opstina": "Surčin",
        "lokacija": "Surčin (mesto)"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Ada Ciganlija"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Banovo Brdo"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Bele Vode"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Velika Moštanica"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Vodovodska"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Golf"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Žarkovo"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Železnik"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Ibarska Magistrala"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Julino Brdo"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Košutnjak"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Makiš"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Novi Železnik"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Orlovača"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Ostružnica"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Pećani"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Repište"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Rupčine"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Rucka"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Rušanj"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Sremčica"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Sunčana Padina"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Trgovačka"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Umka"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Filmski grad"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Careva Ćuprija"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Cerak"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Cerak Vinogradi"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Cerak - Stari Cerak"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Čukarica"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Čukarica - Centar"
    },
    {
        "grad": "Beograd",
        "opstina": "Čukarica",
        "lokacija": "Čukarička Padina"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Begeč",
        "lokacija": "Begeč"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Budisava",
        "lokacija": "Budisava"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Bukovac",
        "lokacija": "Bukovac"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Veternik",
        "lokacija": "Veternik"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Kać",
        "lokacija": "Kać"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Kać",
        "lokacija": "Vinogradi"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Kać",
        "lokacija": "Petrovdansko Naselje"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Kisač",
        "lokacija": "Kisač"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Kisač",
        "lokacija": "Tankosićevo"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Kovilj",
        "lokacija": "Kovilj"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Ledinci",
        "lokacija": "Ledinci"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Ledinci",
        "lokacija": "Bubanja"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Ledinci",
        "lokacija": "Vučkovac"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Ledinci",
        "lokacija": "Stari Ledinci"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Novi Sad"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Adamovićevo Naselje"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Avijatičarsko Naselje"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Adice"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Banatić"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Bangladeš"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Bistrica - (Novo Naselje)"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Bulevar Evrope"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Bulevar Oslobođenja"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Bulevar Patrijarha Pavla"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Bulevar Cara Lazara"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Veliki Rit"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Veternička Rampa"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Vidovdansko Naselje"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Gornje Livade"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Grbavica"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Detelinara"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Detelinara - Nova Detelinara"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Železnička Stanica"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Industrijska Zona Jug"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Industrijska Zona Sever"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Jugovićevo"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Kameničko Ostrvo"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Kamenjar"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Kej"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Klisa"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Liman"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Liman 1"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Liman 2"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Liman 3"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Liman 4"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Nemanovci"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Pejićevi Salaši"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Pervazovo Naselje"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Podbara"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Radna Zona Sever 1"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Radna Zona Sever 2"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Radna Zona Sever 3"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Radna Zona Sever 4"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Rafinerija"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Ribarsko Ostrvo"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Rimski Šančevi"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Rotkvarija"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Sajlovo"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Sajam"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Sajmište"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Salajka"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Satelit"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Slana Bara"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Spens"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Stari grad"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Telep"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Telep - Južni"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Telep - Severni"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Futoška"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Futoški Put"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Centar"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Šangaj"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad",
        "lokacija": "Štrand"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Petrovaradin"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Alibegovac"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Vezirac"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "gradić"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Karagača"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Mišeluk"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Novi Majur"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Petrovaradinska Ada"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Petrovaradinska Tvrđava"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Radna Zona Istok"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Radna Zona Pobeda"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Ribnjak"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Sadovi"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Stari Majur"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Tekije"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Trandžament"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Centar"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Petrovaradin",
        "lokacija": "Širine (Puckaroš)"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Sremska Kamenica",
        "lokacija": "Sremska Kamenica"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Sremska Kamenica",
        "lokacija": "Bocke"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Sremska Kamenica",
        "lokacija": "Glavica"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Sremska Kamenica",
        "lokacija": "Kip"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Sremska Kamenica",
        "lokacija": "Paragovo"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Sremska Kamenica",
        "lokacija": "Popovica"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Sremska Kamenica",
        "lokacija": "Sremska Kamenica - Gornja"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Sremska Kamenica",
        "lokacija": "Sremska Kamenica - Donja"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Sremska Kamenica",
        "lokacija": "Tatarsko Brdo"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Novi Sad - Sremska Kamenica",
        "lokacija": "Čardak"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Rumenka",
        "lokacija": "Rumenka"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Stepanovićevo",
        "lokacija": "Stepanovićevo"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Futog",
        "lokacija": "Futog"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Futog",
        "lokacija": "Novi Futog"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Futog",
        "lokacija": "Stari Futog"
    },
    {
        "grad": "Novi Sad",
        "opstina": "Čenej",
        "lokacija": "Čenej"
    },
    {
        "grad": "Niš",
        "opstina": "Niš",
        "lokacija": "Niš"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Medijana"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Božidar Adžija"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Brzi Brod"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Bulevar Dr Zorana Đinđića"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Bulevar Zona 1"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Bulevar Zona 2"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Bulevar Zona 3"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Bulevar Nemanjića"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Vatrogasni Dom"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Vojni Dom"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "gradska Bolnica"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Dom Zdravlja"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Duvanište"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Dušanov Bazar"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Kičevo"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Krive Livade"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Krivi Vir"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Merger"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Medicinski Fakultet"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Merkator"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Obilićev Venac"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Pravni Fakultet"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Sinđečićev Trg"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Trg Kralja Aleksandra"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Trg Svetog Save"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Trg Učitelja Tase"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Trošarina"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Ćele Kula"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Filozofski fakultet"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Centar"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Crveni Pevac"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Čair"
    },
    {
        "grad": "Niš",
        "opstina": "Medijana",
        "lokacija": "Šojka"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Niška Banja"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Bancarevo"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Gornja Studena"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Donja Studena"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Ženeva (Devizno Naselje)"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Jelašnica"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Koritnjak"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Kunovica"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Lazarevo Selo"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Manastir"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Nikola Tesla"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Ostrovica"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Prva Kutina"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Prosek"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Ravni Do"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Radikina Bara"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Rautovo"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Sićevo"
    },
    {
        "grad": "Niš",
        "opstina": "Niška Banja",
        "lokacija": "Čukljenik"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Palilula"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "9. Maj"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Apelovac"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Berbatov"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Bogoslovija"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Bubanj"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Bubanjska Dolina"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Veterinarska Stanica"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Vukmanovo"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Gabrovac"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Gabrovačka Reka"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Gabrovački Put"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Delijski Vis"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Donje Vlase"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Durmitorska"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Elektronska Industrija"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Železnička Stanica"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Kalač Brdo"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Kovanluk"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "KP Dom"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Krušce"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Lalinac"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Ledena Stena"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Mašinska Industrija"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Međurovo"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Milka Protić"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Mokranjčeva"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Monopol"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Mramor"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Mramorski Potok"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Nova Železnička Stanica"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Njegoševa"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Pasi Poljana"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "PMF"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Put Za Medoševac"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Rasadnik"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Svetinikolska Crkva"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Staro Groblje"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Stočni Trg"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Suvi Do"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Tutunović Podrum"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Ured"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Fakultet Zaštite na Radu"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Crvena Zvezda"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Crni Put"
    },
    {
        "grad": "Niš",
        "opstina": "Palilula",
        "lokacija": "Čokot"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Pantelej"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Beverli Hils"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Brenica"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Vinik"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Voćarska"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Vrelo"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Gornja Vrežina"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Gornji Matejevac"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Donja Vrežina"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Donji Matejevac"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Durlan"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Jagodin Mala"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Jasenovik"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Knez Selo"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Knjaževačka"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Malča"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Oreovac"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Pasjača"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Somborska"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Cerje"
    },
    {
        "grad": "Niš",
        "opstina": "Pantelej",
        "lokacija": "Čalije"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Crveni Krst"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Aerodrom"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Autobuska Stanica"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Beograd Mala"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Berčinac"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Branko Bjegović"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Bulevar Nikole Tesle"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Vele Polje"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Velika Pijaca"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Vrtište"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Gornja Toponica"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Gornja Trnava"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Gornj Komren"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Donja Toponica"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Donja Trnava"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Donji Komren"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Jagodin Mala"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Kravlje"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Leskovik"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Medoševac"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Mezgraja"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Miljkovac"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Paligrace"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Paljina"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Podvinik"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Popovac"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Ratko Jović"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Rujnik"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Sečanica"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Supovac"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Tvrđava"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Tehnički Fakulteti"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Trupale"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Hum"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Humska"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Centar"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Čamurlija"
    },
    {
        "grad": "Niš",
        "opstina": "Crveni Krst",
        "lokacija": "Šljaka"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac",
        "lokacija": "Kragujevac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Aerodrom"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Gornje Grbice"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Gornje Jarušice"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Desimirovac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Donje Grbice"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Jovanovac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Lužnice"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Mali Šenj"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Mironić"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Novi Milanovac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Opornica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Pajazitovo"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Poskurice"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Resnik"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Cvetojevac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Cerovac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Čumić"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Šljivovac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Aerodrom",
        "lokacija": "Šumarice"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Pivara"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Autobuska Stanica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Baljkovac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Beloševac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Botunje"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Brioni"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Bresnica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Bukorovac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Velika Sugubina"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Velike Pčelice"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Gornje Komarice"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Gornja Sabanta"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Donje Komarice"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Donja Sabanta"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Dulene"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Železnička Stanica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Ilina Voda"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Ilićevo"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Jabučje"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Jazbine"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Karaula"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Korman"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Lepenica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Maršić"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Nova Kolonija"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Paluze"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Teferič"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Trmbas"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Pivara",
        "lokacija": "Cair"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Stanovo"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Adžine Livade"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Veliko Polje"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Vinjište"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Vojna Žica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Goločelo"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Grošnica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Divostin"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Donje Polje"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Dragobraća"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Drača"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Drenovac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Đuriselo"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Erdeč"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Korićani"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Kutlovo"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Ortoteks"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Popova Šuma"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Prekopeča"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Rogojevac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Senjak"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Trešnjevak"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stanovo",
        "lokacija": "Ćava"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Stari grad"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Bagremar"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Bubanj"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Vašarište"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Veliki Park"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Grujina Česma"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Erdoglija"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Kolonija"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Lekina Bara"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Lepenica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Licika"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Ljubine Livade"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Mala Vaga"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Palilule"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Prvi Maj"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Svetozar Marković"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Slovačko Groblje"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Smallville"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Stara Varoš"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Stara Radnička Kolonija"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Sušica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Cvetkovina"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Centar"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Centralna Radionica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Crvena Zvezda"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stari grad",
        "lokacija": "Šest Topola"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stragari",
        "lokacija": "Stragari"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stragari",
        "lokacija": "Veliki Šenj"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stragari",
        "lokacija": "Vlakča"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stragari",
        "lokacija": "Dobrača"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stragari",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stragari",
        "lokacija": "Kotraža"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stragari",
        "lokacija": "Ljubičevac"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stragari",
        "lokacija": "Mala Vrbica"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stragari",
        "lokacija": "Masloševo"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stragari",
        "lokacija": "Ramaća"
    },
    {
        "grad": "Kragujevac",
        "opstina": "Kragujevac - Stragari",
        "lokacija": "Ugljarevac"
    },
    {
        "grad": "Priština",
        "opstina": "Priština",
        "lokacija": "Priština"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Aktaš"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Arberija"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Velanija"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Veternik"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Dardanija"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Kalabrija"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Lakrište"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Pejton"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Sinji Dol"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Sunčani Breg"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Tasliđe"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Ulpijana"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Univerzitetsko Naselje"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Priština",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Priština",
        "opstina": "Ajvalija",
        "lokacija": "Ajvalija"
    },
    {
        "grad": "Priština",
        "opstina": "Ajkobila",
        "lokacija": "Ajkobila"
    },
    {
        "grad": "Priština",
        "opstina": "Badovac",
        "lokacija": "Badovac"
    },
    {
        "grad": "Priština",
        "opstina": "Balaban",
        "lokacija": "Balaban"
    },
    {
        "grad": "Priština",
        "opstina": "Bariljevo",
        "lokacija": "Bariljevo"
    },
    {
        "grad": "Priština",
        "opstina": "Besinje",
        "lokacija": "Besinje"
    },
    {
        "grad": "Priština",
        "opstina": "Businje",
        "lokacija": "Businje"
    },
    {
        "grad": "Priština",
        "opstina": "Vrani Do",
        "lokacija": "Vrani Do"
    },
    {
        "grad": "Priština",
        "opstina": "Glogovica",
        "lokacija": "Glogovica"
    },
    {
        "grad": "Priština",
        "opstina": "Gornja Brnjica",
        "lokacija": "Gornja Brnjica"
    },
    {
        "grad": "Priština",
        "opstina": "Gračanica",
        "lokacija": "Gračanica"
    },
    {
        "grad": "Priština",
        "opstina": "Graštica",
        "lokacija": "Graštica"
    },
    {
        "grad": "Priština",
        "opstina": "Dabiševac",
        "lokacija": "Dabiševac"
    },
    {
        "grad": "Priština",
        "opstina": "Devet Jugovića",
        "lokacija": "Devet Jugovića"
    },
    {
        "grad": "Priština",
        "opstina": "Donja Brnjica",
        "lokacija": "Donja Brnjica"
    },
    {
        "grad": "Priština",
        "opstina": "Dragovac",
        "lokacija": "Dragovac"
    },
    {
        "grad": "Priština",
        "opstina": "Drenovac",
        "lokacija": "Drenovac"
    },
    {
        "grad": "Priština",
        "opstina": "Zlatare",
        "lokacija": "Zlatare"
    },
    {
        "grad": "Priština",
        "opstina": "Zlaš",
        "lokacija": "Zlaš"
    },
    {
        "grad": "Priština",
        "opstina": "Kačikol",
        "lokacija": "Kačikol"
    },
    {
        "grad": "Priština",
        "opstina": "Kojlovica",
        "lokacija": "Kojlovica"
    },
    {
        "grad": "Priština",
        "opstina": "Kolić",
        "lokacija": "Kolić"
    },
    {
        "grad": "Priština",
        "opstina": "Kukavica",
        "lokacija": "Kukavica"
    },
    {
        "grad": "Priština",
        "opstina": "Laplje Selo",
        "lokacija": "Laplje Selo"
    },
    {
        "grad": "Priština",
        "opstina": "Lebane",
        "lokacija": "Lebane"
    },
    {
        "grad": "Priština",
        "opstina": "Lukare",
        "lokacija": "Lukare"
    },
    {
        "grad": "Priština",
        "opstina": "Makovac",
        "lokacija": "Makovac"
    },
    {
        "grad": "Priština",
        "opstina": "Marevce",
        "lokacija": "Marevce"
    },
    {
        "grad": "Priština",
        "opstina": "Matičane",
        "lokacija": "Matičane"
    },
    {
        "grad": "Priština",
        "opstina": "Mramor",
        "lokacija": "Mramor"
    },
    {
        "grad": "Priština",
        "opstina": "Niševce",
        "lokacija": "Niševce"
    },
    {
        "grad": "Priština",
        "opstina": "Orlović",
        "lokacija": "Orlović"
    },
    {
        "grad": "Priština",
        "opstina": "Preoce",
        "lokacija": "Preoce"
    },
    {
        "grad": "Priština",
        "opstina": "Propaštica",
        "lokacija": "Propaštica"
    },
    {
        "grad": "Priština",
        "opstina": "Prugovac",
        "lokacija": "Prugovac"
    },
    {
        "grad": "Priština",
        "opstina": "Radoševac",
        "lokacija": "Radoševac"
    },
    {
        "grad": "Priština",
        "opstina": "Rimanište",
        "lokacija": "Rimanište"
    },
    {
        "grad": "Priština",
        "opstina": "Sićevo",
        "lokacija": "Sićevo"
    },
    {
        "grad": "Priština",
        "opstina": "Slivovo",
        "lokacija": "Slivovo"
    },
    {
        "grad": "Priština",
        "opstina": "Sofalija",
        "lokacija": "Sofalija"
    },
    {
        "grad": "Priština",
        "opstina": "Sušica",
        "lokacija": "Sušica"
    },
    {
        "grad": "Priština",
        "opstina": "Teneš Do",
        "lokacija": "Teneš Do"
    },
    {
        "grad": "Priština",
        "opstina": "Trudna",
        "lokacija": "Trudna"
    },
    {
        "grad": "Priština",
        "opstina": "Čaglavica",
        "lokacija": "Čaglavica"
    },
    {
        "grad": "Priština",
        "opstina": "Šarban",
        "lokacija": "Šarban"
    },
    {
        "grad": "Priština",
        "opstina": "Šaškovac",
        "lokacija": "Šaškovac"
    },
    {
        "grad": "Ada",
        "opstina": "Ada",
        "lokacija": "Ada"
    },
    {
        "grad": "Ada",
        "opstina": "Gradska lokacija",
        "lokacija": "Druga Mesna Zajednica"
    },
    {
        "grad": "Ada",
        "opstina": "Gradska lokacija",
        "lokacija": "Prva Mesna Zajednica"
    },
    {
        "grad": "Ada",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Ada",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Ada",
        "opstina": "Mol",
        "lokacija": "Mol"
    },
    {
        "grad": "Ada",
        "opstina": "Obornjača",
        "lokacija": "Obornjača"
    },
    {
        "grad": "Ada",
        "opstina": "Sterijino",
        "lokacija": "Sterijino"
    },
    {
        "grad": "Ada",
        "opstina": "Utrine",
        "lokacija": "Utrine"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Aleksandrovac",
        "lokacija": "Aleksandrovac"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Bzenice",
        "lokacija": "Bzenice"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Bobote",
        "lokacija": "Bobote"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Boturići",
        "lokacija": "Boturići"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Bratići",
        "lokacija": "Bratići"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Velika Vrbnica",
        "lokacija": "Velika Vrbnica"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Velja Glava",
        "lokacija": "Velja Glava"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Venčac",
        "lokacija": "Venčac"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Vitkovo",
        "lokacija": "Vitkovo"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Vražogrnci",
        "lokacija": "Vražogrnci"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Vranštica",
        "lokacija": "Vranštica"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Vrbnica",
        "lokacija": "Vrbnica"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Garevina",
        "lokacija": "Garevina"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Gornja Zleginja",
        "lokacija": "Gornja Zleginja"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Gornje Rataje",
        "lokacija": "Gornje Rataje"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Gornji Vratari",
        "lokacija": "Gornji Vratari"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Gornji Stupanj",
        "lokacija": "Gornji Stupanj"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Grčak",
        "lokacija": "Grčak"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Dašnica",
        "lokacija": "Dašnica"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Dobroljupci",
        "lokacija": "Dobroljupci"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Donja Zleginja",
        "lokacija": "Donja Zleginja"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Donje Rataje",
        "lokacija": "Donje Rataje"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Donji Vratari",
        "lokacija": "Donji Vratari"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Donji Stupanj",
        "lokacija": "Donji Stupanj"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Drenča",
        "lokacija": "Drenča"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Jelakci",
        "lokacija": "Jelakci"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Kožetin",
        "lokacija": "Kožetin"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Koznica",
        "lokacija": "Koznica"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Latkovac",
        "lokacija": "Latkovac"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Laćisled",
        "lokacija": "Laćisled"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Lesenovci",
        "lokacija": "Lesenovci"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Leskovica",
        "lokacija": "Leskovica"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Ljubinci",
        "lokacija": "Ljubinci"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Mrmoš",
        "lokacija": "Mrmoš"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Novaci",
        "lokacija": "Novaci"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Panjevac",
        "lokacija": "Panjevac"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Parčin",
        "lokacija": "Parčin"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Pleš",
        "lokacija": "Pleš"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Ploča",
        "lokacija": "Ploča"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Popovci",
        "lokacija": "Popovci"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Puhovac",
        "lokacija": "Puhovac"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Raklja",
        "lokacija": "Raklja"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Ržanica",
        "lokacija": "Ržanica"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Rogavčina",
        "lokacija": "Rogavčina"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Rokci",
        "lokacija": "Rokci"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Rudenice",
        "lokacija": "Rudenice"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Stanjevo",
        "lokacija": "Stanjevo"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Starci",
        "lokacija": "Starci"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Strmenica",
        "lokacija": "Strmenica"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Stubal",
        "lokacija": "Stubal"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Subotica",
        "lokacija": "Subotica"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Tržac",
        "lokacija": "Tržac"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Trnavci",
        "lokacija": "Trnavci"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Tuleš",
        "lokacija": "Tuleš"
    },
    {
        "grad": "Aleksandrovac",
        "opstina": "Šljivovo",
        "lokacija": "Šljivovo"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Aleksinac",
        "lokacija": "Aleksinac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gradska lokacija",
        "lokacija": "Žitkovački Put"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona Kukiš"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gradska lokacija",
        "lokacija": "Logorište"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gradska lokacija",
        "lokacija": "Mikro Naselje"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Naselje"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gradska lokacija",
        "lokacija": "Padalište"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gradska lokacija",
        "lokacija": "Palilula"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Aleksinački Bujmir",
        "lokacija": "Aleksinački Bujmir"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Aleksinački Rudnik",
        "lokacija": "Aleksinački Rudnik"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Bankovac",
        "lokacija": "Bankovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Beli Breg",
        "lokacija": "Beli Breg"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Belja",
        "lokacija": "Belja"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Bobovište",
        "lokacija": "Bobovište"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Bovan",
        "lokacija": "Bovan"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Bradarac",
        "lokacija": "Bradarac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Vakup",
        "lokacija": "Vakup"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Veliki Drenovac",
        "lokacija": "Veliki Drenovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Vitkovac",
        "lokacija": "Vitkovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Vrelo",
        "lokacija": "Vrelo"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Vrćenovica",
        "lokacija": "Vrćenovica"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Vukanja",
        "lokacija": "Vukanja"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Vukašinovac",
        "lokacija": "Vukašinovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Glogovica",
        "lokacija": "Glogovica"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Golešnica",
        "lokacija": "Golešnica"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gornja Peščanica",
        "lokacija": "Gornja Peščanica"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gornje Suhotno",
        "lokacija": "Gornje Suhotno"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gornji Adrovac",
        "lokacija": "Gornji Adrovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gornji Krupac",
        "lokacija": "Gornji Krupac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gornji Ljubeš",
        "lokacija": "Gornji Ljubeš"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Gredetin",
        "lokacija": "Gredetin"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Grejač",
        "lokacija": "Grejač"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Dašnica",
        "lokacija": "Dašnica"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Deligrad",
        "lokacija": "Deligrad"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Dobrujevac",
        "lokacija": "Dobrujevac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Donja Peščanica",
        "lokacija": "Donja Peščanica"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Donje Suhotno",
        "lokacija": "Donje Suhotno"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Donji Adrovac",
        "lokacija": "Donji Adrovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Donji Krupac",
        "lokacija": "Donji Krupac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Donji Ljubeš",
        "lokacija": "Donji Ljubeš"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Draževac",
        "lokacija": "Draževac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Žitkovac",
        "lokacija": "Žitkovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Jakovlje",
        "lokacija": "Jakovlje"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Jasenje",
        "lokacija": "Jasenje"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Kamenica",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Katun",
        "lokacija": "Katun"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Koprivnica",
        "lokacija": "Koprivnica"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Korman",
        "lokacija": "Korman"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Kraljevo",
        "lokacija": "Kraljevo"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Krušje",
        "lokacija": "Krušje"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Kulina",
        "lokacija": "Kulina"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Lipovac",
        "lokacija": "Lipovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Loznac",
        "lokacija": "Loznac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Loćika",
        "lokacija": "Loćika"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Lužane",
        "lokacija": "Lužane"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Ljupten",
        "lokacija": "Ljupten"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Mali Drenovac",
        "lokacija": "Mali Drenovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Mozgovo",
        "lokacija": "Mozgovo"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Moravac",
        "lokacija": "Moravac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Moravski Bujmir",
        "lokacija": "Moravski Bujmir"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Nozrina",
        "lokacija": "Nozrina"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Porodin",
        "lokacija": "Porodin"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Prekonozi",
        "lokacija": "Prekonozi"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Prćilovica",
        "lokacija": "Prćilovica"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Prugovac",
        "lokacija": "Prugovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Radevce",
        "lokacija": "Radevce"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Rsovac",
        "lokacija": "Rsovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Rutevac",
        "lokacija": "Rutevac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Srezovac",
        "lokacija": "Srezovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Stanci",
        "lokacija": "Stanci"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Stublina",
        "lokacija": "Stublina"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Subotinac",
        "lokacija": "Subotinac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Tešica",
        "lokacija": "Tešica"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Trnjane",
        "lokacija": "Trnjane"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Ćićina",
        "lokacija": "Ćićina"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Crna Bara",
        "lokacija": "Crna Bara"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Česta",
        "lokacija": "Česta"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Čukurovac",
        "lokacija": "Čukurovac"
    },
    {
        "grad": "Aleksinac",
        "opstina": "Šurić",
        "lokacija": "Šurić"
    },
    {
        "grad": "Alibunar",
        "opstina": "Alibunar",
        "lokacija": "Alibunar"
    },
    {
        "grad": "Alibunar",
        "opstina": "Gradska lokacija",
        "lokacija": "Vašarište"
    },
    {
        "grad": "Alibunar",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Alibunar",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Alibunar",
        "opstina": "Banatski Karlovac",
        "lokacija": "Banatski Karlovac"
    },
    {
        "grad": "Alibunar",
        "opstina": "Vladimirovac",
        "lokacija": "Vladimirovac"
    },
    {
        "grad": "Alibunar",
        "opstina": "Devojački Bunar",
        "lokacija": "Devojački Bunar"
    },
    {
        "grad": "Alibunar",
        "opstina": "Dobrica",
        "lokacija": "Dobrica"
    },
    {
        "grad": "Alibunar",
        "opstina": "Ilandža",
        "lokacija": "Ilandža"
    },
    {
        "grad": "Alibunar",
        "opstina": "Janošik",
        "lokacija": "Janošik"
    },
    {
        "grad": "Alibunar",
        "opstina": "Lokve",
        "lokacija": "Lokve"
    },
    {
        "grad": "Alibunar",
        "opstina": "Nikolinci",
        "lokacija": "Nikolinci"
    },
    {
        "grad": "Alibunar",
        "opstina": "Novi Kozjak",
        "lokacija": "Novi Kozjak"
    },
    {
        "grad": "Alibunar",
        "opstina": "Seleuš",
        "lokacija": "Seleuš"
    },
    {
        "grad": "Apatin",
        "opstina": "Apatin",
        "lokacija": "Apatin"
    },
    {
        "grad": "Apatin",
        "opstina": "Gradska lokacija",
        "lokacija": "Popini Vinogradi"
    },
    {
        "grad": "Apatin",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Apatin",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Apatin",
        "opstina": "Kupusina",
        "lokacija": "Kupusina"
    },
    {
        "grad": "Apatin",
        "opstina": "Prigrevica",
        "lokacija": "Prigrevica"
    },
    {
        "grad": "Apatin",
        "opstina": "Svilojevo",
        "lokacija": "Svilojevo"
    },
    {
        "grad": "Apatin",
        "opstina": "Sonta",
        "lokacija": "Sonta"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Aranđelovac",
        "lokacija": "Aranđelovac"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Đajino Brdo"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Đikino Brdo"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Đunis"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Zlatar"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Jelinac"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Ješovac"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kolonija"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Otvoreno Polje"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Preseka"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Risovača"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Seničani"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Slatina"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Banja",
        "lokacija": "Banja"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Bosuta",
        "lokacija": "Bosuta"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Brezovac",
        "lokacija": "Brezovac"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Bukovik",
        "lokacija": "Bukovik"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Bukulja",
        "lokacija": "Bukulja"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Venčane",
        "lokacija": "Venčane"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Vrbica",
        "lokacija": "Vrbica"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Vukosavci",
        "lokacija": "Vukosavci"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Garaši",
        "lokacija": "Garaši"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Gornja Trešnjevica",
        "lokacija": "Gornja Trešnjevica"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Darosava",
        "lokacija": "Darosava"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Jelovik",
        "lokacija": "Jelovik"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Kopljare",
        "lokacija": "Kopljare"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Misača",
        "lokacija": "Misača"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Orašac",
        "lokacija": "Orašac"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Progoreoci",
        "lokacija": "Progoreoci"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Ranilović",
        "lokacija": "Ranilović"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Stojnik",
        "lokacija": "Stojnik"
    },
    {
        "grad": "Aranđelovac",
        "opstina": "Tulež",
        "lokacija": "Tulež"
    },
    {
        "grad": "Arilje",
        "opstina": "Arilje",
        "lokacija": "Arilje"
    },
    {
        "grad": "Arilje",
        "opstina": "Gradska lokacija",
        "lokacija": "Gruda"
    },
    {
        "grad": "Arilje",
        "opstina": "Gradska lokacija",
        "lokacija": "Mirotin"
    },
    {
        "grad": "Arilje",
        "opstina": "Gradska lokacija",
        "lokacija": "Mlekara"
    },
    {
        "grad": "Arilje",
        "opstina": "Gradska lokacija",
        "lokacija": "Piskavice"
    },
    {
        "grad": "Arilje",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Arilje",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Arilje",
        "opstina": "Bjeluša",
        "lokacija": "Bjeluša"
    },
    {
        "grad": "Arilje",
        "opstina": "Bogojevići",
        "lokacija": "Bogojevići"
    },
    {
        "grad": "Arilje",
        "opstina": "Brekovo",
        "lokacija": "Brekovo"
    },
    {
        "grad": "Arilje",
        "opstina": "Vigošte",
        "lokacija": "Vigošte"
    },
    {
        "grad": "Arilje",
        "opstina": "Virovo",
        "lokacija": "Virovo"
    },
    {
        "grad": "Arilje",
        "opstina": "Visoka",
        "lokacija": "Visoka"
    },
    {
        "grad": "Arilje",
        "opstina": "Vrane",
        "lokacija": "Vrane"
    },
    {
        "grad": "Arilje",
        "opstina": "Grdovići",
        "lokacija": "Grdovići"
    },
    {
        "grad": "Arilje",
        "opstina": "Grivska",
        "lokacija": "Grivska"
    },
    {
        "grad": "Arilje",
        "opstina": "Dobrače",
        "lokacija": "Dobrače"
    },
    {
        "grad": "Arilje",
        "opstina": "Dragojevac",
        "lokacija": "Dragojevac"
    },
    {
        "grad": "Arilje",
        "opstina": "Kruščica",
        "lokacija": "Kruščica"
    },
    {
        "grad": "Arilje",
        "opstina": "Latvica",
        "lokacija": "Latvica"
    },
    {
        "grad": "Arilje",
        "opstina": "Mirosaljci",
        "lokacija": "Mirosaljci"
    },
    {
        "grad": "Arilje",
        "opstina": "Pogled",
        "lokacija": "Pogled"
    },
    {
        "grad": "Arilje",
        "opstina": "Radobuđa",
        "lokacija": "Radobuđa"
    },
    {
        "grad": "Arilje",
        "opstina": "Radoševo",
        "lokacija": "Radoševo"
    },
    {
        "grad": "Arilje",
        "opstina": "Severovo",
        "lokacija": "Severovo"
    },
    {
        "grad": "Arilje",
        "opstina": "Stupčevići",
        "lokacija": "Stupčevići"
    },
    {
        "grad": "Arilje",
        "opstina": "Trešnjevica",
        "lokacija": "Trešnjevica"
    },
    {
        "grad": "Arilje",
        "opstina": "Cerova",
        "lokacija": "Cerova"
    },
    {
        "grad": "Babušnica",
        "opstina": "Babušnica",
        "lokacija": "Babušnica"
    },
    {
        "grad": "Babušnica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Babušnica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Babušnica",
        "opstina": "Berduj",
        "lokacija": "Berduj"
    },
    {
        "grad": "Babušnica",
        "opstina": "Berin Izvor",
        "lokacija": "Berin Izvor"
    },
    {
        "grad": "Babušnica",
        "opstina": "Bogdanovac",
        "lokacija": "Bogdanovac"
    },
    {
        "grad": "Babušnica",
        "opstina": "Bratiševac",
        "lokacija": "Bratiševac"
    },
    {
        "grad": "Babušnica",
        "opstina": "Brestov Dol",
        "lokacija": "Brestov Dol"
    },
    {
        "grad": "Babušnica",
        "opstina": "Vava",
        "lokacija": "Vava"
    },
    {
        "grad": "Babušnica",
        "opstina": "Valniš",
        "lokacija": "Valniš"
    },
    {
        "grad": "Babušnica",
        "opstina": "Veliko Bonjince",
        "lokacija": "Veliko Bonjince"
    },
    {
        "grad": "Babušnica",
        "opstina": "Vojnici",
        "lokacija": "Vojnici"
    },
    {
        "grad": "Babušnica",
        "opstina": "Vrelo",
        "lokacija": "Vrelo"
    },
    {
        "grad": "Babušnica",
        "opstina": "Vuči Del",
        "lokacija": "Vuči Del"
    },
    {
        "grad": "Babušnica",
        "opstina": "Gornje Krnjino",
        "lokacija": "Gornje Krnjino"
    },
    {
        "grad": "Babušnica",
        "opstina": "Gornji Striževac",
        "lokacija": "Gornji Striževac"
    },
    {
        "grad": "Babušnica",
        "opstina": "Gorčinci",
        "lokacija": "Gorčinci"
    },
    {
        "grad": "Babušnica",
        "opstina": "Grnčar",
        "lokacija": "Grnčar"
    },
    {
        "grad": "Babušnica",
        "opstina": "Dol",
        "lokacija": "Dol"
    },
    {
        "grad": "Babušnica",
        "opstina": "Donje Krnjino",
        "lokacija": "Donje Krnjino"
    },
    {
        "grad": "Babušnica",
        "opstina": "Donji Striževac",
        "lokacija": "Donji Striževac"
    },
    {
        "grad": "Babušnica",
        "opstina": "Draginac",
        "lokacija": "Draginac"
    },
    {
        "grad": "Babušnica",
        "opstina": "Dučevac",
        "lokacija": "Dučevac"
    },
    {
        "grad": "Babušnica",
        "opstina": "Zavidnice",
        "lokacija": "Zavidnice"
    },
    {
        "grad": "Babušnica",
        "opstina": "Zvonce",
        "lokacija": "Zvonce"
    },
    {
        "grad": "Babušnica",
        "opstina": "Izvor",
        "lokacija": "Izvor"
    },
    {
        "grad": "Babušnica",
        "opstina": "Jasenov Del",
        "lokacija": "Jasenov Del"
    },
    {
        "grad": "Babušnica",
        "opstina": "Kaluđerovo",
        "lokacija": "Kaluđerovo"
    },
    {
        "grad": "Babušnica",
        "opstina": "Kambelevci",
        "lokacija": "Kambelevci"
    },
    {
        "grad": "Babušnica",
        "opstina": "Kijevac",
        "lokacija": "Kijevac"
    },
    {
        "grad": "Babušnica",
        "opstina": "Leskovica",
        "lokacija": "Leskovica"
    },
    {
        "grad": "Babušnica",
        "opstina": "Linovo",
        "lokacija": "Linovo"
    },
    {
        "grad": "Babušnica",
        "opstina": "Ljuberađa",
        "lokacija": "Ljuberađa"
    },
    {
        "grad": "Babušnica",
        "opstina": "Malo Bonjince",
        "lokacija": "Malo Bonjince"
    },
    {
        "grad": "Babušnica",
        "opstina": "Masurovci",
        "lokacija": "Masurovci"
    },
    {
        "grad": "Babušnica",
        "opstina": "Mezgraja",
        "lokacija": "Mezgraja"
    },
    {
        "grad": "Babušnica",
        "opstina": "Modra Stena",
        "lokacija": "Modra Stena"
    },
    {
        "grad": "Babušnica",
        "opstina": "Našuškovica",
        "lokacija": "Našuškovica"
    },
    {
        "grad": "Babušnica",
        "opstina": "Ostatovica",
        "lokacija": "Ostatovica"
    },
    {
        "grad": "Babušnica",
        "opstina": "Preseka",
        "lokacija": "Preseka"
    },
    {
        "grad": "Babušnica",
        "opstina": "Provaljenik",
        "lokacija": "Provaljenik"
    },
    {
        "grad": "Babušnica",
        "opstina": "Radinjinci",
        "lokacija": "Radinjinci"
    },
    {
        "grad": "Babušnica",
        "opstina": "Radosinj",
        "lokacija": "Radosinj"
    },
    {
        "grad": "Babušnica",
        "opstina": "Radoševac",
        "lokacija": "Radoševac"
    },
    {
        "grad": "Babušnica",
        "opstina": "Rakita",
        "lokacija": "Rakita"
    },
    {
        "grad": "Babušnica",
        "opstina": "Rakov Dol",
        "lokacija": "Rakov Dol"
    },
    {
        "grad": "Babušnica",
        "opstina": "Raljin",
        "lokacija": "Raljin"
    },
    {
        "grad": "Babušnica",
        "opstina": "Resnik",
        "lokacija": "Resnik"
    },
    {
        "grad": "Babušnica",
        "opstina": "Stol",
        "lokacija": "Stol"
    },
    {
        "grad": "Babušnica",
        "opstina": "Strelac",
        "lokacija": "Strelac"
    },
    {
        "grad": "Babušnica",
        "opstina": "Studena",
        "lokacija": "Studena"
    },
    {
        "grad": "Babušnica",
        "opstina": "Suračevo",
        "lokacija": "Suračevo"
    },
    {
        "grad": "Babušnica",
        "opstina": "Crvena Jabuka",
        "lokacija": "Crvena Jabuka"
    },
    {
        "grad": "Babušnica",
        "opstina": "Štrbovac",
        "lokacija": "Štrbovac"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Bajina Bašta",
        "lokacija": "Bajina Bašta"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Bačevci",
        "lokacija": "Bačevci"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Beserovina",
        "lokacija": "Beserovina"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Višesava",
        "lokacija": "Višesava"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Gvozdac",
        "lokacija": "Gvozdac"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Dobrotin",
        "lokacija": "Dobrotin"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Draksin",
        "lokacija": "Draksin"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Dub",
        "lokacija": "Dub"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Zaglavak",
        "lokacija": "Zaglavak"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Zaovine",
        "lokacija": "Zaovine"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Zarožje",
        "lokacija": "Zarožje"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Zaugline",
        "lokacija": "Zaugline"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Zlodol",
        "lokacija": "Zlodol"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Jagoštica",
        "lokacija": "Jagoštica"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Jakalj",
        "lokacija": "Jakalj"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Jelovik",
        "lokacija": "Jelovik"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Konjska Reka",
        "lokacija": "Konjska Reka"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Kostojevići",
        "lokacija": "Kostojevići"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Lug",
        "lokacija": "Lug"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Lještansko",
        "lokacija": "Lještansko"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Mala Reka",
        "lokacija": "Mala Reka"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Obajgora",
        "lokacija": "Obajgora"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Ovčinja",
        "lokacija": "Ovčinja"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Okletac",
        "lokacija": "Okletac"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Osluša",
        "lokacija": "Osluša"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Pepelj",
        "lokacija": "Pepelj"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Perućac",
        "lokacija": "Perućac"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Pilica",
        "lokacija": "Pilica"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Pridoli",
        "lokacija": "Pridoli"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Rastište",
        "lokacija": "Rastište"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Rača",
        "lokacija": "Rača"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Rogačica",
        "lokacija": "Rogačica"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Sijerač",
        "lokacija": "Sijerač"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Solotuša",
        "lokacija": "Solotuša"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Strmovo",
        "lokacija": "Strmovo"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Cerje",
        "lokacija": "Cerje"
    },
    {
        "grad": "Bajina Bašta",
        "opstina": "Crvica",
        "lokacija": "Crvica"
    },
    {
        "grad": "Batočina",
        "opstina": "Batočina",
        "lokacija": "Batočina"
    },
    {
        "grad": "Batočina",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Batočina",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Batočina",
        "opstina": "Badnjevac",
        "lokacija": "Badnjevac"
    },
    {
        "grad": "Batočina",
        "opstina": "Brzan",
        "lokacija": "Brzan"
    },
    {
        "grad": "Batočina",
        "opstina": "gradac",
        "lokacija": "gradac"
    },
    {
        "grad": "Batočina",
        "opstina": "Dobrovodica",
        "lokacija": "Dobrovodica"
    },
    {
        "grad": "Batočina",
        "opstina": "Žirovnica",
        "lokacija": "Žirovnica"
    },
    {
        "grad": "Batočina",
        "opstina": "Kijevo",
        "lokacija": "Kijevo"
    },
    {
        "grad": "Batočina",
        "opstina": "Milatovac",
        "lokacija": "Milatovac"
    },
    {
        "grad": "Batočina",
        "opstina": "Nikšić",
        "lokacija": "Nikšić"
    },
    {
        "grad": "Batočina",
        "opstina": "Prnjavor",
        "lokacija": "Prnjavor"
    },
    {
        "grad": "Batočina",
        "opstina": "Crni Kao",
        "lokacija": "Crni Kao"
    },
    {
        "grad": "Bač",
        "opstina": "Bač",
        "lokacija": "Bač"
    },
    {
        "grad": "Bač",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bač",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bač",
        "opstina": "Bačko Novo Selo",
        "lokacija": "Bačko Novo Selo"
    },
    {
        "grad": "Bač",
        "opstina": "Bođani",
        "lokacija": "Bođani"
    },
    {
        "grad": "Bač",
        "opstina": "Vajska",
        "lokacija": "Vajska"
    },
    {
        "grad": "Bač",
        "opstina": "Plavna",
        "lokacija": "Plavna"
    },
    {
        "grad": "Bač",
        "opstina": "Selenča",
        "lokacija": "Selenča"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Bačka Palanka",
        "lokacija": "Bačka Palanka"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Blok Kaloš 1"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Blok Kaloš 2"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Bratstvo"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Dunav"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Nova Palanka"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Sinaj"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Stara Palanka"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Stari grad"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Vizić",
        "lokacija": "Vizić"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Gajdobra",
        "lokacija": "Gajdobra"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Despotovo",
        "lokacija": "Despotovo"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Karađorđevo",
        "lokacija": "Karađorđevo"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Mladenovo",
        "lokacija": "Mladenovo"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Neštin",
        "lokacija": "Neštin"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Nova Gajdobra",
        "lokacija": "Nova Gajdobra"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Obrovac",
        "lokacija": "Obrovac"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Parage",
        "lokacija": "Parage"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Pivnice",
        "lokacija": "Pivnice"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Silbaš",
        "lokacija": "Silbaš"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Tovariševo",
        "lokacija": "Tovariševo"
    },
    {
        "grad": "Bačka Palanka",
        "opstina": "Čelarevo",
        "lokacija": "Čelarevo"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Bačka Topola",
        "lokacija": "Bačka Topola"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Vašarište"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Bagremovo",
        "lokacija": "Bagremovo"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Bajša",
        "lokacija": "Bajša"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Bački Sokolac",
        "lokacija": "Bački Sokolac"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Bogaraš",
        "lokacija": "Bogaraš"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Gornja Rogatica",
        "lokacija": "Gornja Rogatica"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Gunaroš",
        "lokacija": "Gunaroš"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Zobnatica",
        "lokacija": "Zobnatica"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Kavilo",
        "lokacija": "Kavilo"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Karađorđevo",
        "lokacija": "Karađorđevo"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Krivaja",
        "lokacija": "Krivaja"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Mali Beograd",
        "lokacija": "Mali Beograd"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Mićunovo",
        "lokacija": "Mićunovo"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Novo Orahovo",
        "lokacija": "Novo Orahovo"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Njegoševo",
        "lokacija": "Njegoševo"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Obornjača",
        "lokacija": "Obornjača"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Tomislavci",
        "lokacija": "Tomislavci"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Panonija",
        "lokacija": "Panonija"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Pačir",
        "lokacija": "Pačir"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Pobeda",
        "lokacija": "Pobeda"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Svetićevo",
        "lokacija": "Svetićevo"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Srednji Salaš",
        "lokacija": "Srednji Salaš"
    },
    {
        "grad": "Bačka Topola",
        "opstina": "Stara Moravica",
        "lokacija": "Stara Moravica"
    },
    {
        "grad": "Bački Petrovac",
        "opstina": "Bački Petrovac",
        "lokacija": "Bački Petrovac"
    },
    {
        "grad": "Bački Petrovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bački Petrovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bački Petrovac",
        "opstina": "Gložan",
        "lokacija": "Gložan"
    },
    {
        "grad": "Bački Petrovac",
        "opstina": "Kulpin",
        "lokacija": "Kulpin"
    },
    {
        "grad": "Bački Petrovac",
        "opstina": "Maglić",
        "lokacija": "Maglić"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Bela Palanka",
        "lokacija": "Bela Palanka"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Babin Kal",
        "lokacija": "Babin Kal"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Bežište",
        "lokacija": "Bežište"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Bukurovac",
        "lokacija": "Bukurovac"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Veta",
        "lokacija": "Veta"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Vitanovac",
        "lokacija": "Vitanovac"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Vrandol",
        "lokacija": "Vrandol"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Vrgudinac",
        "lokacija": "Vrgudinac"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Glogovac",
        "lokacija": "Glogovac"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Gornja Glama",
        "lokacija": "Gornja Glama"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Gornja Koritnica",
        "lokacija": "Gornja Koritnica"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Gornji Rinj",
        "lokacija": "Gornji Rinj"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "gradište",
        "lokacija": "gradište"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Divljana",
        "lokacija": "Divljana"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Dolac (naselje)",
        "lokacija": "Dolac (naselje)"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Dolac (selo)",
        "lokacija": "Dolac (selo)"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Donja Glama",
        "lokacija": "Donja Glama"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Donja Koritnica",
        "lokacija": "Donja Koritnica"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Donji Rinj",
        "lokacija": "Donji Rinj"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Draževo",
        "lokacija": "Draževo"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Klenje",
        "lokacija": "Klenje"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Klisura",
        "lokacija": "Klisura"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Kozja",
        "lokacija": "Kozja"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Kosmovac",
        "lokacija": "Kosmovac"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Kremenica",
        "lokacija": "Kremenica"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Krupac",
        "lokacija": "Krupac"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Lanište",
        "lokacija": "Lanište"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Leskovik",
        "lokacija": "Leskovik"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Ljubatovica",
        "lokacija": "Ljubatovica"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Miranovac",
        "lokacija": "Miranovac"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Miranovačka Kula",
        "lokacija": "Miranovačka Kula"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Moklište",
        "lokacija": "Moklište"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Mokra",
        "lokacija": "Mokra"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Oreovac",
        "lokacija": "Oreovac"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Pajež",
        "lokacija": "Pajež"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Sinjac",
        "lokacija": "Sinjac"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Tamnjanica",
        "lokacija": "Tamnjanica"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Telovac",
        "lokacija": "Telovac"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Toponica",
        "lokacija": "Toponica"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Crvena Reka",
        "lokacija": "Crvena Reka"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Crveni Breg",
        "lokacija": "Crveni Breg"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Crnče",
        "lokacija": "Crnče"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Čiflik",
        "lokacija": "Čiflik"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Šljivovik",
        "lokacija": "Šljivovik"
    },
    {
        "grad": "Bela Palanka",
        "opstina": "Špaj",
        "lokacija": "Špaj"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Bela Crkva",
        "lokacija": "Bela Crkva"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Banatska Palanka",
        "lokacija": "Banatska Palanka"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Banatska Subotica",
        "lokacija": "Banatska Subotica"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Vračev Gaj",
        "lokacija": "Vračev Gaj"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Grebenac",
        "lokacija": "Grebenac"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Deliblatska Peščara",
        "lokacija": "Deliblatska Peščara"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Dobričevo",
        "lokacija": "Dobričevo"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Dupljaja",
        "lokacija": "Dupljaja"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Jasenovo",
        "lokacija": "Jasenovo"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Kajtasovo",
        "lokacija": "Kajtasovo"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Kaluđerovo",
        "lokacija": "Kaluđerovo"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Kruščica",
        "lokacija": "Kruščica"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Kusić",
        "lokacija": "Kusić"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Crvena Crkva",
        "lokacija": "Crvena Crkva"
    },
    {
        "grad": "Bela Crkva",
        "opstina": "Češko Selo",
        "lokacija": "Češko Selo"
    },
    {
        "grad": "Beočin",
        "opstina": "Beočin",
        "lokacija": "Beočin"
    },
    {
        "grad": "Beočin",
        "opstina": "Gradska lokacija",
        "lokacija": "Ekonomija"
    },
    {
        "grad": "Beočin",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Beočin",
        "opstina": "Gradska lokacija",
        "lokacija": "Kolonija"
    },
    {
        "grad": "Beočin",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Dunav"
    },
    {
        "grad": "Beočin",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Beočin",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Beočin",
        "opstina": "Gradska lokacija",
        "lokacija": "Šljivik"
    },
    {
        "grad": "Beočin",
        "opstina": "Banoštor",
        "lokacija": "Banoštor"
    },
    {
        "grad": "Beočin",
        "opstina": "Beočin Selo",
        "lokacija": "Beočin Selo"
    },
    {
        "grad": "Beočin",
        "opstina": "Brazilija",
        "lokacija": "Brazilija"
    },
    {
        "grad": "Beočin",
        "opstina": "Grabovo",
        "lokacija": "Grabovo"
    },
    {
        "grad": "Beočin",
        "opstina": "Koruška",
        "lokacija": "Koruška"
    },
    {
        "grad": "Beočin",
        "opstina": "Lug",
        "lokacija": "Lug"
    },
    {
        "grad": "Beočin",
        "opstina": "Rakovac",
        "lokacija": "Rakovac"
    },
    {
        "grad": "Beočin",
        "opstina": "Sviloš",
        "lokacija": "Sviloš"
    },
    {
        "grad": "Beočin",
        "opstina": "Susek",
        "lokacija": "Susek"
    },
    {
        "grad": "Beočin",
        "opstina": "Čerević",
        "lokacija": "Čerević"
    },
    {
        "grad": "Beočin",
        "opstina": "Šakotinac",
        "lokacija": "Šakotinac"
    },
    {
        "grad": "Bečej",
        "opstina": "Bečej",
        "lokacija": "Bečej"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Bratstvo Jedinstvo"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Veljko Vlahović"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Donji grad"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Ivan Perišić"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Kamp Naselje"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Mali Rit"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje 7 Sekretara SKOJ-a"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Picoder"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Putrija"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Ribnjak"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Stari Rit"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bečej",
        "opstina": "Bačko gradište",
        "lokacija": "Bačko gradište"
    },
    {
        "grad": "Bečej",
        "opstina": "Bačko Petrovo Selo",
        "lokacija": "Bačko Petrovo Selo"
    },
    {
        "grad": "Bečej",
        "opstina": "Mileševo",
        "lokacija": "Mileševo"
    },
    {
        "grad": "Bečej",
        "opstina": "Radičević",
        "lokacija": "Radičević"
    },
    {
        "grad": "Blace",
        "opstina": "Blace",
        "lokacija": "Blace"
    },
    {
        "grad": "Blace",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Blace",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Blace",
        "opstina": "Alabana",
        "lokacija": "Alabana"
    },
    {
        "grad": "Blace",
        "opstina": "Barbatovac",
        "lokacija": "Barbatovac"
    },
    {
        "grad": "Blace",
        "opstina": "Brežani",
        "lokacija": "Brežani"
    },
    {
        "grad": "Blace",
        "opstina": "Više Selo",
        "lokacija": "Više Selo"
    },
    {
        "grad": "Blace",
        "opstina": "Vrbovac",
        "lokacija": "Vrbovac"
    },
    {
        "grad": "Blace",
        "opstina": "Gornja Draguša",
        "lokacija": "Gornja Draguša"
    },
    {
        "grad": "Blace",
        "opstina": "Gornja Jošanica",
        "lokacija": "Gornja Jošanica"
    },
    {
        "grad": "Blace",
        "opstina": "Gornje Grgure",
        "lokacija": "Gornje Grgure"
    },
    {
        "grad": "Blace",
        "opstina": "Gornje Svarče",
        "lokacija": "Gornje Svarče"
    },
    {
        "grad": "Blace",
        "opstina": "Donja Draguša",
        "lokacija": "Donja Draguša"
    },
    {
        "grad": "Blace",
        "opstina": "Donja Jošanica",
        "lokacija": "Donja Jošanica"
    },
    {
        "grad": "Blace",
        "opstina": "Donja Rašica",
        "lokacija": "Donja Rašica"
    },
    {
        "grad": "Blace",
        "opstina": "Donje Grgure",
        "lokacija": "Donje Grgure"
    },
    {
        "grad": "Blace",
        "opstina": "Donje Svarče",
        "lokacija": "Donje Svarče"
    },
    {
        "grad": "Blace",
        "opstina": "Drešnica",
        "lokacija": "Drešnica"
    },
    {
        "grad": "Blace",
        "opstina": "Đurevac",
        "lokacija": "Đurevac"
    },
    {
        "grad": "Blace",
        "opstina": "Kačapor",
        "lokacija": "Kačapor"
    },
    {
        "grad": "Blace",
        "opstina": "Kaševar",
        "lokacija": "Kaševar"
    },
    {
        "grad": "Blace",
        "opstina": "Krivaja",
        "lokacija": "Krivaja"
    },
    {
        "grad": "Blace",
        "opstina": "Kutlovac",
        "lokacija": "Kutlovac"
    },
    {
        "grad": "Blace",
        "opstina": "Lazarevac",
        "lokacija": "Lazarevac"
    },
    {
        "grad": "Blace",
        "opstina": "Mala Draguša",
        "lokacija": "Mala Draguša"
    },
    {
        "grad": "Blace",
        "opstina": "Međuhana",
        "lokacija": "Međuhana"
    },
    {
        "grad": "Blace",
        "opstina": "Muzaće",
        "lokacija": "Muzaće"
    },
    {
        "grad": "Blace",
        "opstina": "Popova",
        "lokacija": "Popova"
    },
    {
        "grad": "Blace",
        "opstina": "Prebreza",
        "lokacija": "Prebreza"
    },
    {
        "grad": "Blace",
        "opstina": "Pretežana",
        "lokacija": "Pretežana"
    },
    {
        "grad": "Blace",
        "opstina": "Pretrešnja",
        "lokacija": "Pretrešnja"
    },
    {
        "grad": "Blace",
        "opstina": "Pridvorica",
        "lokacija": "Pridvorica"
    },
    {
        "grad": "Blace",
        "opstina": "Rašica",
        "lokacija": "Rašica"
    },
    {
        "grad": "Blace",
        "opstina": "Sibnica",
        "lokacija": "Sibnica"
    },
    {
        "grad": "Blace",
        "opstina": "Stubal",
        "lokacija": "Stubal"
    },
    {
        "grad": "Blace",
        "opstina": "Suvaja",
        "lokacija": "Suvaja"
    },
    {
        "grad": "Blace",
        "opstina": "Suvi Do",
        "lokacija": "Suvi Do"
    },
    {
        "grad": "Blace",
        "opstina": "Trbunje",
        "lokacija": "Trbunje"
    },
    {
        "grad": "Blace",
        "opstina": "Čungula",
        "lokacija": "Čungula"
    },
    {
        "grad": "Blace",
        "opstina": "Čučale",
        "lokacija": "Čučale"
    },
    {
        "grad": "Blace",
        "opstina": "Džepnica",
        "lokacija": "Džepnica"
    },
    {
        "grad": "Blace",
        "opstina": "Šiljomana",
        "lokacija": "Šiljomana"
    },
    {
        "grad": "Bogatić",
        "opstina": "Bogatić",
        "lokacija": "Bogatić"
    },
    {
        "grad": "Bogatić",
        "opstina": "Gradska lokacija",
        "lokacija": "Sveto Polje"
    },
    {
        "grad": "Bogatić",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bogatić",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bogatić",
        "opstina": "Badovinci",
        "lokacija": "Badovinci"
    },
    {
        "grad": "Bogatić",
        "opstina": "Banovo Polje",
        "lokacija": "Banovo Polje"
    },
    {
        "grad": "Bogatić",
        "opstina": "Belotić",
        "lokacija": "Belotić"
    },
    {
        "grad": "Bogatić",
        "opstina": "Glogovac",
        "lokacija": "Glogovac"
    },
    {
        "grad": "Bogatić",
        "opstina": "Glušci",
        "lokacija": "Glušci"
    },
    {
        "grad": "Bogatić",
        "opstina": "Dublje",
        "lokacija": "Dublje"
    },
    {
        "grad": "Bogatić",
        "opstina": "Klenje",
        "lokacija": "Klenje"
    },
    {
        "grad": "Bogatić",
        "opstina": "Metković",
        "lokacija": "Metković"
    },
    {
        "grad": "Bogatić",
        "opstina": "Očage",
        "lokacija": "Očage"
    },
    {
        "grad": "Bogatić",
        "opstina": "Salaš Crnobarski",
        "lokacija": "Salaš Crnobarski"
    },
    {
        "grad": "Bogatić",
        "opstina": "Sovljak",
        "lokacija": "Sovljak"
    },
    {
        "grad": "Bogatić",
        "opstina": "Uzveće",
        "lokacija": "Uzveće"
    },
    {
        "grad": "Bogatić",
        "opstina": "Crna Bara",
        "lokacija": "Crna Bara"
    },
    {
        "grad": "Bojnik",
        "opstina": "Bojnik",
        "lokacija": "Bojnik"
    },
    {
        "grad": "Bojnik",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bojnik",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bojnik",
        "opstina": "Borince",
        "lokacija": "Borince"
    },
    {
        "grad": "Bojnik",
        "opstina": "Brestovac",
        "lokacija": "Brestovac"
    },
    {
        "grad": "Bojnik",
        "opstina": "Vujanovo",
        "lokacija": "Vujanovo"
    },
    {
        "grad": "Bojnik",
        "opstina": "Gornje Brijanje",
        "lokacija": "Gornje Brijanje"
    },
    {
        "grad": "Bojnik",
        "opstina": "Gornje Konjuvce",
        "lokacija": "Gornje Konjuvce"
    },
    {
        "grad": "Bojnik",
        "opstina": "Granica",
        "lokacija": "Granica"
    },
    {
        "grad": "Bojnik",
        "opstina": "Dobra Voda",
        "lokacija": "Dobra Voda"
    },
    {
        "grad": "Bojnik",
        "opstina": "Donje Konjuvce",
        "lokacija": "Donje Konjuvce"
    },
    {
        "grad": "Bojnik",
        "opstina": "Dragovac",
        "lokacija": "Dragovac"
    },
    {
        "grad": "Bojnik",
        "opstina": "Dubrava",
        "lokacija": "Dubrava"
    },
    {
        "grad": "Bojnik",
        "opstina": "Đinđuša",
        "lokacija": "Đinđuša"
    },
    {
        "grad": "Bojnik",
        "opstina": "Zeletovo",
        "lokacija": "Zeletovo"
    },
    {
        "grad": "Bojnik",
        "opstina": "Zorovac",
        "lokacija": "Zorovac"
    },
    {
        "grad": "Bojnik",
        "opstina": "Ivanje",
        "lokacija": "Ivanje"
    },
    {
        "grad": "Bojnik",
        "opstina": "Kamenica",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Bojnik",
        "opstina": "Kacabać",
        "lokacija": "Kacabać"
    },
    {
        "grad": "Bojnik",
        "opstina": "Kosančić",
        "lokacija": "Kosančić"
    },
    {
        "grad": "Bojnik",
        "opstina": "Lapotince",
        "lokacija": "Lapotince"
    },
    {
        "grad": "Bojnik",
        "opstina": "Lozane",
        "lokacija": "Lozane"
    },
    {
        "grad": "Bojnik",
        "opstina": "Magaš",
        "lokacija": "Magaš"
    },
    {
        "grad": "Bojnik",
        "opstina": "Majkovac",
        "lokacija": "Majkovac"
    },
    {
        "grad": "Bojnik",
        "opstina": "Mijajlica",
        "lokacija": "Mijajlica"
    },
    {
        "grad": "Bojnik",
        "opstina": "Mrveš",
        "lokacija": "Mrveš"
    },
    {
        "grad": "Bojnik",
        "opstina": "Obilić",
        "lokacija": "Obilić"
    },
    {
        "grad": "Bojnik",
        "opstina": "Obražda",
        "lokacija": "Obražda"
    },
    {
        "grad": "Bojnik",
        "opstina": "Orane",
        "lokacija": "Orane"
    },
    {
        "grad": "Bojnik",
        "opstina": "Plavce",
        "lokacija": "Plavce"
    },
    {
        "grad": "Bojnik",
        "opstina": "Pridvorica",
        "lokacija": "Pridvorica"
    },
    {
        "grad": "Bojnik",
        "opstina": "Rečica",
        "lokacija": "Rečica"
    },
    {
        "grad": "Bojnik",
        "opstina": "Savinac",
        "lokacija": "Savinac"
    },
    {
        "grad": "Bojnik",
        "opstina": "Slavnik",
        "lokacija": "Slavnik"
    },
    {
        "grad": "Bojnik",
        "opstina": "Stubla",
        "lokacija": "Stubla"
    },
    {
        "grad": "Bojnik",
        "opstina": "Turjane",
        "lokacija": "Turjane"
    },
    {
        "grad": "Bojnik",
        "opstina": "Ćukovac",
        "lokacija": "Ćukovac"
    },
    {
        "grad": "Bojnik",
        "opstina": "Crkvice",
        "lokacija": "Crkvice"
    },
    {
        "grad": "Boljevac",
        "opstina": "Boljevac",
        "lokacija": "Boljevac"
    },
    {
        "grad": "Boljevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Boljevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Boljevac",
        "opstina": "Bačevica",
        "lokacija": "Bačevica"
    },
    {
        "grad": "Boljevac",
        "opstina": "Bogovina",
        "lokacija": "Bogovina"
    },
    {
        "grad": "Boljevac",
        "opstina": "Boljevac Selo",
        "lokacija": "Boljevac Selo"
    },
    {
        "grad": "Boljevac",
        "opstina": "Valakonje",
        "lokacija": "Valakonje"
    },
    {
        "grad": "Boljevac",
        "opstina": "Vrbovac",
        "lokacija": "Vrbovac"
    },
    {
        "grad": "Boljevac",
        "opstina": "Dobro Polje",
        "lokacija": "Dobro Polje"
    },
    {
        "grad": "Boljevac",
        "opstina": "Dobrujevac",
        "lokacija": "Dobrujevac"
    },
    {
        "grad": "Boljevac",
        "opstina": "Ilino",
        "lokacija": "Ilino"
    },
    {
        "grad": "Boljevac",
        "opstina": "Jablanica",
        "lokacija": "Jablanica"
    },
    {
        "grad": "Boljevac",
        "opstina": "Krivi Vir",
        "lokacija": "Krivi Vir"
    },
    {
        "grad": "Boljevac",
        "opstina": "Lukovo",
        "lokacija": "Lukovo"
    },
    {
        "grad": "Boljevac",
        "opstina": "Mali Izvor",
        "lokacija": "Mali Izvor"
    },
    {
        "grad": "Boljevac",
        "opstina": "Mirovo",
        "lokacija": "Mirovo"
    },
    {
        "grad": "Boljevac",
        "opstina": "Osnić",
        "lokacija": "Osnić"
    },
    {
        "grad": "Boljevac",
        "opstina": "Podgorac",
        "lokacija": "Podgorac"
    },
    {
        "grad": "Boljevac",
        "opstina": "Rtanj",
        "lokacija": "Rtanj"
    },
    {
        "grad": "Boljevac",
        "opstina": "Rujište",
        "lokacija": "Rujište"
    },
    {
        "grad": "Boljevac",
        "opstina": "Savinac",
        "lokacija": "Savinac"
    },
    {
        "grad": "Boljevac",
        "opstina": "Sumrakovac",
        "lokacija": "Sumrakovac"
    },
    {
        "grad": "Bor",
        "opstina": "Bor",
        "lokacija": "Bor"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "4. Mesna Zajednica"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "5. Mesna Zajednica"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Bolničko Naselje"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Kučajna"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Metalurg"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Bor 2"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Sunce"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Novi gradski Centar"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Selište"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Slatinsko Naselje"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Staro Selište"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Čoka Boruluj"
    },
    {
        "grad": "Bor",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bor",
        "opstina": "Borsko Jezero",
        "lokacija": "Borsko Jezero"
    },
    {
        "grad": "Bor",
        "opstina": "Brestovac",
        "lokacija": "Brestovac"
    },
    {
        "grad": "Bor",
        "opstina": "Brestovačka Banja",
        "lokacija": "Brestovačka Banja"
    },
    {
        "grad": "Bor",
        "opstina": "Bučje",
        "lokacija": "Bučje"
    },
    {
        "grad": "Bor",
        "opstina": "Gornjane",
        "lokacija": "Gornjane"
    },
    {
        "grad": "Bor",
        "opstina": "Donja Bela Reka",
        "lokacija": "Donja Bela Reka"
    },
    {
        "grad": "Bor",
        "opstina": "Zlot",
        "lokacija": "Zlot"
    },
    {
        "grad": "Bor",
        "opstina": "Krivelj",
        "lokacija": "Krivelj"
    },
    {
        "grad": "Bor",
        "opstina": "Luka",
        "lokacija": "Luka"
    },
    {
        "grad": "Bor",
        "opstina": "Metovnica",
        "lokacija": "Metovnica"
    },
    {
        "grad": "Bor",
        "opstina": "Oštrelj",
        "lokacija": "Oštrelj"
    },
    {
        "grad": "Bor",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Bor",
        "opstina": "Tanda",
        "lokacija": "Tanda"
    },
    {
        "grad": "Bor",
        "opstina": "Topla",
        "lokacija": "Topla"
    },
    {
        "grad": "Bor",
        "opstina": "Šarbanovac",
        "lokacija": "Šarbanovac"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Bosilegrad",
        "lokacija": "Bosilegrad"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Barje",
        "lokacija": "Barje"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Belut",
        "lokacija": "Belut"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Bistar",
        "lokacija": "Bistar"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Brankovci",
        "lokacija": "Brankovci"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Bresnica",
        "lokacija": "Bresnica"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Buceljevo",
        "lokacija": "Buceljevo"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Gložje",
        "lokacija": "Gložje"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Goleš",
        "lokacija": "Goleš"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Gornja Lisina",
        "lokacija": "Gornja Lisina"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Gornja Ljubata",
        "lokacija": "Gornja Ljubata"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Gornja Ržana",
        "lokacija": "Gornja Ržana"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Gornje Tlamino",
        "lokacija": "Gornje Tlamino"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Grujinci",
        "lokacija": "Grujinci"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Doganica",
        "lokacija": "Doganica"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Donja Lisina",
        "lokacija": "Donja Lisina"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Donja Ljubata",
        "lokacija": "Donja Ljubata"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Donja Ržana",
        "lokacija": "Donja Ržana"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Donje Tlamino",
        "lokacija": "Donje Tlamino"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Dukat",
        "lokacija": "Dukat"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Žeravino",
        "lokacija": "Žeravino"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Zli Dol",
        "lokacija": "Zli Dol"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Izvor",
        "lokacija": "Izvor"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Jarešnik",
        "lokacija": "Jarešnik"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Karamanica",
        "lokacija": "Karamanica"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Milevci",
        "lokacija": "Milevci"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Mlekominci",
        "lokacija": "Mlekominci"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Musulj",
        "lokacija": "Musulj"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Nazarica",
        "lokacija": "Nazarica"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Paralovo",
        "lokacija": "Paralovo"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Ploča",
        "lokacija": "Ploča"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Radičevci",
        "lokacija": "Radičevci"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Rajčilovci",
        "lokacija": "Rajčilovci"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Resen",
        "lokacija": "Resen"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Ribarci",
        "lokacija": "Ribarci"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Rikačevo",
        "lokacija": "Rikačevo"
    },
    {
        "grad": "Bosilegrad",
        "opstina": "Crnoštica",
        "lokacija": "Crnoštica"
    },
    {
        "grad": "Brus",
        "opstina": "Brus",
        "lokacija": "Brus"
    },
    {
        "grad": "Brus",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Brus",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Brus",
        "opstina": "Batote",
        "lokacija": "Batote"
    },
    {
        "grad": "Brus",
        "opstina": "Belo Polje",
        "lokacija": "Belo Polje"
    },
    {
        "grad": "Brus",
        "opstina": "Blaževo",
        "lokacija": "Blaževo"
    },
    {
        "grad": "Brus",
        "opstina": "Bogiše",
        "lokacija": "Bogiše"
    },
    {
        "grad": "Brus",
        "opstina": "Bozoljin",
        "lokacija": "Bozoljin"
    },
    {
        "grad": "Brus",
        "opstina": "Boranci",
        "lokacija": "Boranci"
    },
    {
        "grad": "Brus",
        "opstina": "Botunja",
        "lokacija": "Botunja"
    },
    {
        "grad": "Brus",
        "opstina": "Brđani",
        "lokacija": "Brđani"
    },
    {
        "grad": "Brus",
        "opstina": "Brzeće",
        "lokacija": "Brzeće"
    },
    {
        "grad": "Brus",
        "opstina": "Budilovina",
        "lokacija": "Budilovina"
    },
    {
        "grad": "Brus",
        "opstina": "Velika Grabovnica",
        "lokacija": "Velika Grabovnica"
    },
    {
        "grad": "Brus",
        "opstina": "Vitoše",
        "lokacija": "Vitoše"
    },
    {
        "grad": "Brus",
        "opstina": "Vlajkovci",
        "lokacija": "Vlajkovci"
    },
    {
        "grad": "Brus",
        "opstina": "Gornje Leviće",
        "lokacija": "Gornje Leviće"
    },
    {
        "grad": "Brus",
        "opstina": "Gornji Lipovac",
        "lokacija": "Gornji Lipovac"
    },
    {
        "grad": "Brus",
        "opstina": "grad",
        "lokacija": "grad"
    },
    {
        "grad": "Brus",
        "opstina": "gradac",
        "lokacija": "gradac"
    },
    {
        "grad": "Brus",
        "opstina": "Graševci",
        "lokacija": "Graševci"
    },
    {
        "grad": "Brus",
        "opstina": "Domiševina",
        "lokacija": "Domiševina"
    },
    {
        "grad": "Brus",
        "opstina": "Donje Leviće",
        "lokacija": "Donje Leviće"
    },
    {
        "grad": "Brus",
        "opstina": "Donji Lipovac",
        "lokacija": "Donji Lipovac"
    },
    {
        "grad": "Brus",
        "opstina": "Drenova",
        "lokacija": "Drenova"
    },
    {
        "grad": "Brus",
        "opstina": "Drtevci",
        "lokacija": "Drtevci"
    },
    {
        "grad": "Brus",
        "opstina": "Dupci",
        "lokacija": "Dupci"
    },
    {
        "grad": "Brus",
        "opstina": "Đerekare",
        "lokacija": "Đerekari"
    },
    {
        "grad": "Brus",
        "opstina": "Žarevo",
        "lokacija": "Žarevo"
    },
    {
        "grad": "Brus",
        "opstina": "Žilinci",
        "lokacija": "Žilinci"
    },
    {
        "grad": "Brus",
        "opstina": "Žiljci",
        "lokacija": "Žiljci"
    },
    {
        "grad": "Brus",
        "opstina": "Žunje",
        "lokacija": "Žunje"
    },
    {
        "grad": "Brus",
        "opstina": "Zlatari",
        "lokacija": "Zlatari"
    },
    {
        "grad": "Brus",
        "opstina": "Igroš",
        "lokacija": "Igroš"
    },
    {
        "grad": "Brus",
        "opstina": "Iričići",
        "lokacija": "Iričići"
    },
    {
        "grad": "Brus",
        "opstina": "Kneževo",
        "lokacija": "Kneževo"
    },
    {
        "grad": "Brus",
        "opstina": "Kobilje",
        "lokacija": "Kobilje"
    },
    {
        "grad": "Brus",
        "opstina": "Kovizle",
        "lokacija": "Kovizla"
    },
    {
        "grad": "Brus",
        "opstina": "Kovioci",
        "lokacija": "Kovioci"
    },
    {
        "grad": "Brus",
        "opstina": "Kočine",
        "lokacija": "Kočine"
    },
    {
        "grad": "Brus",
        "opstina": "Kriva Reka",
        "lokacija": "Kriva Reka"
    },
    {
        "grad": "Brus",
        "opstina": "Lepenac",
        "lokacija": "Lepenac"
    },
    {
        "grad": "Brus",
        "opstina": "Livađe",
        "lokacija": "Livađe"
    },
    {
        "grad": "Brus",
        "opstina": "Mala Vrbnica",
        "lokacija": "Mala Vrbnica"
    },
    {
        "grad": "Brus",
        "opstina": "Mala Grabovnica",
        "lokacija": "Mala Grabovnica"
    },
    {
        "grad": "Brus",
        "opstina": "Milentija",
        "lokacija": "Milentija"
    },
    {
        "grad": "Brus",
        "opstina": "Osreci",
        "lokacija": "Osredci"
    },
    {
        "grad": "Brus",
        "opstina": "Paljevštica",
        "lokacija": "Paljevštica"
    },
    {
        "grad": "Brus",
        "opstina": "Ravni",
        "lokacija": "Ravni"
    },
    {
        "grad": "Brus",
        "opstina": "Ravnište",
        "lokacija": "Ravnište"
    },
    {
        "grad": "Brus",
        "opstina": "Radmanovo",
        "lokacija": "Radmanovo"
    },
    {
        "grad": "Brus",
        "opstina": "Radunje",
        "lokacija": "Radunje"
    },
    {
        "grad": "Brus",
        "opstina": "Razbojna",
        "lokacija": "Razbojna"
    },
    {
        "grad": "Brus",
        "opstina": "Ribari",
        "lokacija": "Ribari"
    },
    {
        "grad": "Brus",
        "opstina": "Stanuloviće",
        "lokacija": "Stanulovići"
    },
    {
        "grad": "Brus",
        "opstina": "Strojinci",
        "lokacija": "Strojinci"
    },
    {
        "grad": "Brus",
        "opstina": "Sudimlja",
        "lokacija": "Sudimlja"
    },
    {
        "grad": "Brus",
        "opstina": "Tršanovci",
        "lokacija": "Tršanovci"
    },
    {
        "grad": "Brus",
        "opstina": "Čokotar",
        "lokacija": "Čokotar"
    },
    {
        "grad": "Brus",
        "opstina": "Šošiće",
        "lokacija": "Šošiće"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Bujanovac",
        "lokacija": "Bujanovac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Baraljevac",
        "lokacija": "Baraljevac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Biljača",
        "lokacija": "Biljača"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Bogdanovac",
        "lokacija": "Bogdanovac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Božinjevac",
        "lokacija": "Božinjevac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Borovac",
        "lokacija": "Borovac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Bratoselce",
        "lokacija": "Bratoselce"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Breznica",
        "lokacija": "Breznica"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Brnjare",
        "lokacija": "Brnjare"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Buštranje",
        "lokacija": "Buštranje"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Veliki Trnovac",
        "lokacija": "Veliki Trnovac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Vogance",
        "lokacija": "Vogance"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Vrban",
        "lokacija": "Vrban"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Gornje Novo Selo",
        "lokacija": "Gornje Novo Selo"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Gramada",
        "lokacija": "Gramada"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Dobrosin",
        "lokacija": "Dobrosin"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Donje Novo Selo",
        "lokacija": "Donje Novo Selo"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Drežnica",
        "lokacija": "Drežnica"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Đorđevac",
        "lokacija": "Đorđevac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Žbevac",
        "lokacija": "Žbevac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Žuželjica",
        "lokacija": "Žuželjica"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Zarbince",
        "lokacija": "Zarbince"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Jablanica",
        "lokacija": "Jablanica"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Jastrebac",
        "lokacija": "Jastrebac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Karadnik",
        "lokacija": "Karadnik"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Klenike",
        "lokacija": "Klenike"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Klinovac",
        "lokacija": "Klinovac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Končulj",
        "lokacija": "Končulj"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Košarno",
        "lokacija": "Košarno"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Krševica",
        "lokacija": "Krševica"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Kuštica",
        "lokacija": "Kuštica"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Levosoje",
        "lokacija": "Levosoje"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Letovica",
        "lokacija": "Letovica"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Lopardince",
        "lokacija": "Lopardince"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Lukarce",
        "lokacija": "Lukarce"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Lučane",
        "lokacija": "Lučane"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Ljiljance",
        "lokacija": "Ljiljance"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Mali Trnovac",
        "lokacija": "Mali Trnovac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Muhovac",
        "lokacija": "Muhovac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Negovac",
        "lokacija": "Negovac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Nesalce",
        "lokacija": "Nesalce"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Oslare",
        "lokacija": "Oslare"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Pretina",
        "lokacija": "Pretina"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Pribovce",
        "lokacija": "Pribovce"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Ravno Bučje",
        "lokacija": "Ravno Bučje"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Rakovac",
        "lokacija": "Rakovac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Rusce",
        "lokacija": "Rusce"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Samoljica",
        "lokacija": "Samoljica"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Sveta Petka",
        "lokacija": "Sveta Petka"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Sebrat",
        "lokacija": "Sebrat"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Sejace",
        "lokacija": "Sejace"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Spančevac",
        "lokacija": "Spančevac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Srpska Kuća",
        "lokacija": "Srpska Kuća"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Starac",
        "lokacija": "Starac"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Suharno",
        "lokacija": "Suharno"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Trejak",
        "lokacija": "Trejak"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Turija",
        "lokacija": "Turija"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Uzovo",
        "lokacija": "Uzovo"
    },
    {
        "grad": "Bujanovac",
        "opstina": "Čar",
        "lokacija": "Čar"
    },
    {
        "grad": "Valjevo",
        "opstina": "Valjevo",
        "lokacija": "Valjevo"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Bair"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Belo Polje"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Boričevac"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Brđani"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Vidrak"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Vujićev Venac"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "gradac"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Železnička Stanica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Zlokućani"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Ilidža"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Jadar"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Kasarna"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Kolubara"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Kolubara 1"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Kosančićev Venac"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Krušik"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Nada Purić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje 27. Novembar"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Milivoja Bjelice"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Milorad Pavlović"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Oslobodioca Valjeva"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Sreten Dudić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Zbratimljenih gradova"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Naselje"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Pećina"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Peti Puk"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Popare"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Radino Brdo"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Senjak"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Sinđelićev Blok"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Tešnjar"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Valjevo",
        "opstina": "Babina Luka",
        "lokacija": "Babina Luka"
    },
    {
        "grad": "Valjevo",
        "opstina": "Balinović",
        "lokacija": "Balinović"
    },
    {
        "grad": "Valjevo",
        "opstina": "Bačevci",
        "lokacija": "Bačevci"
    },
    {
        "grad": "Valjevo",
        "opstina": "Belić",
        "lokacija": "Belić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Beloševac",
        "lokacija": "Beloševac"
    },
    {
        "grad": "Valjevo",
        "opstina": "Beomužević",
        "lokacija": "Beomužević"
    },
    {
        "grad": "Valjevo",
        "opstina": "Blizonje",
        "lokacija": "Blizonje"
    },
    {
        "grad": "Valjevo",
        "opstina": "Bobova",
        "lokacija": "Bobova"
    },
    {
        "grad": "Valjevo",
        "opstina": "Bogatić",
        "lokacija": "Bogatić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Brangović",
        "lokacija": "Brangović"
    },
    {
        "grad": "Valjevo",
        "opstina": "Brankovina",
        "lokacija": "Brankovina"
    },
    {
        "grad": "Valjevo",
        "opstina": "Brezovice",
        "lokacija": "Brezovice"
    },
    {
        "grad": "Valjevo",
        "opstina": "Bujačić",
        "lokacija": "Bujačić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Veselinovac",
        "lokacija": "Veselinovac"
    },
    {
        "grad": "Valjevo",
        "opstina": "Vlaščić",
        "lokacija": "Vlaščić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Vragočanica",
        "lokacija": "Vragočanica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Vujinovača",
        "lokacija": "Vujinovača"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gola Glava",
        "lokacija": "Gola Glava"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gorić",
        "lokacija": "Gorić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gornja Bukovica",
        "lokacija": "Gornja Bukovica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gornja Grabovica",
        "lokacija": "Gornja Grabovica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Gornje Leskovice",
        "lokacija": "Gornje Leskovice"
    },
    {
        "grad": "Valjevo",
        "opstina": "Degurić",
        "lokacija": "Degurić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Divci",
        "lokacija": "Divci"
    },
    {
        "grad": "Valjevo",
        "opstina": "Divčibare",
        "lokacija": "Divčibare"
    },
    {
        "grad": "Valjevo",
        "opstina": "Donja Bukovica",
        "lokacija": "Donja Bukovica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Donje Leskovice",
        "lokacija": "Donje Leskovice"
    },
    {
        "grad": "Valjevo",
        "opstina": "Dračić",
        "lokacija": "Dračić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Dročine",
        "lokacija": "Dročine"
    },
    {
        "grad": "Valjevo",
        "opstina": "Dupljaj",
        "lokacija": "Dupljaj"
    },
    {
        "grad": "Valjevo",
        "opstina": "Žabari",
        "lokacija": "Žabari"
    },
    {
        "grad": "Valjevo",
        "opstina": "Zabrdica",
        "lokacija": "Zabrdica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Zarube",
        "lokacija": "Zarube"
    },
    {
        "grad": "Valjevo",
        "opstina": "Zlatarić",
        "lokacija": "Zlatarić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Jazovik",
        "lokacija": "Jazovik"
    },
    {
        "grad": "Valjevo",
        "opstina": "Jasenica",
        "lokacija": "Jasenica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Jovanja",
        "lokacija": "Jovanja"
    },
    {
        "grad": "Valjevo",
        "opstina": "Joševa",
        "lokacija": "Joševa"
    },
    {
        "grad": "Valjevo",
        "opstina": "Kamenica",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Klanica",
        "lokacija": "Klanica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Klinci",
        "lokacija": "Klinci"
    },
    {
        "grad": "Valjevo",
        "opstina": "Kovačice",
        "lokacija": "Kovačice"
    },
    {
        "grad": "Valjevo",
        "opstina": "Kozličić",
        "lokacija": "Kozličić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Kotešica",
        "lokacija": "Kotešica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Kunice",
        "lokacija": "Kunice"
    },
    {
        "grad": "Valjevo",
        "opstina": "Lelić",
        "lokacija": "Lelić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Loznica",
        "lokacija": "Loznica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Lukavac",
        "lokacija": "Lukavac"
    },
    {
        "grad": "Valjevo",
        "opstina": "Majinović",
        "lokacija": "Majinović"
    },
    {
        "grad": "Valjevo",
        "opstina": "Mijači",
        "lokacija": "Mijači"
    },
    {
        "grad": "Valjevo",
        "opstina": "Miličinica",
        "lokacija": "Miličinica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Mrčić",
        "lokacija": "Mrčić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Oglađenovac",
        "lokacija": "Oglađenovac"
    },
    {
        "grad": "Valjevo",
        "opstina": "Osladić",
        "lokacija": "Osladić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Paklje",
        "lokacija": "Paklje"
    },
    {
        "grad": "Valjevo",
        "opstina": "Paune",
        "lokacija": "Paune"
    },
    {
        "grad": "Valjevo",
        "opstina": "Petnica",
        "lokacija": "Petnica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Popučke",
        "lokacija": "Popučke"
    },
    {
        "grad": "Valjevo",
        "opstina": "Prijezdić",
        "lokacija": "Prijezdić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Pričević",
        "lokacija": "Pričević"
    },
    {
        "grad": "Valjevo",
        "opstina": "Rabas",
        "lokacija": "Rabas"
    },
    {
        "grad": "Valjevo",
        "opstina": "Ravnje",
        "lokacija": "Ravnje"
    },
    {
        "grad": "Valjevo",
        "opstina": "Rađevo Selo",
        "lokacija": "Rađevo Selo"
    },
    {
        "grad": "Valjevo",
        "opstina": "Rebelj",
        "lokacija": "Rebelj"
    },
    {
        "grad": "Valjevo",
        "opstina": "Rovni",
        "lokacija": "Rovni"
    },
    {
        "grad": "Valjevo",
        "opstina": "Sandalj",
        "lokacija": "Sandalj"
    },
    {
        "grad": "Valjevo",
        "opstina": "Sedlari",
        "lokacija": "Sedlari"
    },
    {
        "grad": "Valjevo",
        "opstina": "Sitarice",
        "lokacija": "Sitarice"
    },
    {
        "grad": "Valjevo",
        "opstina": "Sovač",
        "lokacija": "Sovač"
    },
    {
        "grad": "Valjevo",
        "opstina": "Stanina Reka",
        "lokacija": "Stanina Reka"
    },
    {
        "grad": "Valjevo",
        "opstina": "Stapar",
        "lokacija": "Stapar"
    },
    {
        "grad": "Valjevo",
        "opstina": "Strmna Gora",
        "lokacija": "Strmna Gora"
    },
    {
        "grad": "Valjevo",
        "opstina": "Stubo",
        "lokacija": "Stubo"
    },
    {
        "grad": "Valjevo",
        "opstina": "Suvodanje",
        "lokacija": "Suvodanje"
    },
    {
        "grad": "Valjevo",
        "opstina": "Sušica",
        "lokacija": "Sušica"
    },
    {
        "grad": "Valjevo",
        "opstina": "Taor",
        "lokacija": "Taor"
    },
    {
        "grad": "Valjevo",
        "opstina": "Tubravić",
        "lokacija": "Tubravić"
    },
    {
        "grad": "Valjevo",
        "opstina": "Tupanci",
        "lokacija": "Tupanci"
    },
    {
        "grad": "Varvarin",
        "opstina": "Varvarin",
        "lokacija": "Varvarin"
    },
    {
        "grad": "Varvarin",
        "opstina": "Gradska lokacija",
        "lokacija": "Poljce 1"
    },
    {
        "grad": "Varvarin",
        "opstina": "Gradska lokacija",
        "lokacija": "Poljce 2"
    },
    {
        "grad": "Varvarin",
        "opstina": "Gradska lokacija",
        "lokacija": "Rasadnik"
    },
    {
        "grad": "Varvarin",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Varvarin",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Varvarin",
        "opstina": "Bačina",
        "lokacija": "Bačina"
    },
    {
        "grad": "Varvarin",
        "opstina": "Bošnjane",
        "lokacija": "Bošnjane"
    },
    {
        "grad": "Varvarin",
        "opstina": "Varvarin (selo)",
        "lokacija": "Varvarin (selo)"
    },
    {
        "grad": "Varvarin",
        "opstina": "Gornji Katun",
        "lokacija": "Gornji Katun"
    },
    {
        "grad": "Varvarin",
        "opstina": "Gornji Krčin",
        "lokacija": "Gornji Krčin"
    },
    {
        "grad": "Varvarin",
        "opstina": "Donji Katun",
        "lokacija": "Donji Katun"
    },
    {
        "grad": "Varvarin",
        "opstina": "Donji Krčin",
        "lokacija": "Donji Krčin"
    },
    {
        "grad": "Varvarin",
        "opstina": "Zalogovac",
        "lokacija": "Zalogovac"
    },
    {
        "grad": "Varvarin",
        "opstina": "Izbenica",
        "lokacija": "Izbenica"
    },
    {
        "grad": "Varvarin",
        "opstina": "Karanovac",
        "lokacija": "Karanovac"
    },
    {
        "grad": "Varvarin",
        "opstina": "Mala Kruševica",
        "lokacija": "Mala Kruševica"
    },
    {
        "grad": "Varvarin",
        "opstina": "Marenovo",
        "lokacija": "Marenovo"
    },
    {
        "grad": "Varvarin",
        "opstina": "Maskare",
        "lokacija": "Maskare"
    },
    {
        "grad": "Varvarin",
        "opstina": "Obrež",
        "lokacija": "Obrež"
    },
    {
        "grad": "Varvarin",
        "opstina": "Orašje",
        "lokacija": "Orašje"
    },
    {
        "grad": "Varvarin",
        "opstina": "Pajkovac",
        "lokacija": "Pajkovac"
    },
    {
        "grad": "Varvarin",
        "opstina": "Parcane",
        "lokacija": "Parcane"
    },
    {
        "grad": "Varvarin",
        "opstina": "Suvaja",
        "lokacija": "Suvaja"
    },
    {
        "grad": "Varvarin",
        "opstina": "Toljevac",
        "lokacija": "Toljevac"
    },
    {
        "grad": "Varvarin",
        "opstina": "Cernica",
        "lokacija": "Cernica"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Velika Plana",
        "lokacija": "Velika Plana"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Gradska lokacija",
        "lokacija": "Bugarija"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Gradska lokacija",
        "lokacija": "Đurakovac"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Naselje"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Gradska lokacija",
        "lokacija": "Stari Odbor"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Bresje",
        "lokacija": "Bresje"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Veliko Orašje",
        "lokacija": "Veliko Orašje"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Donja Livadica",
        "lokacija": "Donja Livadica"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Krnjevo",
        "lokacija": "Krnjevo"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Kupusina",
        "lokacija": "Kupusina"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Lozovik",
        "lokacija": "Lozovik"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Markovac",
        "lokacija": "Markovac"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Miloševac",
        "lokacija": "Miloševac"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Radovanje",
        "lokacija": "Radovanje"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Rakinac",
        "lokacija": "Rakinac"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Staro Selo",
        "lokacija": "Staro Selo"
    },
    {
        "grad": "Velika Plana",
        "opstina": "Trnovče",
        "lokacija": "Trnovče"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Veliko gradište",
        "lokacija": "Veliko gradište"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Gradska lokacija",
        "lokacija": "Beli Bagrem"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Gradska lokacija",
        "lokacija": "Vinogradi"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Biskuplje",
        "lokacija": "Biskuplje"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Garevo",
        "lokacija": "Garevo"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Desine",
        "lokacija": "Desine"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Doljašnica",
        "lokacija": "Doljašnica"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Đurakovo",
        "lokacija": "Đurakovo"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Zatonje",
        "lokacija": "Zatonje"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Kamijevo",
        "lokacija": "Kamijevo"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Kisiljevo",
        "lokacija": "Kisiljevo"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Kumane",
        "lokacija": "Kumane"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Kurjače",
        "lokacija": "Kurjače"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Kusiće",
        "lokacija": "Kusiće"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Ljubinje",
        "lokacija": "Ljubinje"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Majilovac",
        "lokacija": "Majilovac"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Makce",
        "lokacija": "Makce"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Ostrovo",
        "lokacija": "Ostrovo"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Pečanica",
        "lokacija": "Pečanica"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Požeženo",
        "lokacija": "Požeženo"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Popovac",
        "lokacija": "Popovac"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Ram",
        "lokacija": "Ram"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Sirakovo",
        "lokacija": "Sirakovo"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Srebrno Jezero",
        "lokacija": "Srebrno Jezero"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Srednjevo",
        "lokacija": "Srednjevo"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Topolovnik",
        "lokacija": "Topolovnik"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Tribrode",
        "lokacija": "Tribrode"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Carevac",
        "lokacija": "Carevac"
    },
    {
        "grad": "Veliko gradište",
        "opstina": "Češljeva bara",
        "lokacija": "Češljeva bara"
    },
    {
        "grad": "Vitina",
        "opstina": "Vitina",
        "lokacija": "Vitina"
    },
    {
        "grad": "Vitina",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Vitina",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Vitina",
        "opstina": "Balance",
        "lokacija": "Balance"
    },
    {
        "grad": "Vitina",
        "opstina": "Begunce",
        "lokacija": "Begunce"
    },
    {
        "grad": "Vitina",
        "opstina": "Binač",
        "lokacija": "Binač"
    },
    {
        "grad": "Vitina",
        "opstina": "Buzovik",
        "lokacija": "Buzovik"
    },
    {
        "grad": "Vitina",
        "opstina": "Veliki Goden",
        "lokacija": "Veliki Goden"
    },
    {
        "grad": "Vitina",
        "opstina": "Vrban",
        "lokacija": "Vrban"
    },
    {
        "grad": "Vitina",
        "opstina": "Vrbovac",
        "lokacija": "Vrbovac"
    },
    {
        "grad": "Vitina",
        "opstina": "Vrnavokolo",
        "lokacija": "Vrnavokolo"
    },
    {
        "grad": "Vitina",
        "opstina": "Vrnez",
        "lokacija": "Vrnez"
    },
    {
        "grad": "Vitina",
        "opstina": "Gornja Budrika",
        "lokacija": "Gornja Budrika"
    },
    {
        "grad": "Vitina",
        "opstina": "Gornja Slatina",
        "lokacija": "Gornja Slatina"
    },
    {
        "grad": "Vitina",
        "opstina": "Gornja Stubla",
        "lokacija": "Gornja Stubla"
    },
    {
        "grad": "Vitina",
        "opstina": "Grmovo",
        "lokacija": "Grmovo"
    },
    {
        "grad": "Vitina",
        "opstina": "Grnčar",
        "lokacija": "Grnčar"
    },
    {
        "grad": "Vitina",
        "opstina": "Gušica",
        "lokacija": "Gušica"
    },
    {
        "grad": "Vitina",
        "opstina": "Debelde",
        "lokacija": "Debelde"
    },
    {
        "grad": "Vitina",
        "opstina": "Devaja",
        "lokacija": "Devaja"
    },
    {
        "grad": "Vitina",
        "opstina": "Donja Slatina",
        "lokacija": "Donja Slatina"
    },
    {
        "grad": "Vitina",
        "opstina": "Donja Stubla",
        "lokacija": "Donja Stubla"
    },
    {
        "grad": "Vitina",
        "opstina": "Donje Ramnjane",
        "lokacija": "Donje Ramnjane"
    },
    {
        "grad": "Vitina",
        "opstina": "Drobeš",
        "lokacija": "Drobeš"
    },
    {
        "grad": "Vitina",
        "opstina": "Đelekare",
        "lokacija": "Đelekare"
    },
    {
        "grad": "Vitina",
        "opstina": "Žitinje",
        "lokacija": "Žitinje"
    },
    {
        "grad": "Vitina",
        "opstina": "Jerli Sadovina",
        "lokacija": "Jerli Sadovina"
    },
    {
        "grad": "Vitina",
        "opstina": "Kabaš",
        "lokacija": "Kabaš"
    },
    {
        "grad": "Vitina",
        "opstina": "Klokot",
        "lokacija": "Klokot"
    },
    {
        "grad": "Vitina",
        "opstina": "Letnica",
        "lokacija": "Letnica"
    },
    {
        "grad": "Vitina",
        "opstina": "Ljubište",
        "lokacija": "Ljubište"
    },
    {
        "grad": "Vitina",
        "opstina": "Mijak",
        "lokacija": "Mijak"
    },
    {
        "grad": "Vitina",
        "opstina": "Mogila",
        "lokacija": "Mogila"
    },
    {
        "grad": "Vitina",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Vitina",
        "opstina": "Podgorce",
        "lokacija": "Podgorce"
    },
    {
        "grad": "Vitina",
        "opstina": "Požaranje",
        "lokacija": "Požaranje"
    },
    {
        "grad": "Vitina",
        "opstina": "Ravnište",
        "lokacija": "Ravnište"
    },
    {
        "grad": "Vitina",
        "opstina": "Radivojce",
        "lokacija": "Radivojce"
    },
    {
        "grad": "Vitina",
        "opstina": "Ribnik",
        "lokacija": "Ribnik"
    },
    {
        "grad": "Vitina",
        "opstina": "Smira",
        "lokacija": "Smira"
    },
    {
        "grad": "Vitina",
        "opstina": "Trpeza",
        "lokacija": "Trpeza"
    },
    {
        "grad": "Vitina",
        "opstina": "Trstenik",
        "lokacija": "Trstenik"
    },
    {
        "grad": "Vitina",
        "opstina": "Čerkez Sadovina",
        "lokacija": "Čerkez Sadovina"
    },
    {
        "grad": "Vitina",
        "opstina": "Čiflak",
        "lokacija": "Čiflak"
    },
    {
        "grad": "Vitina",
        "opstina": "Šašare",
        "lokacija": "Šašare"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Vladimirci",
        "lokacija": "Vladimirci"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Belotić",
        "lokacija": "Belotić"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Beljin",
        "lokacija": "Beljin"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Bobovik",
        "lokacija": "Bobovik"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Vlasenica",
        "lokacija": "Vlasenica"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Vukošić",
        "lokacija": "Vukošić"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Vučevica",
        "lokacija": "Vučevica"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Debrc",
        "lokacija": "Debrc"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Dragojevac",
        "lokacija": "Dragojevac"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Zvezd",
        "lokacija": "Zvezd"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Jazovnik",
        "lokacija": "Jazovnik"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Jalovik",
        "lokacija": "Jalovik"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Kaona",
        "lokacija": "Kaona"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Kozarica",
        "lokacija": "Kozarica"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Krnić",
        "lokacija": "Krnić"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Krnule",
        "lokacija": "Krnule"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Kujavica",
        "lokacija": "Kujavica"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Lojanice",
        "lokacija": "Lojanice"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Matijevac",
        "lokacija": "Matijevac"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Mesarci",
        "lokacija": "Mesarci"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Mehovine",
        "lokacija": "Mehovine"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Mrovska",
        "lokacija": "Mrovska"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Pejinović",
        "lokacija": "Pejinović"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Provo",
        "lokacija": "Provo"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Riđake",
        "lokacija": "Riđake"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Skupljen",
        "lokacija": "Skupljen"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Suvo Selo",
        "lokacija": "Suvo Selo"
    },
    {
        "grad": "Vladimirci",
        "opstina": "Trbušac",
        "lokacija": "Trbušac"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Vladičin Han",
        "lokacija": "Vladičin Han"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Gradska lokacija",
        "lokacija": "Kula"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Gradska lokacija",
        "lokacija": "Poljana"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Balinovce",
        "lokacija": "Balinovce"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Bačvište",
        "lokacija": "Bačvište"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Belanovce",
        "lokacija": "Belanovce"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Beliševo",
        "lokacija": "Beliševo"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Bogoševo",
        "lokacija": "Bogoševo"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Brestovo",
        "lokacija": "Brestovo"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Vrbovo",
        "lokacija": "Vrbovo"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Garinje",
        "lokacija": "Garinje"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Gornje Jabukovo",
        "lokacija": "Gornje Jabukovo"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Gramađe",
        "lokacija": "Gramađe"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Dekutince",
        "lokacija": "Dekutince"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Donje Jabukovo",
        "lokacija": "Donje Jabukovo"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Dupljane",
        "lokacija": "Dupljane"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Žitorađe",
        "lokacija": "Žitorađe"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Zebince",
        "lokacija": "Zebince"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Jagnjilo",
        "lokacija": "Jagnjilo"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Jastrebac",
        "lokacija": "Jastrebac"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Jovac",
        "lokacija": "Jovac"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Kalimance",
        "lokacija": "Kalimance"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Kacapun",
        "lokacija": "Kacapun"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Koznica",
        "lokacija": "Koznica"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Kopitarce",
        "lokacija": "Kopitarce"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Kostomlatica",
        "lokacija": "Kostomlatica"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Kržince",
        "lokacija": "Kržince"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Kukavica",
        "lokacija": "Kukavica"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Kunovo",
        "lokacija": "Kunovo"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Lebet",
        "lokacija": "Lebet"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Lepenica",
        "lokacija": "Lepenica"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Letovište",
        "lokacija": "Letovište"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Ljutež",
        "lokacija": "Ljutež"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Mazarać",
        "lokacija": "Mazarać"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Manajle",
        "lokacija": "Manajle"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Manjak",
        "lokacija": "Manjak"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Mrtvica",
        "lokacija": "Mrtvica"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Ostrovica",
        "lokacija": "Ostrovica"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Polom",
        "lokacija": "Polom"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Prekodolce",
        "lokacija": "Prekodolce"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Priboj",
        "lokacija": "Priboj"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Ravna Reka",
        "lokacija": "Ravna Reka"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Rdovo",
        "lokacija": "Rdovo"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Repince",
        "lokacija": "Repince"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Repište",
        "lokacija": "Repište"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Ružić",
        "lokacija": "Ružić"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Solačka Sena",
        "lokacija": "Solačka Sena"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Srneći Dol",
        "lokacija": "Srneći Dol"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Stubal",
        "lokacija": "Stubal"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Suva Morava",
        "lokacija": "Suva Morava"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Tegovište",
        "lokacija": "Tegovište"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Urvič",
        "lokacija": "Urvič"
    },
    {
        "grad": "Vladičin Han",
        "opstina": "Džep",
        "lokacija": "Džep"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Vlasotince",
        "lokacija": "Vlasotince"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gradska lokacija",
        "lokacija": "Gornja Mala"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gradska lokacija",
        "lokacija": "Donja Mala"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gradska lokacija",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gradska lokacija",
        "lokacija": "Manastiršte"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Aleksine",
        "lokacija": "Aleksine"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Batulovce",
        "lokacija": "Batulovce"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Boljare",
        "lokacija": "Boljare"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Borin Do",
        "lokacija": "Borin Do"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Brezovica",
        "lokacija": "Brezovica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gložane",
        "lokacija": "Gložane"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gornja Lomnica",
        "lokacija": "Gornja Lomnica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gornja Lopušnja",
        "lokacija": "Gornja Lopušnja"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gornji Dejan",
        "lokacija": "Gornji Dejan"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gornji Orah",
        "lokacija": "Gornji Orah"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gornji Prisjan",
        "lokacija": "Gornji Prisjan"
    },
    {
        "grad": "Vlasotince",
        "opstina": "gradište",
        "lokacija": "gradište"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Gunjetina",
        "lokacija": "Gunjetina"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Dadince",
        "lokacija": "Dadince"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Dobroviš",
        "lokacija": "Dobroviš"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Donja Lomnica",
        "lokacija": "Donja Lomnica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Donja Lopušnja",
        "lokacija": "Donja Lopušnja"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Donje Gare",
        "lokacija": "Donje Gare"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Donji Dejan",
        "lokacija": "Donji Dejan"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Donji Prisjan",
        "lokacija": "Donji Prisjan"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Zlatićevo",
        "lokacija": "Zlatićevo"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Javorje",
        "lokacija": "Javorje"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Jakovljevo",
        "lokacija": "Jakovljevo"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Jastrebac",
        "lokacija": "Jastrebac"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Kozilo",
        "lokacija": "Kozilo"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Komarica",
        "lokacija": "Komarica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Konopnica",
        "lokacija": "Konopnica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Kruševica",
        "lokacija": "Kruševica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Kukavica",
        "lokacija": "Kukavica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Ladovica",
        "lokacija": "Ladovica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Lipovica",
        "lokacija": "Lipovica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Orašje",
        "lokacija": "Orašje"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Ostrc",
        "lokacija": "Ostrc"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Pržojne",
        "lokacija": "Pržojne"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Prilepac",
        "lokacija": "Prilepac"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Ravna Gora",
        "lokacija": "Ravna Gora"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Ravni Del",
        "lokacija": "Ravni Del"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Samarnica",
        "lokacija": "Samarnica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Svođe",
        "lokacija": "Svođe"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Skrapež",
        "lokacija": "Skrapež"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Sredor",
        "lokacija": "Sredor"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Stajkovce",
        "lokacija": "Stajkovce"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Stranjevo",
        "lokacija": "Stranjevo"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Tegošnica",
        "lokacija": "Tegošnica"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Crna Bara",
        "lokacija": "Crna Bara"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Crnatovo",
        "lokacija": "Crnatovo"
    },
    {
        "grad": "Vlasotince",
        "opstina": "Šišave",
        "lokacija": "Šišave"
    },
    {
        "grad": "Vranje",
        "opstina": "Vranje",
        "lokacija": "Vranje"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Autobuska Stanica"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Beli Most"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Bunuševac"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Viktor Bubanj"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Gornja Čaršija"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Gornji Asambair"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Donje Vranje"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Donji Asambair"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Ledena Stena"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Ogledna Stanica"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Odžinka"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Palestina"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Panađurište"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Raška"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Rudina"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Sobina"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Tulbe"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Ćoška"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Šapranački Rid"
    },
    {
        "grad": "Vranje",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Vranje",
        "opstina": "Aleksandrovac",
        "lokacija": "Aleksandrovac"
    },
    {
        "grad": "Vranje",
        "opstina": "Babina Poljana",
        "lokacija": "Babina Poljana"
    },
    {
        "grad": "Vranje",
        "opstina": "Barbarušnice",
        "lokacija": "Barbarušnice"
    },
    {
        "grad": "Vranje",
        "opstina": "Barelić",
        "lokacija": "Barelić"
    },
    {
        "grad": "Vranje",
        "opstina": "Beli Breg",
        "lokacija": "Beli Breg"
    },
    {
        "grad": "Vranje",
        "opstina": "Bojin Del",
        "lokacija": "Bojin Del"
    },
    {
        "grad": "Vranje",
        "opstina": "Bresnica",
        "lokacija": "Bresnica"
    },
    {
        "grad": "Vranje",
        "opstina": "Bujkovac",
        "lokacija": "Bujkovac"
    },
    {
        "grad": "Vranje",
        "opstina": "Buljesovce",
        "lokacija": "Buljesovce"
    },
    {
        "grad": "Vranje",
        "opstina": "Buštranje",
        "lokacija": "Buštranje"
    },
    {
        "grad": "Vranje",
        "opstina": "Viševce",
        "lokacija": "Viševce"
    },
    {
        "grad": "Vranje",
        "opstina": "Vlase",
        "lokacija": "Vlase"
    },
    {
        "grad": "Vranje",
        "opstina": "Vranjska Banja",
        "lokacija": "Vranjska Banja"
    },
    {
        "grad": "Vranje",
        "opstina": "Vrtogoš",
        "lokacija": "Vrtogoš"
    },
    {
        "grad": "Vranje",
        "opstina": "Golemo Selo",
        "lokacija": "Golemo Selo"
    },
    {
        "grad": "Vranje",
        "opstina": "Gornja Otulja",
        "lokacija": "Gornja Otulja"
    },
    {
        "grad": "Vranje",
        "opstina": "Gornje Žapsko",
        "lokacija": "Gornje Žapsko"
    },
    {
        "grad": "Vranje",
        "opstina": "Gornje Punoševce",
        "lokacija": "Gornje Punoševce"
    },
    {
        "grad": "Vranje",
        "opstina": "Gornje Trebešinje",
        "lokacija": "Gornje Trebešinje"
    },
    {
        "grad": "Vranje",
        "opstina": "Gornji Neradovac",
        "lokacija": "Gornji Neradovac"
    },
    {
        "grad": "Vranje",
        "opstina": "gradnja",
        "lokacija": "gradnja"
    },
    {
        "grad": "Vranje",
        "opstina": "Gumerište",
        "lokacija": "Gumerište"
    },
    {
        "grad": "Vranje",
        "opstina": "Davidovac",
        "lokacija": "Davidovac"
    },
    {
        "grad": "Vranje",
        "opstina": "Dobrejance",
        "lokacija": "Dobrejance"
    },
    {
        "grad": "Vranje",
        "opstina": "Donja Otulja",
        "lokacija": "Donja Otulja"
    },
    {
        "grad": "Vranje",
        "opstina": "Donje Žapsko",
        "lokacija": "Donje Žapsko"
    },
    {
        "grad": "Vranje",
        "opstina": "Donje Punoševce",
        "lokacija": "Donje Punoševce"
    },
    {
        "grad": "Vranje",
        "opstina": "Donje Trebešinje",
        "lokacija": "Donje Trebešinje"
    },
    {
        "grad": "Vranje",
        "opstina": "Donji Neradovac",
        "lokacija": "Donji Neradovac"
    },
    {
        "grad": "Vranje",
        "opstina": "Dragobužde",
        "lokacija": "Dragobužde"
    },
    {
        "grad": "Vranje",
        "opstina": "Drenovac",
        "lokacija": "Drenovac"
    },
    {
        "grad": "Vranje",
        "opstina": "Dubnica",
        "lokacija": "Dubnica"
    },
    {
        "grad": "Vranje",
        "opstina": "Duga Luka",
        "lokacija": "Duga Luka"
    },
    {
        "grad": "Vranje",
        "opstina": "Dupan",
        "lokacija": "Dulan"
    },
    {
        "grad": "Vranje",
        "opstina": "Dupeljevo",
        "lokacija": "Dupeljevo"
    },
    {
        "grad": "Vranje",
        "opstina": "Zlatokop",
        "lokacija": "Zlatokop"
    },
    {
        "grad": "Vranje",
        "opstina": "Izumno",
        "lokacija": "Izumno"
    },
    {
        "grad": "Vranje",
        "opstina": "Katun",
        "lokacija": "Katun"
    },
    {
        "grad": "Vranje",
        "opstina": "Klašnice",
        "lokacija": "Klašnice"
    },
    {
        "grad": "Vranje",
        "opstina": "Klisurica",
        "lokacija": "Klisurica"
    },
    {
        "grad": "Vranje",
        "opstina": "Kopanjane",
        "lokacija": "Kopanjane"
    },
    {
        "grad": "Vranje",
        "opstina": "Korbevac",
        "lokacija": "Korbevac"
    },
    {
        "grad": "Vranje",
        "opstina": "Korbul",
        "lokacija": "Korbul"
    },
    {
        "grad": "Vranje",
        "opstina": "Koćura",
        "lokacija": "Koćura"
    },
    {
        "grad": "Vranje",
        "opstina": "Kriva Feja",
        "lokacija": "Kriva Feja"
    },
    {
        "grad": "Vranje",
        "opstina": "Kruševa Glava",
        "lokacija": "Kruševa Glava"
    },
    {
        "grad": "Vranje",
        "opstina": "Kumarevo",
        "lokacija": "Kumarevo"
    },
    {
        "grad": "Vranje",
        "opstina": "Kupinince",
        "lokacija": "Kupinince"
    },
    {
        "grad": "Vranje",
        "opstina": "Lalince",
        "lokacija": "Lalince"
    },
    {
        "grad": "Vranje",
        "opstina": "Leva Reka",
        "lokacija": "Leva Reka"
    },
    {
        "grad": "Vranje",
        "opstina": "Lepčince",
        "lokacija": "Lepčince"
    },
    {
        "grad": "Vranje",
        "opstina": "Lipovac",
        "lokacija": "Lipovac"
    },
    {
        "grad": "Vranje",
        "opstina": "Lukovo",
        "lokacija": "Lukovo"
    },
    {
        "grad": "Vranje",
        "opstina": "Margance",
        "lokacija": "Margance"
    },
    {
        "grad": "Vranje",
        "opstina": "Mečkovac",
        "lokacija": "Mečkovac"
    },
    {
        "grad": "Vranje",
        "opstina": "Mijakovce",
        "lokacija": "Mijakovce"
    },
    {
        "grad": "Vranje",
        "opstina": "Mijovce",
        "lokacija": "Mijovce"
    },
    {
        "grad": "Vranje",
        "opstina": "Milanovo",
        "lokacija": "Milanovo"
    },
    {
        "grad": "Vranje",
        "opstina": "Milivojce",
        "lokacija": "Milivojce"
    },
    {
        "grad": "Vranje",
        "opstina": "Moštanica",
        "lokacija": "Moštanica"
    },
    {
        "grad": "Vranje",
        "opstina": "Nastavce",
        "lokacija": "Nastavce"
    },
    {
        "grad": "Vranje",
        "opstina": "Nesvrta",
        "lokacija": "Nesvrta"
    },
    {
        "grad": "Vranje",
        "opstina": "Nova Brezovica",
        "lokacija": "Nova Brezovica"
    },
    {
        "grad": "Vranje",
        "opstina": "Oblička Sena",
        "lokacija": "Oblička Sena"
    },
    {
        "grad": "Vranje",
        "opstina": "Ostra Glava",
        "lokacija": "Ostra Glava"
    },
    {
        "grad": "Vranje",
        "opstina": "Pavlovac",
        "lokacija": "Pavlovac"
    },
    {
        "grad": "Vranje",
        "opstina": "Panevlje",
        "lokacija": "Panevlje"
    },
    {
        "grad": "Vranje",
        "opstina": "Pljačkovica",
        "lokacija": "Pljačkovica"
    },
    {
        "grad": "Vranje",
        "opstina": "Prvonek",
        "lokacija": "Prvonek"
    },
    {
        "grad": "Vranje",
        "opstina": "Prevalac",
        "lokacija": "Prevalac"
    },
    {
        "grad": "Vranje",
        "opstina": "Preobraženje",
        "lokacija": "Preobraženje"
    },
    {
        "grad": "Vranje",
        "opstina": "Ranutovac",
        "lokacija": "Ranutovac"
    },
    {
        "grad": "Vranje",
        "opstina": "Rataje",
        "lokacija": "Rataje"
    },
    {
        "grad": "Vranje",
        "opstina": "Ribince",
        "lokacija": "Ribince"
    },
    {
        "grad": "Vranje",
        "opstina": "Ristovac",
        "lokacija": "Ristovac"
    },
    {
        "grad": "Vranje",
        "opstina": "Roždace",
        "lokacija": "Roždace"
    },
    {
        "grad": "Vranje",
        "opstina": "Rusce",
        "lokacija": "Rusce"
    },
    {
        "grad": "Vranje",
        "opstina": "Sebevranje",
        "lokacija": "Sebevranje"
    },
    {
        "grad": "Vranje",
        "opstina": "Sikirje",
        "lokacija": "Sikirje"
    },
    {
        "grad": "Vranje",
        "opstina": "Slivnica",
        "lokacija": "Slivnica"
    },
    {
        "grad": "Vranje",
        "opstina": "Smiljević",
        "lokacija": "Smiljević"
    },
    {
        "grad": "Vranje",
        "opstina": "Soderce",
        "lokacija": "Soderce"
    },
    {
        "grad": "Vranje",
        "opstina": "Srednji Del",
        "lokacija": "Srednji Del"
    },
    {
        "grad": "Vranje",
        "opstina": "Stance",
        "lokacija": "Stance"
    },
    {
        "grad": "Vranje",
        "opstina": "Stara Brezovica",
        "lokacija": "Stara Brezovica"
    },
    {
        "grad": "Vranje",
        "opstina": "Stari Glog",
        "lokacija": "Stari Glog"
    },
    {
        "grad": "Vranje",
        "opstina": "Strešak",
        "lokacija": "Strešak"
    },
    {
        "grad": "Vranje",
        "opstina": "Stropsko",
        "lokacija": "Stropsko"
    },
    {
        "grad": "Vranje",
        "opstina": "Struganica",
        "lokacija": "Struganica"
    },
    {
        "grad": "Vranje",
        "opstina": "Studena",
        "lokacija": "Studena"
    },
    {
        "grad": "Vranje",
        "opstina": "Suvi Dol",
        "lokacija": "Suvi Dol"
    },
    {
        "grad": "Vranje",
        "opstina": "Surdul",
        "lokacija": "Surdul"
    },
    {
        "grad": "Vranje",
        "opstina": "Tesovište",
        "lokacija": "Tesovište"
    },
    {
        "grad": "Vranje",
        "opstina": "Tibužde",
        "lokacija": "Tibužde"
    },
    {
        "grad": "Vranje",
        "opstina": "Toplac",
        "lokacija": "Toplac"
    },
    {
        "grad": "Vranje",
        "opstina": "Trstena",
        "lokacija": "Trstena"
    },
    {
        "grad": "Vranje",
        "opstina": "Tumba",
        "lokacija": "Tumba"
    },
    {
        "grad": "Vranje",
        "opstina": "Ćukovac",
        "lokacija": "Ćukovac"
    },
    {
        "grad": "Vranje",
        "opstina": "Ćurkovica",
        "lokacija": "Ćurkovica"
    },
    {
        "grad": "Vranje",
        "opstina": "Urmanica",
        "lokacija": "Urmanica"
    },
    {
        "grad": "Vranje",
        "opstina": "Uševce",
        "lokacija": "Uševce"
    },
    {
        "grad": "Vranje",
        "opstina": "Crni Vrh",
        "lokacija": "Crni Vrh"
    },
    {
        "grad": "Vranje",
        "opstina": "Crni Lug",
        "lokacija": "Crni Lug"
    },
    {
        "grad": "Vranje",
        "opstina": "Čestelin",
        "lokacija": "Čestelin"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Vrnjačka Banja",
        "lokacija": "Vrnjačka Banja"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gradska lokacija",
        "lokacija": "Borjak"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gradska lokacija",
        "lokacija": "Dubrava"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gradska lokacija",
        "lokacija": "Jezero"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gradska lokacija",
        "lokacija": "Piskavac"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gradska lokacija",
        "lokacija": "Raj"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gradska lokacija",
        "lokacija": "Slatina"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gradska lokacija",
        "lokacija": "Snežnik"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gradska lokacija",
        "lokacija": "Sunčani Breg"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gradska lokacija",
        "lokacija": "Čajkino Brdo"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Vraneši",
        "lokacija": "Vraneši"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Vrnjci",
        "lokacija": "Vrnjci"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Vukušica",
        "lokacija": "Vukušica"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Goč",
        "lokacija": "Goč"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Gračac",
        "lokacija": "Gračac"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Lipova",
        "lokacija": "Lipova"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Otroci",
        "lokacija": "Otroci"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Podunavci",
        "lokacija": "Podunavci"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Rsavci",
        "lokacija": "Rsavci"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Ruđinci",
        "lokacija": "Ruđinci"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Stanišinci",
        "lokacija": "Stanišinci"
    },
    {
        "grad": "Vrnjačka Banja",
        "opstina": "Štulac",
        "lokacija": "Štulac"
    },
    {
        "grad": "Vršac",
        "opstina": "Vršac",
        "lokacija": "Vršac"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Balata"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Vinogradski Kraj"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Vojnički Trg"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Guduričko Naselje"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Irig Mala"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Istočni Vršac"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kalvarija"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kozluk"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kormanter"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kuštiljsko Naselje"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Mali Rit"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Margitsko Naselje"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Gudurički Put"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Breg"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Paorski Kraj"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Radakova Mala"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Staklenik Mala"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Helvecija"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Hemograd"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Crkvenjačka Mala"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Čukur Mala"
    },
    {
        "grad": "Vršac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Vršac",
        "opstina": "Vatin",
        "lokacija": "Vatin"
    },
    {
        "grad": "Vršac",
        "opstina": "Veliko Središte",
        "lokacija": "Veliko Središte"
    },
    {
        "grad": "Vršac",
        "opstina": "Vlajkovac",
        "lokacija": "Vlajkovac"
    },
    {
        "grad": "Vršac",
        "opstina": "Vojvodinci",
        "lokacija": "Vojvodinci"
    },
    {
        "grad": "Vršac",
        "opstina": "Vršački Ritovi",
        "lokacija": "Vršački Ritovi"
    },
    {
        "grad": "Vršac",
        "opstina": "Gudurica",
        "lokacija": "Gudurica"
    },
    {
        "grad": "Vršac",
        "opstina": "Zagajica",
        "lokacija": "Zagajica"
    },
    {
        "grad": "Vršac",
        "opstina": "Izbište",
        "lokacija": "Izbište"
    },
    {
        "grad": "Vršac",
        "opstina": "Jablanka",
        "lokacija": "Jablanka"
    },
    {
        "grad": "Vršac",
        "opstina": "Kuštilj",
        "lokacija": "Kuštilj"
    },
    {
        "grad": "Vršac",
        "opstina": "Mali Žam",
        "lokacija": "Mali Žam"
    },
    {
        "grad": "Vršac",
        "opstina": "Malo Središte",
        "lokacija": "Malo Središte"
    },
    {
        "grad": "Vršac",
        "opstina": "Markovac",
        "lokacija": "Markovac"
    },
    {
        "grad": "Vršac",
        "opstina": "Mesić",
        "lokacija": "Mesić"
    },
    {
        "grad": "Vršac",
        "opstina": "Orešac",
        "lokacija": "Orešac"
    },
    {
        "grad": "Vršac",
        "opstina": "Pavliš",
        "lokacija": "Pavliš"
    },
    {
        "grad": "Vršac",
        "opstina": "Parta",
        "lokacija": "Parta"
    },
    {
        "grad": "Vršac",
        "opstina": "Potporanj",
        "lokacija": "Potporanj"
    },
    {
        "grad": "Vršac",
        "opstina": "Ritiševo",
        "lokacija": "Ritiševo"
    },
    {
        "grad": "Vršac",
        "opstina": "Sočica",
        "lokacija": "Sočica"
    },
    {
        "grad": "Vršac",
        "opstina": "Straža",
        "lokacija": "Straža"
    },
    {
        "grad": "Vršac",
        "opstina": "Uljma",
        "lokacija": "Uljma"
    },
    {
        "grad": "Vršac",
        "opstina": "Šušara",
        "lokacija": "Šušara"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Vučitrn",
        "lokacija": "Vučitrn"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Balince",
        "lokacija": "Balince"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Banjska",
        "lokacija": "Banjska"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Benčuk",
        "lokacija": "Benčuk"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Bečić",
        "lokacija": "Bečić"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Bivoljak",
        "lokacija": "Bivoljak"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Bošljane",
        "lokacija": "Bošljane"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Brusnik",
        "lokacija": "Brusnik"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Bukoš",
        "lokacija": "Bukoš"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Velika Reka",
        "lokacija": "Velika Reka"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Vesekovce",
        "lokacija": "Vesekovce"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Viljance",
        "lokacija": "Viljance"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Vrnica",
        "lokacija": "Vrnica"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Galica",
        "lokacija": "Galica"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Glavotina",
        "lokacija": "Glavotina"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Gojbulja",
        "lokacija": "Gojbulja"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Gornja Dubnica",
        "lokacija": "Gornja Dubnica"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Gornja Sudimlja",
        "lokacija": "Gornja Sudimlja"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Gornje Stanovce",
        "lokacija": "Gornje Stanovce"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Gornji Svračak",
        "lokacija": "Gornji Svračak"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Grace",
        "lokacija": "Grace"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Gumnište",
        "lokacija": "Gumnište"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Dobra Luka",
        "lokacija": "Dobra Luka"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Doljak",
        "lokacija": "Doljak"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Donja Dubnica",
        "lokacija": "Donja Dubnica"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Donja Sudimlja",
        "lokacija": "Donja Sudimlja"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Donje Stanovce",
        "lokacija": "Donje Stanovce"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Donji Svračak",
        "lokacija": "Donji Svračak"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Drvare",
        "lokacija": "Drvare"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Dubovac",
        "lokacija": "Dubovac"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Žilivoda",
        "lokacija": "Žilivoda"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Zagorje",
        "lokacija": "Zagorje"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Jezero",
        "lokacija": "Jezero"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Karače",
        "lokacija": "Karače"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Kolo",
        "lokacija": "Kolo"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Kunovik",
        "lokacija": "Kunovik"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Kurilovo",
        "lokacija": "Kurilovo"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Lug Dunica",
        "lokacija": "Lug Dunica"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Mavrić",
        "lokacija": "Mavrić"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Mijalić",
        "lokacija": "Mijalić"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Miroče",
        "lokacija": "Miroče"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Nevoljane",
        "lokacija": "Nevoljane"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Nedakovac",
        "lokacija": "Nedakovac"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Novo Selo Begovo",
        "lokacija": "Novo Selo Begovo"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Novo Selo Mađunsko",
        "lokacija": "Novo Selo Mađunsko"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Okraštica",
        "lokacija": "Okraštica"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Ošljane",
        "lokacija": "Ošljane"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Pantina",
        "lokacija": "Pantina"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Pasoma",
        "lokacija": "Pasoma"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Pestovo",
        "lokacija": "Pestovo"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Prilužje",
        "lokacija": "Prilužje"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Resnik",
        "lokacija": "Resnik"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Ropica",
        "lokacija": "Ropica"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Samodreža",
        "lokacija": "Samodreža"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Skočna",
        "lokacija": "Skočna"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Skrovna",
        "lokacija": "Skrovna"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Slakovce",
        "lokacija": "Slakovce"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Smrekovnica",
        "lokacija": "Smrekovnica"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Strovce",
        "lokacija": "Strovce"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Taradža",
        "lokacija": "Taradža"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Trlabuć",
        "lokacija": "Trlabuć"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Hercegovo",
        "lokacija": "Hercegovo"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Cecelija",
        "lokacija": "Cecelija"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Šalce",
        "lokacija": "Šalce"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Šljivovica",
        "lokacija": "Šljivovica"
    },
    {
        "grad": "Vučitrn",
        "opstina": "Štitarica",
        "lokacija": "Štitarica"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Gadžin Han",
        "lokacija": "Gadžin Han"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Veliki Vrtop",
        "lokacija": "Veliki Vrtop"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Veliki Krčimir",
        "lokacija": "Veliki Krčimir"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Vilandrica",
        "lokacija": "Vilandrica"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Gare",
        "lokacija": "Gare"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Gornje Vlase",
        "lokacija": "Gornje Vlase"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Gornje Dragovlje",
        "lokacija": "Gornje Dragovlje"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Gornji Barbeš",
        "lokacija": "Gornji Barbeš"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Gornji Dušnik",
        "lokacija": "Gornji Dušnik"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Grkinja",
        "lokacija": "Grkinja"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Donje Dragovlje",
        "lokacija": "Donje Dragovlje"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Donji Barbeš",
        "lokacija": "Donji Barbeš"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Donji Dušnik",
        "lokacija": "Donji Dušnik"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Duga Poljana",
        "lokacija": "Duga Poljana"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Dukat",
        "lokacija": "Dukat"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Jagličje",
        "lokacija": "Jagličje"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Kaletinac",
        "lokacija": "Kaletinac"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Koprivnica",
        "lokacija": "Koprivnica"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Krastavče",
        "lokacija": "Krastavče"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Ličje",
        "lokacija": "Ličje"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Mali Vrtop",
        "lokacija": "Mali Vrtop"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Mali Krčimir",
        "lokacija": "Mali Krčimir"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Marina Kutina",
        "lokacija": "Marina Kutina"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Miljkovac",
        "lokacija": "Miljkovac"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Ovsinjinac",
        "lokacija": "Ovsinjinac"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Ravna Dubrava",
        "lokacija": "Ravna Dubrava"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Semče",
        "lokacija": "Semče"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Sopotnica",
        "lokacija": "Sopotnica"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Taskovići",
        "lokacija": "Taskovići"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Toponica",
        "lokacija": "Toponica"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Ćelije",
        "lokacija": "Ćelije"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Čagrovac",
        "lokacija": "Čagrovac"
    },
    {
        "grad": "Gadžin Han",
        "opstina": "Šebet",
        "lokacija": "Šebet"
    },
    {
        "grad": "Glogovac",
        "opstina": "Glogovac",
        "lokacija": "Glogovac"
    },
    {
        "grad": "Glogovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Glogovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Glogovac",
        "opstina": "Banjica",
        "lokacija": "Banjica"
    },
    {
        "grad": "Glogovac",
        "opstina": "Beriša",
        "lokacija": "Beriša"
    },
    {
        "grad": "Glogovac",
        "opstina": "Vasiljevo",
        "lokacija": "Vasiljevo"
    },
    {
        "grad": "Glogovac",
        "opstina": "Vrbovac",
        "lokacija": "Vrbovac"
    },
    {
        "grad": "Glogovac",
        "opstina": "Vučak",
        "lokacija": "Vučak"
    },
    {
        "grad": "Glogovac",
        "opstina": "Gladno Selo",
        "lokacija": "Gladno Selo"
    },
    {
        "grad": "Glogovac",
        "opstina": "Globare",
        "lokacija": "Globare"
    },
    {
        "grad": "Glogovac",
        "opstina": "Godance",
        "lokacija": "Godance"
    },
    {
        "grad": "Glogovac",
        "opstina": "Gornja Koretica",
        "lokacija": "Gornja Koretica"
    },
    {
        "grad": "Glogovac",
        "opstina": "Gornja Fuštica",
        "lokacija": "Gornja Fuštica"
    },
    {
        "grad": "Glogovac",
        "opstina": "Gornje Obrinje",
        "lokacija": "Gornje Obrinje"
    },
    {
        "grad": "Glogovac",
        "opstina": "Gornji Zabelj",
        "lokacija": "Gornji Zabelj"
    },
    {
        "grad": "Glogovac",
        "opstina": "gradica",
        "lokacija": "gradica"
    },
    {
        "grad": "Glogovac",
        "opstina": "Dobroševac",
        "lokacija": "Dobroševac"
    },
    {
        "grad": "Glogovac",
        "opstina": "Domanek",
        "lokacija": "Domanek"
    },
    {
        "grad": "Glogovac",
        "opstina": "Donja Koretica",
        "lokacija": "Donja Koretica"
    },
    {
        "grad": "Glogovac",
        "opstina": "Donja Fuštica",
        "lokacija": "Donja Fuštica"
    },
    {
        "grad": "Glogovac",
        "opstina": "Donji Zabelj",
        "lokacija": "Donji Zabelj"
    },
    {
        "grad": "Glogovac",
        "opstina": "Kišna Reka",
        "lokacija": "Kišna Reka"
    },
    {
        "grad": "Glogovac",
        "opstina": "Komorane",
        "lokacija": "Komorane"
    },
    {
        "grad": "Glogovac",
        "opstina": "Krajkovo",
        "lokacija": "Krajkovo"
    },
    {
        "grad": "Glogovac",
        "opstina": "Lapušnik",
        "lokacija": "Lapušnik"
    },
    {
        "grad": "Glogovac",
        "opstina": "Likošane",
        "lokacija": "Likošane"
    },
    {
        "grad": "Glogovac",
        "opstina": "Negrovce",
        "lokacija": "Negrovce"
    },
    {
        "grad": "Glogovac",
        "opstina": "Nekovce",
        "lokacija": "Nekovce"
    },
    {
        "grad": "Glogovac",
        "opstina": "Novo Čikatovo",
        "lokacija": "Novo Čikatovo"
    },
    {
        "grad": "Glogovac",
        "opstina": "Orlate",
        "lokacija": "Orlate"
    },
    {
        "grad": "Glogovac",
        "opstina": "Poklek",
        "lokacija": "Poklek"
    },
    {
        "grad": "Glogovac",
        "opstina": "Poluža",
        "lokacija": "Poluža"
    },
    {
        "grad": "Glogovac",
        "opstina": "Stankovce",
        "lokacija": "Stankovce"
    },
    {
        "grad": "Glogovac",
        "opstina": "Staro Čikatovo",
        "lokacija": "Staro Čikatovo"
    },
    {
        "grad": "Glogovac",
        "opstina": "Trdevac",
        "lokacija": "Trdevac"
    },
    {
        "grad": "Glogovac",
        "opstina": "Trpeza",
        "lokacija": "Trpeza"
    },
    {
        "grad": "Glogovac",
        "opstina": "Trstenik",
        "lokacija": "Trstenik"
    },
    {
        "grad": "Glogovac",
        "opstina": "Štrbulovo",
        "lokacija": "Štrbulovo"
    },
    {
        "grad": "Glogovac",
        "opstina": "Štutica",
        "lokacija": "Štutica"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Gnjilane",
        "lokacija": "Gnjilane"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Bilince",
        "lokacija": "Bilince"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Brasaljce",
        "lokacija": "Brasaljce"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Bukovik",
        "lokacija": "Bukovik"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Burince",
        "lokacija": "Burince"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Velekince",
        "lokacija": "Velekince"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Vladovo",
        "lokacija": "Vladovo"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Vlaštica",
        "lokacija": "Vlaštica"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Vrapčić",
        "lokacija": "Vrapčić"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Vrbica",
        "lokacija": "Vrbica"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Gadiš",
        "lokacija": "Gadiš"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Gornje Kusce",
        "lokacija": "Gornje Kusce"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Gornje Slakovce",
        "lokacija": "Gornje Slakovce"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Gornji Livoč",
        "lokacija": "Gornji Livoč"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Gornji Makreš",
        "lokacija": "Gornji Makreš"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Gumnište",
        "lokacija": "Gumnište"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Dobrčane",
        "lokacija": "Dobrčane"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Donja Budriga",
        "lokacija": "Donja Budriga"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Donje Slakovce",
        "lokacija": "Donje Slakovce"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Donji Livoč",
        "lokacija": "Donji Livoč"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Donji Makreš",
        "lokacija": "Donji Makreš"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Draganac",
        "lokacija": "Draganac"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Dunavo",
        "lokacija": "Dunavo"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Žegovac",
        "lokacija": "Žegovac"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Žegovačka Vrbica",
        "lokacija": "Žegovačka Vrbica"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Žegra",
        "lokacija": "Žegra"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Inatovce",
        "lokacija": "Inatovce"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Kišno Polje",
        "lokacija": "Kišno Polje"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Kmetovce",
        "lokacija": "Kmetovce"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Koretište",
        "lokacija": "Koretište"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Kravarica",
        "lokacija": "Kravarica"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Lipovica",
        "lokacija": "Lipovica"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Lovce",
        "lokacija": "Lovce"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Mali Goden",
        "lokacija": "Mali Goden"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Mališevo",
        "lokacija": "Mališevo"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Mozgovo",
        "lokacija": "Mozgovo"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Mučibaba",
        "lokacija": "Mučibaba"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Nosalje",
        "lokacija": "Nosalje"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Paralovo",
        "lokacija": "Paralovo"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Parteš",
        "lokacija": "Parteš"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Pasjak",
        "lokacija": "Pasjak"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Pasjane",
        "lokacija": "Pasjane"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Pidić",
        "lokacija": "Pidić"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Podgrađe",
        "lokacija": "Podgrađe"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Poneš",
        "lokacija": "Poneš"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Prilepnica",
        "lokacija": "Prilepnica"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Sapar",
        "lokacija": "Sapar"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Slubica",
        "lokacija": "Slubica"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Stanišor",
        "lokacija": "Stanišor"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Stančić",
        "lokacija": "Stančić"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Straža",
        "lokacija": "Straža"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Stublina",
        "lokacija": "Stublina"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Ugljare",
        "lokacija": "Ugljare"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Cernica",
        "lokacija": "Cernica"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Čelik",
        "lokacija": "Čelik"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Šilovo",
        "lokacija": "Šilovo"
    },
    {
        "grad": "Gnjilane",
        "opstina": "Šurlane",
        "lokacija": "Šurlane"
    },
    {
        "grad": "Golubac",
        "opstina": "Golubac",
        "lokacija": "Golubac"
    },
    {
        "grad": "Golubac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Golubac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Golubac",
        "opstina": "Barič",
        "lokacija": "Barič"
    },
    {
        "grad": "Golubac",
        "opstina": "Bikinje",
        "lokacija": "Bikinje"
    },
    {
        "grad": "Golubac",
        "opstina": "Braničevo",
        "lokacija": "Braničevo"
    },
    {
        "grad": "Golubac",
        "opstina": "Brnjica",
        "lokacija": "Brnjica"
    },
    {
        "grad": "Golubac",
        "opstina": "Vinci",
        "lokacija": "Vinci"
    },
    {
        "grad": "Golubac",
        "opstina": "Vojilovo",
        "lokacija": "Vojilovo"
    },
    {
        "grad": "Golubac",
        "opstina": "Dvorište",
        "lokacija": "Dvorište"
    },
    {
        "grad": "Golubac",
        "opstina": "Dobra",
        "lokacija": "Dobra"
    },
    {
        "grad": "Golubac",
        "opstina": "Donja Kruševica",
        "lokacija": "Donja Kruševica"
    },
    {
        "grad": "Golubac",
        "opstina": "Dušmanić",
        "lokacija": "Dušmanić"
    },
    {
        "grad": "Golubac",
        "opstina": "Žitkovica",
        "lokacija": "Žitkovica"
    },
    {
        "grad": "Golubac",
        "opstina": "Klenje",
        "lokacija": "Klenje"
    },
    {
        "grad": "Golubac",
        "opstina": "Krivača",
        "lokacija": "Krivača"
    },
    {
        "grad": "Golubac",
        "opstina": "Kudreš",
        "lokacija": "Kudreš"
    },
    {
        "grad": "Golubac",
        "opstina": "Maleševo",
        "lokacija": "Maleševo"
    },
    {
        "grad": "Golubac",
        "opstina": "Miljević",
        "lokacija": "Miljević"
    },
    {
        "grad": "Golubac",
        "opstina": "Mrčkovac",
        "lokacija": "Mrčkovac"
    },
    {
        "grad": "Golubac",
        "opstina": "Ponikve",
        "lokacija": "Ponikve"
    },
    {
        "grad": "Golubac",
        "opstina": "Radoševac",
        "lokacija": "Radoševac"
    },
    {
        "grad": "Golubac",
        "opstina": "Sladinac",
        "lokacija": "Sladinac"
    },
    {
        "grad": "Golubac",
        "opstina": "Snegotin",
        "lokacija": "Snegotin"
    },
    {
        "grad": "Golubac",
        "opstina": "Usije",
        "lokacija": "Usije"
    },
    {
        "grad": "Golubac",
        "opstina": "Šuvajić",
        "lokacija": "Šuvajić"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gornji Milanovac",
        "lokacija": "Gornji Milanovac"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Backovac"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Brankovo Brdo"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Grobnice"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Despotovica"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Ivice"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Neškovića Brdo"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Rasadnik"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Trijangla"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Belo Polje",
        "lokacija": "Belo Polje"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Berišići",
        "lokacija": "Berišići"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Bogdanica",
        "lokacija": "Bogdanica"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Boljkovci",
        "lokacija": "Boljkovci"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Brajići",
        "lokacija": "Brajići"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Brđani",
        "lokacija": "Brđani"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Brezna",
        "lokacija": "Brezna"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Brezovica",
        "lokacija": "Brezovica"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Brusnica",
        "lokacija": "Brusnica"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Varnice",
        "lokacija": "Varnice"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Velereč",
        "lokacija": "Velereč"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Vraćevšnica",
        "lokacija": "Vraćevšnica"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Vrnčani",
        "lokacija": "Vrnčani"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gojna Gora",
        "lokacija": "Gojna Gora"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gornja Vrbava",
        "lokacija": "Gornja Vrbava"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gornja Crnuća",
        "lokacija": "Gornja Crnuća"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gornji Banjani",
        "lokacija": "Gornji Banjani"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Gornji Branetići",
        "lokacija": "Gornji Branetići"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Grabovica",
        "lokacija": "Grabovica"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Davidovica",
        "lokacija": "Davidovica"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Donja Vrbava",
        "lokacija": "Donja Vrbava"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Donja Crnuća",
        "lokacija": "Donja Crnuća"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Donji Branetići",
        "lokacija": "Donji Branetići"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Dragolj",
        "lokacija": "Dragolj"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Drenova",
        "lokacija": "Drenova"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Družetići",
        "lokacija": "Družetići"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Zagrađe",
        "lokacija": "Zagrađe"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Jablanica",
        "lokacija": "Jablanica"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Kalimanići",
        "lokacija": "Kalimanići"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Kamenica",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Klatičevo",
        "lokacija": "Klatičevo"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Koštunići",
        "lokacija": "Koštunići"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Kriva Reka",
        "lokacija": "Kriva Reka"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Leušići",
        "lokacija": "Leušići"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Lipovac",
        "lokacija": "Lipovac"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Lozanj",
        "lokacija": "Lozanj"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Ločevci",
        "lokacija": "Ločevci"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Lunjevica",
        "lokacija": "Lunjevica"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Ljevaja",
        "lokacija": "Ljevaja"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Ljutovnica",
        "lokacija": "Ljutovnica"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Majdan",
        "lokacija": "Majdan"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Mutanj",
        "lokacija": "Mutanj"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Nakučani",
        "lokacija": "Nakučani"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Nevade",
        "lokacija": "Nevade"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Ozrem",
        "lokacija": "Ozrem"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Polom",
        "lokacija": "Polom"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Pranjani",
        "lokacija": "Pranjani"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Prnjavor",
        "lokacija": "Prnjavor"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Ravna Gora",
        "lokacija": "Ravna Gora"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Reljinci",
        "lokacija": "Reljinci"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Rudnik",
        "lokacija": "Rudnik"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Ručići",
        "lokacija": "Ručići"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Svračkovci",
        "lokacija": "Svračkovci"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Semedraž",
        "lokacija": "Semedraž"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Sinoševići",
        "lokacija": "Sinoševići"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Srezojevci",
        "lokacija": "Srezojevci"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Takovo",
        "lokacija": "Takovo"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Teočin",
        "lokacija": "Teočin"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Trudelj",
        "lokacija": "Trudelj"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Ugrinovci",
        "lokacija": "Ugrinovci"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Cerova",
        "lokacija": "Cerova"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Šarani",
        "lokacija": "Šarani"
    },
    {
        "grad": "Gornji Milanovac",
        "opstina": "Šilopaj",
        "lokacija": "Šilopaj"
    },
    {
        "grad": "Despotovac",
        "opstina": "Despotovac",
        "lokacija": "Despotovac"
    },
    {
        "grad": "Despotovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Despotovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Despotovac",
        "opstina": "Balajnac",
        "lokacija": "Balajnac"
    },
    {
        "grad": "Despotovac",
        "opstina": "Bare",
        "lokacija": "Bare"
    },
    {
        "grad": "Despotovac",
        "opstina": "Beljajka",
        "lokacija": "Beljajka"
    },
    {
        "grad": "Despotovac",
        "opstina": "Bogava",
        "lokacija": "Bogava"
    },
    {
        "grad": "Despotovac",
        "opstina": "Brestovo",
        "lokacija": "Brestovo"
    },
    {
        "grad": "Despotovac",
        "opstina": "Bukovac",
        "lokacija": "Bukovac"
    },
    {
        "grad": "Despotovac",
        "opstina": "Veliki Popović",
        "lokacija": "Veliki Popović"
    },
    {
        "grad": "Despotovac",
        "opstina": "Vitance",
        "lokacija": "Vitance"
    },
    {
        "grad": "Despotovac",
        "opstina": "Vojnik",
        "lokacija": "Vojnik"
    },
    {
        "grad": "Despotovac",
        "opstina": "Grabovica",
        "lokacija": "Grabovica"
    },
    {
        "grad": "Despotovac",
        "opstina": "Dvorište",
        "lokacija": "Dvorište"
    },
    {
        "grad": "Despotovac",
        "opstina": "Despotovac (selo)",
        "lokacija": "Despotovac (selo)"
    },
    {
        "grad": "Despotovac",
        "opstina": "Židilje",
        "lokacija": "Židilje"
    },
    {
        "grad": "Despotovac",
        "opstina": "Zlatovo",
        "lokacija": "Zlatovo"
    },
    {
        "grad": "Despotovac",
        "opstina": "Jasenovo",
        "lokacija": "Jasenovo"
    },
    {
        "grad": "Despotovac",
        "opstina": "Jezero",
        "lokacija": "Jezero"
    },
    {
        "grad": "Despotovac",
        "opstina": "Jelovac",
        "lokacija": "Jelovac"
    },
    {
        "grad": "Despotovac",
        "opstina": "Lipovica",
        "lokacija": "Lipovica"
    },
    {
        "grad": "Despotovac",
        "opstina": "Lomnica",
        "lokacija": "Lomnica"
    },
    {
        "grad": "Despotovac",
        "opstina": "Makvište",
        "lokacija": "Makvište"
    },
    {
        "grad": "Despotovac",
        "opstina": "Medveđa",
        "lokacija": "Medveđa"
    },
    {
        "grad": "Despotovac",
        "opstina": "Miliva",
        "lokacija": "Miliva"
    },
    {
        "grad": "Despotovac",
        "opstina": "Panjevac",
        "lokacija": "Panjevac"
    },
    {
        "grad": "Despotovac",
        "opstina": "Plažane",
        "lokacija": "Plažane"
    },
    {
        "grad": "Despotovac",
        "opstina": "Popovnjak",
        "lokacija": "Popovnjak"
    },
    {
        "grad": "Despotovac",
        "opstina": "Ravna Reka",
        "lokacija": "Ravna Reka"
    },
    {
        "grad": "Despotovac",
        "opstina": "Resavica",
        "lokacija": "Resavica"
    },
    {
        "grad": "Despotovac",
        "opstina": "Resavica (selo)",
        "lokacija": "Resavica (selo)"
    },
    {
        "grad": "Despotovac",
        "opstina": "Senjski Rudnik",
        "lokacija": "Senjski Rudnik"
    },
    {
        "grad": "Despotovac",
        "opstina": "Sladaja",
        "lokacija": "Sladaja"
    },
    {
        "grad": "Despotovac",
        "opstina": "Stenjevac",
        "lokacija": "Stenjevac"
    },
    {
        "grad": "Despotovac",
        "opstina": "Strmosten",
        "lokacija": "Strmosten"
    },
    {
        "grad": "Despotovac",
        "opstina": "Trućevac",
        "lokacija": "Trućevac"
    },
    {
        "grad": "Dečani",
        "opstina": "Dečani",
        "lokacija": "Dečani"
    },
    {
        "grad": "Dečani",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Dečani",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Dečani",
        "opstina": "Babaloć",
        "lokacija": "Babaloć"
    },
    {
        "grad": "Dečani",
        "opstina": "Belaje",
        "lokacija": "Belaje"
    },
    {
        "grad": "Dečani",
        "opstina": "Beleg",
        "lokacija": "Beleg"
    },
    {
        "grad": "Dečani",
        "opstina": "Vokša",
        "lokacija": "Vokša"
    },
    {
        "grad": "Dečani",
        "opstina": "Glođane",
        "lokacija": "Glođane"
    },
    {
        "grad": "Dečani",
        "opstina": "Gornja Luka",
        "lokacija": "Gornja Luka"
    },
    {
        "grad": "Dečani",
        "opstina": "Gornji Ratiš",
        "lokacija": "Gornji Ratiš"
    },
    {
        "grad": "Dečani",
        "opstina": "Gornji Streoc",
        "lokacija": "Gornji Streoc"
    },
    {
        "grad": "Dečani",
        "opstina": "Gornji Crnobreg",
        "lokacija": "Gornji Crnobreg"
    },
    {
        "grad": "Dečani",
        "opstina": "Gramočelj",
        "lokacija": "Gramočelj"
    },
    {
        "grad": "Dečani",
        "opstina": "Dašinovac",
        "lokacija": "Dašinovac"
    },
    {
        "grad": "Dečani",
        "opstina": "Donja Luka",
        "lokacija": "Donja Luka"
    },
    {
        "grad": "Dečani",
        "opstina": "Donji Ratiš",
        "lokacija": "Donji Ratiš"
    },
    {
        "grad": "Dečani",
        "opstina": "Donji Streoc",
        "lokacija": "Donji Streoc"
    },
    {
        "grad": "Dečani",
        "opstina": "Donji Crnobreg",
        "lokacija": "Donji Crnobreg"
    },
    {
        "grad": "Dečani",
        "opstina": "Drenovac",
        "lokacija": "Drenovac"
    },
    {
        "grad": "Dečani",
        "opstina": "Dubovik",
        "lokacija": "Dubovik"
    },
    {
        "grad": "Dečani",
        "opstina": "Dubrava",
        "lokacija": "Dubrava"
    },
    {
        "grad": "Dečani",
        "opstina": "Đocaj",
        "lokacija": "Đocaj"
    },
    {
        "grad": "Dečani",
        "opstina": "Istinić",
        "lokacija": "Istinić"
    },
    {
        "grad": "Dečani",
        "opstina": "Jasić",
        "lokacija": "Jasić"
    },
    {
        "grad": "Dečani",
        "opstina": "Junik",
        "lokacija": "Junik"
    },
    {
        "grad": "Dečani",
        "opstina": "Kodralija",
        "lokacija": "Kodralija"
    },
    {
        "grad": "Dečani",
        "opstina": "Loćane",
        "lokacija": "Loćane"
    },
    {
        "grad": "Dečani",
        "opstina": "Ljubuša",
        "lokacija": "Ljubuša"
    },
    {
        "grad": "Dečani",
        "opstina": "Ljumbarda",
        "lokacija": "Ljumbarda"
    },
    {
        "grad": "Dečani",
        "opstina": "Maznik",
        "lokacija": "Maznik"
    },
    {
        "grad": "Dečani",
        "opstina": "Mali Vranovac",
        "lokacija": "Mali Vranovac"
    },
    {
        "grad": "Dečani",
        "opstina": "Papić",
        "lokacija": "Papić"
    },
    {
        "grad": "Dečani",
        "opstina": "Papraćane",
        "lokacija": "Papraćane"
    },
    {
        "grad": "Dečani",
        "opstina": "Pobrđe",
        "lokacija": "Pobrđe"
    },
    {
        "grad": "Dečani",
        "opstina": "Požar",
        "lokacija": "Požar"
    },
    {
        "grad": "Dečani",
        "opstina": "Prekoluka",
        "lokacija": "Prekoluka"
    },
    {
        "grad": "Dečani",
        "opstina": "Prilep",
        "lokacija": "Prilep"
    },
    {
        "grad": "Dečani",
        "opstina": "Rastavica",
        "lokacija": "Rastavica"
    },
    {
        "grad": "Dečani",
        "opstina": "Rznić",
        "lokacija": "Rznić"
    },
    {
        "grad": "Dečani",
        "opstina": "Slup",
        "lokacija": "Slup"
    },
    {
        "grad": "Dečani",
        "opstina": "Huljaj",
        "lokacija": "Huljaj"
    },
    {
        "grad": "Dečani",
        "opstina": "Šaptelj",
        "lokacija": "Šaptelj"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Dimitrovgrad",
        "lokacija": "Dimitrovgrad"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Boljev Dol",
        "lokacija": "Boljev Dol"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Banjski Dol",
        "lokacija": "Banjski Dol"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Barje",
        "lokacija": "Barje"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Bačevo",
        "lokacija": "Bačevo"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Beleš",
        "lokacija": "Beleš"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Bilo",
        "lokacija": "Bilo"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Braćevci",
        "lokacija": "Braćevci"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Brebevnica",
        "lokacija": "Brebevnica"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Verzar",
        "lokacija": "Verzar"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Visočki Odorovci",
        "lokacija": "Visočki Odorovci"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Vlkovija",
        "lokacija": "Vlkovija"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Vrapča",
        "lokacija": "Vrapča"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Gojin Dol",
        "lokacija": "Gojin Dol"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Gornja Nevlja",
        "lokacija": "Gornja Nevlja"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Gornji Krivodol",
        "lokacija": "Gornji Krivodol"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "gradinje",
        "lokacija": "gradinje"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Grapa",
        "lokacija": "Grapa"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Gulenovci",
        "lokacija": "Gulenovci"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Donja Nevlja",
        "lokacija": "Donja Nevlja"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Donji Krivodol",
        "lokacija": "Donji Krivodol"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Dragovita",
        "lokacija": "Dragovita"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Željuša",
        "lokacija": "Željuša"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Izatovci",
        "lokacija": "Izatovci"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Iskrovci",
        "lokacija": "Iskrovci"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Kamenica",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Kusa Vrana",
        "lokacija": "Kusa Vrana"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Lukavica",
        "lokacija": "Lukavica"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Mazgoš",
        "lokacija": "Mazgoš"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Mojinci",
        "lokacija": "Mojinci"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Paskašija",
        "lokacija": "Paskašija"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Petačinci",
        "lokacija": "Petačinci"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Petrlaš",
        "lokacija": "Petrlaš"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Planinica",
        "lokacija": "Planinica"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Poganovo",
        "lokacija": "Poganovo"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Prača",
        "lokacija": "Prača"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Protopopinci",
        "lokacija": "Protopopinci"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Radejna",
        "lokacija": "Radejna"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Senokos",
        "lokacija": "Senokos"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Skrvenica",
        "lokacija": "Skrvenica"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Slivnica",
        "lokacija": "Slivnica"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Smilovci",
        "lokacija": "Smilovci"
    },
    {
        "grad": "Dimitrovgrad",
        "opstina": "Trnski Odorovci",
        "lokacija": "Trnski Odorovci"
    },
    {
        "grad": "Doljevac",
        "opstina": "Doljevac",
        "lokacija": "Doljevac"
    },
    {
        "grad": "Doljevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Doljevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Doljevac",
        "opstina": "Belotinac",
        "lokacija": "Belotinac"
    },
    {
        "grad": "Doljevac",
        "opstina": "Klisura",
        "lokacija": "Klisura"
    },
    {
        "grad": "Doljevac",
        "opstina": "Knežica",
        "lokacija": "Knežica"
    },
    {
        "grad": "Doljevac",
        "opstina": "Kočane",
        "lokacija": "Kočane"
    },
    {
        "grad": "Doljevac",
        "opstina": "Malošište",
        "lokacija": "Malošište"
    },
    {
        "grad": "Doljevac",
        "opstina": "Mekiš",
        "lokacija": "Mekiš"
    },
    {
        "grad": "Doljevac",
        "opstina": "Orljane",
        "lokacija": "Orljane"
    },
    {
        "grad": "Doljevac",
        "opstina": "Perutina",
        "lokacija": "Perutina"
    },
    {
        "grad": "Doljevac",
        "opstina": "Pukovac",
        "lokacija": "Pukovac"
    },
    {
        "grad": "Doljevac",
        "opstina": "Rusna",
        "lokacija": "Rusna"
    },
    {
        "grad": "Doljevac",
        "opstina": "Ćurlina",
        "lokacija": "Ćurlina"
    },
    {
        "grad": "Doljevac",
        "opstina": "Čapljinac",
        "lokacija": "Čapljinac"
    },
    {
        "grad": "Doljevac",
        "opstina": "Čečina",
        "lokacija": "Čečina"
    },
    {
        "grad": "Doljevac",
        "opstina": "Šainovac",
        "lokacija": "Šainovac"
    },
    {
        "grad": "Doljevac",
        "opstina": "Šarlince",
        "lokacija": "Šarlince"
    },
    {
        "grad": "Dragaš",
        "opstina": "Dragaš",
        "lokacija": "Dragaš"
    },
    {
        "grad": "Dragaš",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Dragaš",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Dragaš",
        "opstina": "Bačka",
        "lokacija": "Bačka"
    },
    {
        "grad": "Dragaš",
        "opstina": "Brod",
        "lokacija": "Brod"
    },
    {
        "grad": "Dragaš",
        "opstina": "Vranište",
        "lokacija": "Vranište"
    },
    {
        "grad": "Dragaš",
        "opstina": "Globočica",
        "lokacija": "Globočica"
    },
    {
        "grad": "Dragaš",
        "opstina": "Gornja Rapča",
        "lokacija": "Gornja Rapča"
    },
    {
        "grad": "Dragaš",
        "opstina": "Gornji Krstac",
        "lokacija": "Gornji Krstac"
    },
    {
        "grad": "Dragaš",
        "opstina": "Dikance",
        "lokacija": "Dikance"
    },
    {
        "grad": "Dragaš",
        "opstina": "Donja Rapča",
        "lokacija": "Donja Rapča"
    },
    {
        "grad": "Dragaš",
        "opstina": "Donji Krstac",
        "lokacija": "Donji Krstac"
    },
    {
        "grad": "Dragaš",
        "opstina": "Zli Potok",
        "lokacija": "Zli Potok"
    },
    {
        "grad": "Dragaš",
        "opstina": "Kruševo",
        "lokacija": "Kruševo"
    },
    {
        "grad": "Dragaš",
        "opstina": "Kukuljane",
        "lokacija": "Kukuljane"
    },
    {
        "grad": "Dragaš",
        "opstina": "Leštane",
        "lokacija": "Leštane"
    },
    {
        "grad": "Dragaš",
        "opstina": "Ljubovište",
        "lokacija": "Ljubovište"
    },
    {
        "grad": "Dragaš",
        "opstina": "Mlike",
        "lokacija": "Mlike"
    },
    {
        "grad": "Dragaš",
        "opstina": "Orčuša",
        "lokacija": "Orčuša"
    },
    {
        "grad": "Dragaš",
        "opstina": "Radeša",
        "lokacija": "Radeša"
    },
    {
        "grad": "Dragaš",
        "opstina": "Restelica",
        "lokacija": "Restelica"
    },
    {
        "grad": "Đakovica",
        "opstina": "Đakovica",
        "lokacija": "Đakovica"
    },
    {
        "grad": "Đakovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Đakovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Đakovica",
        "opstina": "Babaj Boks",
        "lokacija": "Babaj Boks"
    },
    {
        "grad": "Đakovica",
        "opstina": "Bardonić",
        "lokacija": "Bardonić"
    },
    {
        "grad": "Đakovica",
        "opstina": "Bardosan",
        "lokacija": "Bardosan"
    },
    {
        "grad": "Đakovica",
        "opstina": "Batuša",
        "lokacija": "Batuša"
    },
    {
        "grad": "Đakovica",
        "opstina": "Berjak",
        "lokacija": "Berjak"
    },
    {
        "grad": "Đakovica",
        "opstina": "Bec",
        "lokacija": "Bec"
    },
    {
        "grad": "Đakovica",
        "opstina": "Bistražin",
        "lokacija": "Bistražin"
    },
    {
        "grad": "Đakovica",
        "opstina": "Brekovac",
        "lokacija": "Brekovac"
    },
    {
        "grad": "Đakovica",
        "opstina": "Brovina",
        "lokacija": "Brovina"
    },
    {
        "grad": "Đakovica",
        "opstina": "Vogovo",
        "lokacija": "Vogovo"
    },
    {
        "grad": "Đakovica",
        "opstina": "Vranić",
        "lokacija": "Vranić"
    },
    {
        "grad": "Đakovica",
        "opstina": "Goden",
        "lokacija": "Goden"
    },
    {
        "grad": "Đakovica",
        "opstina": "Gornje Novo Selo",
        "lokacija": "Gornje Novo Selo"
    },
    {
        "grad": "Đakovica",
        "opstina": "Grgoc",
        "lokacija": "Grgoc"
    },
    {
        "grad": "Đakovica",
        "opstina": "Grčina",
        "lokacija": "Grčina"
    },
    {
        "grad": "Đakovica",
        "opstina": "Guska",
        "lokacija": "Guska"
    },
    {
        "grad": "Đakovica",
        "opstina": "Dalašaj",
        "lokacija": "Dalašaj"
    },
    {
        "grad": "Đakovica",
        "opstina": "Damjane",
        "lokacija": "Damjane"
    },
    {
        "grad": "Đakovica",
        "opstina": "Deva",
        "lokacija": "Deva"
    },
    {
        "grad": "Đakovica",
        "opstina": "Doblibare",
        "lokacija": "Doblibare"
    },
    {
        "grad": "Đakovica",
        "opstina": "Dobrić",
        "lokacija": "Dobrić"
    },
    {
        "grad": "Đakovica",
        "opstina": "Dobroš",
        "lokacija": "Dobroš"
    },
    {
        "grad": "Đakovica",
        "opstina": "Dolj",
        "lokacija": "Dolj"
    },
    {
        "grad": "Đakovica",
        "opstina": "Donje Novo Selo",
        "lokacija": "Donje Novo Selo"
    },
    {
        "grad": "Đakovica",
        "opstina": "Donji Biteš",
        "lokacija": "Donji Biteš"
    },
    {
        "grad": "Đakovica",
        "opstina": "Dužnje",
        "lokacija": "Dužnje"
    },
    {
        "grad": "Đakovica",
        "opstina": "Dujak",
        "lokacija": "Dujak"
    },
    {
        "grad": "Đakovica",
        "opstina": "Ereč",
        "lokacija": "Ereč"
    },
    {
        "grad": "Đakovica",
        "opstina": "Žabelj",
        "lokacija": "Žabelj"
    },
    {
        "grad": "Đakovica",
        "opstina": "Ždrelo",
        "lokacija": "Ždrelo"
    },
    {
        "grad": "Đakovica",
        "opstina": "Žub",
        "lokacija": "Žub"
    },
    {
        "grad": "Đakovica",
        "opstina": "Zulfaj",
        "lokacija": "Zulfaj"
    },
    {
        "grad": "Đakovica",
        "opstina": "Jablanica",
        "lokacija": "Jablanica"
    },
    {
        "grad": "Đakovica",
        "opstina": "Janoš",
        "lokacija": "Janoš"
    },
    {
        "grad": "Đakovica",
        "opstina": "Jahoc",
        "lokacija": "Jahoc"
    },
    {
        "grad": "Đakovica",
        "opstina": "Kodralija",
        "lokacija": "Kodralija"
    },
    {
        "grad": "Đakovica",
        "opstina": "Korenica",
        "lokacija": "Korenica"
    },
    {
        "grad": "Đakovica",
        "opstina": "Košare",
        "lokacija": "Košare"
    },
    {
        "grad": "Đakovica",
        "opstina": "Kraljane",
        "lokacija": "Kraljane"
    },
    {
        "grad": "Đakovica",
        "opstina": "Kusar",
        "lokacija": "Kusar"
    },
    {
        "grad": "Đakovica",
        "opstina": "Kuševac",
        "lokacija": "Kuševac"
    },
    {
        "grad": "Đakovica",
        "opstina": "Lipovac",
        "lokacija": "Lipovac"
    },
    {
        "grad": "Đakovica",
        "opstina": "Lugađija",
        "lokacija": "Lugađija"
    },
    {
        "grad": "Đakovica",
        "opstina": "Ljugbunar",
        "lokacija": "Ljugbunar"
    },
    {
        "grad": "Đakovica",
        "opstina": "Marmule",
        "lokacija": "Marmule"
    },
    {
        "grad": "Đakovica",
        "opstina": "Meja Orize",
        "lokacija": "Meja Orize"
    },
    {
        "grad": "Đakovica",
        "opstina": "Meća",
        "lokacija": "Meća"
    },
    {
        "grad": "Đakovica",
        "opstina": "Moglica",
        "lokacija": "Moglica"
    },
    {
        "grad": "Đakovica",
        "opstina": "Molić",
        "lokacija": "Molić"
    },
    {
        "grad": "Đakovica",
        "opstina": "Morina",
        "lokacija": "Morina"
    },
    {
        "grad": "Đakovica",
        "opstina": "Nec",
        "lokacija": "Nec"
    },
    {
        "grad": "Đakovica",
        "opstina": "Nivokaz",
        "lokacija": "Nivokaz"
    },
    {
        "grad": "Đakovica",
        "opstina": "Osek Paša",
        "lokacija": "Osek Paša"
    },
    {
        "grad": "Đakovica",
        "opstina": "Osek Hilja",
        "lokacija": "Osek Hilja"
    },
    {
        "grad": "Đakovica",
        "opstina": "Paljabarda",
        "lokacija": "Paljabarda"
    },
    {
        "grad": "Đakovica",
        "opstina": "Pacaj",
        "lokacija": "Pacaj"
    },
    {
        "grad": "Đakovica",
        "opstina": "Petrušan",
        "lokacija": "Petrušan"
    },
    {
        "grad": "Đakovica",
        "opstina": "Pljančor",
        "lokacija": "Pljančor"
    },
    {
        "grad": "Đakovica",
        "opstina": "Ponoševac",
        "lokacija": "Ponoševac"
    },
    {
        "grad": "Đakovica",
        "opstina": "Popovac",
        "lokacija": "Popovac"
    },
    {
        "grad": "Đakovica",
        "opstina": "Radonjić",
        "lokacija": "Radonjić"
    },
    {
        "grad": "Đakovica",
        "opstina": "Rakovina",
        "lokacija": "Rakovina"
    },
    {
        "grad": "Đakovica",
        "opstina": "Rakoc",
        "lokacija": "Rakoc"
    },
    {
        "grad": "Đakovica",
        "opstina": "Ramoc",
        "lokacija": "Ramoc"
    },
    {
        "grad": "Đakovica",
        "opstina": "Racaj",
        "lokacija": "Racaj"
    },
    {
        "grad": "Đakovica",
        "opstina": "Rača",
        "lokacija": "Rača"
    },
    {
        "grad": "Đakovica",
        "opstina": "Raškoc",
        "lokacija": "Raškoc"
    },
    {
        "grad": "Đakovica",
        "opstina": "Ripaj Madanaj",
        "lokacija": "Ripaj Madanaj"
    },
    {
        "grad": "Đakovica",
        "opstina": "Rogovo",
        "lokacija": "Rogovo"
    },
    {
        "grad": "Đakovica",
        "opstina": "Skivjane",
        "lokacija": "Skivjane"
    },
    {
        "grad": "Đakovica",
        "opstina": "Smać",
        "lokacija": "Smać"
    },
    {
        "grad": "Đakovica",
        "opstina": "Smonica",
        "lokacija": "Smonica"
    },
    {
        "grad": "Đakovica",
        "opstina": "Sopot",
        "lokacija": "Sopot"
    },
    {
        "grad": "Đakovica",
        "opstina": "Stubla",
        "lokacija": "Stubla"
    },
    {
        "grad": "Đakovica",
        "opstina": "Trakanić",
        "lokacija": "Trakanić"
    },
    {
        "grad": "Đakovica",
        "opstina": "Ćerim",
        "lokacija": "Ćerim"
    },
    {
        "grad": "Đakovica",
        "opstina": "Ujz",
        "lokacija": "Ujz"
    },
    {
        "grad": "Đakovica",
        "opstina": "Firaja",
        "lokacija": "Firaja"
    },
    {
        "grad": "Đakovica",
        "opstina": "Firza",
        "lokacija": "Firza"
    },
    {
        "grad": "Đakovica",
        "opstina": "Crmljane",
        "lokacija": "Crmljane"
    },
    {
        "grad": "Đakovica",
        "opstina": "Šeremet",
        "lokacija": "Šeremet"
    },
    {
        "grad": "Đakovica",
        "opstina": "Šišman",
        "lokacija": "Šišman"
    },
    {
        "grad": "Žabalj",
        "opstina": "Žabalj",
        "lokacija": "Žabalj"
    },
    {
        "grad": "Žabalj",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Čikmeže"
    },
    {
        "grad": "Žabalj",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Žabalj",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Žabalj",
        "opstina": "Gospođinci",
        "lokacija": "Gospođinci"
    },
    {
        "grad": "Žabalj",
        "opstina": "Đurđevo",
        "lokacija": "Đurđevo"
    },
    {
        "grad": "Žabalj",
        "opstina": "Čurug",
        "lokacija": "Čurug"
    },
    {
        "grad": "Žabari",
        "opstina": "Žabari",
        "lokacija": "Žabari"
    },
    {
        "grad": "Žabari",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Žabari",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Žabari",
        "opstina": "Aleksandrovac",
        "lokacija": "Aleksandrovac"
    },
    {
        "grad": "Žabari",
        "opstina": "Brzohode",
        "lokacija": "Brzohode"
    },
    {
        "grad": "Žabari",
        "opstina": "Viteževo",
        "lokacija": "Viteževo"
    },
    {
        "grad": "Žabari",
        "opstina": "Vlaški Do",
        "lokacija": "Vlaški Do"
    },
    {
        "grad": "Žabari",
        "opstina": "Kočetin",
        "lokacija": "Kočetin"
    },
    {
        "grad": "Žabari",
        "opstina": "Mirijevo",
        "lokacija": "Mirijevo"
    },
    {
        "grad": "Žabari",
        "opstina": "Oreovica",
        "lokacija": "Oreovica"
    },
    {
        "grad": "Žabari",
        "opstina": "Polatna",
        "lokacija": "Polatna"
    },
    {
        "grad": "Žabari",
        "opstina": "Porodin",
        "lokacija": "Porodin"
    },
    {
        "grad": "Žabari",
        "opstina": "Svinjarevo",
        "lokacija": "Svinjarevo"
    },
    {
        "grad": "Žabari",
        "opstina": "Sibnica",
        "lokacija": "Sibnica"
    },
    {
        "grad": "Žabari",
        "opstina": "Simićevo",
        "lokacija": "Simićevo"
    },
    {
        "grad": "Žabari",
        "opstina": "Tićevac",
        "lokacija": "Tićevac"
    },
    {
        "grad": "Žabari",
        "opstina": "Četereže",
        "lokacija": "Četereže"
    },
    {
        "grad": "Žagubica",
        "opstina": "Žagubica",
        "lokacija": "Žagubica"
    },
    {
        "grad": "Žagubica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Žagubica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Žagubica",
        "opstina": "Bliznak",
        "lokacija": "Bliznak"
    },
    {
        "grad": "Žagubica",
        "opstina": "Breznica",
        "lokacija": "Breznica"
    },
    {
        "grad": "Žagubica",
        "opstina": "Vukovac",
        "lokacija": "Vukovac"
    },
    {
        "grad": "Žagubica",
        "opstina": "Izvarica",
        "lokacija": "Izvarica"
    },
    {
        "grad": "Žagubica",
        "opstina": "Jošanica",
        "lokacija": "Jošanica"
    },
    {
        "grad": "Žagubica",
        "opstina": "Krepoljin",
        "lokacija": "Krepoljin"
    },
    {
        "grad": "Žagubica",
        "opstina": "Krupaja",
        "lokacija": "Krupaja"
    },
    {
        "grad": "Žagubica",
        "opstina": "Laznica",
        "lokacija": "Laznica"
    },
    {
        "grad": "Žagubica",
        "opstina": "Lipe",
        "lokacija": "Lipe"
    },
    {
        "grad": "Žagubica",
        "opstina": "Medveđica",
        "lokacija": "Medveđica"
    },
    {
        "grad": "Žagubica",
        "opstina": "Milanovac",
        "lokacija": "Milanovac"
    },
    {
        "grad": "Žagubica",
        "opstina": "Milatovac",
        "lokacija": "Milatovac"
    },
    {
        "grad": "Žagubica",
        "opstina": "Osanica",
        "lokacija": "Osanica"
    },
    {
        "grad": "Žagubica",
        "opstina": "Ribare",
        "lokacija": "Ribare"
    },
    {
        "grad": "Žagubica",
        "opstina": "Selište",
        "lokacija": "Selište"
    },
    {
        "grad": "Žagubica",
        "opstina": "Sige",
        "lokacija": "Sige"
    },
    {
        "grad": "Žagubica",
        "opstina": "Suvi Do",
        "lokacija": "Suvi Do"
    },
    {
        "grad": "Žitište",
        "opstina": "Žitište",
        "lokacija": "Žitište"
    },
    {
        "grad": "Žitište",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Žitište",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Žitište",
        "opstina": "Banatski Dvor",
        "lokacija": "Banatski Dvor"
    },
    {
        "grad": "Žitište",
        "opstina": "Banatsko Višnjićevo",
        "lokacija": "Banatsko Višnjićevo"
    },
    {
        "grad": "Žitište",
        "opstina": "Banatsko Karađorđevo",
        "lokacija": "Banatsko Karađorđevo"
    },
    {
        "grad": "Žitište",
        "opstina": "Međa",
        "lokacija": "Međa"
    },
    {
        "grad": "Žitište",
        "opstina": "Novi Itebej",
        "lokacija": "Novi Itebej"
    },
    {
        "grad": "Žitište",
        "opstina": "Ravni Topolovac",
        "lokacija": "Ravni Topolovac"
    },
    {
        "grad": "Žitište",
        "opstina": "Srpski Itebej",
        "lokacija": "Srpski Itebej"
    },
    {
        "grad": "Žitište",
        "opstina": "Torak",
        "lokacija": "Torak"
    },
    {
        "grad": "Žitište",
        "opstina": "Torda",
        "lokacija": "Torda"
    },
    {
        "grad": "Žitište",
        "opstina": "Hetin",
        "lokacija": "Hetin"
    },
    {
        "grad": "Žitište",
        "opstina": "Čestereg",
        "lokacija": "Čestereg"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Žitorađa",
        "lokacija": "Žitorađa"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Asanovac",
        "lokacija": "Asanovac"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Badnjevac",
        "lokacija": "Badnjevac"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Vlahovo",
        "lokacija": "Vlahovo"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Voljčince",
        "lokacija": "Voljčince"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Glašince",
        "lokacija": "Glašince"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Gornje Crnatovo",
        "lokacija": "Gornje Crnatovo"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Gornji Drenovac",
        "lokacija": "Gornji Drenovac"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Grudaš",
        "lokacija": "Grudaš"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Debeli Lug",
        "lokacija": "Debeli Lug"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Donje Crnatovo",
        "lokacija": "Donje Crnatovo"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Donji Drenovac",
        "lokacija": "Donji Drenovac"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Držanovac",
        "lokacija": "Držanovac"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Dubovo",
        "lokacija": "Dubovo"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Đakus",
        "lokacija": "Đakus"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Zladovac",
        "lokacija": "Zladovac"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Izvor",
        "lokacija": "Izvor"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Jasenica",
        "lokacija": "Jasenica"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Kare",
        "lokacija": "Kare"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Konjarnik",
        "lokacija": "Konjarnik"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Lukomir",
        "lokacija": "Lukomir"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Novo Momčilovo",
        "lokacija": "Novo Momčilovo"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Pejkovac",
        "lokacija": "Pejkovac"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Podina",
        "lokacija": "Podina"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Rečica",
        "lokacija": "Rečica"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Samarinovac",
        "lokacija": "Samarinovac"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Stara Božurna",
        "lokacija": "Stara Božurna"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Staro Momčilovo",
        "lokacija": "Staro Momčilovo"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Studenac",
        "lokacija": "Studenac"
    },
    {
        "grad": "Žitorađa",
        "opstina": "Toponica",
        "lokacija": "Toponica"
    },
    {
        "grad": "Zaječar",
        "opstina": "Zaječar",
        "lokacija": "Zaječar"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Beli Breg"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Višnjar"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Vlačić"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Vlaška Mala"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Gnjilak"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Gojkova Jaruga"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "gradež"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Dva brata"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Živinarnik"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Zvezdanska Krivina"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Ključ"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Kotlujevac"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Kraljevica"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Lubničko Brdo"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Muljak"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Plaža"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Oskoruša"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Pazarište"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Pikovo Imanje"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Pišura"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Podliv"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Popova Plaža"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Selište"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Timok"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Cerak"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Šljivarksi Put"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gradska lokacija",
        "lokacija": "Šljivarsko Brdo"
    },
    {
        "grad": "Zaječar",
        "opstina": "Borovac",
        "lokacija": "Borovac"
    },
    {
        "grad": "Zaječar",
        "opstina": "Brusnik",
        "lokacija": "Brusnik"
    },
    {
        "grad": "Zaječar",
        "opstina": "Velika Jasikova",
        "lokacija": "Velika Jasikova"
    },
    {
        "grad": "Zaječar",
        "opstina": "Veliki Izvor",
        "lokacija": "Veliki Izvor"
    },
    {
        "grad": "Zaječar",
        "opstina": "Veliki Jasenovac",
        "lokacija": "Veliki Jasenovac"
    },
    {
        "grad": "Zaječar",
        "opstina": "Vražogrnac",
        "lokacija": "Vražogrnac"
    },
    {
        "grad": "Zaječar",
        "opstina": "Vratarnica",
        "lokacija": "Vratarnica"
    },
    {
        "grad": "Zaječar",
        "opstina": "Vrbica",
        "lokacija": "Vrbica"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gamzigrad",
        "lokacija": "Gamzigrad"
    },
    {
        "grad": "Zaječar",
        "opstina": "Glogovica",
        "lokacija": "Glogovica"
    },
    {
        "grad": "Zaječar",
        "opstina": "Gornja Bela Reka",
        "lokacija": "Gornja Bela Reka"
    },
    {
        "grad": "Zaječar",
        "opstina": "gradovsko",
        "lokacija": "gradovsko"
    },
    {
        "grad": "Zaječar",
        "opstina": "Grlište",
        "lokacija": "Grlište"
    },
    {
        "grad": "Zaječar",
        "opstina": "Grljan",
        "lokacija": "Grljan"
    },
    {
        "grad": "Zaječar",
        "opstina": "Dubočane",
        "lokacija": "Dubočane"
    },
    {
        "grad": "Zaječar",
        "opstina": "Zagrađe",
        "lokacija": "Zagrađe"
    },
    {
        "grad": "Zaječar",
        "opstina": "Zvezdan",
        "lokacija": "Zvezdan"
    },
    {
        "grad": "Zaječar",
        "opstina": "Jelašnica",
        "lokacija": "Jelašnica"
    },
    {
        "grad": "Zaječar",
        "opstina": "Klenovac",
        "lokacija": "Klenovac"
    },
    {
        "grad": "Zaječar",
        "opstina": "Koprivnica",
        "lokacija": "Koprivnica"
    },
    {
        "grad": "Zaječar",
        "opstina": "Lasovo",
        "lokacija": "Lasovo"
    },
    {
        "grad": "Zaječar",
        "opstina": "Lenovac",
        "lokacija": "Lenovac"
    },
    {
        "grad": "Zaječar",
        "opstina": "Leskovac",
        "lokacija": "Leskovac"
    },
    {
        "grad": "Zaječar",
        "opstina": "Lubnica",
        "lokacija": "Lubnica"
    },
    {
        "grad": "Zaječar",
        "opstina": "Mala Jasikova",
        "lokacija": "Mala Jasikova"
    },
    {
        "grad": "Zaječar",
        "opstina": "Mali Izvor",
        "lokacija": "Mali Izvor"
    },
    {
        "grad": "Zaječar",
        "opstina": "Mali Jasenovac",
        "lokacija": "Mali Jasenovac"
    },
    {
        "grad": "Zaječar",
        "opstina": "Marinovac",
        "lokacija": "Marinovac"
    },
    {
        "grad": "Zaječar",
        "opstina": "Metriš",
        "lokacija": "Metriš"
    },
    {
        "grad": "Zaječar",
        "opstina": "Nikoličevo",
        "lokacija": "Nikoličevo"
    },
    {
        "grad": "Zaječar",
        "opstina": "Planinica",
        "lokacija": "Planinica"
    },
    {
        "grad": "Zaječar",
        "opstina": "Prlita",
        "lokacija": "Prlita"
    },
    {
        "grad": "Zaječar",
        "opstina": "Rgotina",
        "lokacija": "Rgotina"
    },
    {
        "grad": "Zaječar",
        "opstina": "Salaš",
        "lokacija": "Salaš"
    },
    {
        "grad": "Zaječar",
        "opstina": "Selačka",
        "lokacija": "Selačka"
    },
    {
        "grad": "Zaječar",
        "opstina": "Stara Planina",
        "lokacija": "Stara Planina"
    },
    {
        "grad": "Zaječar",
        "opstina": "Tabakovac",
        "lokacija": "Tabakovac"
    },
    {
        "grad": "Zaječar",
        "opstina": "Trnavac",
        "lokacija": "Trnavac"
    },
    {
        "grad": "Zaječar",
        "opstina": "Halovo",
        "lokacija": "Halovo"
    },
    {
        "grad": "Zaječar",
        "opstina": "Čokonjar",
        "lokacija": "Čokonjar"
    },
    {
        "grad": "Zaječar",
        "opstina": "Šipikovo",
        "lokacija": "Šipikovo"
    },
    {
        "grad": "Zaječar",
        "opstina": "Šljivar",
        "lokacija": "Šljivar"
    },
    {
        "grad": "Zvečan",
        "opstina": "Zvečan",
        "lokacija": "Zvečan"
    },
    {
        "grad": "Zvečan",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Zvečan",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Zvečan",
        "opstina": "Banov Do",
        "lokacija": "Banov Do"
    },
    {
        "grad": "Zvečan",
        "opstina": "Banjska",
        "lokacija": "Banjska"
    },
    {
        "grad": "Zvečan",
        "opstina": "Banjska Reka",
        "lokacija": "Banjska Reka"
    },
    {
        "grad": "Zvečan",
        "opstina": "Banjski Suvi Do",
        "lokacija": "Banjski Suvi Do"
    },
    {
        "grad": "Zvečan",
        "opstina": "Boljetin",
        "lokacija": "Boljetin"
    },
    {
        "grad": "Zvečan",
        "opstina": "Bresnica",
        "lokacija": "Bresnica"
    },
    {
        "grad": "Zvečan",
        "opstina": "Valač",
        "lokacija": "Valač"
    },
    {
        "grad": "Zvečan",
        "opstina": "Veliko Rudare",
        "lokacija": "Veliko Rudare"
    },
    {
        "grad": "Zvečan",
        "opstina": "Vilište",
        "lokacija": "Vilište"
    },
    {
        "grad": "Zvečan",
        "opstina": "Grabovac",
        "lokacija": "Grabovac"
    },
    {
        "grad": "Zvečan",
        "opstina": "Grižani",
        "lokacija": "Grižani"
    },
    {
        "grad": "Zvečan",
        "opstina": "Doljane",
        "lokacija": "Doljane"
    },
    {
        "grad": "Zvečan",
        "opstina": "Žaža",
        "lokacija": "Žaža"
    },
    {
        "grad": "Zvečan",
        "opstina": "Žerovnica",
        "lokacija": "Žerovnica"
    },
    {
        "grad": "Zvečan",
        "opstina": "Žitkovac",
        "lokacija": "Žitkovac"
    },
    {
        "grad": "Zvečan",
        "opstina": "Izvori",
        "lokacija": "Izvori"
    },
    {
        "grad": "Zvečan",
        "opstina": "Jankov Potok",
        "lokacija": "Jankov Potok"
    },
    {
        "grad": "Zvečan",
        "opstina": "Joševik",
        "lokacija": "Joševik"
    },
    {
        "grad": "Zvečan",
        "opstina": "Kamenica",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Zvečan",
        "opstina": "Korilje",
        "lokacija": "Korilje"
    },
    {
        "grad": "Zvečan",
        "opstina": "Kula",
        "lokacija": "Kula"
    },
    {
        "grad": "Zvečan",
        "opstina": "Lipa",
        "lokacija": "Lipa"
    },
    {
        "grad": "Zvečan",
        "opstina": "Lipovica",
        "lokacija": "Lipovica"
    },
    {
        "grad": "Zvečan",
        "opstina": "Lovac",
        "lokacija": "Lovac"
    },
    {
        "grad": "Zvečan",
        "opstina": "Lozište",
        "lokacija": "Lozište"
    },
    {
        "grad": "Zvečan",
        "opstina": "Lokva",
        "lokacija": "Lokva"
    },
    {
        "grad": "Zvečan",
        "opstina": "Mali Zvečan",
        "lokacija": "Mali Zvečan"
    },
    {
        "grad": "Zvečan",
        "opstina": "Malo Rudare",
        "lokacija": "Malo Rudare"
    },
    {
        "grad": "Zvečan",
        "opstina": "Matica",
        "lokacija": "Matica"
    },
    {
        "grad": "Zvečan",
        "opstina": "Meki Do",
        "lokacija": "Meki Do"
    },
    {
        "grad": "Zvečan",
        "opstina": "Oraovica",
        "lokacija": "Oraovica"
    },
    {
        "grad": "Zvečan",
        "opstina": "Rudine",
        "lokacija": "Rudine"
    },
    {
        "grad": "Zvečan",
        "opstina": "Sendo",
        "lokacija": "Sendo"
    },
    {
        "grad": "Zvečan",
        "opstina": "Srbovac",
        "lokacija": "Srbovac"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Zrenjanin",
        "lokacija": "Zrenjanin"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "4. Juli"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Bagljaš"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Berbersko Novo"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Berbersko Staro"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Budžak"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "gradulnica"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "gradulnica Guvno"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Dolja"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Dositej Obradović"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Duvanik"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Žitni Trg"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Zeleno Polje"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Lesnina"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Mala Amerika"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Mičkel"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Mužlja"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Mužljanska Kolonija"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Nova Kolonija"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Putnikovo"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Ruža Šulman"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Stari Bagljaš"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Čontika"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Šećerana"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Gradska lokacija",
        "lokacija": "Šumica"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Aradac",
        "lokacija": "Aradac"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Banatski Despotovac",
        "lokacija": "Banatski Despotovac"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Banja Rusanda",
        "lokacija": "Banja Rusanda"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Belo Blato",
        "lokacija": "Belo Blato"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Botoš",
        "lokacija": "Botoš"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Elemir",
        "lokacija": "Elemir"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Ečka",
        "lokacija": "Ečka"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Jankov Most",
        "lokacija": "Jankov Most"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Klek",
        "lokacija": "Klek"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Knićanin",
        "lokacija": "Knićanin"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Lazarevo",
        "lokacija": "Lazarevo"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Lukino Selo",
        "lokacija": "Lukino Selo"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Lukićevo",
        "lokacija": "Lukićevo"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Melenci",
        "lokacija": "Melenci"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Mihajlovo",
        "lokacija": "Mihajlovo"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Orlovat",
        "lokacija": "Orlovat"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Perlez",
        "lokacija": "Perlez"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Stajićevo",
        "lokacija": "Stajićevo"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Taraš",
        "lokacija": "Taraš"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Tomaševac",
        "lokacija": "Tomaševac"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Farkaždin",
        "lokacija": "Farkaždin"
    },
    {
        "grad": "Zrenjanin",
        "opstina": "Čenta",
        "lokacija": "Čenta"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Zubin Potok",
        "lokacija": "Zubin Potok"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Babiće",
        "lokacija": "Babiće"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Babudovica",
        "lokacija": "Babudovica"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Banja",
        "lokacija": "Banja"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Bojnoviće",
        "lokacija": "Bojnoviće"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Brnjak",
        "lokacija": "Brnjak"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Bube",
        "lokacija": "Bube"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Burlate",
        "lokacija": "Burlate"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Velika Kaludra",
        "lokacija": "Velika Kaludra"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Velji Breg",
        "lokacija": "Velji Breg"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Vitakovo",
        "lokacija": "Vitakovo"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Vojmisliće",
        "lokacija": "Vojmisliće"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Vrba",
        "lokacija": "Vrba"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Vukojeviće",
        "lokacija": "Vukojeviće"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Vukosavljeviće",
        "lokacija": "Vukosavljeviće"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Gazivode",
        "lokacija": "Gazivode"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Gornje Varage",
        "lokacija": "Gornje Varage"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Gornji Jasenovik",
        "lokacija": "Gornji Jasenovik"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Gornji Strmac",
        "lokacija": "Gornji Strmac"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Dobroševina",
        "lokacija": "Dobroševina"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Donje Varage",
        "lokacija": "Donje Varage"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Donji Jasenovik",
        "lokacija": "Donji Jasenovik"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Dragalica",
        "lokacija": "Dragalica"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Drainoviće",
        "lokacija": "Drainoviće"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Dren",
        "lokacija": "Dren"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Žarevi",
        "lokacija": "Žarevi"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Zagrađe",
        "lokacija": "Zagrađe"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Zagulje",
        "lokacija": "Zagulje"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Zečeviće",
        "lokacija": "Zečeviće"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Zupče",
        "lokacija": "Zupče"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Jabuka",
        "lokacija": "Jabuka"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Jagnjenica",
        "lokacija": "Jagnjenica"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Junake",
        "lokacija": "Junake"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Kijevce",
        "lokacija": "Kijevce"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Klečke",
        "lokacija": "Klečke"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Kobilja Glava",
        "lokacija": "Kobilja Glava"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Kovače",
        "lokacija": "Kovače"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Kozarevo",
        "lokacija": "Kozarevo"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Kopiloviće",
        "lokacija": "Kopiloviće"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Krligate",
        "lokacija": "Krligate"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Ledenik",
        "lokacija": "Ledenik"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Lučka Reka",
        "lokacija": "Lučka Reka"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Mala Kaludra",
        "lokacija": "Mala Kaludra"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Međeđi Potok",
        "lokacija": "Međeđi Potok"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Oklace",
        "lokacija": "Oklace"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Padine",
        "lokacija": "Padine"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Paruci",
        "lokacija": "Paruci"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Prevlak",
        "lokacija": "Prevlak"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Prelez",
        "lokacija": "Prelez"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Preseka",
        "lokacija": "Preseka"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Pridvorica",
        "lokacija": "Pridvorica"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Rančiće",
        "lokacija": "Rančiće"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Rezala",
        "lokacija": "Rezala"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Rujište",
        "lokacija": "Rujište"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Tušiće",
        "lokacija": "Tušiće"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Ugljare",
        "lokacija": "Ugljare"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Crepulja",
        "lokacija": "Crepulja"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Čabra",
        "lokacija": "Čabra"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Čečevo",
        "lokacija": "Čečevo"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Češanoviće",
        "lokacija": "Češanoviće"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Čitluk",
        "lokacija": "Čitluk"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Šipovo",
        "lokacija": "Šipovo"
    },
    {
        "grad": "Zubin Potok",
        "opstina": "Štuoce",
        "lokacija": "Štuoce"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Ivanjica",
        "lokacija": "Ivanjica"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Gradska lokacija",
        "lokacija": "Buk"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Gradska lokacija",
        "lokacija": "Kušićan"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Gradska lokacija",
        "lokacija": "Lučka Reka"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Gradska lokacija",
        "lokacija": "Mrkočevac"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Bedina Varoš",
        "lokacija": "Bedina Varoš"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Bratljevo",
        "lokacija": "Bratljevo"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Brezova",
        "lokacija": "Brezova"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Brusnik",
        "lokacija": "Brusnik"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Budoželja",
        "lokacija": "Budoželja"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Bukovica",
        "lokacija": "Bukovica"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Vasiljevići",
        "lokacija": "Vasiljevići"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Vionica",
        "lokacija": "Vionica"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Vrmbaje",
        "lokacija": "Vrmbaje"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Vučak",
        "lokacija": "Vučak"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Gleđica",
        "lokacija": "Gleđica"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Golija",
        "lokacija": "Golija"
    },
    {
        "grad": "Ivanjica",
        "opstina": "gradac",
        "lokacija": "gradac"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Dajići",
        "lokacija": "Dajići"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Devići",
        "lokacija": "Devići"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Deretin",
        "lokacija": "Deretin"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Dobri Do",
        "lokacija": "Dobri Do"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Dubrava",
        "lokacija": "Dubrava"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Erčege",
        "lokacija": "Erčege"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Javorska Ravna Gora",
        "lokacija": "Javorska Ravna Gora"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Katići",
        "lokacija": "Katići"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Klekova",
        "lokacija": "Klekova"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Kovilje",
        "lokacija": "Kovilje"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Komadine",
        "lokacija": "Komadine"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Koritnik",
        "lokacija": "Koritnik"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Kosovica",
        "lokacija": "Kosovica"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Kumanica",
        "lokacija": "Kumanica"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Kušići",
        "lokacija": "Kušići"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Lisa",
        "lokacija": "Lisa"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Luke",
        "lokacija": "Luke"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Mana",
        "lokacija": "Mana"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Maskova",
        "lokacija": "Maskova"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Medovine",
        "lokacija": "Medovine"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Međurečje",
        "lokacija": "Međurečje"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Močioci",
        "lokacija": "Močioci"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Opaljenik",
        "lokacija": "Opaljenik"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Osonica",
        "lokacija": "Osonica"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Preseka",
        "lokacija": "Preseka"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Prilike",
        "lokacija": "Prilike"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Ravna Gora",
        "lokacija": "Ravna Gora"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Radaljevo",
        "lokacija": "Radaljevo"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Rovine",
        "lokacija": "Rovine"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Rokci",
        "lokacija": "Rokci"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Sveštica",
        "lokacija": "Sveštica"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Sivčina",
        "lokacija": "Sivčina"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Smiljevac",
        "lokacija": "Smiljevac"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Čečina",
        "lokacija": "Čečina"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Šarenik",
        "lokacija": "Šarenik"
    },
    {
        "grad": "Ivanjica",
        "opstina": "Šume",
        "lokacija": "Šume"
    },
    {
        "grad": "Inđija",
        "opstina": "Inđija",
        "lokacija": "Inđija"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Aleksandrija"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Atina"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Blok 43"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Blok 44"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Blok 63"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Boška Buha"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Jugoistočna Radna Zona"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Moskva"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Naselje"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Severoistočna Radna Zona"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Srpski Kraj"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Šangaj"
    },
    {
        "grad": "Inđija",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Inđija",
        "opstina": "Beška",
        "lokacija": "Beška"
    },
    {
        "grad": "Inđija",
        "opstina": "Jarkovci",
        "lokacija": "Jarkovci"
    },
    {
        "grad": "Inđija",
        "opstina": "Krčedin",
        "lokacija": "Krčedin"
    },
    {
        "grad": "Inđija",
        "opstina": "Ljukovo",
        "lokacija": "Ljukovo"
    },
    {
        "grad": "Inđija",
        "opstina": "Maradik",
        "lokacija": "Maradik"
    },
    {
        "grad": "Inđija",
        "opstina": "Novi Karlovci",
        "lokacija": "Novi Karlovci"
    },
    {
        "grad": "Inđija",
        "opstina": "Novi Slankamen",
        "lokacija": "Novi Slankamen"
    },
    {
        "grad": "Inđija",
        "opstina": "Slankamenačka Banja",
        "lokacija": "Slankamenačka Banja"
    },
    {
        "grad": "Inđija",
        "opstina": "Slankamenački Vinogradi",
        "lokacija": "Slankamenački Vinogradi"
    },
    {
        "grad": "Inđija",
        "opstina": "Stari Slankamen",
        "lokacija": "Stari Slankamen"
    },
    {
        "grad": "Inđija",
        "opstina": "Čortanovci",
        "lokacija": "Čortanovci"
    },
    {
        "grad": "Irig",
        "opstina": "Irig",
        "lokacija": "Irig"
    },
    {
        "grad": "Irig",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Irig",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Irig",
        "opstina": "Velika Remeta",
        "lokacija": "Velika Remeta"
    },
    {
        "grad": "Irig",
        "opstina": "Vrdnik",
        "lokacija": "Vrdnik"
    },
    {
        "grad": "Irig",
        "opstina": "Vrdnik Banja",
        "lokacija": "Vrdnik Banja"
    },
    {
        "grad": "Irig",
        "opstina": "Grgeteg",
        "lokacija": "Grgeteg"
    },
    {
        "grad": "Irig",
        "opstina": "Dobrodol",
        "lokacija": "Dobrodol"
    },
    {
        "grad": "Irig",
        "opstina": "Jazak",
        "lokacija": "Jazak"
    },
    {
        "grad": "Irig",
        "opstina": "Krstašice",
        "lokacija": "Krstašice"
    },
    {
        "grad": "Irig",
        "opstina": "Krušedol Prnjavor",
        "lokacija": "Krušedol Prnjavor"
    },
    {
        "grad": "Irig",
        "opstina": "Krušedol Selo",
        "lokacija": "Krušedol Selo"
    },
    {
        "grad": "Irig",
        "opstina": "Mala Remeta",
        "lokacija": "Mala Remeta"
    },
    {
        "grad": "Irig",
        "opstina": "Neradin",
        "lokacija": "Neradin"
    },
    {
        "grad": "Irig",
        "opstina": "Rivica",
        "lokacija": "Rivica"
    },
    {
        "grad": "Irig",
        "opstina": "Šatrinci",
        "lokacija": "Šatrinci"
    },
    {
        "grad": "Istok",
        "opstina": "Istok",
        "lokacija": "Istok"
    },
    {
        "grad": "Istok",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Istok",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Istok",
        "opstina": "Banja",
        "lokacija": "Banja"
    },
    {
        "grad": "Istok",
        "opstina": "Banjica",
        "lokacija": "Banjica"
    },
    {
        "grad": "Istok",
        "opstina": "Begov Lukavac",
        "lokacija": "Begov Lukavac"
    },
    {
        "grad": "Istok",
        "opstina": "Belica",
        "lokacija": "Belica"
    },
    {
        "grad": "Istok",
        "opstina": "Belo Polje",
        "lokacija": "Belo Polje"
    },
    {
        "grad": "Istok",
        "opstina": "Verić",
        "lokacija": "Verić"
    },
    {
        "grad": "Istok",
        "opstina": "Vrelo",
        "lokacija": "Vrelo"
    },
    {
        "grad": "Istok",
        "opstina": "Dobruša",
        "lokacija": "Dobruša"
    },
    {
        "grad": "Istok",
        "opstina": "Donji Istok",
        "lokacija": "Donji Istok"
    },
    {
        "grad": "Istok",
        "opstina": "Dragoljevac",
        "lokacija": "Dragoljevac"
    },
    {
        "grad": "Istok",
        "opstina": "Drenje",
        "lokacija": "Drenje"
    },
    {
        "grad": "Istok",
        "opstina": "Dubrava",
        "lokacija": "Dubrava"
    },
    {
        "grad": "Istok",
        "opstina": "Đurakovac",
        "lokacija": "Đurakovac"
    },
    {
        "grad": "Istok",
        "opstina": "Žakovo",
        "lokacija": "Žakovo"
    },
    {
        "grad": "Istok",
        "opstina": "Žač",
        "lokacija": "Žač"
    },
    {
        "grad": "Istok",
        "opstina": "Zablaće",
        "lokacija": "Zablaće"
    },
    {
        "grad": "Istok",
        "opstina": "Kaličane",
        "lokacija": "Kaličane"
    },
    {
        "grad": "Istok",
        "opstina": "Kašica",
        "lokacija": "Kašica"
    },
    {
        "grad": "Istok",
        "opstina": "Kovrage",
        "lokacija": "Kovrage"
    },
    {
        "grad": "Istok",
        "opstina": "Koš",
        "lokacija": "Koš"
    },
    {
        "grad": "Istok",
        "opstina": "Krnjina",
        "lokacija": "Krnjina"
    },
    {
        "grad": "Istok",
        "opstina": "Lugovo",
        "lokacija": "Lugovo"
    },
    {
        "grad": "Istok",
        "opstina": "Ljubovo",
        "lokacija": "Ljubovo"
    },
    {
        "grad": "Istok",
        "opstina": "Ljubožda",
        "lokacija": "Ljubožda"
    },
    {
        "grad": "Istok",
        "opstina": "Malo Dubovo",
        "lokacija": "Malo Dubovo"
    },
    {
        "grad": "Istok",
        "opstina": "Mojstir",
        "lokacija": "Mojstir"
    },
    {
        "grad": "Istok",
        "opstina": "Muževine",
        "lokacija": "Muževine"
    },
    {
        "grad": "Istok",
        "opstina": "Novi Verić",
        "lokacija": "Novi Verić"
    },
    {
        "grad": "Istok",
        "opstina": "Orno Brdo",
        "lokacija": "Orno Brdo"
    },
    {
        "grad": "Istok",
        "opstina": "Osojane",
        "lokacija": "Osojane"
    },
    {
        "grad": "Istok",
        "opstina": "Poljane",
        "lokacija": "Poljane"
    },
    {
        "grad": "Istok",
        "opstina": "Prekale",
        "lokacija": "Prekale"
    },
    {
        "grad": "Istok",
        "opstina": "Prigoda",
        "lokacija": "Prigoda"
    },
    {
        "grad": "Istok",
        "opstina": "Rakoš",
        "lokacija": "Rakoš"
    },
    {
        "grad": "Istok",
        "opstina": "Sinaje",
        "lokacija": "Sinaje"
    },
    {
        "grad": "Istok",
        "opstina": "Srbobran",
        "lokacija": "Srbobran"
    },
    {
        "grad": "Istok",
        "opstina": "Starodvorane",
        "lokacija": "Starodvorane"
    },
    {
        "grad": "Istok",
        "opstina": "Studenica",
        "lokacija": "Studenica"
    },
    {
        "grad": "Istok",
        "opstina": "Suvi Lukavac",
        "lokacija": "Suvi Lukavac"
    },
    {
        "grad": "Istok",
        "opstina": "Suvo Grlo",
        "lokacija": "Suvo Grlo"
    },
    {
        "grad": "Istok",
        "opstina": "Sušica",
        "lokacija": "Sušica"
    },
    {
        "grad": "Istok",
        "opstina": "Tomance",
        "lokacija": "Tomance"
    },
    {
        "grad": "Istok",
        "opstina": "Trbuhovac",
        "lokacija": "Trbuhovac"
    },
    {
        "grad": "Istok",
        "opstina": "Tučep",
        "lokacija": "Tučep"
    },
    {
        "grad": "Istok",
        "opstina": "Ukča",
        "lokacija": "Ukča"
    },
    {
        "grad": "Istok",
        "opstina": "Crkolez",
        "lokacija": "Crkolez"
    },
    {
        "grad": "Istok",
        "opstina": "Crni Lug",
        "lokacija": "Crni Lug"
    },
    {
        "grad": "Istok",
        "opstina": "Crnce",
        "lokacija": "Crnce"
    },
    {
        "grad": "Istok",
        "opstina": "Šaljinovica",
        "lokacija": "Šaljinovica"
    },
    {
        "grad": "Jagodina",
        "opstina": "Jagodina",
        "lokacija": "Jagodina"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Aqua Park"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Budžino Brdo"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Vašarište"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "gradski Stadion"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Dimitrija Tucovića"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Đurđevo Brdo"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Kajsijar"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Kolonija"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Kupusara"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Levač"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Lipar"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Železnički Most"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Pijaca"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Pivara"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Ribarski Put"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Rusko Groblje"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Sarina Međa"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Svetozarevo"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Solaris"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Strelište"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Tabane"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Trnava"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gradska lokacija",
        "lokacija": "Tavrića Obori"
    },
    {
        "grad": "Jagodina",
        "opstina": "Bagrdan",
        "lokacija": "Bagrdan"
    },
    {
        "grad": "Jagodina",
        "opstina": "Belica",
        "lokacija": "Belica"
    },
    {
        "grad": "Jagodina",
        "opstina": "Bresje",
        "lokacija": "Bresje"
    },
    {
        "grad": "Jagodina",
        "opstina": "Bukovče",
        "lokacija": "Bukovče"
    },
    {
        "grad": "Jagodina",
        "opstina": "Bunar",
        "lokacija": "Bunar"
    },
    {
        "grad": "Jagodina",
        "opstina": "Vinorača",
        "lokacija": "Vinorača"
    },
    {
        "grad": "Jagodina",
        "opstina": "Voljavče",
        "lokacija": "Voljavče"
    },
    {
        "grad": "Jagodina",
        "opstina": "Vranovac",
        "lokacija": "Vranovac"
    },
    {
        "grad": "Jagodina",
        "opstina": "Vrba",
        "lokacija": "Vrba"
    },
    {
        "grad": "Jagodina",
        "opstina": "Glavinci",
        "lokacija": "Glavinci"
    },
    {
        "grad": "Jagodina",
        "opstina": "Glogovac",
        "lokacija": "Glogovac"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gornje Štiplje",
        "lokacija": "Gornje Štiplje"
    },
    {
        "grad": "Jagodina",
        "opstina": "Gornji Račnik",
        "lokacija": "Gornji Račnik"
    },
    {
        "grad": "Jagodina",
        "opstina": "Deonica",
        "lokacija": "Deonica"
    },
    {
        "grad": "Jagodina",
        "opstina": "Dobra Voda",
        "lokacija": "Dobra Voda"
    },
    {
        "grad": "Jagodina",
        "opstina": "Donje Štiplje",
        "lokacija": "Donje Štiplje"
    },
    {
        "grad": "Jagodina",
        "opstina": "Donji Račnik",
        "lokacija": "Donji Račnik"
    },
    {
        "grad": "Jagodina",
        "opstina": "Dragocvet",
        "lokacija": "Dragocvet"
    },
    {
        "grad": "Jagodina",
        "opstina": "Dragoševac",
        "lokacija": "Dragoševac"
    },
    {
        "grad": "Jagodina",
        "opstina": "Dražmirovac",
        "lokacija": "Dražmirovac"
    },
    {
        "grad": "Jagodina",
        "opstina": "Duboka",
        "lokacija": "Duboka"
    },
    {
        "grad": "Jagodina",
        "opstina": "Ivkovački Prnjavor",
        "lokacija": "Ivkovački Prnjavor"
    },
    {
        "grad": "Jagodina",
        "opstina": "Jošanički Prnjavor",
        "lokacija": "Jošanički Prnjavor"
    },
    {
        "grad": "Jagodina",
        "opstina": "Kalenovac",
        "lokacija": "Kalenovac"
    },
    {
        "grad": "Jagodina",
        "opstina": "Kovačevac",
        "lokacija": "Kovačevac"
    },
    {
        "grad": "Jagodina",
        "opstina": "Kolare",
        "lokacija": "Kolare"
    },
    {
        "grad": "Jagodina",
        "opstina": "Končarevo",
        "lokacija": "Končarevo"
    },
    {
        "grad": "Jagodina",
        "opstina": "Kočino Selo",
        "lokacija": "Kočino Selo"
    },
    {
        "grad": "Jagodina",
        "opstina": "Lovci",
        "lokacija": "Lovci"
    },
    {
        "grad": "Jagodina",
        "opstina": "Lozovik",
        "lokacija": "Lozovik"
    },
    {
        "grad": "Jagodina",
        "opstina": "Lukar",
        "lokacija": "Lukar"
    },
    {
        "grad": "Jagodina",
        "opstina": "Majur",
        "lokacija": "Majur"
    },
    {
        "grad": "Jagodina",
        "opstina": "Mali Popović",
        "lokacija": "Mali Popović"
    },
    {
        "grad": "Jagodina",
        "opstina": "Medojevac",
        "lokacija": "Medojevac"
    },
    {
        "grad": "Jagodina",
        "opstina": "Međureč",
        "lokacija": "Međureč"
    },
    {
        "grad": "Jagodina",
        "opstina": "Miloševo",
        "lokacija": "Miloševo"
    },
    {
        "grad": "Jagodina",
        "opstina": "Mišević",
        "lokacija": "Mišević"
    },
    {
        "grad": "Jagodina",
        "opstina": "Novo Lanište",
        "lokacija": "Novo Lanište"
    },
    {
        "grad": "Jagodina",
        "opstina": "Rajkinac",
        "lokacija": "Rajkinac"
    },
    {
        "grad": "Jagodina",
        "opstina": "Rakitovo",
        "lokacija": "Rakitovo"
    },
    {
        "grad": "Jagodina",
        "opstina": "Ribare",
        "lokacija": "Ribare"
    },
    {
        "grad": "Jagodina",
        "opstina": "Ribnik",
        "lokacija": "Ribnik"
    },
    {
        "grad": "Jagodina",
        "opstina": "Siokovac",
        "lokacija": "Siokovac"
    },
    {
        "grad": "Jagodina",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Jagodina",
        "opstina": "Staro Lanište",
        "lokacija": "Staro Lanište"
    },
    {
        "grad": "Jagodina",
        "opstina": "Staro Selo",
        "lokacija": "Staro Selo"
    },
    {
        "grad": "Jagodina",
        "opstina": "Strižilo",
        "lokacija": "Strižilo"
    },
    {
        "grad": "Jagodina",
        "opstina": "Topola",
        "lokacija": "Topola"
    },
    {
        "grad": "Jagodina",
        "opstina": "Crnče",
        "lokacija": "Crnče"
    },
    {
        "grad": "Jagodina",
        "opstina": "Šantarovac",
        "lokacija": "Šantarovac"
    },
    {
        "grad": "Jagodina",
        "opstina": "Šuljkovac",
        "lokacija": "Šuljkovac"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Kanjiža",
        "lokacija": "Kanjiža"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Gradska lokacija",
        "lokacija": "Banja Kanjiža"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Adorjan",
        "lokacija": "Adorjan"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Velebit",
        "lokacija": "Velebit"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Doline",
        "lokacija": "Doline"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Zimonić",
        "lokacija": "Zimonjić"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Male Pijace",
        "lokacija": "Male Pijace"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Mali Pesak",
        "lokacija": "Mali Pesak"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Martonoš",
        "lokacija": "Martonoš"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Orom",
        "lokacija": "Orom"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Totovo Selo",
        "lokacija": "Totovo Selo"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Trešnjevac",
        "lokacija": "Trešnjevac"
    },
    {
        "grad": "Kanjiža",
        "opstina": "Horgoš",
        "lokacija": "Horgoš"
    },
    {
        "grad": "Kačanik",
        "opstina": "Kačanik",
        "lokacija": "Kačanik"
    },
    {
        "grad": "Kačanik",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kačanik",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kačanik",
        "opstina": "Banjica",
        "lokacija": "Banjica"
    },
    {
        "grad": "Kačanik",
        "opstina": "Belograce",
        "lokacija": "Belograce"
    },
    {
        "grad": "Kačanik",
        "opstina": "Bičevac",
        "lokacija": "Bičevac"
    },
    {
        "grad": "Kačanik",
        "opstina": "Bob",
        "lokacija": "Bob"
    },
    {
        "grad": "Kačanik",
        "opstina": "Vata",
        "lokacija": "Vata"
    },
    {
        "grad": "Kačanik",
        "opstina": "Vrtolnica",
        "lokacija": "Vrtolnica"
    },
    {
        "grad": "Kačanik",
        "opstina": "Gabrica",
        "lokacija": "Gabrica"
    },
    {
        "grad": "Kačanik",
        "opstina": "Gajre",
        "lokacija": "Gajre"
    },
    {
        "grad": "Kačanik",
        "opstina": "Globočica",
        "lokacija": "Globočica"
    },
    {
        "grad": "Kačanik",
        "opstina": "Gorance",
        "lokacija": "Gorance"
    },
    {
        "grad": "Kačanik",
        "opstina": "Gornja Grlica",
        "lokacija": "Gornja Grlica"
    },
    {
        "grad": "Kačanik",
        "opstina": "Dimce",
        "lokacija": "Dimce"
    },
    {
        "grad": "Kačanik",
        "opstina": "Doganović",
        "lokacija": "Doganović"
    },
    {
        "grad": "Kačanik",
        "opstina": "Drenova Glava",
        "lokacija": "Drenova Glava"
    },
    {
        "grad": "Kačanik",
        "opstina": "Drobnjak",
        "lokacija": "Drobnjak"
    },
    {
        "grad": "Kačanik",
        "opstina": "Dubrava",
        "lokacija": "Dubrava"
    },
    {
        "grad": "Kačanik",
        "opstina": "Dura",
        "lokacija": "Dura"
    },
    {
        "grad": "Kačanik",
        "opstina": "Đeneral Janković",
        "lokacija": "Đeneral Janković"
    },
    {
        "grad": "Kačanik",
        "opstina": "Đurđev Dol",
        "lokacija": "Đurđev Dol"
    },
    {
        "grad": "Kačanik",
        "opstina": "Eleza",
        "lokacija": "Eleza"
    },
    {
        "grad": "Kačanik",
        "opstina": "Ivaja",
        "lokacija": "Ivaja"
    },
    {
        "grad": "Kačanik",
        "opstina": "Kovačevac",
        "lokacija": "Kovačevac"
    },
    {
        "grad": "Kačanik",
        "opstina": "Korbulić",
        "lokacija": "Korbulić"
    },
    {
        "grad": "Kačanik",
        "opstina": "Kotlina",
        "lokacija": "Kotlina"
    },
    {
        "grad": "Kačanik",
        "opstina": "Krivenik",
        "lokacija": "Krivenik"
    },
    {
        "grad": "Kačanik",
        "opstina": "Lanište",
        "lokacija": "Lanište"
    },
    {
        "grad": "Kačanik",
        "opstina": "Nećavce",
        "lokacija": "Nećavce"
    },
    {
        "grad": "Kačanik",
        "opstina": "Nika",
        "lokacija": "Nika"
    },
    {
        "grad": "Kačanik",
        "opstina": "Nikovce",
        "lokacija": "Nikovce"
    },
    {
        "grad": "Kačanik",
        "opstina": "Palivodenica",
        "lokacija": "Palivodenica"
    },
    {
        "grad": "Kačanik",
        "opstina": "Pustenik",
        "lokacija": "Pustenik"
    },
    {
        "grad": "Kačanik",
        "opstina": "Režance",
        "lokacija": "Režance"
    },
    {
        "grad": "Kačanik",
        "opstina": "Reka",
        "lokacija": "Reka"
    },
    {
        "grad": "Kačanik",
        "opstina": "Runjevo",
        "lokacija": "Runjevo"
    },
    {
        "grad": "Kačanik",
        "opstina": "Semanje",
        "lokacija": "Semanje"
    },
    {
        "grad": "Kačanik",
        "opstina": "Sečište",
        "lokacija": "Sečište"
    },
    {
        "grad": "Kačanik",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Kačanik",
        "opstina": "Sopotnica",
        "lokacija": "Sopotnica"
    },
    {
        "grad": "Kačanik",
        "opstina": "Stagovo",
        "lokacija": "Stagovo"
    },
    {
        "grad": "Kačanik",
        "opstina": "Stari Kačanik",
        "lokacija": "Stari Kačanik"
    },
    {
        "grad": "Kačanik",
        "opstina": "Straža",
        "lokacija": "Straža"
    },
    {
        "grad": "Kikinda",
        "opstina": "Kikinda",
        "lokacija": "Kikinda"
    },
    {
        "grad": "Kikinda",
        "opstina": "Gradska lokacija",
        "lokacija": "ABC Naselje"
    },
    {
        "grad": "Kikinda",
        "opstina": "Gradska lokacija",
        "lokacija": "Blok 35"
    },
    {
        "grad": "Kikinda",
        "opstina": "Gradska lokacija",
        "lokacija": "Blok 36"
    },
    {
        "grad": "Kikinda",
        "opstina": "Gradska lokacija",
        "lokacija": "Železnička stanica"
    },
    {
        "grad": "Kikinda",
        "opstina": "Gradska lokacija",
        "lokacija": "Mikronaselje"
    },
    {
        "grad": "Kikinda",
        "opstina": "Gradska lokacija",
        "lokacija": "Pristanište"
    },
    {
        "grad": "Kikinda",
        "opstina": "Gradska lokacija",
        "lokacija": "Strelište"
    },
    {
        "grad": "Kikinda",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kikinda",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kikinda",
        "opstina": "Banatska Topola",
        "lokacija": "Banatska Topola"
    },
    {
        "grad": "Kikinda",
        "opstina": "Banatsko Veliko Selo",
        "lokacija": "Banatsko Veliko Selo"
    },
    {
        "grad": "Kikinda",
        "opstina": "Bašaid",
        "lokacija": "Bašaid"
    },
    {
        "grad": "Kikinda",
        "opstina": "Iđoš",
        "lokacija": "Iđoš"
    },
    {
        "grad": "Kikinda",
        "opstina": "Mokrin",
        "lokacija": "Mokrin"
    },
    {
        "grad": "Kikinda",
        "opstina": "Nakovo",
        "lokacija": "Nakovo"
    },
    {
        "grad": "Kikinda",
        "opstina": "Novi Kozarci",
        "lokacija": "Novi Kozarci"
    },
    {
        "grad": "Kikinda",
        "opstina": "Rusko Selo",
        "lokacija": "Rusko Selo"
    },
    {
        "grad": "Kikinda",
        "opstina": "Sajan",
        "lokacija": "Sajan"
    },
    {
        "grad": "Kladovo",
        "opstina": "Kladovo",
        "lokacija": "Kladovo"
    },
    {
        "grad": "Kladovo",
        "opstina": "Gradska lokacija",
        "lokacija": "Dunav"
    },
    {
        "grad": "Kladovo",
        "opstina": "Gradska lokacija",
        "lokacija": "Pemci"
    },
    {
        "grad": "Kladovo",
        "opstina": "Gradska lokacija",
        "lokacija": "Pesak"
    },
    {
        "grad": "Kladovo",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kladovo",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kladovo",
        "opstina": "Brza Palanka",
        "lokacija": "Brza Palanka"
    },
    {
        "grad": "Kladovo",
        "opstina": "Vajuga",
        "lokacija": "Vajuga"
    },
    {
        "grad": "Kladovo",
        "opstina": "Velesnica",
        "lokacija": "Velesnica"
    },
    {
        "grad": "Kladovo",
        "opstina": "Velika Vrbica",
        "lokacija": "Velika Vrbica"
    },
    {
        "grad": "Kladovo",
        "opstina": "Velika Kamenica",
        "lokacija": "Velika Kamenica"
    },
    {
        "grad": "Kladovo",
        "opstina": "Grabovica",
        "lokacija": "Grabovica"
    },
    {
        "grad": "Kladovo",
        "opstina": "Davidovac",
        "lokacija": "Davidovac"
    },
    {
        "grad": "Kladovo",
        "opstina": "Kladušnica",
        "lokacija": "Kladušnica"
    },
    {
        "grad": "Kladovo",
        "opstina": "Korbovo",
        "lokacija": "Korbovo"
    },
    {
        "grad": "Kladovo",
        "opstina": "Kostol",
        "lokacija": "Kostol"
    },
    {
        "grad": "Kladovo",
        "opstina": "Kupuzište",
        "lokacija": "Kupuzište"
    },
    {
        "grad": "Kladovo",
        "opstina": "Ljubičevac",
        "lokacija": "Ljubičevac"
    },
    {
        "grad": "Kladovo",
        "opstina": "Mala Vrbica",
        "lokacija": "Mala Vrbica"
    },
    {
        "grad": "Kladovo",
        "opstina": "Manastirica",
        "lokacija": "Manastirica"
    },
    {
        "grad": "Kladovo",
        "opstina": "Milutinovac",
        "lokacija": "Milutinovac"
    },
    {
        "grad": "Kladovo",
        "opstina": "Novi Sip",
        "lokacija": "Novi Sip"
    },
    {
        "grad": "Kladovo",
        "opstina": "Petrovo Selo",
        "lokacija": "Petrovo Selo"
    },
    {
        "grad": "Kladovo",
        "opstina": "Podvrška",
        "lokacija": "Podvrška"
    },
    {
        "grad": "Kladovo",
        "opstina": "Reka",
        "lokacija": "Reka"
    },
    {
        "grad": "Kladovo",
        "opstina": "Rečica",
        "lokacija": "Rečica"
    },
    {
        "grad": "Kladovo",
        "opstina": "Rtkovo",
        "lokacija": "Rtkovo"
    },
    {
        "grad": "Kladovo",
        "opstina": "Stara Brza Palanka",
        "lokacija": "Stara Brza Palanka"
    },
    {
        "grad": "Kladovo",
        "opstina": "Tekija",
        "lokacija": "Tekija"
    },
    {
        "grad": "Klina",
        "opstina": "Klina",
        "lokacija": "Klina"
    },
    {
        "grad": "Klina",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Klina",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Klina",
        "opstina": "Balince",
        "lokacija": "Balince"
    },
    {
        "grad": "Klina",
        "opstina": "Berkovo",
        "lokacija": "Berkovo"
    },
    {
        "grad": "Klina",
        "opstina": "Biča",
        "lokacija": "Biča"
    },
    {
        "grad": "Klina",
        "opstina": "Bobovac",
        "lokacija": "Bobovac"
    },
    {
        "grad": "Klina",
        "opstina": "Bokšić",
        "lokacija": "Bokšić"
    },
    {
        "grad": "Klina",
        "opstina": "Budisavci",
        "lokacija": "Budisavci"
    },
    {
        "grad": "Klina",
        "opstina": "Veliki Đurđevik",
        "lokacija": "Veliki Đurđevik"
    },
    {
        "grad": "Klina",
        "opstina": "Veliko Kruševo",
        "lokacija": "Veliko Kruševo"
    },
    {
        "grad": "Klina",
        "opstina": "Vidanje",
        "lokacija": "Vidanje"
    },
    {
        "grad": "Klina",
        "opstina": "Vlaški Drenovac",
        "lokacija": "Vlaški Drenovac"
    },
    {
        "grad": "Klina",
        "opstina": "Volujak",
        "lokacija": "Volujak"
    },
    {
        "grad": "Klina",
        "opstina": "Vrmnica",
        "lokacija": "Vrmnica"
    },
    {
        "grad": "Klina",
        "opstina": "Golubovac",
        "lokacija": "Golubovac"
    },
    {
        "grad": "Klina",
        "opstina": "Gornji Petrič",
        "lokacija": "Gornji Petrič"
    },
    {
        "grad": "Klina",
        "opstina": "Grabanica",
        "lokacija": "Grabanica"
    },
    {
        "grad": "Klina",
        "opstina": "Grabac",
        "lokacija": "Grabac"
    },
    {
        "grad": "Klina",
        "opstina": "Grebnik",
        "lokacija": "Grebnik"
    },
    {
        "grad": "Klina",
        "opstina": "Deič",
        "lokacija": "Deič"
    },
    {
        "grad": "Klina",
        "opstina": "Dobra Voda",
        "lokacija": "Dobra Voda"
    },
    {
        "grad": "Klina",
        "opstina": "Dobri Dol",
        "lokacija": "Dobri Dol"
    },
    {
        "grad": "Klina",
        "opstina": "Dolac",
        "lokacija": "Dolac"
    },
    {
        "grad": "Klina",
        "opstina": "Dolovo",
        "lokacija": "Dolovo"
    },
    {
        "grad": "Klina",
        "opstina": "Donji Petrič",
        "lokacija": "Donji Petrič"
    },
    {
        "grad": "Klina",
        "opstina": "Drenovac",
        "lokacija": "Drenovac"
    },
    {
        "grad": "Klina",
        "opstina": "Drenovčić",
        "lokacija": "Drenovčić"
    },
    {
        "grad": "Klina",
        "opstina": "Drsnik",
        "lokacija": "Drsnik"
    },
    {
        "grad": "Klina",
        "opstina": "Dugonjive",
        "lokacija": "Dugonjive"
    },
    {
        "grad": "Klina",
        "opstina": "Duš",
        "lokacija": "Duš"
    },
    {
        "grad": "Klina",
        "opstina": "Dušević",
        "lokacija": "Dušević"
    },
    {
        "grad": "Klina",
        "opstina": "Zabrđe",
        "lokacija": "Zabrđe"
    },
    {
        "grad": "Klina",
        "opstina": "Zajmovo",
        "lokacija": "Zajmovo"
    },
    {
        "grad": "Klina",
        "opstina": "Zlokućane",
        "lokacija": "Zlokućane"
    },
    {
        "grad": "Klina",
        "opstina": "Iglarevo",
        "lokacija": "Iglarevo"
    },
    {
        "grad": "Klina",
        "opstina": "Jagoda",
        "lokacija": "Jagoda"
    },
    {
        "grad": "Klina",
        "opstina": "Jelovac",
        "lokacija": "Jelovac"
    },
    {
        "grad": "Klina",
        "opstina": "Jošanica",
        "lokacija": "Jošanica"
    },
    {
        "grad": "Klina",
        "opstina": "Kijevo",
        "lokacija": "Kijevo"
    },
    {
        "grad": "Klina",
        "opstina": "Klinavac",
        "lokacija": "Klinavac"
    },
    {
        "grad": "Klina",
        "opstina": "Kluz",
        "lokacija": "Kluz"
    },
    {
        "grad": "Klina",
        "opstina": "Krnjine",
        "lokacija": "Krnjince"
    },
    {
        "grad": "Klina",
        "opstina": "Leskovac",
        "lokacija": "Leskovac"
    },
    {
        "grad": "Klina",
        "opstina": "Lozica",
        "lokacija": "Lozica"
    },
    {
        "grad": "Klina",
        "opstina": "Mali Đurđevik",
        "lokacija": "Mali Đurđevik"
    },
    {
        "grad": "Klina",
        "opstina": "Malo Kruševo",
        "lokacija": "Malo Kruševo"
    },
    {
        "grad": "Klina",
        "opstina": "Mlečane",
        "lokacija": "Mlečane"
    },
    {
        "grad": "Klina",
        "opstina": "Naglavci",
        "lokacija": "Naglavci"
    },
    {
        "grad": "Klina",
        "opstina": "Pločice",
        "lokacija": "Pločice"
    },
    {
        "grad": "Klina",
        "opstina": "Pograđe",
        "lokacija": "Pograđe"
    },
    {
        "grad": "Klina",
        "opstina": "Prčevo",
        "lokacija": "Prčevo"
    },
    {
        "grad": "Klina",
        "opstina": "Radulovac",
        "lokacija": "Radulovac"
    },
    {
        "grad": "Klina",
        "opstina": "Renovac",
        "lokacija": "Renovac"
    },
    {
        "grad": "Klina",
        "opstina": "Resnik",
        "lokacija": "Resnik"
    },
    {
        "grad": "Klina",
        "opstina": "Rudice",
        "lokacija": "Rudice"
    },
    {
        "grad": "Klina",
        "opstina": "Svrhe",
        "lokacija": "Svrhe"
    },
    {
        "grad": "Klina",
        "opstina": "Sićevo",
        "lokacija": "Sićevo"
    },
    {
        "grad": "Klina",
        "opstina": "Skorošnik",
        "lokacija": "Skorošnik"
    },
    {
        "grad": "Klina",
        "opstina": "Stup",
        "lokacija": "Stup"
    },
    {
        "grad": "Klina",
        "opstina": "Cerovik",
        "lokacija": "Cerovik"
    },
    {
        "grad": "Klina",
        "opstina": "Crni Lug",
        "lokacija": "Crni Lug"
    },
    {
        "grad": "Klina",
        "opstina": "Čabić",
        "lokacija": "Čabić"
    },
    {
        "grad": "Klina",
        "opstina": "Českovo",
        "lokacija": "Českovo"
    },
    {
        "grad": "Klina",
        "opstina": "Čupevo",
        "lokacija": "Čupevo"
    },
    {
        "grad": "Klina",
        "opstina": "Štupelj",
        "lokacija": "Štupelj"
    },
    {
        "grad": "Knić",
        "opstina": "Knić",
        "lokacija": "Knić"
    },
    {
        "grad": "Knić",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Knić",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Knić",
        "opstina": "Bajčetina",
        "lokacija": "Bajčetina"
    },
    {
        "grad": "Knić",
        "opstina": "Baloslave",
        "lokacija": "Baloslave"
    },
    {
        "grad": "Knić",
        "opstina": "Bare",
        "lokacija": "Bare"
    },
    {
        "grad": "Knić",
        "opstina": "Bečevica",
        "lokacija": "Bečevica"
    },
    {
        "grad": "Knić",
        "opstina": "Borač",
        "lokacija": "Borač"
    },
    {
        "grad": "Knić",
        "opstina": "Brestovac",
        "lokacija": "Brestovac"
    },
    {
        "grad": "Knić",
        "opstina": "Brnjica",
        "lokacija": "Brnjica"
    },
    {
        "grad": "Knić",
        "opstina": "Bumbarevo brdo",
        "lokacija": "Bumbarevo brdo"
    },
    {
        "grad": "Knić",
        "opstina": "Vrbeta",
        "lokacija": "Vrbeta"
    },
    {
        "grad": "Knić",
        "opstina": "Vučkovica",
        "lokacija": "Vučkovica"
    },
    {
        "grad": "Knić",
        "opstina": "Grabovac",
        "lokacija": "Grabovac"
    },
    {
        "grad": "Knić",
        "opstina": "Grivac",
        "lokacija": "Grivac"
    },
    {
        "grad": "Knić",
        "opstina": "Gruža",
        "lokacija": "Gruža"
    },
    {
        "grad": "Knić",
        "opstina": "Gružansko Jezereo",
        "lokacija": "Gružansko Jezero"
    },
    {
        "grad": "Knić",
        "opstina": "Guberevac",
        "lokacija": "Guberevac"
    },
    {
        "grad": "Knić",
        "opstina": "Guncati",
        "lokacija": "Guncati"
    },
    {
        "grad": "Knić",
        "opstina": "Dragušica",
        "lokacija": "Dragušica"
    },
    {
        "grad": "Knić",
        "opstina": "Dubrava",
        "lokacija": "Dubrava"
    },
    {
        "grad": "Knić",
        "opstina": "Žunje",
        "lokacija": "Žunje"
    },
    {
        "grad": "Knić",
        "opstina": "Zabojnica",
        "lokacija": "Zabojnica"
    },
    {
        "grad": "Knić",
        "opstina": "Kikojevac",
        "lokacija": "Kikojevac"
    },
    {
        "grad": "Knić",
        "opstina": "Keneževac",
        "lokacija": "Keneževac"
    },
    {
        "grad": "Knić",
        "opstina": "Konjuša",
        "lokacija": "Konjuša"
    },
    {
        "grad": "Knić",
        "opstina": "Kusovac",
        "lokacija": "Kusovac"
    },
    {
        "grad": "Knić",
        "opstina": "Leskovac",
        "lokacija": "Leskovac"
    },
    {
        "grad": "Knić",
        "opstina": "Lipnica",
        "lokacija": "Lipnica"
    },
    {
        "grad": "Knić",
        "opstina": "Ljubić",
        "lokacija": "Ljubić"
    },
    {
        "grad": "Knić",
        "opstina": "Ljuljaci",
        "lokacija": "Ljuljaci"
    },
    {
        "grad": "Knić",
        "opstina": "Oplanić",
        "lokacija": "Oplanić"
    },
    {
        "grad": "Knić",
        "opstina": "Pajsijević",
        "lokacija": "Pajsijević"
    },
    {
        "grad": "Knić",
        "opstina": "Pretoke",
        "lokacija": "Pretoke"
    },
    {
        "grad": "Knić",
        "opstina": "Ravni Gaj",
        "lokacija": "Ravni Gaj"
    },
    {
        "grad": "Knić",
        "opstina": "Radmilović",
        "lokacija": "Radmilović"
    },
    {
        "grad": "Knić",
        "opstina": "Rašković",
        "lokacija": "Rašković"
    },
    {
        "grad": "Knić",
        "opstina": "Sumorovac",
        "lokacija": "Sumorovac"
    },
    {
        "grad": "Knić",
        "opstina": "Toponica",
        "lokacija": "Toponica"
    },
    {
        "grad": "Knić",
        "opstina": "Čestin",
        "lokacija": "Čestin"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Knjaževac",
        "lokacija": "Knjaževac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Gradska lokacija",
        "lokacija": "Glavičica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Gradska lokacija",
        "lokacija": "Jezava"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Gradska lokacija",
        "lokacija": "Mladost"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje 9. Brigade"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Gradska lokacija",
        "lokacija": "Sastavak"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Aldina Reka",
        "lokacija": "Aldina Reka"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Aldinac",
        "lokacija": "Aldinac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Babin Zub",
        "lokacija": "Babin Zub"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Balanovac",
        "lokacija": "Balanovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Balinac",
        "lokacija": "Balinac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Balta Berilovac",
        "lokacija": "Balta Berilovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Banjski Orešac",
        "lokacija": "Banjski Orešac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Beli Potok",
        "lokacija": "Beli Potok"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Berčinovac",
        "lokacija": "Berčinovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Božinovac",
        "lokacija": "Božinovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Bulinovac",
        "lokacija": "Bulinovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Bučje",
        "lokacija": "Bučje"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Valevac",
        "lokacija": "Valevac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Vasilj",
        "lokacija": "Vasilj"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Vidovac",
        "lokacija": "Vidovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Vina",
        "lokacija": "Vina"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Vitkovac",
        "lokacija": "Vitkovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Vlaško Polje",
        "lokacija": "Vlaško Polje"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Vrtovac",
        "lokacija": "Vrtovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Gabrovnica",
        "lokacija": "Gabrovnica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Glogovac",
        "lokacija": "Glogovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Gornja Kamenica",
        "lokacija": "Gornja Kamenica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Gornja Sokolovica",
        "lokacija": "Gornja Sokolovica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Gornje Zuniče",
        "lokacija": "Gornje Zuniče"
    },
    {
        "grad": "Knjaževac",
        "opstina": "gradište",
        "lokacija": "gradište"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Grezna",
        "lokacija": "Grezna"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Debelica",
        "lokacija": "Debelica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Dejanovac",
        "lokacija": "Dejanovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Donja Kamenica",
        "lokacija": "Donja Kamenica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Donja Sokolovica",
        "lokacija": "Donja Sokolovica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Donje Zuniče",
        "lokacija": "Donje Zuniče"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Drvnik",
        "lokacija": "Drvnik"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Drenovac",
        "lokacija": "Drenovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Drečinovac",
        "lokacija": "Drečinovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Žlne",
        "lokacija": "Žlne"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Žukovac",
        "lokacija": "Žukovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Zorunovac",
        "lokacija": "Zorunovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Zubetinac",
        "lokacija": "Zubetinac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Inovo",
        "lokacija": "Inovo"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Jakovac",
        "lokacija": "Jakovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Jalovik Izvor",
        "lokacija": "Jalovik Izvor"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Janja",
        "lokacija": "Janja"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Jelašnica",
        "lokacija": "Jelašnica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Kaličina",
        "lokacija": "Kaličina"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Kalna",
        "lokacija": "Kalna"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Kandalica",
        "lokacija": "Kandalica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Koželj",
        "lokacija": "Koželj"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Krenta",
        "lokacija": "Krenta"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Lepena",
        "lokacija": "Lepena"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Lokva",
        "lokacija": "Lokva"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Manjinac",
        "lokacija": "Manjinac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Miljkovac",
        "lokacija": "Miljkovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Minićevo",
        "lokacija": "Minićevo"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Mučibaba",
        "lokacija": "Mučibaba"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Novo Korito",
        "lokacija": "Novo Korito"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Orešac",
        "lokacija": "Orešac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Ošljane",
        "lokacija": "Ošljane"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Papratna",
        "lokacija": "Papratna"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Petruša",
        "lokacija": "Petruša"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Podvis",
        "lokacija": "Podvis"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Ponor",
        "lokacija": "Ponor"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Potrkanje",
        "lokacija": "Potrkanje"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Pričevac",
        "lokacija": "Pričevac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Ravna",
        "lokacija": "Ravna"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Ravno Bučje",
        "lokacija": "Ravno Bučje"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Radičevac",
        "lokacija": "Radičevac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Rgošte",
        "lokacija": "Rgošte"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Repušnica",
        "lokacija": "Repušnica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Svrljiška Topla",
        "lokacija": "Svrljiška Topla"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Skrobnica",
        "lokacija": "Skrobnica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Stanjinac",
        "lokacija": "Stanjinac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Staro Korito",
        "lokacija": "Staro Korito"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Stogazovac",
        "lokacija": "Stogazovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Tatrasnica",
        "lokacija": "Tatrasnica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Trgovište",
        "lokacija": "Trgovište"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Trnovac",
        "lokacija": "Trnovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Ćuštica",
        "lokacija": "Ćuštica"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Crvenje",
        "lokacija": "Crvenje"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Crni Vrh",
        "lokacija": "Crni Vrh"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Šarbanovac",
        "lokacija": "Šarbanovac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Šesti Gabar",
        "lokacija": "Šesti Gabar"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Štipina",
        "lokacija": "Štipina"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Štitarac",
        "lokacija": "Štitarac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Štrbac",
        "lokacija": "Štrbac"
    },
    {
        "grad": "Knjaževac",
        "opstina": "Šuman Topla",
        "lokacija": "Šuman Topla"
    },
    {
        "grad": "Kovačica",
        "opstina": "Kovačica",
        "lokacija": "Kovačica"
    },
    {
        "grad": "Kovačica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kovačica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kovačica",
        "opstina": "Debeljača",
        "lokacija": "Debeljača"
    },
    {
        "grad": "Kovačica",
        "opstina": "Idvor",
        "lokacija": "Idvor"
    },
    {
        "grad": "Kovačica",
        "opstina": "Padina",
        "lokacija": "Padina"
    },
    {
        "grad": "Kovačica",
        "opstina": "Putnikovo",
        "lokacija": "Putnikovo"
    },
    {
        "grad": "Kovačica",
        "opstina": "Samoš",
        "lokacija": "Samoš"
    },
    {
        "grad": "Kovačica",
        "opstina": "Uzdin",
        "lokacija": "Uzdin"
    },
    {
        "grad": "Kovačica",
        "opstina": "Crepaja",
        "lokacija": "Crepaja"
    },
    {
        "grad": "Kovin",
        "opstina": "Kovin",
        "lokacija": "Kovin"
    },
    {
        "grad": "Kovin",
        "opstina": "Gradska lokacija",
        "lokacija": "Dunav"
    },
    {
        "grad": "Kovin",
        "opstina": "Gradska lokacija",
        "lokacija": "Klek"
    },
    {
        "grad": "Kovin",
        "opstina": "Gradska lokacija",
        "lokacija": "Kolonija"
    },
    {
        "grad": "Kovin",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kovin",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kovin",
        "opstina": "Bavanište",
        "lokacija": "Bavanište"
    },
    {
        "grad": "Kovin",
        "opstina": "Gaj",
        "lokacija": "Gaj"
    },
    {
        "grad": "Kovin",
        "opstina": "Deliblato",
        "lokacija": "Deliblato"
    },
    {
        "grad": "Kovin",
        "opstina": "Deliblato",
        "lokacija": "Deliblato - Deliblatska Peščara"
    },
    {
        "grad": "Kovin",
        "opstina": "Deliblato",
        "lokacija": "Deliblato - Čardak"
    },
    {
        "grad": "Kovin",
        "opstina": "Dubovac",
        "lokacija": "Dubovac"
    },
    {
        "grad": "Kovin",
        "opstina": "Malo Bavanište",
        "lokacija": "Malo Bavanište"
    },
    {
        "grad": "Kovin",
        "opstina": "Mramorak",
        "lokacija": "Mramorak"
    },
    {
        "grad": "Kovin",
        "opstina": "Pločica",
        "lokacija": "Pločica"
    },
    {
        "grad": "Kovin",
        "opstina": "Skorenovac",
        "lokacija": "Skorenovac"
    },
    {
        "grad": "Kovin",
        "opstina": "Crna Bara",
        "lokacija": "Crna Bara"
    },
    {
        "grad": "Kovin",
        "opstina": "Šumarak",
        "lokacija": "Šumarak"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Kosjerić",
        "lokacija": "Kosjerić"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Bjeloperica",
        "lokacija": "Bjeloperica"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Brajkovići",
        "lokacija": "Brajkovići"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Varda",
        "lokacija": "Varda"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Galovići",
        "lokacija": "Galovići"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Godečevo",
        "lokacija": "Godečevo"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Godljevo",
        "lokacija": "Godljevo"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Gornja Pološnica",
        "lokacija": "Gornja Pološnica"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Donja Pološnica",
        "lokacija": "Donja Pološnica"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Drenovci",
        "lokacija": "Drenovci"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Dubnica",
        "lokacija": "Dubnica"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Kosjerić (selo)",
        "lokacija": "Kosjerić (selo)"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Makovište",
        "lokacija": "Makovište"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Mionica",
        "lokacija": "Mionica"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Mrčići",
        "lokacija": "Mrčići"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Mušići",
        "lokacija": "Mušići"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Paramun",
        "lokacija": "Paramun"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Radanovci",
        "lokacija": "Radanovci"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Rosići",
        "lokacija": "Rosići"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Ruda Bukva",
        "lokacija": "Ruda Bukva"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Seča Reka",
        "lokacija": "Seča Reka"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Skakavci",
        "lokacija": "Skakavci"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Stojići",
        "lokacija": "Stojići"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Subjel",
        "lokacija": "Subjel"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Tubići",
        "lokacija": "Tubići"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Cikote",
        "lokacija": "Cikote"
    },
    {
        "grad": "Kosjerić",
        "opstina": "Ševrljuge",
        "lokacija": "Ševrljuge"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Kosovo Polje",
        "lokacija": "Kosovo Polje"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Ariljača",
        "lokacija": "Ariljača"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Batuse",
        "lokacija": "Batuse"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Bresje",
        "lokacija": "Bresje"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Velika Slatina",
        "lokacija": "Velika Slatina"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Veliki Belaćevac",
        "lokacija": "Veliki Belaćevac"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Vragolija",
        "lokacija": "Vragolija"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Gornje Dobrevo",
        "lokacija": "Gornje Dobrevo"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Dobri Dub",
        "lokacija": "Dobri Dub"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Donje Dobrevo",
        "lokacija": "Donje Dobrevo"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Donji Grabovac",
        "lokacija": "Donji Grabovac"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Ence",
        "lokacija": "Ence"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Kuzmin",
        "lokacija": "Kuzmin"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Mala Slatina",
        "lokacija": "Mala Slatina"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Mali Belaćevac",
        "lokacija": "Mali Belaćevac"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Nakarade",
        "lokacija": "Nakarade"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Pomazatin",
        "lokacija": "Pomazatin"
    },
    {
        "grad": "Kosovo Polje",
        "opstina": "Ugljare",
        "lokacija": "Ugljare"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Kosovska Kamenica",
        "lokacija": "Kosovska Kamenica"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Ajnovce",
        "lokacija": "Ajnovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Berivojce",
        "lokacija": "Berivojce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Blato",
        "lokacija": "Blato"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Boževce",
        "lokacija": "Boževce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Boljevce",
        "lokacija": "Boljevce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Bosce",
        "lokacija": "Bosce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Bratilovce",
        "lokacija": "Bratilovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Busovata",
        "lokacija": "Busovata"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Bušince",
        "lokacija": "Bušince"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Vaganeš",
        "lokacija": "Vaganeš"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Veliko Ropotovo",
        "lokacija": "Veliko Ropotovo"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Veljeglava",
        "lokacija": "Veljeglava"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Vrućevce",
        "lokacija": "Vrućevce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Glogovce",
        "lokacija": "Glogovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Gmince",
        "lokacija": "Gmince"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Gogolovce",
        "lokacija": "Gogolovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Gornja Šipašnica",
        "lokacija": "Gornja Šipašnica"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Gornje Karačevo",
        "lokacija": "Gornje Karačevo"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Gornje Korminjane",
        "lokacija": "Gornje Korminjane"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Građenik",
        "lokacija": "Građenik"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Grizime",
        "lokacija": "Grizime"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Daždince",
        "lokacija": "Daždince"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Dajkovce",
        "lokacija": "Dajkovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Desivojce",
        "lokacija": "Desivojce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Domorovce",
        "lokacija": "Domorovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Donja Šipašnica",
        "lokacija": "Donja Šipašnica"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Donje Karačevo",
        "lokacija": "Donje Karačevo"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Donje Korminjane",
        "lokacija": "Donje Korminjane"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Drenovce",
        "lokacija": "Drenovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Đuriševce",
        "lokacija": "Đuriševce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Žuja",
        "lokacija": "Žuja"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Zajčevce",
        "lokacija": "Zajčevce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Kololeč",
        "lokacija": "Kololeč"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Koprivnica",
        "lokacija": "Koprivnica"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Koretin",
        "lokacija": "Koretin"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Kostadince",
        "lokacija": "Kostadince"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Krajnidel",
        "lokacija": "Krajnidel"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Kremenata",
        "lokacija": "Kremenata"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Kriljevo",
        "lokacija": "Kriljevo"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Lisocka",
        "lokacija": "Lisocka"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Ljačić",
        "lokacija": "Ljačić"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Lještar",
        "lokacija": "Lještar"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Malo Ropotovo",
        "lokacija": "Malo Ropotovo"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Marovce",
        "lokacija": "Marovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Mešina",
        "lokacija": "Mešina"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Miganovce",
        "lokacija": "Miganovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Močare",
        "lokacija": "Močare"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Mučivrce",
        "lokacija": "Mučivrce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Ogošte",
        "lokacija": "Ogošte"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Odanovce",
        "lokacija": "Odanovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Odevce",
        "lokacija": "Odevce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Oraovica",
        "lokacija": "Oraovica"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Pančelo",
        "lokacija": "Pančelo"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Petrovce",
        "lokacija": "Petrovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Polička",
        "lokacija": "Polička"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Rajanovce",
        "lokacija": "Rajanovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Ranilug",
        "lokacija": "Ranilug"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Robovac",
        "lokacija": "Robovac"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Rogačica",
        "lokacija": "Rogačica"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Svirce",
        "lokacija": "Svirce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Sedlare",
        "lokacija": "Sedlare"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Strezovce",
        "lokacija": "Strezovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Strelica",
        "lokacija": "Strelica"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Tirince",
        "lokacija": "Tirince"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Tomance",
        "lokacija": "Tomance"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Toponica",
        "lokacija": "Toponica"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Trstena",
        "lokacija": "Trstena"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Tuđevce",
        "lokacija": "Tuđevce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Firićeja",
        "lokacija": "Firićeja"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Carevce",
        "lokacija": "Carevce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Čarakovce",
        "lokacija": "Čarakovce"
    },
    {
        "grad": "Kosovska Kamenica",
        "opstina": "Šajić",
        "lokacija": "Šajić"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Kosovska Mitrovica",
        "lokacija": "Kosovska Mitrovica"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Bošnjačka Mahala"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Brđani"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Ibar"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Mikro Naselje"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Tamnik"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Tri Solitera"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Bajgora",
        "lokacija": "Bajgora"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Bare",
        "lokacija": "Bare"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Bataire",
        "lokacija": "Bataire"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Brabonjić",
        "lokacija": "Brabonjić"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Vaganica",
        "lokacija": "Vaganica"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Veliki Kičić",
        "lokacija": "Veliki Kičić"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Vidomirić",
        "lokacija": "Vidomirić"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Vidušić",
        "lokacija": "Vidušić"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Vlahinje",
        "lokacija": "Vlahinje"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Vrbnica",
        "lokacija": "Vrbnica"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gornje Vinarce",
        "lokacija": "Gornje Vinarce"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gornje Žabare",
        "lokacija": "Gornje Žabare"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gornje Rašane",
        "lokacija": "Gornje Rašane"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gornji Suvi Do",
        "lokacija": "Gornji Suvi Do"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Gušavac",
        "lokacija": "Gušavac"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Dedinje",
        "lokacija": "Dedinje"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Donje Vinarce",
        "lokacija": "Donje Vinarce"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Donje Žabare",
        "lokacija": "Donje Žabare"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Donje Rašane",
        "lokacija": "Donje Rašane"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Donji Suvi Do",
        "lokacija": "Donji Suvi Do"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Zabrđe",
        "lokacija": "Zabrđe"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Zasela",
        "lokacija": "Zasela"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Zijača",
        "lokacija": "Zijača"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Kačandol",
        "lokacija": "Kačandol"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Kovačica",
        "lokacija": "Kovačica"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Kopriva",
        "lokacija": "Kopriva"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Košutovo",
        "lokacija": "Košutovo"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Kutlovac",
        "lokacija": "Kutlovac"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Lisica",
        "lokacija": "Lisica"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Ljušta",
        "lokacija": "Ljušta"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Mađare",
        "lokacija": "Mađare"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Mažić",
        "lokacija": "Mažić"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Malo Kičiće",
        "lokacija": "Malo Kičiće"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Meljenica",
        "lokacija": "Meljenica"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Ovčare",
        "lokacija": "Ovčare"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Orahovo",
        "lokacija": "Orahovo"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Pirče",
        "lokacija": "Pirče"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Prvi Tunel",
        "lokacija": "Prvi Tunel"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Reka",
        "lokacija": "Reka"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Ržana",
        "lokacija": "Ržana"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Svinjare",
        "lokacija": "Svinjare"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Seljance",
        "lokacija": "Seljance"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Stari Trg (rud. naselje)",
        "lokacija": "Stari Trg (rud. naselje)"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Stari Trg (selo)",
        "lokacija": "Stari Trg (selo)"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Strana",
        "lokacija": "Strana"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Trstena",
        "lokacija": "Trstena"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Šipolje",
        "lokacija": "Šipolje"
    },
    {
        "grad": "Kosovska Mitrovica",
        "opstina": "Šupkovac",
        "lokacija": "Šupkovac"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Koceljeva",
        "lokacija": "Koceljeva"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Batalage",
        "lokacija": "Batalage"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Brdarica",
        "lokacija": "Brdarica"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Bresnica",
        "lokacija": "Bresnica"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Galović",
        "lokacija": "Galović"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Goločelo",
        "lokacija": "Goločelo"
    },
    {
        "grad": "Koceljeva",
        "opstina": "gradojević",
        "lokacija": "gradojević"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Donje Crniljevo",
        "lokacija": "Donje Crniljevo"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Draginje",
        "lokacija": "Draginje"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Družetić",
        "lokacija": "Družetić"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Zukve",
        "lokacija": "Zukve"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Kamenica",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Ljutice",
        "lokacija": "Ljutice"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Mali Bošnjak",
        "lokacija": "Mali Bošnjak"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Svileuva",
        "lokacija": "Svileuva"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Subotica",
        "lokacija": "Subotica"
    },
    {
        "grad": "Koceljeva",
        "opstina": "Ćukovine",
        "lokacija": "Ćukovine"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Kraljevo",
        "lokacija": "Kraljevo"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Bogavčevo Brdo"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Boračko Naselje"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Braće Jevremović"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Braće Jovanović"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Braće Pirić"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Bunjačko Brdo"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Vojvode Stepe"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Vojno Naselje"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "gradski Kej"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Grdica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Dositejeva"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Zelengora"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Ibar"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Jarčujak"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Jovana Deroka"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Jovac"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Karađorđeva"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Kovanluk"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Kovači"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Moše Pijade"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Voćareve Livade"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Pampula"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Pic - Mala"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Ribnica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Sijaće Polje"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Stara Čaršija"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Francuska Kolonija"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Higijenski Zavod"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Crveni Krst"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Adrani",
        "lokacija": "Adrani"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Bapsko Polje",
        "lokacija": "Bapsko Polje"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Bare",
        "lokacija": "Bare"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Beranovac",
        "lokacija": "Beranovac"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Bzovik",
        "lokacija": "Bzovik"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Bogutovac",
        "lokacija": "Bogutovac"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Bogutovac",
        "lokacija": "Bogutovac - Bogutovačka Banja"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Bojanići",
        "lokacija": "Bojanići"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Borovo",
        "lokacija": "Borovo"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Brezna",
        "lokacija": "Brezna"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Brezova",
        "lokacija": "Brezova"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Bresnik",
        "lokacija": "Bresnik"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Bukovica",
        "lokacija": "Bukovica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Vitanovac",
        "lokacija": "Vitanovac"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Vitkovac",
        "lokacija": "Vitkovac"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Vrba",
        "lokacija": "Vrba"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Vrdila",
        "lokacija": "Vrdila"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Vrh",
        "lokacija": "Vrh"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gledić",
        "lokacija": "Gledić"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Godačica",
        "lokacija": "Godačica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Gokčanica",
        "lokacija": "Gokčanica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Grdica",
        "lokacija": "Grdica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Dedevci",
        "lokacija": "Dedevci"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Dolac",
        "lokacija": "Dolac"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Dragosinjci",
        "lokacija": "Dragosinjci"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Dražiniće",
        "lokacija": "Dražiniće"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Drakčići",
        "lokacija": "Drakčići"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Drlupa",
        "lokacija": "Drlupa"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Đakovo",
        "lokacija": "Đakovo"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Žiča",
        "lokacija": "Žiča"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Zaklopača",
        "lokacija": "Zaklopača"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Zakuta",
        "lokacija": "Zakuta"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Zamčanje",
        "lokacija": "Zamčanje"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Zasad",
        "lokacija": "Zasad"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Kamenica",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Kamenjani",
        "lokacija": "Kamenjani"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Konarevo",
        "lokacija": "Konarevo"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Lađevci",
        "lokacija": "Lađevci"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Lazac",
        "lokacija": "Lazac"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Leševo",
        "lokacija": "Leševo"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Lozno",
        "lokacija": "Lozno"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Lopatnica",
        "lokacija": "Lopatnica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Maglič",
        "lokacija": "Maglič"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Mataruge",
        "lokacija": "Mataruge"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Maratuška Banja",
        "lokacija": "Maratuška Banja"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Međurečje",
        "lokacija": "Međurečje"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Meljanica",
        "lokacija": "Meljanica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Metikoš",
        "lokacija": "Metikoš"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Milavčići",
        "lokacija": "Milavčići"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Milakovac",
        "lokacija": "Milakovac"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Miliće",
        "lokacija": "Miliće"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Miločaj",
        "lokacija": "Miločaj"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Mlanča",
        "lokacija": "Mlanča"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Mošin Gaj",
        "lokacija": "Mošin Gaj"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Mrsać",
        "lokacija": "Mrsać"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Musina Reka",
        "lokacija": "Musina Reka"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Obrva",
        "lokacija": "Obrva"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Oplanići",
        "lokacija": "Oplanići"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Orlja Glava",
        "lokacija": "Orlja Glava"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Pekčanica",
        "lokacija": "Pekčanica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Petropolje",
        "lokacija": "Petropolje"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Pečenog",
        "lokacija": "Pečenog"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Plana",
        "lokacija": "Plana"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Polumir",
        "lokacija": "Polumir"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Popovići",
        "lokacija": "Popovići"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Predoloe",
        "lokacija": "Predoloe"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Progorelica",
        "lokacija": "Progorelica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Ravanica",
        "lokacija": "Ravanica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Ratina",
        "lokacija": "Ratina"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Reka",
        "lokacija": "Reka"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Ribnica",
        "lokacija": "Ribnica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Ribnica",
        "lokacija": "Ribnica - Zmajevac"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Roćevići",
        "lokacija": "Roćevići"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Rudno",
        "lokacija": "Rudno"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Rudnjak",
        "lokacija": "Rudnjak"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Savovo",
        "lokacija": "Savovo"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Samaila",
        "lokacija": "Samaila"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Sibnica",
        "lokacija": "Sibnica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Sirča",
        "lokacija": "Sirča"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Stanča",
        "lokacija": "Stanča"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Stubal",
        "lokacija": "Stubal"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Tavnik",
        "lokacija": "Tavnik"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Tadenje",
        "lokacija": "Tadenje"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Tepeče",
        "lokacija": "Tepeče"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Tolišnica",
        "lokacija": "Tolišnica"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Trgovište",
        "lokacija": "Trgovište"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Trešnjar",
        "lokacija": "Trešnjar"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Ušće",
        "lokacija": "Ušće"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Cvetke",
        "lokacija": "Cvetke"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Cerje",
        "lokacija": "Cerje"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Čibukovac",
        "lokacija": "Čibukovac"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Čukojevac",
        "lokacija": "Čukojevac"
    },
    {
        "grad": "Kraljevo",
        "opstina": "Šumarice",
        "lokacija": "Šumarice"
    },
    {
        "grad": "Krupanj",
        "opstina": "Krupanj",
        "lokacija": "Krupanj"
    },
    {
        "grad": "Krupanj",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Krupanj",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Krupanj",
        "opstina": "Banjevac",
        "lokacija": "Banjevac"
    },
    {
        "grad": "Krupanj",
        "opstina": "Bela Crkva",
        "lokacija": "Bela Crkva"
    },
    {
        "grad": "Krupanj",
        "opstina": "Bogoštica",
        "lokacija": "Bogoštica"
    },
    {
        "grad": "Krupanj",
        "opstina": "Brezovice",
        "lokacija": "Brezovice"
    },
    {
        "grad": "Krupanj",
        "opstina": "Brštica",
        "lokacija": "Brštica"
    },
    {
        "grad": "Krupanj",
        "opstina": "Vrbić",
        "lokacija": "Vrbić"
    },
    {
        "grad": "Krupanj",
        "opstina": "Dvorska",
        "lokacija": "Dvorska"
    },
    {
        "grad": "Krupanj",
        "opstina": "Zavlaka",
        "lokacija": "Zavlaka"
    },
    {
        "grad": "Krupanj",
        "opstina": "Kostajnik",
        "lokacija": "Kostajnik"
    },
    {
        "grad": "Krupanj",
        "opstina": "Krasava",
        "lokacija": "Krasava"
    },
    {
        "grad": "Krupanj",
        "opstina": "Kržava",
        "lokacija": "Kržava"
    },
    {
        "grad": "Krupanj",
        "opstina": "Likodra",
        "lokacija": "Likodra"
    },
    {
        "grad": "Krupanj",
        "opstina": "Lipenović",
        "lokacija": "Lipenović"
    },
    {
        "grad": "Krupanj",
        "opstina": "Mojković",
        "lokacija": "Mojković"
    },
    {
        "grad": "Krupanj",
        "opstina": "Planina",
        "lokacija": "Planina"
    },
    {
        "grad": "Krupanj",
        "opstina": "Ravnaja",
        "lokacija": "Ravnaja"
    },
    {
        "grad": "Krupanj",
        "opstina": "Stave",
        "lokacija": "Stave"
    },
    {
        "grad": "Krupanj",
        "opstina": "Tolisavac",
        "lokacija": "Tolisavac"
    },
    {
        "grad": "Krupanj",
        "opstina": "Tomanj",
        "lokacija": "Tomanj"
    },
    {
        "grad": "Krupanj",
        "opstina": "Cvetulja",
        "lokacija": "Cvetulja"
    },
    {
        "grad": "Krupanj",
        "opstina": "Cerova",
        "lokacija": "Cerova"
    },
    {
        "grad": "Krupanj",
        "opstina": "Šljivova",
        "lokacija": "Šljivova"
    },
    {
        "grad": "Kruševac",
        "opstina": "Kruševac",
        "lokacija": "Kruševac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Aerodrom"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Bagdala"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Bare"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Blagoja Parovića"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Bolnica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Bronks"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Vlado Jurić"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kolonija"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Lazarica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Malo Golovode"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Mudrakovac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Nova Pijaca"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Pakašnica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Pejton"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Prnjavor"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Rasadnik"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Stara Čaršija"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Trg Kosturnica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Ujedinjene Nacije"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Šumice"
    },
    {
        "grad": "Kruševac",
        "opstina": "Begovo Brdo",
        "lokacija": "Begovo Brdo"
    },
    {
        "grad": "Kruševac",
        "opstina": "Bela Voda",
        "lokacija": "Bela Voda"
    },
    {
        "grad": "Kruševac",
        "opstina": "Belasica",
        "lokacija": "Belasica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Bivolje",
        "lokacija": "Bivolje"
    },
    {
        "grad": "Kruševac",
        "opstina": "Bovan",
        "lokacija": "Bovan"
    },
    {
        "grad": "Kruševac",
        "opstina": "Bojince",
        "lokacija": "Bojince"
    },
    {
        "grad": "Kruševac",
        "opstina": "Boljevac",
        "lokacija": "Boljevac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Brajkovac",
        "lokacija": "Brajkovac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Bukovica",
        "lokacija": "Bukovica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Buci",
        "lokacija": "Buci"
    },
    {
        "grad": "Kruševac",
        "opstina": "Velika Kruševica",
        "lokacija": "Velika Kruševica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Velika Lomnica",
        "lokacija": "Velika Lomnica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Veliki Kupci",
        "lokacija": "Veliki Kupci"
    },
    {
        "grad": "Kruševac",
        "opstina": "Veliki Šiljegovac",
        "lokacija": "Veliki Šiljegovac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Veliko Golovode",
        "lokacija": "Veliko Golovode"
    },
    {
        "grad": "Kruševac",
        "opstina": "Veliko Krušince",
        "lokacija": "Veliko Krušince"
    },
    {
        "grad": "Kruševac",
        "opstina": "Vitanovac",
        "lokacija": "Vitanovac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Vratare",
        "lokacija": "Vratare"
    },
    {
        "grad": "Kruševac",
        "opstina": "Vučak",
        "lokacija": "Vučak"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gavez",
        "lokacija": "Gavez"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gaglovo",
        "lokacija": "Gaglovo"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gari",
        "lokacija": "Gari"
    },
    {
        "grad": "Kruševac",
        "opstina": "Globare",
        "lokacija": "Globare"
    },
    {
        "grad": "Kruševac",
        "opstina": "Globoder",
        "lokacija": "Globoder"
    },
    {
        "grad": "Kruševac",
        "opstina": "Gornji Stepoš",
        "lokacija": "Gornji Stepoš"
    },
    {
        "grad": "Kruševac",
        "opstina": "Grevci",
        "lokacija": "Grevci"
    },
    {
        "grad": "Kruševac",
        "opstina": "Grkljane",
        "lokacija": "Grkljane"
    },
    {
        "grad": "Kruševac",
        "opstina": "Dvorane",
        "lokacija": "Dvorane"
    },
    {
        "grad": "Kruševac",
        "opstina": "Dedina",
        "lokacija": "Dedina"
    },
    {
        "grad": "Kruševac",
        "opstina": "Dobromir",
        "lokacija": "Dobromir"
    },
    {
        "grad": "Kruševac",
        "opstina": "Doljane",
        "lokacija": "Doljane"
    },
    {
        "grad": "Kruševac",
        "opstina": "Donji Stepoš",
        "lokacija": "Donji Stepoš"
    },
    {
        "grad": "Kruševac",
        "opstina": "Đunis",
        "lokacija": "Đunis"
    },
    {
        "grad": "Kruševac",
        "opstina": "Žabare",
        "lokacija": "Žabare"
    },
    {
        "grad": "Kruševac",
        "opstina": "Zdravinje",
        "lokacija": "Zdravinje"
    },
    {
        "grad": "Kruševac",
        "opstina": "Zebica",
        "lokacija": "Zebica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Zubovac",
        "lokacija": "Zubovac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Jablanica",
        "lokacija": "Jablanica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Jasika",
        "lokacija": "Jasika"
    },
    {
        "grad": "Kruševac",
        "opstina": "Jošje",
        "lokacija": "Jošje"
    },
    {
        "grad": "Kruševac",
        "opstina": "Kamenare",
        "lokacija": "Kamenare"
    },
    {
        "grad": "Kruševac",
        "opstina": "Kaonik",
        "lokacija": "Kaonik"
    },
    {
        "grad": "Kruševac",
        "opstina": "Kapidžija",
        "lokacija": "Kapidžija"
    },
    {
        "grad": "Kruševac",
        "opstina": "Kobilje",
        "lokacija": "Kobilje"
    },
    {
        "grad": "Kruševac",
        "opstina": "Komorane",
        "lokacija": "Komorane"
    },
    {
        "grad": "Kruševac",
        "opstina": "Konjuh",
        "lokacija": "Konjuh"
    },
    {
        "grad": "Kruševac",
        "opstina": "Koševi",
        "lokacija": "Koševi"
    },
    {
        "grad": "Kruševac",
        "opstina": "Krvavica",
        "lokacija": "Krvavica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Kukljin",
        "lokacija": "Kukljin"
    },
    {
        "grad": "Kruševac",
        "opstina": "Lazarevac",
        "lokacija": "Lazarevac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Lazarica",
        "lokacija": "Lazarica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Lipovac",
        "lokacija": "Lipovac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Lovci",
        "lokacija": "Lovci"
    },
    {
        "grad": "Kruševac",
        "opstina": "Lukavac",
        "lokacija": "Lukavac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Ljubava",
        "lokacija": "Ljubava"
    },
    {
        "grad": "Kruševac",
        "opstina": "Majdevo",
        "lokacija": "Majdevo"
    },
    {
        "grad": "Kruševac",
        "opstina": "Makrešane",
        "lokacija": "Makrešane"
    },
    {
        "grad": "Kruševac",
        "opstina": "Mala Vrbnica",
        "lokacija": "Mala Vrbnica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Mala Reka",
        "lokacija": "Mala Reka"
    },
    {
        "grad": "Kruševac",
        "opstina": "Mali Kupci",
        "lokacija": "Mali Kupci"
    },
    {
        "grad": "Kruševac",
        "opstina": "Mali Šiljegovac",
        "lokacija": "Mali Šiljegovac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Malo Krušince",
        "lokacija": "Malo Krušince"
    },
    {
        "grad": "Kruševac",
        "opstina": "Mačkovac",
        "lokacija": "Mačkovac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Meševo",
        "lokacija": "Meševo"
    },
    {
        "grad": "Kruševac",
        "opstina": "Modrica",
        "lokacija": "Modrica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Naupare",
        "lokacija": "Naupare"
    },
    {
        "grad": "Kruševac",
        "opstina": "Padež",
        "lokacija": "Padež"
    },
    {
        "grad": "Kruševac",
        "opstina": "Parunovac",
        "lokacija": "Parunovac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Pasjak",
        "lokacija": "Pasjak"
    },
    {
        "grad": "Kruševac",
        "opstina": "Pepeljevac",
        "lokacija": "Pepeljevac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Petina",
        "lokacija": "Petina"
    },
    {
        "grad": "Kruševac",
        "opstina": "Pozlata",
        "lokacija": "Pozlata"
    },
    {
        "grad": "Kruševac",
        "opstina": "Poljaci",
        "lokacija": "Poljaci"
    },
    {
        "grad": "Kruševac",
        "opstina": "Ribare",
        "lokacija": "Ribare"
    },
    {
        "grad": "Kruševac",
        "opstina": "Ribarska Banja",
        "lokacija": "Ribarska Banja"
    },
    {
        "grad": "Kruševac",
        "opstina": "Rlica",
        "lokacija": "Rlica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Rosica",
        "lokacija": "Rosica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Sebečevac",
        "lokacija": "Sebečevac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Sezemče",
        "lokacija": "Sezemče"
    },
    {
        "grad": "Kruševac",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Kruševac",
        "opstina": "Srndalje",
        "lokacija": "Srndalje"
    },
    {
        "grad": "Kruševac",
        "opstina": "Srnje",
        "lokacija": "Srnje"
    },
    {
        "grad": "Kruševac",
        "opstina": "Stanci",
        "lokacija": "Stanci"
    },
    {
        "grad": "Kruševac",
        "opstina": "Suvaja",
        "lokacija": "Suvaja"
    },
    {
        "grad": "Kruševac",
        "opstina": "Sušica",
        "lokacija": "Sušica"
    },
    {
        "grad": "Kruševac",
        "opstina": "Tekija",
        "lokacija": "Tekija"
    },
    {
        "grad": "Kruševac",
        "opstina": "Trebotin",
        "lokacija": "Trebotin"
    },
    {
        "grad": "Kruševac",
        "opstina": "Trmčare",
        "lokacija": "Trmčare"
    },
    {
        "grad": "Kruševac",
        "opstina": "Ćelije",
        "lokacija": "Ćelije"
    },
    {
        "grad": "Kruševac",
        "opstina": "Cerova",
        "lokacija": "Cerova"
    },
    {
        "grad": "Kruševac",
        "opstina": "Crkvina",
        "lokacija": "Crkvina"
    },
    {
        "grad": "Kruševac",
        "opstina": "Čitluk",
        "lokacija": "Čitluk"
    },
    {
        "grad": "Kruševac",
        "opstina": "Šavrane",
        "lokacija": "Šavrane"
    },
    {
        "grad": "Kruševac",
        "opstina": "Šanac",
        "lokacija": "Šanac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Šašilovac",
        "lokacija": "Šašilovac"
    },
    {
        "grad": "Kruševac",
        "opstina": "Šogolj",
        "lokacija": "Šogolj"
    },
    {
        "grad": "Kruševac",
        "opstina": "Štitare",
        "lokacija": "Štitare"
    },
    {
        "grad": "Kula",
        "opstina": "Kula",
        "lokacija": "Kula"
    },
    {
        "grad": "Kula",
        "opstina": "Gradska lokacija",
        "lokacija": "Gornji grad"
    },
    {
        "grad": "Kula",
        "opstina": "Gradska lokacija",
        "lokacija": "Donji grad"
    },
    {
        "grad": "Kula",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kula",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kula",
        "opstina": "Kruščić",
        "lokacija": "Kruščić"
    },
    {
        "grad": "Kula",
        "opstina": "Lipar",
        "lokacija": "Lipar"
    },
    {
        "grad": "Kula",
        "opstina": "Nova Crvenka",
        "lokacija": "Nova Crvenka"
    },
    {
        "grad": "Kula",
        "opstina": "Ruski Krstur",
        "lokacija": "Ruski Krstur"
    },
    {
        "grad": "Kula",
        "opstina": "Sivac",
        "lokacija": "Sivac"
    },
    {
        "grad": "Kula",
        "opstina": "Crvenka",
        "lokacija": "Crvenka"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Kuršumlija",
        "lokacija": "Kuršumlija"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Gradska lokacija",
        "lokacija": "Veljkoviće"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Gradska lokacija",
        "lokacija": "Pantiće"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Gradska lokacija",
        "lokacija": "Rasadnik"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Babica",
        "lokacija": "Babica"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Barlovo",
        "lokacija": "Barlovo"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Baćoglava",
        "lokacija": "Baćoglava"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Belo Polje",
        "lokacija": "Belo Polje"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Bogujevac",
        "lokacija": "Bogujevac"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Vasiljevac",
        "lokacija": "Vasiljevac"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Veliko Pupavce",
        "lokacija": "Veliko Pupavce"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Visoka",
        "lokacija": "Visoka"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Vlahinja",
        "lokacija": "Vlahinja"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Vrelo",
        "lokacija": "Vrelo"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Vrševac",
        "lokacija": "Vrševac"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Vukojevac",
        "lokacija": "Vukojevac"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Gornja Mikuljana",
        "lokacija": "Gornja Mikuljana"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Gornje Točane",
        "lokacija": "Gornje Točane"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Grabovnica",
        "lokacija": "Grabovnica"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Dabinovac",
        "lokacija": "Dabinovac"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Dankoviće",
        "lokacija": "Dankoviće"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Degrmen",
        "lokacija": "Degrmen"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Dedinac",
        "lokacija": "Dedinac"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Dešiška",
        "lokacija": "Dešiška"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Dobri Do",
        "lokacija": "Dobri Do"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Donja Mikuljana",
        "lokacija": "Donja Mikuljana"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Donje Točane",
        "lokacija": "Donje Točane"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Dubrava",
        "lokacija": "Dubrava"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Đake",
        "lokacija": "Đake"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Žalica",
        "lokacija": "Žalica"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Žegrova",
        "lokacija": "Žegrova"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Žuč",
        "lokacija": "Žuč"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Zagrađe",
        "lokacija": "Zagrađe"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Zebice",
        "lokacija": "Zebice"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Ivan Kula",
        "lokacija": "Ivan Kula"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Igrište",
        "lokacija": "Igrište"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Kastrat",
        "lokacija": "Kastrat"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Konjuva",
        "lokacija": "Konjuva"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Kosmača",
        "lokacija": "Kosmača"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Krtok",
        "lokacija": "Krtok"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Krčmare",
        "lokacija": "Krčmare"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Kupinovo",
        "lokacija": "Kupinovo"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Kuršumlijska Banja",
        "lokacija": "Kuršumlijska Banja"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Kutlovo",
        "lokacija": "Kutlovo"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Lukovo",
        "lokacija": "Lukovo"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Ljutova",
        "lokacija": "Ljutova"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Ljuša",
        "lokacija": "Ljuša"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Magovo",
        "lokacija": "Magovo"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Mala Kosanica",
        "lokacija": "Mala Kosanica"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Maričiće",
        "lokacija": "Maričiće"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Markoviće",
        "lokacija": "Markoviće"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Matarova",
        "lokacija": "Matarova"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Mačja Stena",
        "lokacija": "Mačja Stena"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Mačkovac",
        "lokacija": "Mačkovac"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Merdare",
        "lokacija": "Merdare"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Merćez",
        "lokacija": "Merćez"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Mehane",
        "lokacija": "Mehane"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Mirnica",
        "lokacija": "Mirnica"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Mrče",
        "lokacija": "Mrče"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Nevada",
        "lokacija": "Nevada"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Orlovac",
        "lokacija": "Orlovac"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Parada",
        "lokacija": "Parada"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Pačarađa",
        "lokacija": "Pačarađa"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Pevaštica",
        "lokacija": "Pevaštica"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Pepeljevac",
        "lokacija": "Pepeljevac"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Perunika",
        "lokacija": "Perunika"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Pljakovo",
        "lokacija": "Pljakovo"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Prevetica",
        "lokacija": "Prevetica"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Prekorađe",
        "lokacija": "Prekorađe"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Prolom",
        "lokacija": "Prolom"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Prolom Banja",
        "lokacija": "Prolom Banja"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Ravni Šort",
        "lokacija": "Ravni Šort"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Rastelica",
        "lokacija": "Rastelica"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Rača",
        "lokacija": "Rača"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Rudare",
        "lokacija": "Rudare"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Sagonjevo",
        "lokacija": "Sagonjevo"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Samokovo",
        "lokacija": "Samokovo"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Svinjište",
        "lokacija": "Svinjište"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Sekirača",
        "lokacija": "Sekirača"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Selište",
        "lokacija": "Selište"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Selova",
        "lokacija": "Selova"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Seoce",
        "lokacija": "Seoce"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Spance",
        "lokacija": "Spance"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Tačevac",
        "lokacija": "Tačevac"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Tijovac",
        "lokacija": "Tijovac"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Tmava",
        "lokacija": "Tmava"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Trebinje",
        "lokacija": "Trebinje"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Trećak",
        "lokacija": "Trećak"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Trmka",
        "lokacija": "Trmka"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Trn",
        "lokacija": "Trn"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Trpeza",
        "lokacija": "Trpeza"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Šatra",
        "lokacija": "Šatra"
    },
    {
        "grad": "Kuršumlija",
        "opstina": "Štava",
        "lokacija": "Štava"
    },
    {
        "grad": "Kučevo",
        "opstina": "Kučevo",
        "lokacija": "Kučevo"
    },
    {
        "grad": "Kučevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Kučevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Kučevo",
        "opstina": "Blagojev Kamen",
        "lokacija": "Blagojev Kamen"
    },
    {
        "grad": "Kučevo",
        "opstina": "Brodica",
        "lokacija": "Brodica"
    },
    {
        "grad": "Kučevo",
        "opstina": "Bukovska",
        "lokacija": "Bukovska"
    },
    {
        "grad": "Kučevo",
        "opstina": "Velika Bresnica",
        "lokacija": "Velika Bresnica"
    },
    {
        "grad": "Kučevo",
        "opstina": "Voluja",
        "lokacija": "Voluja"
    },
    {
        "grad": "Kučevo",
        "opstina": "Vuković",
        "lokacija": "Vuković"
    },
    {
        "grad": "Kučevo",
        "opstina": "Duboka",
        "lokacija": "Duboka"
    },
    {
        "grad": "Kučevo",
        "opstina": "Zelenik",
        "lokacija": "Zelenik"
    },
    {
        "grad": "Kučevo",
        "opstina": "Kaona",
        "lokacija": "Kaona"
    },
    {
        "grad": "Kučevo",
        "opstina": "Kučajna",
        "lokacija": "Kučajna"
    },
    {
        "grad": "Kučevo",
        "opstina": "Lješnica",
        "lokacija": "Lješnica"
    },
    {
        "grad": "Kučevo",
        "opstina": "Mala Bresnica",
        "lokacija": "Mala Bresnica"
    },
    {
        "grad": "Kučevo",
        "opstina": "Mišljenovac",
        "lokacija": "Mišljenovac"
    },
    {
        "grad": "Kučevo",
        "opstina": "Mustapić",
        "lokacija": "Mustapić"
    },
    {
        "grad": "Kučevo",
        "opstina": "Neresnica",
        "lokacija": "Neresnica"
    },
    {
        "grad": "Kučevo",
        "opstina": "Rabrovo",
        "lokacija": "Rabrovo"
    },
    {
        "grad": "Kučevo",
        "opstina": "Ravnište",
        "lokacija": "Ravnište"
    },
    {
        "grad": "Kučevo",
        "opstina": "Radenka",
        "lokacija": "Radenka"
    },
    {
        "grad": "Kučevo",
        "opstina": "Rakova Bara",
        "lokacija": "Rakova Bara"
    },
    {
        "grad": "Kučevo",
        "opstina": "Sena",
        "lokacija": "Sena"
    },
    {
        "grad": "Kučevo",
        "opstina": "Srpce",
        "lokacija": "Srpce"
    },
    {
        "grad": "Kučevo",
        "opstina": "Turija",
        "lokacija": "Turija"
    },
    {
        "grad": "Kučevo",
        "opstina": "Homoljske Planine",
        "lokacija": "Homoljske Planine"
    },
    {
        "grad": "Kučevo",
        "opstina": "Ceremošnja",
        "lokacija": "Ceremošnja"
    },
    {
        "grad": "Kučevo",
        "opstina": "Cerovica",
        "lokacija": "Cerovica"
    },
    {
        "grad": "Kučevo",
        "opstina": "Ševica",
        "lokacija": "Ševica"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Lajkovac",
        "lokacija": "Lajkovac"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Bajevac",
        "lokacija": "Bajevac"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Bogovađa",
        "lokacija": "Bogovađa"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Vračević",
        "lokacija": "Vračević"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Donji Lajkovac",
        "lokacija": "Donji Lajkovac"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Jabučje",
        "lokacija": "Jabučje"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Lajkovac Selo",
        "lokacija": "Lajkovac Selo"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Mali Borak",
        "lokacija": "Mali Borak"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Markova Crkva",
        "lokacija": "Markova Crkva"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Nepričava",
        "lokacija": "Nepričava"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Pepeljevac",
        "lokacija": "Pepeljevac"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Pridvorica",
        "lokacija": "Pridvorica"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Ratkovac",
        "lokacija": "Ratkovac"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Rubribreza",
        "lokacija": "Rubribreza"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Skobalj",
        "lokacija": "Skobalj"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Slovac",
        "lokacija": "Slovac"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Stepanje",
        "lokacija": "Stepanje"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Strmovo",
        "lokacija": "Strmovo"
    },
    {
        "grad": "Lajkovac",
        "opstina": "Ćelije",
        "lokacija": "Ćelije"
    },
    {
        "grad": "Lapovo",
        "opstina": "Lapovo",
        "lokacija": "Lapovo"
    },
    {
        "grad": "Lapovo",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Lapovo",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Lapovo",
        "opstina": "Lapovo Selo",
        "lokacija": "Lapovo Selo"
    },
    {
        "grad": "Lebane",
        "opstina": "Lebane",
        "lokacija": "Lebane"
    },
    {
        "grad": "Lebane",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Lebane",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Lebane",
        "opstina": "Bačevina",
        "lokacija": "Bačevina"
    },
    {
        "grad": "Lebane",
        "opstina": "Bošnjace",
        "lokacija": "Bošnjace"
    },
    {
        "grad": "Lebane",
        "opstina": "Buvce",
        "lokacija": "Buvce"
    },
    {
        "grad": "Lebane",
        "opstina": "Veliko Vojlovce",
        "lokacija": "Veliko Vojlovce"
    },
    {
        "grad": "Lebane",
        "opstina": "Geglja",
        "lokacija": "Geglja"
    },
    {
        "grad": "Lebane",
        "opstina": "Goli Rid",
        "lokacija": "Goli Rid"
    },
    {
        "grad": "Lebane",
        "opstina": "Gornje Vranovce",
        "lokacija": "Gornje Vranovce"
    },
    {
        "grad": "Lebane",
        "opstina": "Grgurovce",
        "lokacija": "Grgurovce"
    },
    {
        "grad": "Lebane",
        "opstina": "Donje Vranovce",
        "lokacija": "Donje Vranovce"
    },
    {
        "grad": "Lebane",
        "opstina": "Drvodelj",
        "lokacija": "Drvodelj"
    },
    {
        "grad": "Lebane",
        "opstina": "Ždeglovo",
        "lokacija": "Ždeglovo"
    },
    {
        "grad": "Lebane",
        "opstina": "Klajić",
        "lokacija": "Klajić"
    },
    {
        "grad": "Lebane",
        "opstina": "Konjino",
        "lokacija": "Konjino"
    },
    {
        "grad": "Lebane",
        "opstina": "Krivača",
        "lokacija": "Krivača"
    },
    {
        "grad": "Lebane",
        "opstina": "Lalinovac",
        "lokacija": "Lalinovac"
    },
    {
        "grad": "Lebane",
        "opstina": "Lipovica",
        "lokacija": "Lipovica"
    },
    {
        "grad": "Lebane",
        "opstina": "Lugare",
        "lokacija": "Lugare"
    },
    {
        "grad": "Lebane",
        "opstina": "Malo Vojlovce",
        "lokacija": "Malo Vojlovce"
    },
    {
        "grad": "Lebane",
        "opstina": "Nova Topola",
        "lokacija": "Nova Topola"
    },
    {
        "grad": "Lebane",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Lebane",
        "opstina": "Pertate",
        "lokacija": "Pertate"
    },
    {
        "grad": "Lebane",
        "opstina": "Petrovac",
        "lokacija": "Petrovac"
    },
    {
        "grad": "Lebane",
        "opstina": "Popovce",
        "lokacija": "Popovce"
    },
    {
        "grad": "Lebane",
        "opstina": "Poroštica",
        "lokacija": "Poroštica"
    },
    {
        "grad": "Lebane",
        "opstina": "Prekopčelica",
        "lokacija": "Prekopčelica"
    },
    {
        "grad": "Lebane",
        "opstina": "Radevce",
        "lokacija": "Radevce"
    },
    {
        "grad": "Lebane",
        "opstina": "Radinovac",
        "lokacija": "Radinovac"
    },
    {
        "grad": "Lebane",
        "opstina": "Rafuna",
        "lokacija": "Rafuna"
    },
    {
        "grad": "Lebane",
        "opstina": "Svinjarica",
        "lokacija": "Svinjarica"
    },
    {
        "grad": "Lebane",
        "opstina": "Sekicol",
        "lokacija": "Sekicol"
    },
    {
        "grad": "Lebane",
        "opstina": "Slišane",
        "lokacija": "Slišane"
    },
    {
        "grad": "Lebane",
        "opstina": "Togočevce",
        "lokacija": "Togočevce"
    },
    {
        "grad": "Lebane",
        "opstina": "Ćenovac",
        "lokacija": "Ćenovac"
    },
    {
        "grad": "Lebane",
        "opstina": "Cekavica",
        "lokacija": "Cekavica"
    },
    {
        "grad": "Lebane",
        "opstina": "Šarce",
        "lokacija": "Šarce"
    },
    {
        "grad": "Lebane",
        "opstina": "Šilovo",
        "lokacija": "Šilovo"
    },
    {
        "grad": "Lebane",
        "opstina": "Štulac",
        "lokacija": "Štulac"
    },
    {
        "grad": "Lebane",
        "opstina": "Šumane",
        "lokacija": "Šumane"
    },
    {
        "grad": "Leposavić",
        "opstina": "Leposavić",
        "lokacija": "Leposavić"
    },
    {
        "grad": "Leposavić",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Leposavić",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Leposavić",
        "opstina": "Bare",
        "lokacija": "Bare"
    },
    {
        "grad": "Leposavić",
        "opstina": "Belo Brdo",
        "lokacija": "Belo Brdo"
    },
    {
        "grad": "Leposavić",
        "opstina": "Beluće",
        "lokacija": "Beluće"
    },
    {
        "grad": "Leposavić",
        "opstina": "Berberište",
        "lokacija": "Berberište"
    },
    {
        "grad": "Leposavić",
        "opstina": "Bistrica",
        "lokacija": "Bistrica"
    },
    {
        "grad": "Leposavić",
        "opstina": "Borova",
        "lokacija": "Borova"
    },
    {
        "grad": "Leposavić",
        "opstina": "Borčane",
        "lokacija": "Borčane"
    },
    {
        "grad": "Leposavić",
        "opstina": "Brzance",
        "lokacija": "Brzance"
    },
    {
        "grad": "Leposavić",
        "opstina": "Vitanoviće",
        "lokacija": "Vitanoviće"
    },
    {
        "grad": "Leposavić",
        "opstina": "Vračevo",
        "lokacija": "Vračevo"
    },
    {
        "grad": "Leposavić",
        "opstina": "Vuča",
        "lokacija": "Vuča"
    },
    {
        "grad": "Leposavić",
        "opstina": "Gnježdane",
        "lokacija": "Gnježdane"
    },
    {
        "grad": "Leposavić",
        "opstina": "Gornji Krnjin",
        "lokacija": "Gornji Krnjin"
    },
    {
        "grad": "Leposavić",
        "opstina": "Graničane",
        "lokacija": "Graničane"
    },
    {
        "grad": "Leposavić",
        "opstina": "Grkaje",
        "lokacija": "Grkaje"
    },
    {
        "grad": "Leposavić",
        "opstina": "Guvnište",
        "lokacija": "Guvnište"
    },
    {
        "grad": "Leposavić",
        "opstina": "Gulije",
        "lokacija": "Gulije"
    },
    {
        "grad": "Leposavić",
        "opstina": "Desetak",
        "lokacija": "Desetak"
    },
    {
        "grad": "Leposavić",
        "opstina": "Dobrava",
        "lokacija": "Dobrava"
    },
    {
        "grad": "Leposavić",
        "opstina": "Donje Isevo",
        "lokacija": "Donje Isevo"
    },
    {
        "grad": "Leposavić",
        "opstina": "Donji Krnjin",
        "lokacija": "Donji Krnjin"
    },
    {
        "grad": "Leposavić",
        "opstina": "Dren",
        "lokacija": "Dren"
    },
    {
        "grad": "Leposavić",
        "opstina": "Duboka",
        "lokacija": "Duboka"
    },
    {
        "grad": "Leposavić",
        "opstina": "Zabrđe",
        "lokacija": "Zabrđe"
    },
    {
        "grad": "Leposavić",
        "opstina": "Zavrata",
        "lokacija": "Zavrata"
    },
    {
        "grad": "Leposavić",
        "opstina": "Zemanica",
        "lokacija": "Zemanica"
    },
    {
        "grad": "Leposavić",
        "opstina": "Zrnosek",
        "lokacija": "Zrnosek"
    },
    {
        "grad": "Leposavić",
        "opstina": "Ibarsko Postenje",
        "lokacija": "Ibarsko Postenje"
    },
    {
        "grad": "Leposavić",
        "opstina": "Jarinje",
        "lokacija": "Jarinje"
    },
    {
        "grad": "Leposavić",
        "opstina": "Jelakce",
        "lokacija": "Jelakce"
    },
    {
        "grad": "Leposavić",
        "opstina": "Jošanica",
        "lokacija": "Jošanica"
    },
    {
        "grad": "Leposavić",
        "opstina": "Kajkovo",
        "lokacija": "Kajkovo"
    },
    {
        "grad": "Leposavić",
        "opstina": "Kamenica",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Leposavić",
        "opstina": "Kijevčiće",
        "lokacija": "Kijevčiće"
    },
    {
        "grad": "Leposavić",
        "opstina": "Koporiće",
        "lokacija": "Koporiće"
    },
    {
        "grad": "Leposavić",
        "opstina": "Kostin Potok",
        "lokacija": "Kostin Potok"
    },
    {
        "grad": "Leposavić",
        "opstina": "Košutica",
        "lokacija": "Košutica"
    },
    {
        "grad": "Leposavić",
        "opstina": "Košutovo",
        "lokacija": "Košutovo"
    },
    {
        "grad": "Leposavić",
        "opstina": "Kruševo",
        "lokacija": "Kruševo"
    },
    {
        "grad": "Leposavić",
        "opstina": "Kruščica",
        "lokacija": "Kruščica"
    },
    {
        "grad": "Leposavić",
        "opstina": "Kutnje",
        "lokacija": "Kutnje"
    },
    {
        "grad": "Leposavić",
        "opstina": "Lazine",
        "lokacija": "Lazine"
    },
    {
        "grad": "Leposavić",
        "opstina": "Lešak",
        "lokacija": "Lešak"
    },
    {
        "grad": "Leposavić",
        "opstina": "Lozno",
        "lokacija": "Lozno"
    },
    {
        "grad": "Leposavić",
        "opstina": "Majdevo",
        "lokacija": "Majdevo"
    },
    {
        "grad": "Leposavić",
        "opstina": "Mekiniće",
        "lokacija": "Mekiniće"
    },
    {
        "grad": "Leposavić",
        "opstina": "Miokoviće",
        "lokacija": "Miokoviće"
    },
    {
        "grad": "Leposavić",
        "opstina": "Mioliće",
        "lokacija": "Mioliće"
    },
    {
        "grad": "Leposavić",
        "opstina": "Mošnica",
        "lokacija": "Mošnica"
    },
    {
        "grad": "Leposavić",
        "opstina": "Ostraće",
        "lokacija": "Ostraće"
    },
    {
        "grad": "Leposavić",
        "opstina": "Plakaonica",
        "lokacija": "Plakaonica"
    },
    {
        "grad": "Leposavić",
        "opstina": "Planinica",
        "lokacija": "Planinica"
    },
    {
        "grad": "Leposavić",
        "opstina": "Popovce",
        "lokacija": "Popovce"
    },
    {
        "grad": "Leposavić",
        "opstina": "Potkomlje",
        "lokacija": "Potkomlje"
    },
    {
        "grad": "Leposavić",
        "opstina": "Pridvorica",
        "lokacija": "Pridvorica"
    },
    {
        "grad": "Leposavić",
        "opstina": "Rvatska",
        "lokacija": "Rvatska"
    },
    {
        "grad": "Leposavić",
        "opstina": "Rodelj",
        "lokacija": "Rodelj"
    },
    {
        "grad": "Leposavić",
        "opstina": "Rucmance",
        "lokacija": "Rucmance"
    },
    {
        "grad": "Leposavić",
        "opstina": "Seoce",
        "lokacija": "Seoce"
    },
    {
        "grad": "Leposavić",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Leposavić",
        "opstina": "Sočanica",
        "lokacija": "Sočanica"
    },
    {
        "grad": "Leposavić",
        "opstina": "Tvrđan",
        "lokacija": "Tvrđan"
    },
    {
        "grad": "Leposavić",
        "opstina": "Trebiće",
        "lokacija": "Trebiće"
    },
    {
        "grad": "Leposavić",
        "opstina": "Trikose",
        "lokacija": "Trikose"
    },
    {
        "grad": "Leposavić",
        "opstina": "Ćirkoviće",
        "lokacija": "Ćirkoviće"
    },
    {
        "grad": "Leposavić",
        "opstina": "Ulije",
        "lokacija": "Ulije"
    },
    {
        "grad": "Leposavić",
        "opstina": "Ceranja",
        "lokacija": "Ceranja"
    },
    {
        "grad": "Leposavić",
        "opstina": "Crveni",
        "lokacija": "Crveni"
    },
    {
        "grad": "Leposavić",
        "opstina": "Crnatovo",
        "lokacija": "Crnatovo"
    },
    {
        "grad": "Leposavić",
        "opstina": "Šaljska Bistrica",
        "lokacija": "Šaljska Bistrica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Leskovac",
        "lokacija": "Leskovac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "ATD"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Vaskovo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Dubočica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Zatvor"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Zele Veljković"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kosta Stamenković"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kumalak"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Morava"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Ohridsko Naselje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Podrum"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Prva Južnomoravska Brigada"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Rade Žunić"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Radničko Naselje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Solidarnost"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Hisar"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Čifluk Mira"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Štrkovo Naselje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Babičko",
        "lokacija": "Babičko"
    },
    {
        "grad": "Leskovac",
        "opstina": "Badince",
        "lokacija": "Badince"
    },
    {
        "grad": "Leskovac",
        "opstina": "Barje",
        "lokacija": "Barje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Belanovce",
        "lokacija": "Belanovce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Beli Potok",
        "lokacija": "Beli Potok"
    },
    {
        "grad": "Leskovac",
        "opstina": "Bistrica",
        "lokacija": "Bistrica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Bobište",
        "lokacija": "Bobište"
    },
    {
        "grad": "Leskovac",
        "opstina": "Bogojevce",
        "lokacija": "Bogojevce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Bojišina",
        "lokacija": "Bojišina"
    },
    {
        "grad": "Leskovac",
        "opstina": "Boćevica",
        "lokacija": "Boćevica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Bratmilovce",
        "lokacija": "Bratmilovce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Brejanovce",
        "lokacija": "Brejanovce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Brestovac",
        "lokacija": "Brestovac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Brza",
        "lokacija": "Brza"
    },
    {
        "grad": "Leskovac",
        "opstina": "Bričevlje",
        "lokacija": "Bričevlje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Bukova Glava",
        "lokacija": "Bukova Glava"
    },
    {
        "grad": "Leskovac",
        "opstina": "Bunuški Čifluk",
        "lokacija": "Bunuški Čifluk"
    },
    {
        "grad": "Leskovac",
        "opstina": "Velika Biljanica",
        "lokacija": "Velika Biljanica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Velika Grabovnica",
        "lokacija": "Velika Grabovnica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Velika Kopašnica",
        "lokacija": "Velika Kopašnica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Velika Sejanica",
        "lokacija": "Velika Sejanica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Veliko Trnjane",
        "lokacija": "Veliko Trnjane"
    },
    {
        "grad": "Leskovac",
        "opstina": "Vilje Kolo",
        "lokacija": "Vilje Kolo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Vina",
        "lokacija": "Vina"
    },
    {
        "grad": "Leskovac",
        "opstina": "Vinarce",
        "lokacija": "Vinarce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Vlase",
        "lokacija": "Vlase"
    },
    {
        "grad": "Leskovac",
        "opstina": "Vučje",
        "lokacija": "Vučje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gagince",
        "lokacija": "Gagince"
    },
    {
        "grad": "Leskovac",
        "opstina": "Golema Njiva",
        "lokacija": "Golema Njiva"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gorina",
        "lokacija": "Gorina"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gornja Bunuša",
        "lokacija": "Gornja Bunuša"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gornja Jajina",
        "lokacija": "Gornja Jajina"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gornja Kupinovica",
        "lokacija": "Gornja Kupinovica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gornja Lokošnica",
        "lokacija": "Gornja Lokošnica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gornja Slatina",
        "lokacija": "Gornja Slatina"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gornje Krajince",
        "lokacija": "Gornje Krajince"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gornje Sinkovce",
        "lokacija": "Gornje Sinkovce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gornje Stopanje",
        "lokacija": "Gornje Stopanje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gornje Trnjane",
        "lokacija": "Gornje Trnjane"
    },
    {
        "grad": "Leskovac",
        "opstina": "Gornji Bunibrod",
        "lokacija": "Gornji Bunibrod"
    },
    {
        "grad": "Leskovac",
        "opstina": "gradašnica",
        "lokacija": "gradašnica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Grajevce",
        "lokacija": "Grajevce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Graovo",
        "lokacija": "Graovo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Grdanica",
        "lokacija": "Grdanica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Grdelica (varoš)",
        "lokacija": "Grdelica (varoš)"
    },
    {
        "grad": "Leskovac",
        "opstina": "Grdelica (selo)",
        "lokacija": "Grdelica (selo)"
    },
    {
        "grad": "Leskovac",
        "opstina": "Guberevac",
        "lokacija": "Guberevac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Dedina Bara",
        "lokacija": "Dedina Bara"
    },
    {
        "grad": "Leskovac",
        "opstina": "Dobrotin",
        "lokacija": "Dobrotin"
    },
    {
        "grad": "Leskovac",
        "opstina": "Donja Bunuša",
        "lokacija": "Donja Bunuša"
    },
    {
        "grad": "Leskovac",
        "opstina": "Donja Jajina",
        "lokacija": "Donja Jajina"
    },
    {
        "grad": "Leskovac",
        "opstina": "Donja Kupinovica",
        "lokacija": "Donja Kupinovica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Donja Lokošnica",
        "lokacija": "Donja Lokošnica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Donja Slatina",
        "lokacija": "Donja Slatina"
    },
    {
        "grad": "Leskovac",
        "opstina": "Donje Brijanje",
        "lokacija": "Donje Brijanje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Donje Krajince",
        "lokacija": "Donje Krajince"
    },
    {
        "grad": "Leskovac",
        "opstina": "Donje Sinkovce",
        "lokacija": "Donje Sinkovce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Donje Stopanje",
        "lokacija": "Donje Stopanje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Donje Trnjane",
        "lokacija": "Donje Trnjane"
    },
    {
        "grad": "Leskovac",
        "opstina": "Donji Bunibrod",
        "lokacija": "Donji Bunibrod"
    },
    {
        "grad": "Leskovac",
        "opstina": "Draškovac",
        "lokacija": "Draškovac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Drvodelja",
        "lokacija": "Drvodelja"
    },
    {
        "grad": "Leskovac",
        "opstina": "Drćevac",
        "lokacija": "Drćevac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Dušanovo",
        "lokacija": "Dušanovo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Žabljane",
        "lokacija": "Žabljane"
    },
    {
        "grad": "Leskovac",
        "opstina": "Živkovo",
        "lokacija": "Živkovo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Žižavica",
        "lokacija": "Žižavica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Zagužane",
        "lokacija": "Zagužane"
    },
    {
        "grad": "Leskovac",
        "opstina": "Zalužnje",
        "lokacija": "Zalužnje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Zlokućane",
        "lokacija": "Zlokućane"
    },
    {
        "grad": "Leskovac",
        "opstina": "Zloćudovo",
        "lokacija": "Zloćudovo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Zoljevo",
        "lokacija": "Zoljevo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Igrište",
        "lokacija": "Igrište"
    },
    {
        "grad": "Leskovac",
        "opstina": "Jarsenovo",
        "lokacija": "Jarsenovo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Jašunja",
        "lokacija": "Jašunja"
    },
    {
        "grad": "Leskovac",
        "opstina": "Jelašnica",
        "lokacija": "Jelašnica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Kaluđerce",
        "lokacija": "Kaluđerce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Karađorđevac",
        "lokacija": "Karađorđevac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Kaštavar",
        "lokacija": "Kaštavar"
    },
    {
        "grad": "Leskovac",
        "opstina": "Kovačeva Bara",
        "lokacija": "Kovačeva Bara"
    },
    {
        "grad": "Leskovac",
        "opstina": "Kozare",
        "lokacija": "Kozare"
    },
    {
        "grad": "Leskovac",
        "opstina": "Koraćevac",
        "lokacija": "Koraćevac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Krpejce",
        "lokacija": "Krpejce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Kukulovce",
        "lokacija": "Kukulovce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Kumarevo",
        "lokacija": "Kumarevo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Kutleš",
        "lokacija": "Kutleš"
    },
    {
        "grad": "Leskovac",
        "opstina": "Lipovica",
        "lokacija": "Lipovica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Ličin Dol",
        "lokacija": "Ličin Dol"
    },
    {
        "grad": "Leskovac",
        "opstina": "Mala Biljanica",
        "lokacija": "Mala Biljanica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Mala Grabovnica",
        "lokacija": "Mala Grabovnica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Mala Kopašnica",
        "lokacija": "Mala Kopašnica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Manojlovce",
        "lokacija": "Manojlovce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Međa",
        "lokacija": "Međa"
    },
    {
        "grad": "Leskovac",
        "opstina": "Melovo",
        "lokacija": "Melovo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Milanovo",
        "lokacija": "Milanovo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Miroševce",
        "lokacija": "Miroševce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Mrkovica",
        "lokacija": "Mrkovica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Mrštane",
        "lokacija": "Mrštane"
    },
    {
        "grad": "Leskovac",
        "opstina": "Navalin",
        "lokacija": "Navalin"
    },
    {
        "grad": "Leskovac",
        "opstina": "Nakrivanj",
        "lokacija": "Nakrivanj"
    },
    {
        "grad": "Leskovac",
        "opstina": "Nesvrta",
        "lokacija": "Nesvrta"
    },
    {
        "grad": "Leskovac",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Nomanica",
        "lokacija": "Nomanica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Oraovica (kod Grdelice)",
        "lokacija": "Oraovica (kod Grdelice)"
    },
    {
        "grad": "Leskovac",
        "opstina": "Oraovica (kod Crkovnice)",
        "lokacija": "Oraovica (kod Crkovnice)"
    },
    {
        "grad": "Leskovac",
        "opstina": "Orašac",
        "lokacija": "Orašac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Oruglica",
        "lokacija": "Oruglica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Padež",
        "lokacija": "Padež"
    },
    {
        "grad": "Leskovac",
        "opstina": "Palikuća",
        "lokacija": "Palikuća"
    },
    {
        "grad": "Leskovac",
        "opstina": "Palojce",
        "lokacija": "Palojce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Petrovac",
        "lokacija": "Petrovac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Pečenjevce",
        "lokacija": "Pečenjevce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Piskupovo",
        "lokacija": "Piskupovo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Podrimce",
        "lokacija": "Podrimce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Predejane (varoš)",
        "lokacija": "Predejane (varoš)"
    },
    {
        "grad": "Leskovac",
        "opstina": "Predejane (selo)",
        "lokacija": "Predejane (selo)"
    },
    {
        "grad": "Leskovac",
        "opstina": "Presečina",
        "lokacija": "Presečina"
    },
    {
        "grad": "Leskovac",
        "opstina": "Priboj",
        "lokacija": "Priboj"
    },
    {
        "grad": "Leskovac",
        "opstina": "Ravni Del",
        "lokacija": "Ravni Del"
    },
    {
        "grad": "Leskovac",
        "opstina": "Radonjica",
        "lokacija": "Radonjica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Razgojna",
        "lokacija": "Razgojna"
    },
    {
        "grad": "Leskovac",
        "opstina": "Rajno Polje",
        "lokacija": "Rajno Polje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Rudare",
        "lokacija": "Rudare"
    },
    {
        "grad": "Leskovac",
        "opstina": "Svirce",
        "lokacija": "Svirce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Slavujevce",
        "lokacija": "Slavujevce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Leskovac",
        "opstina": "Smrdan",
        "lokacija": "Smrdan"
    },
    {
        "grad": "Leskovac",
        "opstina": "Strojkovce",
        "lokacija": "Strojkovce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Stupnica",
        "lokacija": "Stupnica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Suševlje",
        "lokacija": "Suševlje"
    },
    {
        "grad": "Leskovac",
        "opstina": "Todorovce",
        "lokacija": "Todorovce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Tulovo",
        "lokacija": "Tulovo"
    },
    {
        "grad": "Leskovac",
        "opstina": "Tupalovce",
        "lokacija": "Tupalovce"
    },
    {
        "grad": "Leskovac",
        "opstina": "Turekovac",
        "lokacija": "Turekovac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Crveni Breg",
        "lokacija": "Crveni Breg"
    },
    {
        "grad": "Leskovac",
        "opstina": "Crkovnica",
        "lokacija": "Crkovnica"
    },
    {
        "grad": "Leskovac",
        "opstina": "Crcavac",
        "lokacija": "Crcavac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Čekmin",
        "lokacija": "Čekmin"
    },
    {
        "grad": "Leskovac",
        "opstina": "Čifluk Razgojnski",
        "lokacija": "Čifluk Razgojnski"
    },
    {
        "grad": "Leskovac",
        "opstina": "Čukljenik",
        "lokacija": "Čukljenik"
    },
    {
        "grad": "Leskovac",
        "opstina": "Šainovac",
        "lokacija": "Šainovac"
    },
    {
        "grad": "Leskovac",
        "opstina": "Šarlince",
        "lokacija": "Šarlince"
    },
    {
        "grad": "Leskovac",
        "opstina": "Šišince",
        "lokacija": "Šišince"
    },
    {
        "grad": "Lipljan",
        "opstina": "Lipljan",
        "lokacija": "Lipljan"
    },
    {
        "grad": "Lipljan",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Lipljan",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Lipljan",
        "opstina": "Androvac",
        "lokacija": "Androvac"
    },
    {
        "grad": "Lipljan",
        "opstina": "Bandulić",
        "lokacija": "Bandulić"
    },
    {
        "grad": "Lipljan",
        "opstina": "Banjica",
        "lokacija": "Banjica"
    },
    {
        "grad": "Lipljan",
        "opstina": "Brus",
        "lokacija": "Brus"
    },
    {
        "grad": "Lipljan",
        "opstina": "Bujance",
        "lokacija": "Bujance"
    },
    {
        "grad": "Lipljan",
        "opstina": "Bukovica",
        "lokacija": "Bukovica"
    },
    {
        "grad": "Lipljan",
        "opstina": "Varigovce",
        "lokacija": "Varigovce"
    },
    {
        "grad": "Lipljan",
        "opstina": "Velika Dobranja",
        "lokacija": "Velika Dobranja"
    },
    {
        "grad": "Lipljan",
        "opstina": "Veliki Alaš",
        "lokacija": "Veliki Alaš"
    },
    {
        "grad": "Lipljan",
        "opstina": "Veliko Ribare",
        "lokacija": "Veliko Ribare"
    },
    {
        "grad": "Lipljan",
        "opstina": "Vogačica",
        "lokacija": "Vogačica"
    },
    {
        "grad": "Lipljan",
        "opstina": "Vrelo",
        "lokacija": "Vrelo"
    },
    {
        "grad": "Lipljan",
        "opstina": "Vrševce",
        "lokacija": "Vrševce"
    },
    {
        "grad": "Lipljan",
        "opstina": "Glavica",
        "lokacija": "Glavica"
    },
    {
        "grad": "Lipljan",
        "opstina": "Glanica",
        "lokacija": "Glanica"
    },
    {
        "grad": "Lipljan",
        "opstina": "Glogovce",
        "lokacija": "Glogovce"
    },
    {
        "grad": "Lipljan",
        "opstina": "Goleško Vrelo",
        "lokacija": "Goleško Vrelo"
    },
    {
        "grad": "Lipljan",
        "opstina": "Gornja Gušterica",
        "lokacija": "Gornja Gušterica"
    },
    {
        "grad": "Lipljan",
        "opstina": "Gornje Gadimlje",
        "lokacija": "Gornje Gadimlje"
    },
    {
        "grad": "Lipljan",
        "opstina": "Guvno Selo",
        "lokacija": "Guvno Selo"
    },
    {
        "grad": "Lipljan",
        "opstina": "Divljaka",
        "lokacija": "Divljaka"
    },
    {
        "grad": "Lipljan",
        "opstina": "Dobrotin",
        "lokacija": "Dobrotin"
    },
    {
        "grad": "Lipljan",
        "opstina": "Donja Gušterica",
        "lokacija": "Donja Gušterica"
    },
    {
        "grad": "Lipljan",
        "opstina": "Donje Gadimlje",
        "lokacija": "Donje Gadimlje"
    },
    {
        "grad": "Lipljan",
        "opstina": "Zlokućane",
        "lokacija": "Zlokućane"
    },
    {
        "grad": "Lipljan",
        "opstina": "Janjevo",
        "lokacija": "Janjevo"
    },
    {
        "grad": "Lipljan",
        "opstina": "Klečka",
        "lokacija": "Klečka"
    },
    {
        "grad": "Lipljan",
        "opstina": "Konjsko",
        "lokacija": "Konjsko"
    },
    {
        "grad": "Lipljan",
        "opstina": "Konjuh",
        "lokacija": "Konjuh"
    },
    {
        "grad": "Lipljan",
        "opstina": "Krajište",
        "lokacija": "Krajište"
    },
    {
        "grad": "Lipljan",
        "opstina": "Krajmirovce",
        "lokacija": "Krajmirovce"
    },
    {
        "grad": "Lipljan",
        "opstina": "Laletić",
        "lokacija": "Laletić"
    },
    {
        "grad": "Lipljan",
        "opstina": "Lepina",
        "lokacija": "Lepina"
    },
    {
        "grad": "Lipljan",
        "opstina": "Livađe",
        "lokacija": "Livađe"
    },
    {
        "grad": "Lipljan",
        "opstina": "Lipovica",
        "lokacija": "Lipovica"
    },
    {
        "grad": "Lipljan",
        "opstina": "Lug",
        "lokacija": "Lug"
    },
    {
        "grad": "Lipljan",
        "opstina": "Lugadžija",
        "lokacija": "Lugadžija"
    },
    {
        "grad": "Lipljan",
        "opstina": "Magura",
        "lokacija": "Magura"
    },
    {
        "grad": "Lipljan",
        "opstina": "Mala Dobranja",
        "lokacija": "Mala Dobranja"
    },
    {
        "grad": "Lipljan",
        "opstina": "Mali Alaš",
        "lokacija": "Mali Alaš"
    },
    {
        "grad": "Lipljan",
        "opstina": "Malo Gracko",
        "lokacija": "Malo Gracko"
    },
    {
        "grad": "Lipljan",
        "opstina": "Malo Ribare",
        "lokacija": "Malo Ribare"
    },
    {
        "grad": "Lipljan",
        "opstina": "Marevce",
        "lokacija": "Marevce"
    },
    {
        "grad": "Lipljan",
        "opstina": "Medvece",
        "lokacija": "Medvece"
    },
    {
        "grad": "Lipljan",
        "opstina": "Mirena",
        "lokacija": "Mirena"
    },
    {
        "grad": "Lipljan",
        "opstina": "Muhadžer Babuš",
        "lokacija": "Muhadžer Babuš"
    },
    {
        "grad": "Lipljan",
        "opstina": "Novo Rujce",
        "lokacija": "Novo Rujce"
    },
    {
        "grad": "Lipljan",
        "opstina": "Oklap",
        "lokacija": "Oklap"
    },
    {
        "grad": "Lipljan",
        "opstina": "Okosnica",
        "lokacija": "Okosnica"
    },
    {
        "grad": "Lipljan",
        "opstina": "Plitković",
        "lokacija": "Plitković"
    },
    {
        "grad": "Lipljan",
        "opstina": "Poturovce",
        "lokacija": "Poturovce"
    },
    {
        "grad": "Lipljan",
        "opstina": "Rabovce",
        "lokacija": "Rabovce"
    },
    {
        "grad": "Lipljan",
        "opstina": "Radevo",
        "lokacija": "Radevo"
    },
    {
        "grad": "Lipljan",
        "opstina": "Rusinovce",
        "lokacija": "Rusinovce"
    },
    {
        "grad": "Lipljan",
        "opstina": "Sedlare",
        "lokacija": "Sedlare"
    },
    {
        "grad": "Lipljan",
        "opstina": "Skulanevo",
        "lokacija": "Skulanevo"
    },
    {
        "grad": "Lipljan",
        "opstina": "Slovinje",
        "lokacija": "Slovinje"
    },
    {
        "grad": "Lipljan",
        "opstina": "Smoluša",
        "lokacija": "Smoluša"
    },
    {
        "grad": "Lipljan",
        "opstina": "Staro Gracko",
        "lokacija": "Staro Gracko"
    },
    {
        "grad": "Lipljan",
        "opstina": "Staro Rujce",
        "lokacija": "Staro Rujce"
    },
    {
        "grad": "Lipljan",
        "opstina": "Suvi Do",
        "lokacija": "Suvi Do"
    },
    {
        "grad": "Lipljan",
        "opstina": "Teća",
        "lokacija": "Teća"
    },
    {
        "grad": "Lipljan",
        "opstina": "Topličane",
        "lokacija": "Topličane"
    },
    {
        "grad": "Lipljan",
        "opstina": "Torina",
        "lokacija": "Torina"
    },
    {
        "grad": "Lipljan",
        "opstina": "Trbovce",
        "lokacija": "Trbovce"
    },
    {
        "grad": "Lipljan",
        "opstina": "Crni Breg",
        "lokacija": "Crni Breg"
    },
    {
        "grad": "Lipljan",
        "opstina": "Čelopek",
        "lokacija": "Čelopek"
    },
    {
        "grad": "Lipljan",
        "opstina": "Čučuljaga",
        "lokacija": "Čučuljaga"
    },
    {
        "grad": "Lipljan",
        "opstina": "Šišarka",
        "lokacija": "Šišarka"
    },
    {
        "grad": "Loznica",
        "opstina": "Loznica",
        "lokacija": "Loznica"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Banjski Šor"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "gradilište"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Kličevac"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Klupci"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Krajišnici"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Lagator"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Lamele"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Lozničko Polje"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Naselje"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Crnogora"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Šabački put"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Šanac"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Loznica",
        "opstina": "Gradska lokacija",
        "lokacija": "Šulovača"
    },
    {
        "grad": "Loznica",
        "opstina": "Banja Badanja",
        "lokacija": "Banja Badanja"
    },
    {
        "grad": "Loznica",
        "opstina": "Banja Koviljača",
        "lokacija": "Banja Koviljača"
    },
    {
        "grad": "Loznica",
        "opstina": "Baščeluci",
        "lokacija": "Baščeluci"
    },
    {
        "grad": "Loznica",
        "opstina": "Bradić",
        "lokacija": "Bradić"
    },
    {
        "grad": "Loznica",
        "opstina": "Brezjak",
        "lokacija": "Brezjak"
    },
    {
        "grad": "Loznica",
        "opstina": "Brnjac",
        "lokacija": "Brnjac"
    },
    {
        "grad": "Loznica",
        "opstina": "Veliko Selo",
        "lokacija": "Veliko Selo"
    },
    {
        "grad": "Loznica",
        "opstina": "Voćnjak",
        "lokacija": "Voćnjak"
    },
    {
        "grad": "Loznica",
        "opstina": "Gornja Badanja",
        "lokacija": "Gornja Badanja"
    },
    {
        "grad": "Loznica",
        "opstina": "Gornja Borina",
        "lokacija": "Gornja Borina"
    },
    {
        "grad": "Loznica",
        "opstina": "Gornja Koviljača",
        "lokacija": "Gornja Koviljača"
    },
    {
        "grad": "Loznica",
        "opstina": "Gornja Sipulja",
        "lokacija": "Gornja Sipulja"
    },
    {
        "grad": "Loznica",
        "opstina": "Gornje Nedeljice",
        "lokacija": "Gornje Nedeljice"
    },
    {
        "grad": "Loznica",
        "opstina": "Gornji Dobrić",
        "lokacija": "Gornji Dobrić"
    },
    {
        "grad": "Loznica",
        "opstina": "Grnčara",
        "lokacija": "Grnčara"
    },
    {
        "grad": "Loznica",
        "opstina": "Donja Badanja",
        "lokacija": "Donja Badanja"
    },
    {
        "grad": "Loznica",
        "opstina": "Donja Sipulja",
        "lokacija": "Donja Sipulja"
    },
    {
        "grad": "Loznica",
        "opstina": "Donje Nedeljice",
        "lokacija": "Donje Nedeljice"
    },
    {
        "grad": "Loznica",
        "opstina": "Donji Dobrić",
        "lokacija": "Donji Dobrić"
    },
    {
        "grad": "Loznica",
        "opstina": "Draginac",
        "lokacija": "Draginac"
    },
    {
        "grad": "Loznica",
        "opstina": "Zajača",
        "lokacija": "Zajača"
    },
    {
        "grad": "Loznica",
        "opstina": "Jadranska Lešnica",
        "lokacija": "Jadranska Lešnica"
    },
    {
        "grad": "Loznica",
        "opstina": "Jarebice",
        "lokacija": "Jarebice"
    },
    {
        "grad": "Loznica",
        "opstina": "Jelav",
        "lokacija": "Jelav"
    },
    {
        "grad": "Loznica",
        "opstina": "Joševa",
        "lokacija": "Joševa"
    },
    {
        "grad": "Loznica",
        "opstina": "Jugovići",
        "lokacija": "Jugovići"
    },
    {
        "grad": "Loznica",
        "opstina": "Kamenica",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Loznica",
        "opstina": "Kozjak",
        "lokacija": "Kozjak"
    },
    {
        "grad": "Loznica",
        "opstina": "Korenita",
        "lokacija": "Korenita"
    },
    {
        "grad": "Loznica",
        "opstina": "Lešnica",
        "lokacija": "Lešnica"
    },
    {
        "grad": "Loznica",
        "opstina": "Lipnica",
        "lokacija": "Lipnica"
    },
    {
        "grad": "Loznica",
        "opstina": "Lipnički Šor",
        "lokacija": "Lipnički Šor"
    },
    {
        "grad": "Loznica",
        "opstina": "Milina",
        "lokacija": "Milina"
    },
    {
        "grad": "Loznica",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Loznica",
        "opstina": "Paskovac",
        "lokacija": "Paskovac"
    },
    {
        "grad": "Loznica",
        "opstina": "Ploča",
        "lokacija": "Ploča"
    },
    {
        "grad": "Loznica",
        "opstina": "Pomijača",
        "lokacija": "Pomijača"
    },
    {
        "grad": "Loznica",
        "opstina": "Ribarice",
        "lokacija": "Ribarice"
    },
    {
        "grad": "Loznica",
        "opstina": "Runjani",
        "lokacija": "Runjani"
    },
    {
        "grad": "Loznica",
        "opstina": "Simino Brdo",
        "lokacija": "Simino Brdo"
    },
    {
        "grad": "Loznica",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Loznica",
        "opstina": "Straža",
        "lokacija": "Straža"
    },
    {
        "grad": "Loznica",
        "opstina": "Stupnica",
        "lokacija": "Stupnica"
    },
    {
        "grad": "Loznica",
        "opstina": "Tekeriš",
        "lokacija": "Tekeriš"
    },
    {
        "grad": "Loznica",
        "opstina": "Trbosilje",
        "lokacija": "Trbosilje"
    },
    {
        "grad": "Loznica",
        "opstina": "Trbušnica",
        "lokacija": "Trbušnica"
    },
    {
        "grad": "Loznica",
        "opstina": "Tršić",
        "lokacija": "Tršić"
    },
    {
        "grad": "Loznica",
        "opstina": "Filipovići",
        "lokacija": "Filipovići"
    },
    {
        "grad": "Loznica",
        "opstina": "Cikote",
        "lokacija": "Cikote"
    },
    {
        "grad": "Loznica",
        "opstina": "Čokešina",
        "lokacija": "Čokešina"
    },
    {
        "grad": "Loznica",
        "opstina": "Šurice",
        "lokacija": "Šurice"
    },
    {
        "grad": "Lučani",
        "opstina": "Lučani",
        "lokacija": "Lučani"
    },
    {
        "grad": "Lučani",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Lučani",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Lučani",
        "opstina": "Beli Kamen",
        "lokacija": "Beli Kamen"
    },
    {
        "grad": "Lučani",
        "opstina": "Viča",
        "lokacija": "Viča"
    },
    {
        "grad": "Lučani",
        "opstina": "Vlasteljice",
        "lokacija": "Vlasteljice"
    },
    {
        "grad": "Lučani",
        "opstina": "Vučkovica",
        "lokacija": "Vučkovica"
    },
    {
        "grad": "Lučani",
        "opstina": "Goračići",
        "lokacija": "Goračići"
    },
    {
        "grad": "Lučani",
        "opstina": "Gornja Kravarica",
        "lokacija": "Gornja Kravarica"
    },
    {
        "grad": "Lučani",
        "opstina": "Gornji Dubac",
        "lokacija": "Gornji Dubac"
    },
    {
        "grad": "Lučani",
        "opstina": "Grab",
        "lokacija": "Grab"
    },
    {
        "grad": "Lučani",
        "opstina": "Guberevci",
        "lokacija": "Guberevci"
    },
    {
        "grad": "Lučani",
        "opstina": "Guča",
        "lokacija": "Guča"
    },
    {
        "grad": "Lučani",
        "opstina": "Guča Selo",
        "lokacija": "Guča Selo"
    },
    {
        "grad": "Lučani",
        "opstina": "Dljin",
        "lokacija": "Dljin"
    },
    {
        "grad": "Lučani",
        "opstina": "Donja Kravarica",
        "lokacija": "Donja Kravarica"
    },
    {
        "grad": "Lučani",
        "opstina": "Donji Dubac",
        "lokacija": "Donji Dubac"
    },
    {
        "grad": "Lučani",
        "opstina": "Dučalovići",
        "lokacija": "Dučalovići"
    },
    {
        "grad": "Lučani",
        "opstina": "Đerađ",
        "lokacija": "Đerađ"
    },
    {
        "grad": "Lučani",
        "opstina": "Živica",
        "lokacija": "Živica"
    },
    {
        "grad": "Lučani",
        "opstina": "Zeoke",
        "lokacija": "Zeoke"
    },
    {
        "grad": "Lučani",
        "opstina": "Kaona",
        "lokacija": "Kaona"
    },
    {
        "grad": "Lučani",
        "opstina": "Kotraža",
        "lokacija": "Kotraža"
    },
    {
        "grad": "Lučani",
        "opstina": "Krivača",
        "lokacija": "Krivača"
    },
    {
        "grad": "Lučani",
        "opstina": "Krstac",
        "lokacija": "Krstac"
    },
    {
        "grad": "Lučani",
        "opstina": "Lis",
        "lokacija": "Lis"
    },
    {
        "grad": "Lučani",
        "opstina": "Lisice",
        "lokacija": "Lisice"
    },
    {
        "grad": "Lučani",
        "opstina": "Lučani Selo",
        "lokacija": "Lučani Selo"
    },
    {
        "grad": "Lučani",
        "opstina": "Markovica",
        "lokacija": "Markovica"
    },
    {
        "grad": "Lučani",
        "opstina": "Milatovići",
        "lokacija": "Milatovići"
    },
    {
        "grad": "Lučani",
        "opstina": "Negrišori",
        "lokacija": "Negrišori"
    },
    {
        "grad": "Lučani",
        "opstina": "Puhovo",
        "lokacija": "Puhovo"
    },
    {
        "grad": "Lučani",
        "opstina": "Pšanik",
        "lokacija": "Pšanik"
    },
    {
        "grad": "Lučani",
        "opstina": "Rogača",
        "lokacija": "Rogača"
    },
    {
        "grad": "Lučani",
        "opstina": "Rtari",
        "lokacija": "Rtari"
    },
    {
        "grad": "Lučani",
        "opstina": "Rti",
        "lokacija": "Rti"
    },
    {
        "grad": "Lučani",
        "opstina": "Tijanje",
        "lokacija": "Tijanje"
    },
    {
        "grad": "Lučani",
        "opstina": "Turica",
        "lokacija": "Turica"
    },
    {
        "grad": "Ljig",
        "opstina": "Ljig",
        "lokacija": "Ljig"
    },
    {
        "grad": "Ljig",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Ljig",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Ljig",
        "opstina": "Ba",
        "lokacija": "Ba"
    },
    {
        "grad": "Ljig",
        "opstina": "Babajić",
        "lokacija": "Babajić"
    },
    {
        "grad": "Ljig",
        "opstina": "Belanovica",
        "lokacija": "Belanovica"
    },
    {
        "grad": "Ljig",
        "opstina": "Bošnjanović",
        "lokacija": "Bošnjanović"
    },
    {
        "grad": "Ljig",
        "opstina": "Brančić",
        "lokacija": "Brančić"
    },
    {
        "grad": "Ljig",
        "opstina": "Veliševac",
        "lokacija": "Veliševac"
    },
    {
        "grad": "Ljig",
        "opstina": "Gukoš",
        "lokacija": "Gukoš"
    },
    {
        "grad": "Ljig",
        "opstina": "Dići",
        "lokacija": "Dići"
    },
    {
        "grad": "Ljig",
        "opstina": "Donji Banjani",
        "lokacija": "Donji Banjani"
    },
    {
        "grad": "Ljig",
        "opstina": "Živkovci",
        "lokacija": "Živkovci"
    },
    {
        "grad": "Ljig",
        "opstina": "Ivanovci",
        "lokacija": "Ivanovci"
    },
    {
        "grad": "Ljig",
        "opstina": "Jajčić",
        "lokacija": "Jajčić"
    },
    {
        "grad": "Ljig",
        "opstina": "Kadina Luka",
        "lokacija": "Kadina Luka"
    },
    {
        "grad": "Ljig",
        "opstina": "Kalanjevci",
        "lokacija": "Kalanjevci"
    },
    {
        "grad": "Ljig",
        "opstina": "Kozelj",
        "lokacija": "Kozelj"
    },
    {
        "grad": "Ljig",
        "opstina": "Lalinci",
        "lokacija": "Lalinci"
    },
    {
        "grad": "Ljig",
        "opstina": "Latković",
        "lokacija": "Latković"
    },
    {
        "grad": "Ljig",
        "opstina": "Liplje",
        "lokacija": "Liplje"
    },
    {
        "grad": "Ljig",
        "opstina": "Milavac",
        "lokacija": "Milavac"
    },
    {
        "grad": "Ljig",
        "opstina": "Moravci",
        "lokacija": "Moravci"
    },
    {
        "grad": "Ljig",
        "opstina": "Paležnica",
        "lokacija": "Paležnica"
    },
    {
        "grad": "Ljig",
        "opstina": "Poljanice",
        "lokacija": "Poljanice"
    },
    {
        "grad": "Ljig",
        "opstina": "Rajac",
        "lokacija": "Rajac"
    },
    {
        "grad": "Ljig",
        "opstina": "Slavkovica",
        "lokacija": "Slavkovica"
    },
    {
        "grad": "Ljig",
        "opstina": "Cvetanovac",
        "lokacija": "Cvetanovac"
    },
    {
        "grad": "Ljig",
        "opstina": "Štavica",
        "lokacija": "Štavica"
    },
    {
        "grad": "Ljig",
        "opstina": "Šutci",
        "lokacija": "Šutci"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Ljubovija",
        "lokacija": "Ljubovija"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Gradska lokacija",
        "lokacija": "Vagan"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Gradska lokacija",
        "lokacija": "Đurinovac"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Gradska lokacija",
        "lokacija": "Čitluk"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Berlovine",
        "lokacija": "Berlovine"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Vrhpolje",
        "lokacija": "Vrhpolje"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Gornja Ljuboviđa",
        "lokacija": "Gornja Ljuboviđa"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Gornja Orovica",
        "lokacija": "Gornja Orovica"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Gornja Trešnjica",
        "lokacija": "Gornja Trešnjica"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Gornje Košlje",
        "lokacija": "Gornje Košlje"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Gračanica",
        "lokacija": "Gračanica"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Grčić",
        "lokacija": "Grčić"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Donja Ljuboviđa",
        "lokacija": "Donja Ljuboviđa"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Donja Orovica",
        "lokacija": "Donja Orovica"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Drlače",
        "lokacija": "Drlače"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Duboko",
        "lokacija": "Duboko"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Leović",
        "lokacija": "Leović"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Lonjin",
        "lokacija": "Lonjin"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Orovička Planina",
        "lokacija": "Orovička Planina"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Podnemić",
        "lokacija": "Podnemić"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Postenje",
        "lokacija": "Postenje"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Rujevac",
        "lokacija": "Rujevac"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Savković",
        "lokacija": "Savković"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Selanac",
        "lokacija": "Selanac"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Sokolac",
        "lokacija": "Sokolac"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Tornik",
        "lokacija": "Tornik"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Uzovnica",
        "lokacija": "Uzovnica"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Caparić",
        "lokacija": "Caparić"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Crnča",
        "lokacija": "Crnča"
    },
    {
        "grad": "Ljubovija",
        "opstina": "Čitluk",
        "lokacija": "Čitluk"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Majdanpek",
        "lokacija": "Majdanpek"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Gradska lokacija",
        "lokacija": "Bagremarci"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Gradska lokacija",
        "lokacija": "Vidikovac"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Boljetin",
        "lokacija": "Boljetin"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Vlaole",
        "lokacija": "Vlaole"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Golubinje",
        "lokacija": "Golubinje"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Debeli Lug",
        "lokacija": "Debeli Lug"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Donji Milanovac",
        "lokacija": "Donji Milanovac"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Jasikovo",
        "lokacija": "Jasikovo"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Klokočevac",
        "lokacija": "Klokočevac"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Lepenski Vir",
        "lokacija": "Lepenski Vir"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Leskovo",
        "lokacija": "Leskovo"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Miroč",
        "lokacija": "Miroč"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Mosna",
        "lokacija": "Mosna"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Rudna Glava",
        "lokacija": "Rudna Glava"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Topolnica",
        "lokacija": "Topolnica"
    },
    {
        "grad": "Majdanpek",
        "opstina": "Crnajka",
        "lokacija": "Crnajka"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Mali Zvornik",
        "lokacija": "Mali Zvornik"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Amajić",
        "lokacija": "Amajić"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Brasina",
        "lokacija": "Brasina"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Budišić",
        "lokacija": "Budišić"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Velika Reka",
        "lokacija": "Velika Reka"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Voljevci",
        "lokacija": "Voljevci"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Donja Borina",
        "lokacija": "Donja Borina"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Donja Trešnjica",
        "lokacija": "Donja Trešnjica"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Zvorničko Jezero",
        "lokacija": "Zvorničko Jezero"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Radalj",
        "lokacija": "Radalj"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Sakar",
        "lokacija": "Sakar"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Culine",
        "lokacija": "Culine"
    },
    {
        "grad": "Mali Zvornik",
        "opstina": "Čitluk",
        "lokacija": "Čitluk"
    },
    {
        "grad": "Mali Iđoš",
        "opstina": "Mali Iđoš",
        "lokacija": "Mali Iđoš"
    },
    {
        "grad": "Mali Iđoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Mali Iđoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Mali Iđoš",
        "opstina": "Lovćenac",
        "lokacija": "Lovćenac"
    },
    {
        "grad": "Mali Iđoš",
        "opstina": "Feketić",
        "lokacija": "Feketić"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Aljudovo",
        "lokacija": "Aljudovo"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Batuša",
        "lokacija": "Batuša"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Boževac",
        "lokacija": "Boževac"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Veliko Selo",
        "lokacija": "Veliko Selo"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Veliko Crniće",
        "lokacija": "Veliko Crniće"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Vrbnica",
        "lokacija": "Vrbnica"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Zabrega",
        "lokacija": "Zabrega"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Kalište",
        "lokacija": "Kalište"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Kobilje",
        "lokacija": "Kobilje"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Kravlji Do",
        "lokacija": "Kravlji Do"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Kula",
        "lokacija": "Kula"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Malo gradište",
        "lokacija": "Malo gradište"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Malo Crniće",
        "lokacija": "Malo Crniće"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Salakovac",
        "lokacija": "Salakovac"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Smoljinac",
        "lokacija": "Smoljinac"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Toponica",
        "lokacija": "Toponica"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Crljenac",
        "lokacija": "Crljenac"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Šapine",
        "lokacija": "Šapine"
    },
    {
        "grad": "Malo Crniće",
        "opstina": "Šljivovac",
        "lokacija": "Šljivovac"
    },
    {
        "grad": "Medveđa",
        "opstina": "Medveđa",
        "lokacija": "Medveđa"
    },
    {
        "grad": "Medveđa",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Medveđa",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Medveđa",
        "opstina": "Bogunovac",
        "lokacija": "Bogunovac"
    },
    {
        "grad": "Medveđa",
        "opstina": "Borovac",
        "lokacija": "Borovac"
    },
    {
        "grad": "Medveđa",
        "opstina": "Varadin",
        "lokacija": "Varadin"
    },
    {
        "grad": "Medveđa",
        "opstina": "Velika Braina",
        "lokacija": "Velika Braina"
    },
    {
        "grad": "Medveđa",
        "opstina": "Vrapce",
        "lokacija": "Vrapce"
    },
    {
        "grad": "Medveđa",
        "opstina": "Gazdare",
        "lokacija": "Gazdare"
    },
    {
        "grad": "Medveđa",
        "opstina": "Gornja Lapaštica",
        "lokacija": "Gornja Lapaštica"
    },
    {
        "grad": "Medveđa",
        "opstina": "Gornji Bučumet",
        "lokacija": "Gornji Bučumet"
    },
    {
        "grad": "Medveđa",
        "opstina": "Gornji Gajtan",
        "lokacija": "Gornji Gajtan"
    },
    {
        "grad": "Medveđa",
        "opstina": "Grbavce",
        "lokacija": "Grbavce"
    },
    {
        "grad": "Medveđa",
        "opstina": "Gubavce",
        "lokacija": "Gubavce"
    },
    {
        "grad": "Medveđa",
        "opstina": "Gurgutovo",
        "lokacija": "Gurgutovo"
    },
    {
        "grad": "Medveđa",
        "opstina": "Donja Lapaštica",
        "lokacija": "Donja Lapaštica"
    },
    {
        "grad": "Medveđa",
        "opstina": "Donji Bučumet",
        "lokacija": "Donji Bučumet"
    },
    {
        "grad": "Medveđa",
        "opstina": "Donji Gajtan",
        "lokacija": "Donji Gajtan"
    },
    {
        "grad": "Medveđa",
        "opstina": "Drence",
        "lokacija": "Drence"
    },
    {
        "grad": "Medveđa",
        "opstina": "Đulekare",
        "lokacija": "Đulekare"
    },
    {
        "grad": "Medveđa",
        "opstina": "Kapit",
        "lokacija": "Kapit"
    },
    {
        "grad": "Medveđa",
        "opstina": "Lece",
        "lokacija": "Lece"
    },
    {
        "grad": "Medveđa",
        "opstina": "Mala Braina",
        "lokacija": "Mala Braina"
    },
    {
        "grad": "Medveđa",
        "opstina": "Marovac",
        "lokacija": "Marovac"
    },
    {
        "grad": "Medveđa",
        "opstina": "Maćedonce",
        "lokacija": "Maćedonce"
    },
    {
        "grad": "Medveđa",
        "opstina": "Maćedonce (Retkocersko)",
        "lokacija": "Maćedonce (Retkocersko)"
    },
    {
        "grad": "Medveđa",
        "opstina": "Medevce",
        "lokacija": "Medevce"
    },
    {
        "grad": "Medveđa",
        "opstina": "Mrkonje",
        "lokacija": "Mrkonje"
    },
    {
        "grad": "Medveđa",
        "opstina": "Negosavlje",
        "lokacija": "Negosavlje"
    },
    {
        "grad": "Medveđa",
        "opstina": "Petrilje",
        "lokacija": "Petrilje"
    },
    {
        "grad": "Medveđa",
        "opstina": "Poroštica",
        "lokacija": "Poroštica"
    },
    {
        "grad": "Medveđa",
        "opstina": "Pusto Šilovo",
        "lokacija": "Pusto Šilovo"
    },
    {
        "grad": "Medveđa",
        "opstina": "Ravna Banja",
        "lokacija": "Ravna Banja"
    },
    {
        "grad": "Medveđa",
        "opstina": "Retkocer",
        "lokacija": "Retkocer"
    },
    {
        "grad": "Medveđa",
        "opstina": "Rujkovac",
        "lokacija": "Rujkovac"
    },
    {
        "grad": "Medveđa",
        "opstina": "Svirce",
        "lokacija": "Svirce"
    },
    {
        "grad": "Medveđa",
        "opstina": "Sijarina",
        "lokacija": "Sijarina"
    },
    {
        "grad": "Medveđa",
        "opstina": "Sijarinska Banja",
        "lokacija": "Sijarinska Banja"
    },
    {
        "grad": "Medveđa",
        "opstina": "Sponce",
        "lokacija": "Sponce"
    },
    {
        "grad": "Medveđa",
        "opstina": "Srednji Bučumet",
        "lokacija": "Srednji Bučumet"
    },
    {
        "grad": "Medveđa",
        "opstina": "Stara Banja",
        "lokacija": "Stara Banja"
    },
    {
        "grad": "Medveđa",
        "opstina": "Stubla",
        "lokacija": "Stubla"
    },
    {
        "grad": "Medveđa",
        "opstina": "Tulare",
        "lokacija": "Tulare"
    },
    {
        "grad": "Medveđa",
        "opstina": "Tupale",
        "lokacija": "Tupale"
    },
    {
        "grad": "Medveđa",
        "opstina": "Crni Vrh",
        "lokacija": "Crni Vrh"
    },
    {
        "grad": "Medveđa",
        "opstina": "Čokotin",
        "lokacija": "Čokotin"
    },
    {
        "grad": "Merošina",
        "opstina": "Merošina",
        "lokacija": "Merošina"
    },
    {
        "grad": "Merošina",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Merošina",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Merošina",
        "opstina": "Azbresnica",
        "lokacija": "Azbresnica"
    },
    {
        "grad": "Merošina",
        "opstina": "Aleksandrovo",
        "lokacija": "Aleksandrovo"
    },
    {
        "grad": "Merošina",
        "opstina": "Arbanasce",
        "lokacija": "Arbanasce"
    },
    {
        "grad": "Merošina",
        "opstina": "Balajnac",
        "lokacija": "Balajnac"
    },
    {
        "grad": "Merošina",
        "opstina": "Baličevac",
        "lokacija": "Baličevac"
    },
    {
        "grad": "Merošina",
        "opstina": "Batušinac",
        "lokacija": "Batušinac"
    },
    {
        "grad": "Merošina",
        "opstina": "Biljeg",
        "lokacija": "Biljeg"
    },
    {
        "grad": "Merošina",
        "opstina": "Brest",
        "lokacija": "Brest"
    },
    {
        "grad": "Merošina",
        "opstina": "Bučić",
        "lokacija": "Bučić"
    },
    {
        "grad": "Merošina",
        "opstina": "Gornja Rasovača",
        "lokacija": "Gornja Rasovača"
    },
    {
        "grad": "Merošina",
        "opstina": "gradište",
        "lokacija": "gradište"
    },
    {
        "grad": "Merošina",
        "opstina": "Devča",
        "lokacija": "Devča"
    },
    {
        "grad": "Merošina",
        "opstina": "Dešilovo",
        "lokacija": "Dešilovo"
    },
    {
        "grad": "Merošina",
        "opstina": "Donja Rasovača",
        "lokacija": "Donja Rasovača"
    },
    {
        "grad": "Merošina",
        "opstina": "Dudulajce",
        "lokacija": "Dudulajce"
    },
    {
        "grad": "Merošina",
        "opstina": "Jovanovac",
        "lokacija": "Jovanovac"
    },
    {
        "grad": "Merošina",
        "opstina": "Jug Bogdanovac",
        "lokacija": "Jug Bogdanovac"
    },
    {
        "grad": "Merošina",
        "opstina": "Kovanluk",
        "lokacija": "Kovanluk"
    },
    {
        "grad": "Merošina",
        "opstina": "Kostadinovac",
        "lokacija": "Kostadinovac"
    },
    {
        "grad": "Merošina",
        "opstina": "Krajkovac",
        "lokacija": "Krajkovac"
    },
    {
        "grad": "Merošina",
        "opstina": "Lepaja",
        "lokacija": "Lepaja"
    },
    {
        "grad": "Merošina",
        "opstina": "Mramorsko brdo",
        "lokacija": "Mramorsko brdo"
    },
    {
        "grad": "Merošina",
        "opstina": "Oblačina",
        "lokacija": "Oblačina"
    },
    {
        "grad": "Merošina",
        "opstina": "Padina",
        "lokacija": "Padina"
    },
    {
        "grad": "Merošina",
        "opstina": "Rožina",
        "lokacija": "Rožina"
    },
    {
        "grad": "Merošina",
        "opstina": "Čubura",
        "lokacija": "Čubura"
    },
    {
        "grad": "Mionica",
        "opstina": "Mionica (varošica)",
        "lokacija": "Mionica (varošica)"
    },
    {
        "grad": "Mionica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Mionica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Mionica",
        "opstina": "Banja Vrujci",
        "lokacija": "Banja Vrujci"
    },
    {
        "grad": "Mionica",
        "opstina": "Berkovac",
        "lokacija": "Berkovac"
    },
    {
        "grad": "Mionica",
        "opstina": "Brežđe",
        "lokacija": "Brežđe"
    },
    {
        "grad": "Mionica",
        "opstina": "Bukovac",
        "lokacija": "Bukovac"
    },
    {
        "grad": "Mionica",
        "opstina": "Velika Marišta",
        "lokacija": "Velika Marišta"
    },
    {
        "grad": "Mionica",
        "opstina": "Virovac",
        "lokacija": "Virovac"
    },
    {
        "grad": "Mionica",
        "opstina": "Vrtiglav",
        "lokacija": "Vrtiglav"
    },
    {
        "grad": "Mionica",
        "opstina": "Golubac",
        "lokacija": "Golubac"
    },
    {
        "grad": "Mionica",
        "opstina": "Gornji Lajkovac",
        "lokacija": "Gornji Lajkovac"
    },
    {
        "grad": "Mionica",
        "opstina": "Gornji Mušić",
        "lokacija": "Gornji Mušić"
    },
    {
        "grad": "Mionica",
        "opstina": "Gunjica",
        "lokacija": "Gunjica"
    },
    {
        "grad": "Mionica",
        "opstina": "Donji Mušić",
        "lokacija": "Donji Mušić"
    },
    {
        "grad": "Mionica",
        "opstina": "Dučić",
        "lokacija": "Dučić"
    },
    {
        "grad": "Mionica",
        "opstina": "Đurđevac",
        "lokacija": "Đurđevac"
    },
    {
        "grad": "Mionica",
        "opstina": "Klašnić",
        "lokacija": "Klašnić"
    },
    {
        "grad": "Mionica",
        "opstina": "Ključ",
        "lokacija": "Ključ"
    },
    {
        "grad": "Mionica",
        "opstina": "Komanice",
        "lokacija": "Komanice"
    },
    {
        "grad": "Mionica",
        "opstina": "Krčmar",
        "lokacija": "Krčmar"
    },
    {
        "grad": "Mionica",
        "opstina": "Maljević",
        "lokacija": "Maljević"
    },
    {
        "grad": "Mionica",
        "opstina": "Mionica (selo)",
        "lokacija": "Mionica (selo)"
    },
    {
        "grad": "Mionica",
        "opstina": "Mratišić",
        "lokacija": "Mratišić"
    },
    {
        "grad": "Mionica",
        "opstina": "Nanomir",
        "lokacija": "Nanomir"
    },
    {
        "grad": "Mionica",
        "opstina": "Osečenica",
        "lokacija": "Osečenica"
    },
    {
        "grad": "Mionica",
        "opstina": "Paštrić",
        "lokacija": "Paštrić"
    },
    {
        "grad": "Mionica",
        "opstina": "Planinica",
        "lokacija": "Planinica"
    },
    {
        "grad": "Mionica",
        "opstina": "Popadić",
        "lokacija": "Popadić"
    },
    {
        "grad": "Mionica",
        "opstina": "Radobić",
        "lokacija": "Radobić"
    },
    {
        "grad": "Mionica",
        "opstina": "Rajković",
        "lokacija": "Rajković"
    },
    {
        "grad": "Mionica",
        "opstina": "Rakari",
        "lokacija": "Rakari"
    },
    {
        "grad": "Mionica",
        "opstina": "Robaje",
        "lokacija": "Robaje"
    },
    {
        "grad": "Mionica",
        "opstina": "Sanković",
        "lokacija": "Sanković"
    },
    {
        "grad": "Mionica",
        "opstina": "Struganik",
        "lokacija": "Struganik"
    },
    {
        "grad": "Mionica",
        "opstina": "Tabanović",
        "lokacija": "Tabanović"
    },
    {
        "grad": "Mionica",
        "opstina": "Todorin Do",
        "lokacija": "Todorin Do"
    },
    {
        "grad": "Mionica",
        "opstina": "Tolić",
        "lokacija": "Tolić"
    },
    {
        "grad": "Mionica",
        "opstina": "Šušeoka",
        "lokacija": "Šušeoka"
    },
    {
        "grad": "Negotin",
        "opstina": "Negotin",
        "lokacija": "Negotin"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "Badnjevo"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "Borska Kolonija"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "Bukovski Put"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "Veljko Vlahović"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "Vrelo"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "gradište"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "Miloševski Put"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Kombinat"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "Radujevački Put"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "Rastoka"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Negotin",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Negotin",
        "opstina": "Aleksandrovac",
        "lokacija": "Aleksandrovac"
    },
    {
        "grad": "Negotin",
        "opstina": "Braćevac",
        "lokacija": "Braćevac"
    },
    {
        "grad": "Negotin",
        "opstina": "Brestovac",
        "lokacija": "Brestovac"
    },
    {
        "grad": "Negotin",
        "opstina": "Bukovče",
        "lokacija": "Bukovče"
    },
    {
        "grad": "Negotin",
        "opstina": "Veljkovo",
        "lokacija": "Veljkovo"
    },
    {
        "grad": "Negotin",
        "opstina": "Vidrovac",
        "lokacija": "Vidrovac"
    },
    {
        "grad": "Negotin",
        "opstina": "Vratna",
        "lokacija": "Vratna"
    },
    {
        "grad": "Negotin",
        "opstina": "Dupljane",
        "lokacija": "Dupljane"
    },
    {
        "grad": "Negotin",
        "opstina": "Dušanovac",
        "lokacija": "Dušanovac"
    },
    {
        "grad": "Negotin",
        "opstina": "Dušanovac",
        "lokacija": "Dušanovac - Kusjak"
    },
    {
        "grad": "Negotin",
        "opstina": "Jabukovac",
        "lokacija": "Jabukovac"
    },
    {
        "grad": "Negotin",
        "opstina": "Jasenica",
        "lokacija": "Jasenica"
    },
    {
        "grad": "Negotin",
        "opstina": "Karbulovo",
        "lokacija": "Karbulovo"
    },
    {
        "grad": "Negotin",
        "opstina": "Kobišnica",
        "lokacija": "Kobišnica"
    },
    {
        "grad": "Negotin",
        "opstina": "Kovilovo",
        "lokacija": "Kovilovo"
    },
    {
        "grad": "Negotin",
        "opstina": "Mala Kamenica",
        "lokacija": "Mala Kamenica"
    },
    {
        "grad": "Negotin",
        "opstina": "Malajnica",
        "lokacija": "Malajnica"
    },
    {
        "grad": "Negotin",
        "opstina": "Miloševo",
        "lokacija": "Miloševo"
    },
    {
        "grad": "Negotin",
        "opstina": "Mihajlovac",
        "lokacija": "Mihajlovac"
    },
    {
        "grad": "Negotin",
        "opstina": "Mokranje",
        "lokacija": "Mokranje"
    },
    {
        "grad": "Negotin",
        "opstina": "Plavna",
        "lokacija": "Plavna"
    },
    {
        "grad": "Negotin",
        "opstina": "Popovica",
        "lokacija": "Popovica"
    },
    {
        "grad": "Negotin",
        "opstina": "Prahovo",
        "lokacija": "Prahovo"
    },
    {
        "grad": "Negotin",
        "opstina": "Radujevac",
        "lokacija": "Radujevac"
    },
    {
        "grad": "Negotin",
        "opstina": "Rajac",
        "lokacija": "Rajac"
    },
    {
        "grad": "Negotin",
        "opstina": "Rečka",
        "lokacija": "Rečka"
    },
    {
        "grad": "Negotin",
        "opstina": "Rogljevo",
        "lokacija": "Rogljevo"
    },
    {
        "grad": "Negotin",
        "opstina": "Samarinovac",
        "lokacija": "Samarinovac"
    },
    {
        "grad": "Negotin",
        "opstina": "Sikole",
        "lokacija": "Sikole"
    },
    {
        "grad": "Negotin",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Negotin",
        "opstina": "Smedovac",
        "lokacija": "Smedovac"
    },
    {
        "grad": "Negotin",
        "opstina": "Srbovo",
        "lokacija": "Srbovo"
    },
    {
        "grad": "Negotin",
        "opstina": "Tamnič",
        "lokacija": "Tamnič"
    },
    {
        "grad": "Negotin",
        "opstina": "Trnjane",
        "lokacija": "Trnjane"
    },
    {
        "grad": "Negotin",
        "opstina": "Urovica",
        "lokacija": "Urovica"
    },
    {
        "grad": "Negotin",
        "opstina": "Crnomasnica",
        "lokacija": "Crnomasnica"
    },
    {
        "grad": "Negotin",
        "opstina": "Čubra",
        "lokacija": "Čubra"
    },
    {
        "grad": "Negotin",
        "opstina": "Šarkamen",
        "lokacija": "Šarkamen"
    },
    {
        "grad": "Negotin",
        "opstina": "Štubik",
        "lokacija": "Štubik"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Nova Varoš",
        "lokacija": "Nova Varoš"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Branoševac 1"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Branoševac 2"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Vionik"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Voćnjak"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Zebinovac"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Kuburovina"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Milanovac"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Petlovac"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Potočilo"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Šanac"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Akmačići",
        "lokacija": "Akmačići"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Amzići",
        "lokacija": "Amzići"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Bistrica",
        "lokacija": "Bistrica"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Božetići",
        "lokacija": "Božetići"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Brdo",
        "lokacija": "Brdo"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Bukovik",
        "lokacija": "Bukovik"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Burađa",
        "lokacija": "Burađa"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Vilovi",
        "lokacija": "Vilovi"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Vraneša",
        "lokacija": "Vraneša"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gornja Bela Reka",
        "lokacija": "Gornja Bela Reka"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Gornje Trudovo",
        "lokacija": "Gornje Trudovo"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Debelja",
        "lokacija": "Debelja"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Donja Bela Reka",
        "lokacija": "Donja Bela Reka"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Draglica",
        "lokacija": "Draglica"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Draževići",
        "lokacija": "Draževići"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Drmanovići",
        "lokacija": "Drmanovići"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Zlatar",
        "lokacija": "Zlatar"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Zlatarsko Jezero",
        "lokacija": "Zlatarsko Jezero"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Jasenovo",
        "lokacija": "Jasenovo"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Kokin Brod",
        "lokacija": "Kokin Brod"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Komarani",
        "lokacija": "Komarani"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Kućani",
        "lokacija": "Kućani"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Ljepojevići",
        "lokacija": "Ljepojevići"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Miševići",
        "lokacija": "Miševići"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Negbina",
        "lokacija": "Negbina"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Ojkovica",
        "lokacija": "Ojkovica"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Radijevići",
        "lokacija": "Radijevići"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Radoinja",
        "lokacija": "Radoinja"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Rutoši",
        "lokacija": "Rutoši"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Seništa",
        "lokacija": "Seništa"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Tisovica",
        "lokacija": "Tisovica"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Trudovo",
        "lokacija": "Trudovo"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Čelice",
        "lokacija": "Čelice"
    },
    {
        "grad": "Nova Varoš",
        "opstina": "Štitkovo",
        "lokacija": "Štitkovo"
    },
    {
        "grad": "Nova Crnja",
        "opstina": "Nova Crnja",
        "lokacija": "Nova Crnja"
    },
    {
        "grad": "Nova Crnja",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Nova Crnja",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Nova Crnja",
        "opstina": "Aleksandrovo",
        "lokacija": "Aleksandrovo"
    },
    {
        "grad": "Nova Crnja",
        "opstina": "Vojvoda Stepa",
        "lokacija": "Vojvoda Stepa"
    },
    {
        "grad": "Nova Crnja",
        "opstina": "Radojevo",
        "lokacija": "Radojevo"
    },
    {
        "grad": "Nova Crnja",
        "opstina": "Srpska Crnja",
        "lokacija": "Srpska Crnja"
    },
    {
        "grad": "Nova Crnja",
        "opstina": "Toba",
        "lokacija": "Toba"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Novi Bečej",
        "lokacija": "Novi Bečej"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Vranjevo"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Gerberov Blok"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Klemenov Blok"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Naselje"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Tisa"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Tiski Kej"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Bočar",
        "lokacija": "Bočar"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Kumane",
        "lokacija": "Kumane"
    },
    {
        "grad": "Novi Bečej",
        "opstina": "Novo Miloševo",
        "lokacija": "Novo Miloševo"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Novi Kneževac",
        "lokacija": "Novi Kneževac"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Gradska lokacija",
        "lokacija": "Tisa"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Banatsko Aranđelovo",
        "lokacija": "Banatsko Aranđelovo"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Đala",
        "lokacija": "Đala"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Majdan",
        "lokacija": "Majdan"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Podlokanj",
        "lokacija": "Podlokanj"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Rabe",
        "lokacija": "Rabe"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Siget",
        "lokacija": "Siget"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Srpski Krstur",
        "lokacija": "Srpski Krstur"
    },
    {
        "grad": "Novi Kneževac",
        "opstina": "Filić",
        "lokacija": "Filić"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Novi Pazar",
        "lokacija": "Novi Pazar"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Banja"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Bukreš"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Varevo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Varoš Mahala"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Deževski Put"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Erozija"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Jalija"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Lug"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Mur"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Osoje"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Paralovo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Parice"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Petlače"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Pobrđe"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Rasadnik"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Selakovac"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Svojbor"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Ćeremedžinica"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Hadžet"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Hotkovo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Čerkez Mahala"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Šaćirovići"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Šestovo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gradska lokacija",
        "lokacija": "Šutenovac"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Abuloviće",
        "lokacija": "Abuloviće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Bajevica",
        "lokacija": "Bajevica"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Bare",
        "lokacija": "Bare"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Batnjik",
        "lokacija": "Batnjik"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Bekova",
        "lokacija": "Bekova"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Bele Vode",
        "lokacija": "Bele Vode"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Boturovina",
        "lokacija": "Boturovina"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Brđani",
        "lokacija": "Brđani"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Brestovo",
        "lokacija": "Brestovo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Vever",
        "lokacija": "Vever"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Vidovo",
        "lokacija": "Vidovo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Vitkoviće",
        "lokacija": "Vitkoviće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Vojkoviće",
        "lokacija": "Vojkoviće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Vojniće",
        "lokacija": "Vojniće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Vranovina",
        "lokacija": "Vranovina"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Vučiniće",
        "lokacija": "Vučiniće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Vučja Lokva",
        "lokacija": "Vučja Lokva"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Golice",
        "lokacija": "Golice"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gornja Tušimlja",
        "lokacija": "Gornja Tušimlja"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Goševo",
        "lokacija": "Goševo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Građanoviće",
        "lokacija": "Građanoviće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Gračane",
        "lokacija": "Gračane"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Grubetiće",
        "lokacija": "Grubetiće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Deževa",
        "lokacija": "Deževa"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Dojeviće",
        "lokacija": "Dojeviće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Dojinoviće",
        "lokacija": "Dojinoviće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Dolac",
        "lokacija": "Dolac"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Doljani",
        "lokacija": "Doljani"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Dragočevo",
        "lokacija": "Dragočevo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Dramiće",
        "lokacija": "Dramiće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Žunjeviće",
        "lokacija": "Žunjeviće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Zabrđe",
        "lokacija": "Zabrđe"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Zaguljača",
        "lokacija": "Zaguljača"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Zlatare",
        "lokacija": "Zlatare"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Ivanča",
        "lokacija": "Ivanča"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Izbice",
        "lokacija": "Izbice"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Jablanica",
        "lokacija": "Jablanica"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Javor",
        "lokacija": "Javor"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Janča",
        "lokacija": "Janča"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Jova",
        "lokacija": "Jova"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Kašalj",
        "lokacija": "Kašalj"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Kovačevo",
        "lokacija": "Kovačevo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Kožlje",
        "lokacija": "Kožlje"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Koprivnica",
        "lokacija": "Koprivnica"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Kosuriće",
        "lokacija": "Kosuriće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Kruševo",
        "lokacija": "Kruševo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Kuzmičevo",
        "lokacija": "Kuzmičevo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Leča",
        "lokacija": "Leča"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Lopužnje",
        "lokacija": "Lopužnje"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Lukare",
        "lokacija": "Lukare"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Lukarsko Goševo",
        "lokacija": "Lukarsko Goševo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Lukocrevo",
        "lokacija": "Lukocrevo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Miščiće",
        "lokacija": "Miščiće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Muhovo",
        "lokacija": "Muhovo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Negotinac",
        "lokacija": "Negotinac"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Odojeviće",
        "lokacija": "Odojeviće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Okose",
        "lokacija": "Okose"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Osaonica",
        "lokacija": "Osaonica"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Oholje",
        "lokacija": "Oholje"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Pavlje",
        "lokacija": "Pavlje"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Pasji Potok",
        "lokacija": "Pasji Potok"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Pilareta",
        "lokacija": "Pilareta"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Požega",
        "lokacija": "Požega"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Požežina",
        "lokacija": "Požežina"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Polokce",
        "lokacija": "Polokce"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Pope",
        "lokacija": "Pope"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Postenje",
        "lokacija": "Postenje"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Prćenova",
        "lokacija": "Prćenova"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Pusta Tušimlja",
        "lokacija": "Pusta Tušimlja"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Pustovlah",
        "lokacija": "Pustovlah"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Radaljica",
        "lokacija": "Radaljica"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Rajetiće",
        "lokacija": "Rajetiće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Rajkoviće",
        "lokacija": "Rajkoviće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Rajčinoviće",
        "lokacija": "Rajčinoviće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Rajčinovićka Trnava",
        "lokacija": "Rajčinovićka Trnava"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Rakovac",
        "lokacija": "Rakovac"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Rast",
        "lokacija": "Rast"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Rohovo",
        "lokacija": "Rohovo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Sebečevo",
        "lokacija": "Sebečevo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Sitniče",
        "lokacija": "Sitniče"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Skukovo",
        "lokacija": "Skukovo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Smilov Laz",
        "lokacija": "Smilov Laz"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Srednja Tušimlja",
        "lokacija": "Srednja Tušimlja"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Stradovo",
        "lokacija": "Stradovo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Sudsko Selo",
        "lokacija": "Sudsko Selo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Tenkovo",
        "lokacija": "Tenkovo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Trnava",
        "lokacija": "Trnava"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Tunovo",
        "lokacija": "Tunovo"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Cokoviće",
        "lokacija": "Cokoviće"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Čašić Dolac",
        "lokacija": "Čašić Dolac"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Šavci",
        "lokacija": "Šavci"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Šaronje",
        "lokacija": "Šaronje"
    },
    {
        "grad": "Novi Pazar",
        "opstina": "Štitare",
        "lokacija": "Štitare"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Novo Brdo",
        "lokacija": "Novo Brdo"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Bostane",
        "lokacija": "Bostane"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Zebince",
        "lokacija": "Zebince"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Izvor",
        "lokacija": "Izvor"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Jasenovik",
        "lokacija": "Jasenovik"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Klobukar",
        "lokacija": "Klobukar"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Labljane",
        "lokacija": "Labljane"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Manišince",
        "lokacija": "Manišince"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Prekovce",
        "lokacija": "Prekovce"
    },
    {
        "grad": "Novo Brdo",
        "opstina": "Trnićevce",
        "lokacija": "Trnićevce"
    },
    {
        "grad": "Obilić",
        "opstina": "Obilić",
        "lokacija": "Obilić"
    },
    {
        "grad": "Obilić",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Obilić",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Obilić",
        "opstina": "Ade",
        "lokacija": "Ade"
    },
    {
        "grad": "Obilić",
        "opstina": "Babin Most",
        "lokacija": "Babin Most"
    },
    {
        "grad": "Obilić",
        "opstina": "Bakšija",
        "lokacija": "Bakšija"
    },
    {
        "grad": "Obilić",
        "opstina": "Breznica",
        "lokacija": "Breznica"
    },
    {
        "grad": "Obilić",
        "opstina": "Gornji Grabovac",
        "lokacija": "Gornji Grabovac"
    },
    {
        "grad": "Obilić",
        "opstina": "Kruševac",
        "lokacija": "Kruševac"
    },
    {
        "grad": "Obilić",
        "opstina": "Lazarevo",
        "lokacija": "Lazarevo"
    },
    {
        "grad": "Obilić",
        "opstina": "Leskovčić",
        "lokacija": "Leskovčić"
    },
    {
        "grad": "Obilić",
        "opstina": "Mazgit",
        "lokacija": "Mazgit"
    },
    {
        "grad": "Obilić",
        "opstina": "Miloševo",
        "lokacija": "Miloševo"
    },
    {
        "grad": "Obilić",
        "opstina": "Plemetina",
        "lokacija": "Plemetina"
    },
    {
        "grad": "Obilić",
        "opstina": "Raskovo",
        "lokacija": "Raskovo"
    },
    {
        "grad": "Obilić",
        "opstina": "Rudnik Kosovo",
        "lokacija": "Rudnik Kosovo"
    },
    {
        "grad": "Obilić",
        "opstina": "Sibovac",
        "lokacija": "Sibovac"
    },
    {
        "grad": "Obilić",
        "opstina": "Hamidija",
        "lokacija": "Hamidija"
    },
    {
        "grad": "Obilić",
        "opstina": "Crkvena Vodica",
        "lokacija": "Crkvena Vodica"
    },
    {
        "grad": "Obilić",
        "opstina": "Šipitula",
        "lokacija": "Šipitula"
    },
    {
        "grad": "Opovo",
        "opstina": "Opovo",
        "lokacija": "Opovo"
    },
    {
        "grad": "Opovo",
        "opstina": "Gradska lokacija",
        "lokacija": "Kertiz"
    },
    {
        "grad": "Opovo",
        "opstina": "Gradska lokacija",
        "lokacija": "Tamiš"
    },
    {
        "grad": "Opovo",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Opovo",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Opovo",
        "opstina": "Baranda",
        "lokacija": "Baranda"
    },
    {
        "grad": "Opovo",
        "opstina": "Sakule",
        "lokacija": "Sakule"
    },
    {
        "grad": "Opovo",
        "opstina": "Sefkerin",
        "lokacija": "Sefkerin"
    },
    {
        "grad": "Orahovac",
        "opstina": "Orahovac",
        "lokacija": "Orahovac"
    },
    {
        "grad": "Orahovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Orahovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Orahovac",
        "opstina": "Bela Crkva",
        "lokacija": "Bela Crkva"
    },
    {
        "grad": "Orahovac",
        "opstina": "Bratotin",
        "lokacija": "Bratotin"
    },
    {
        "grad": "Orahovac",
        "opstina": "Brestovac",
        "lokacija": "Brestovac"
    },
    {
        "grad": "Orahovac",
        "opstina": "Brnjača",
        "lokacija": "Brnjača"
    },
    {
        "grad": "Orahovac",
        "opstina": "Bublje",
        "lokacija": "Bublje"
    },
    {
        "grad": "Orahovac",
        "opstina": "Velika Kruša",
        "lokacija": "Velika Kruša"
    },
    {
        "grad": "Orahovac",
        "opstina": "Velika Hoča",
        "lokacija": "Velika Hoča"
    },
    {
        "grad": "Orahovac",
        "opstina": "Vranjak",
        "lokacija": "Vranjak"
    },
    {
        "grad": "Orahovac",
        "opstina": "Gedža",
        "lokacija": "Gedža"
    },
    {
        "grad": "Orahovac",
        "opstina": "Goračevo",
        "lokacija": "Goračevo"
    },
    {
        "grad": "Orahovac",
        "opstina": "Gorić",
        "lokacija": "Gorić"
    },
    {
        "grad": "Orahovac",
        "opstina": "Gornje Potočane",
        "lokacija": "Gornje Potočane"
    },
    {
        "grad": "Orahovac",
        "opstina": "Danjane",
        "lokacija": "Danjane"
    },
    {
        "grad": "Orahovac",
        "opstina": "Dobri Dol",
        "lokacija": "Dobri Dol"
    },
    {
        "grad": "Orahovac",
        "opstina": "Domanek",
        "lokacija": "Domanek"
    },
    {
        "grad": "Orahovac",
        "opstina": "Donje Potočane",
        "lokacija": "Donje Potočane"
    },
    {
        "grad": "Orahovac",
        "opstina": "Dragobilje",
        "lokacija": "Dragobilje"
    },
    {
        "grad": "Orahovac",
        "opstina": "Drenovac",
        "lokacija": "Drenovac"
    },
    {
        "grad": "Orahovac",
        "opstina": "Zatrić",
        "lokacija": "Zatrić"
    },
    {
        "grad": "Orahovac",
        "opstina": "Zočište",
        "lokacija": "Zočište"
    },
    {
        "grad": "Orahovac",
        "opstina": "Zrze",
        "lokacija": "Zrze"
    },
    {
        "grad": "Orahovac",
        "opstina": "Jančište",
        "lokacija": "Jančište"
    },
    {
        "grad": "Orahovac",
        "opstina": "Jović",
        "lokacija": "Jović"
    },
    {
        "grad": "Orahovac",
        "opstina": "Koznik",
        "lokacija": "Koznik"
    },
    {
        "grad": "Orahovac",
        "opstina": "Kramovik",
        "lokacija": "Kramovik"
    },
    {
        "grad": "Orahovac",
        "opstina": "Labučevo",
        "lokacija": "Labučevo"
    },
    {
        "grad": "Orahovac",
        "opstina": "Ljubižda",
        "lokacija": "Ljubižda"
    },
    {
        "grad": "Orahovac",
        "opstina": "Mađare",
        "lokacija": "Mađare"
    },
    {
        "grad": "Orahovac",
        "opstina": "Mala Hoča",
        "lokacija": "Mala Hoča"
    },
    {
        "grad": "Orahovac",
        "opstina": "Mališevo",
        "lokacija": "Mališevo"
    },
    {
        "grad": "Orahovac",
        "opstina": "Milanović",
        "lokacija": "Milanović"
    },
    {
        "grad": "Orahovac",
        "opstina": "Miruša",
        "lokacija": "Miruša"
    },
    {
        "grad": "Orahovac",
        "opstina": "Moralija",
        "lokacija": "Moralija"
    },
    {
        "grad": "Orahovac",
        "opstina": "Mrasor",
        "lokacija": "Mrasor"
    },
    {
        "grad": "Orahovac",
        "opstina": "Našpale",
        "lokacija": "Našpale"
    },
    {
        "grad": "Orahovac",
        "opstina": "Nogavac",
        "lokacija": "Nogavac"
    },
    {
        "grad": "Orahovac",
        "opstina": "Opteruša",
        "lokacija": "Opteruša"
    },
    {
        "grad": "Orahovac",
        "opstina": "Ostrozub",
        "lokacija": "Ostrozub"
    },
    {
        "grad": "Orahovac",
        "opstina": "Pagaruša",
        "lokacija": "Pagaruša"
    },
    {
        "grad": "Orahovac",
        "opstina": "Petković",
        "lokacija": "Petković"
    },
    {
        "grad": "Orahovac",
        "opstina": "Poluža",
        "lokacija": "Poluža"
    },
    {
        "grad": "Orahovac",
        "opstina": "Ponorac",
        "lokacija": "Ponorac"
    },
    {
        "grad": "Orahovac",
        "opstina": "Pusto Selo",
        "lokacija": "Pusto Selo"
    },
    {
        "grad": "Orahovac",
        "opstina": "Radoste",
        "lokacija": "Radoste"
    },
    {
        "grad": "Orahovac",
        "opstina": "Ratkovac",
        "lokacija": "Ratkovac"
    },
    {
        "grad": "Orahovac",
        "opstina": "Retimlje",
        "lokacija": "Retimlje"
    },
    {
        "grad": "Orahovac",
        "opstina": "Sanovac",
        "lokacija": "Sanovac"
    },
    {
        "grad": "Orahovac",
        "opstina": "Saroš",
        "lokacija": "Saroš"
    },
    {
        "grad": "Orahovac",
        "opstina": "Sopnić",
        "lokacija": "Sopnić"
    },
    {
        "grad": "Orahovac",
        "opstina": "Turjak",
        "lokacija": "Turjak"
    },
    {
        "grad": "Orahovac",
        "opstina": "Celina",
        "lokacija": "Celina"
    },
    {
        "grad": "Orahovac",
        "opstina": "Crnovrana",
        "lokacija": "Crnovrana"
    },
    {
        "grad": "Orahovac",
        "opstina": "Čiflak",
        "lokacija": "Čiflak"
    },
    {
        "grad": "Orahovac",
        "opstina": "Čupevo",
        "lokacija": "Čupevo"
    },
    {
        "grad": "Osečina",
        "opstina": "Osečina",
        "lokacija": "Osečina"
    },
    {
        "grad": "Osečina",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Osečina",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Osečina",
        "opstina": "Bastav",
        "lokacija": "Bastav"
    },
    {
        "grad": "Osečina",
        "opstina": "Belotić",
        "lokacija": "Belotić"
    },
    {
        "grad": "Osečina",
        "opstina": "Bratačić",
        "lokacija": "Bratačić"
    },
    {
        "grad": "Osečina",
        "opstina": "Gornje Crniljevo",
        "lokacija": "Gornje Crniljevo"
    },
    {
        "grad": "Osečina",
        "opstina": "Gunjaci",
        "lokacija": "Gunjaci"
    },
    {
        "grad": "Osečina",
        "opstina": "Dragijevica",
        "lokacija": "Dragijevica"
    },
    {
        "grad": "Osečina",
        "opstina": "Dragodol",
        "lokacija": "Dragodol"
    },
    {
        "grad": "Osečina",
        "opstina": "Komirić",
        "lokacija": "Komirić"
    },
    {
        "grad": "Osečina",
        "opstina": "Konjic",
        "lokacija": "Konjic"
    },
    {
        "grad": "Osečina",
        "opstina": "Konjuša",
        "lokacija": "Konjuša"
    },
    {
        "grad": "Osečina",
        "opstina": "Lopatanj",
        "lokacija": "Lopatanj"
    },
    {
        "grad": "Osečina",
        "opstina": "Osečina (selo)",
        "lokacija": "Osečina (selo)"
    },
    {
        "grad": "Osečina",
        "opstina": "Ostružanj",
        "lokacija": "Ostružanj"
    },
    {
        "grad": "Osečina",
        "opstina": "Pecka",
        "lokacija": "Pecka"
    },
    {
        "grad": "Osečina",
        "opstina": "Plužac",
        "lokacija": "Plužac"
    },
    {
        "grad": "Osečina",
        "opstina": "Sirdija",
        "lokacija": "Sirdija"
    },
    {
        "grad": "Osečina",
        "opstina": "Skadar",
        "lokacija": "Skadar"
    },
    {
        "grad": "Osečina",
        "opstina": "Tuđin",
        "lokacija": "Tuđin"
    },
    {
        "grad": "Osečina",
        "opstina": "Carina",
        "lokacija": "Carina"
    },
    {
        "grad": "Odžaci",
        "opstina": "Odžaci",
        "lokacija": "Odžaci"
    },
    {
        "grad": "Odžaci",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Odžaci",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Odžaci",
        "opstina": "Bački Brestovac",
        "lokacija": "Bački Brestovac"
    },
    {
        "grad": "Odžaci",
        "opstina": "Bački Gračac",
        "lokacija": "Bački Gračac"
    },
    {
        "grad": "Odžaci",
        "opstina": "Bogojevo",
        "lokacija": "Bogojevo"
    },
    {
        "grad": "Odžaci",
        "opstina": "Deronje",
        "lokacija": "Deronje"
    },
    {
        "grad": "Odžaci",
        "opstina": "Karavukovo",
        "lokacija": "Karavukovo"
    },
    {
        "grad": "Odžaci",
        "opstina": "Lalić",
        "lokacija": "Lalić"
    },
    {
        "grad": "Odžaci",
        "opstina": "Ratkovo",
        "lokacija": "Ratkovo"
    },
    {
        "grad": "Odžaci",
        "opstina": "Srpski Miletić",
        "lokacija": "Srpski Miletić"
    },
    {
        "grad": "Pančevo",
        "opstina": "Pančevo",
        "lokacija": "Pančevo"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Vojlovica"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Gornji grad Margita"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Donji grad"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Zelengora"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Karaula"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Kotež 1"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Kotež 2"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Kudeljarski Nasip"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Mali Rit"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Misa Vinogradi"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Mladost"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Novi Svet"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Pepeljare"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Skrobara"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Sodara"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Stara Misa"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Stari Tamiš"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Strelište"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Tesla"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Tip Stanko"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Topola"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Utvina Kolonija"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Pančevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Pančevo",
        "opstina": "Banatski Brestovac",
        "lokacija": "Banatski Brestovac"
    },
    {
        "grad": "Pančevo",
        "opstina": "Banatsko Novo Selo",
        "lokacija": "Banatsko Novo Selo"
    },
    {
        "grad": "Pančevo",
        "opstina": "Bela Stena",
        "lokacija": "Bela Stena"
    },
    {
        "grad": "Pančevo",
        "opstina": "Glogonj",
        "lokacija": "Glogonj"
    },
    {
        "grad": "Pančevo",
        "opstina": "Dolovo",
        "lokacija": "Dolovo"
    },
    {
        "grad": "Pančevo",
        "opstina": "Ivanovo",
        "lokacija": "Ivanovo"
    },
    {
        "grad": "Pančevo",
        "opstina": "Jabuka",
        "lokacija": "Jabuka"
    },
    {
        "grad": "Pančevo",
        "opstina": "Kačarevo",
        "lokacija": "Kačarevo"
    },
    {
        "grad": "Pančevo",
        "opstina": "Omoljica",
        "lokacija": "Omoljica"
    },
    {
        "grad": "Pančevo",
        "opstina": "Starčevo",
        "lokacija": "Starčevo"
    },
    {
        "grad": "Pančevo",
        "opstina": "Starčevo",
        "lokacija": "Starčevo - Gornji Kraj"
    },
    {
        "grad": "Pančevo",
        "opstina": "Starčevo",
        "lokacija": "Starčevo - Donji Kraj"
    },
    {
        "grad": "Pančevo",
        "opstina": "Starčevo",
        "lokacija": "Starčevo - Radničko Naselje"
    },
    {
        "grad": "Pančevo",
        "opstina": "Starčevo",
        "lokacija": "Starčevo - Centar"
    },
    {
        "grad": "Pančevo",
        "opstina": "Starčevo",
        "lokacija": "Starčevo - Šumice"
    },
    {
        "grad": "Paraćin",
        "opstina": "Paraćin",
        "lokacija": "Paraćin"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "4. Juli"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "7. Juli"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "11. Kongres"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Branko Krsmanović"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Vrapčane"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Glodžak"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "gradski Stadion"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Dankovo"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Žabare"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Zmič"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Jagodnjak"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Karađorđevo Brdo"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Lozica"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Striško Naselje"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Tekija"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Paraćin",
        "opstina": "Bošnjane",
        "lokacija": "Bošnjane"
    },
    {
        "grad": "Paraćin",
        "opstina": "Buljane",
        "lokacija": "Buljane"
    },
    {
        "grad": "Paraćin",
        "opstina": "Busilovac",
        "lokacija": "Busilovac"
    },
    {
        "grad": "Paraćin",
        "opstina": "Glavica",
        "lokacija": "Glavica"
    },
    {
        "grad": "Paraćin",
        "opstina": "Golubovac",
        "lokacija": "Golubovac"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gornja Mutnica",
        "lokacija": "Gornja Mutnica"
    },
    {
        "grad": "Paraćin",
        "opstina": "Gornje Vidovo",
        "lokacija": "Gornje Vidovo"
    },
    {
        "grad": "Paraćin",
        "opstina": "Davidovac",
        "lokacija": "Davidovac"
    },
    {
        "grad": "Paraćin",
        "opstina": "Donja Mutnica",
        "lokacija": "Donja Mutnica"
    },
    {
        "grad": "Paraćin",
        "opstina": "Donje Vidovo",
        "lokacija": "Donje Vidovo"
    },
    {
        "grad": "Paraćin",
        "opstina": "Drenovac",
        "lokacija": "Drenovac"
    },
    {
        "grad": "Paraćin",
        "opstina": "Zabrega",
        "lokacija": "Zabrega"
    },
    {
        "grad": "Paraćin",
        "opstina": "Izvor",
        "lokacija": "Izvor"
    },
    {
        "grad": "Paraćin",
        "opstina": "Klačevica",
        "lokacija": "Klačevica"
    },
    {
        "grad": "Paraćin",
        "opstina": "Krežbinac",
        "lokacija": "Krežbinac"
    },
    {
        "grad": "Paraćin",
        "opstina": "Lebina",
        "lokacija": "Lebina"
    },
    {
        "grad": "Paraćin",
        "opstina": "Lešje",
        "lokacija": "Lešje"
    },
    {
        "grad": "Paraćin",
        "opstina": "Mirilovac",
        "lokacija": "Mirilovac"
    },
    {
        "grad": "Paraćin",
        "opstina": "Plana",
        "lokacija": "Plana"
    },
    {
        "grad": "Paraćin",
        "opstina": "Popovac",
        "lokacija": "Popovac"
    },
    {
        "grad": "Paraćin",
        "opstina": "Potočac",
        "lokacija": "Potočac"
    },
    {
        "grad": "Paraćin",
        "opstina": "Ratare",
        "lokacija": "Ratare"
    },
    {
        "grad": "Paraćin",
        "opstina": "Raševica",
        "lokacija": "Raševica"
    },
    {
        "grad": "Paraćin",
        "opstina": "Svojnovo",
        "lokacija": "Svojnovo"
    },
    {
        "grad": "Paraćin",
        "opstina": "Sikirica",
        "lokacija": "Sikirica"
    },
    {
        "grad": "Paraćin",
        "opstina": "Sinji Vir",
        "lokacija": "Sinji Vir"
    },
    {
        "grad": "Paraćin",
        "opstina": "Sisevac",
        "lokacija": "Sisevac"
    },
    {
        "grad": "Paraćin",
        "opstina": "Striža",
        "lokacija": "Striža"
    },
    {
        "grad": "Paraćin",
        "opstina": "Stubica",
        "lokacija": "Stubica"
    },
    {
        "grad": "Paraćin",
        "opstina": "Trešnjevica",
        "lokacija": "Trešnjevica"
    },
    {
        "grad": "Paraćin",
        "opstina": "Čepure",
        "lokacija": "Čepure"
    },
    {
        "grad": "Paraćin",
        "opstina": "Šavac",
        "lokacija": "Šavac"
    },
    {
        "grad": "Paraćin",
        "opstina": "Šaludovac",
        "lokacija": "Šaludovac"
    },
    {
        "grad": "Petrovac",
        "opstina": "Petrovac",
        "lokacija": "Petrovac"
    },
    {
        "grad": "Petrovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Petrovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Petrovac",
        "opstina": "Bistrica",
        "lokacija": "Bistrica"
    },
    {
        "grad": "Petrovac",
        "opstina": "Bošnjak",
        "lokacija": "Bošnjak"
    },
    {
        "grad": "Petrovac",
        "opstina": "Burovac",
        "lokacija": "Burovac"
    },
    {
        "grad": "Petrovac",
        "opstina": "Busur",
        "lokacija": "Busur"
    },
    {
        "grad": "Petrovac",
        "opstina": "Vezičevo",
        "lokacija": "Vezičevo"
    },
    {
        "grad": "Petrovac",
        "opstina": "Veliki Popovac",
        "lokacija": "Veliki Popovac"
    },
    {
        "grad": "Petrovac",
        "opstina": "Veliko Laole",
        "lokacija": "Veliko Laole"
    },
    {
        "grad": "Petrovac",
        "opstina": "Vitovnica",
        "lokacija": "Vitovnica"
    },
    {
        "grad": "Petrovac",
        "opstina": "Vošanovac",
        "lokacija": "Vošanovac"
    },
    {
        "grad": "Petrovac",
        "opstina": "Dobrnje",
        "lokacija": "Dobrnje"
    },
    {
        "grad": "Petrovac",
        "opstina": "Dubočka",
        "lokacija": "Dubočka"
    },
    {
        "grad": "Petrovac",
        "opstina": "Ždrelo",
        "lokacija": "Ždrelo"
    },
    {
        "grad": "Petrovac",
        "opstina": "Ždrelo",
        "lokacija": "Ždrelo - Banja Ždrelo"
    },
    {
        "grad": "Petrovac",
        "opstina": "Zabrđe",
        "lokacija": "Zabrđe"
    },
    {
        "grad": "Petrovac",
        "opstina": "Kamenovo",
        "lokacija": "Kamenovo"
    },
    {
        "grad": "Petrovac",
        "opstina": "Kladurovo",
        "lokacija": "Kladurovo"
    },
    {
        "grad": "Petrovac",
        "opstina": "Knežica",
        "lokacija": "Knežica"
    },
    {
        "grad": "Petrovac",
        "opstina": "Krvije",
        "lokacija": "Krvije"
    },
    {
        "grad": "Petrovac",
        "opstina": "Leskovac",
        "lokacija": "Leskovac"
    },
    {
        "grad": "Petrovac",
        "opstina": "Lopušnik",
        "lokacija": "Lopušnik"
    },
    {
        "grad": "Petrovac",
        "opstina": "Malo Laole",
        "lokacija": "Malo Laole"
    },
    {
        "grad": "Petrovac",
        "opstina": "Manastirica",
        "lokacija": "Manastirica"
    },
    {
        "grad": "Petrovac",
        "opstina": "Melnica",
        "lokacija": "Melnica"
    },
    {
        "grad": "Petrovac",
        "opstina": "Oreškovica",
        "lokacija": "Oreškovica"
    },
    {
        "grad": "Petrovac",
        "opstina": "Orljevo",
        "lokacija": "Orljevo"
    },
    {
        "grad": "Petrovac",
        "opstina": "Pankovo",
        "lokacija": "Pankovo"
    },
    {
        "grad": "Petrovac",
        "opstina": "Ranovac",
        "lokacija": "Ranovac"
    },
    {
        "grad": "Petrovac",
        "opstina": "Rašanac",
        "lokacija": "Rašanac"
    },
    {
        "grad": "Petrovac",
        "opstina": "Stamnica",
        "lokacija": "Stamnica"
    },
    {
        "grad": "Petrovac",
        "opstina": "Starčevo",
        "lokacija": "Starčevo"
    },
    {
        "grad": "Petrovac",
        "opstina": "Tabanovac",
        "lokacija": "Tabanovac"
    },
    {
        "grad": "Petrovac",
        "opstina": "Trnovče",
        "lokacija": "Trnovče"
    },
    {
        "grad": "Petrovac",
        "opstina": "Ćovdin",
        "lokacija": "Ćovdin"
    },
    {
        "grad": "Petrovac",
        "opstina": "Šetonje",
        "lokacija": "Šetonje"
    },
    {
        "grad": "Peć",
        "opstina": "Peć",
        "lokacija": "Peć"
    },
    {
        "grad": "Peć",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Peć",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Peć",
        "opstina": "Alagina Reka",
        "lokacija": "Alagina Reka"
    },
    {
        "grad": "Peć",
        "opstina": "Babiće",
        "lokacija": "Babiće"
    },
    {
        "grad": "Peć",
        "opstina": "Barane",
        "lokacija": "Barane"
    },
    {
        "grad": "Peć",
        "opstina": "Belo Polje",
        "lokacija": "Belo Polje"
    },
    {
        "grad": "Peć",
        "opstina": "Blagaje",
        "lokacija": "Blagaje"
    },
    {
        "grad": "Peć",
        "opstina": "Boge",
        "lokacija": "Boge"
    },
    {
        "grad": "Peć",
        "opstina": "Brežanik",
        "lokacija": "Brežanik"
    },
    {
        "grad": "Peć",
        "opstina": "Brestovik",
        "lokacija": "Brestovik"
    },
    {
        "grad": "Peć",
        "opstina": "Brolić",
        "lokacija": "Brolić"
    },
    {
        "grad": "Peć",
        "opstina": "Bučane",
        "lokacija": "Bučane"
    },
    {
        "grad": "Peć",
        "opstina": "Velika Jablanica",
        "lokacija": "Velika Jablanica"
    },
    {
        "grad": "Peć",
        "opstina": "Veliki Štupelj",
        "lokacija": "Veliki Štupelj"
    },
    {
        "grad": "Peć",
        "opstina": "Vitomirica",
        "lokacija": "Vitomirica"
    },
    {
        "grad": "Peć",
        "opstina": "Vragovac",
        "lokacija": "Vragovac"
    },
    {
        "grad": "Peć",
        "opstina": "Vranovac",
        "lokacija": "Vranovac"
    },
    {
        "grad": "Peć",
        "opstina": "Glavičica",
        "lokacija": "Glavičica"
    },
    {
        "grad": "Peć",
        "opstina": "Glođane",
        "lokacija": "Glođane"
    },
    {
        "grad": "Peć",
        "opstina": "Goraždevac",
        "lokacija": "Goraždevac"
    },
    {
        "grad": "Peć",
        "opstina": "Grabovac",
        "lokacija": "Grabovac"
    },
    {
        "grad": "Peć",
        "opstina": "Dobri Do",
        "lokacija": "Dobri Do"
    },
    {
        "grad": "Peć",
        "opstina": "Drelje",
        "lokacija": "Drelje"
    },
    {
        "grad": "Peć",
        "opstina": "Dubovo",
        "lokacija": "Dubovo"
    },
    {
        "grad": "Peć",
        "opstina": "Dubočak",
        "lokacija": "Dubočak"
    },
    {
        "grad": "Peć",
        "opstina": "Duganjive",
        "lokacija": "Duganjive"
    },
    {
        "grad": "Peć",
        "opstina": "Zagrmlje",
        "lokacija": "Zagrmlje"
    },
    {
        "grad": "Peć",
        "opstina": "Zahać",
        "lokacija": "Zahać"
    },
    {
        "grad": "Peć",
        "opstina": "Zlopek",
        "lokacija": "Zlopek"
    },
    {
        "grad": "Peć",
        "opstina": "Jablanica",
        "lokacija": "Jablanica"
    },
    {
        "grad": "Peć",
        "opstina": "Jošanica",
        "lokacija": "Jošanica"
    },
    {
        "grad": "Peć",
        "opstina": "Klinčina",
        "lokacija": "Klinčina"
    },
    {
        "grad": "Peć",
        "opstina": "Kosurić",
        "lokacija": "Kosurić"
    },
    {
        "grad": "Peć",
        "opstina": "Kotradić",
        "lokacija": "Kotradić"
    },
    {
        "grad": "Peć",
        "opstina": "Košutane",
        "lokacija": "Košutane"
    },
    {
        "grad": "Peć",
        "opstina": "Krstovac",
        "lokacija": "Krstovac"
    },
    {
        "grad": "Peć",
        "opstina": "Kruševac",
        "lokacija": "Kruševac"
    },
    {
        "grad": "Peć",
        "opstina": "Kućište",
        "lokacija": "Kućište"
    },
    {
        "grad": "Peć",
        "opstina": "Labljane",
        "lokacija": "Labljane"
    },
    {
        "grad": "Peć",
        "opstina": "Laz Belopać",
        "lokacija": "Laz Belopać"
    },
    {
        "grad": "Peć",
        "opstina": "Lipa",
        "lokacija": "Lipa"
    },
    {
        "grad": "Peć",
        "opstina": "Lođa",
        "lokacija": "Lođa"
    },
    {
        "grad": "Peć",
        "opstina": "Ložane",
        "lokacija": "Ložane"
    },
    {
        "grad": "Peć",
        "opstina": "Lugadžija",
        "lokacija": "Lugadžija"
    },
    {
        "grad": "Peć",
        "opstina": "Ljevoša",
        "lokacija": "Ljevoša"
    },
    {
        "grad": "Peć",
        "opstina": "Lješane",
        "lokacija": "Lješane"
    },
    {
        "grad": "Peć",
        "opstina": "Ljubenić",
        "lokacija": "Ljubenić"
    },
    {
        "grad": "Peć",
        "opstina": "Ljutoglava",
        "lokacija": "Ljutoglava"
    },
    {
        "grad": "Peć",
        "opstina": "Mala Jablanica",
        "lokacija": "Mala Jablanica"
    },
    {
        "grad": "Peć",
        "opstina": "Mali Štupelj",
        "lokacija": "Mali Štupelj"
    },
    {
        "grad": "Peć",
        "opstina": "Maljeviće",
        "lokacija": "Maljeviće"
    },
    {
        "grad": "Peć",
        "opstina": "Milovanac",
        "lokacija": "Milovanac"
    },
    {
        "grad": "Peć",
        "opstina": "Nabrđe",
        "lokacija": "Nabrđe"
    },
    {
        "grad": "Peć",
        "opstina": "Naklo",
        "lokacija": "Naklo"
    },
    {
        "grad": "Peć",
        "opstina": "Nepolje",
        "lokacija": "Nepolje"
    },
    {
        "grad": "Peć",
        "opstina": "Novi Raušić",
        "lokacija": "Novi Raušić"
    },
    {
        "grad": "Peć",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Peć",
        "opstina": "Ozrim",
        "lokacija": "Ozrim"
    },
    {
        "grad": "Peć",
        "opstina": "Osoje",
        "lokacija": "Osoje"
    },
    {
        "grad": "Peć",
        "opstina": "Pašino Selo",
        "lokacija": "Pašino Selo"
    },
    {
        "grad": "Peć",
        "opstina": "Pepiće",
        "lokacija": "Pepiće"
    },
    {
        "grad": "Peć",
        "opstina": "Pištane",
        "lokacija": "Pištane"
    },
    {
        "grad": "Peć",
        "opstina": "Plavljane",
        "lokacija": "Plavljane"
    },
    {
        "grad": "Peć",
        "opstina": "Počešće",
        "lokacija": "Počešće"
    },
    {
        "grad": "Peć",
        "opstina": "Radavac",
        "lokacija": "Radavac"
    },
    {
        "grad": "Peć",
        "opstina": "Raušić",
        "lokacija": "Raušić"
    },
    {
        "grad": "Peć",
        "opstina": "Rašić",
        "lokacija": "Rašić"
    },
    {
        "grad": "Peć",
        "opstina": "Romune",
        "lokacija": "Romune"
    },
    {
        "grad": "Peć",
        "opstina": "Rosulje",
        "lokacija": "Rosulje"
    },
    {
        "grad": "Peć",
        "opstina": "Ruhot",
        "lokacija": "Ruhot"
    },
    {
        "grad": "Peć",
        "opstina": "Svrke",
        "lokacija": "Svrke"
    },
    {
        "grad": "Peć",
        "opstina": "Siga",
        "lokacija": "Siga"
    },
    {
        "grad": "Peć",
        "opstina": "Trebović",
        "lokacija": "Trebović"
    },
    {
        "grad": "Peć",
        "opstina": "Trstenik",
        "lokacija": "Trstenik"
    },
    {
        "grad": "Peć",
        "opstina": "Turjak",
        "lokacija": "Turjak"
    },
    {
        "grad": "Peć",
        "opstina": "Ćuška",
        "lokacija": "Ćuška"
    },
    {
        "grad": "Peć",
        "opstina": "Hadžovići",
        "lokacija": "Hadžovići"
    },
    {
        "grad": "Peć",
        "opstina": "Crni Vrh",
        "lokacija": "Crni Vrh"
    },
    {
        "grad": "Peć",
        "opstina": "Čelopek",
        "lokacija": "Čelopek"
    },
    {
        "grad": "Peć",
        "opstina": "Čungur",
        "lokacija": "Čungur"
    },
    {
        "grad": "Peć",
        "opstina": "Škrelje",
        "lokacija": "Škrelje"
    },
    {
        "grad": "Pećinci",
        "opstina": "Pećinci",
        "lokacija": "Pećinci"
    },
    {
        "grad": "Pećinci",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Pećinci",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Pećinci",
        "opstina": "Ašanja",
        "lokacija": "Ašanja"
    },
    {
        "grad": "Pećinci",
        "opstina": "Brestač",
        "lokacija": "Brestač"
    },
    {
        "grad": "Pećinci",
        "opstina": "Deč",
        "lokacija": "Deč"
    },
    {
        "grad": "Pećinci",
        "opstina": "Donji Tovarnik",
        "lokacija": "Donji Tovarnik"
    },
    {
        "grad": "Pećinci",
        "opstina": "Karlovčić",
        "lokacija": "Karlovčić"
    },
    {
        "grad": "Pećinci",
        "opstina": "Kupinovo",
        "lokacija": "Kupinovo"
    },
    {
        "grad": "Pećinci",
        "opstina": "Obrež",
        "lokacija": "Obrež"
    },
    {
        "grad": "Pećinci",
        "opstina": "Ogar",
        "lokacija": "Ogar"
    },
    {
        "grad": "Pećinci",
        "opstina": "Popinci",
        "lokacija": "Popinci"
    },
    {
        "grad": "Pećinci",
        "opstina": "Prhovo",
        "lokacija": "Prhovo"
    },
    {
        "grad": "Pećinci",
        "opstina": "Sibač",
        "lokacija": "Sibač"
    },
    {
        "grad": "Pećinci",
        "opstina": "Sremski Mihaljevci",
        "lokacija": "Sremski Mihaljevci"
    },
    {
        "grad": "Pećinci",
        "opstina": "Subotište",
        "lokacija": "Subotište"
    },
    {
        "grad": "Pećinci",
        "opstina": "Šimanovci",
        "lokacija": "Šimanovci"
    },
    {
        "grad": "Pirot",
        "opstina": "Pirot",
        "lokacija": "Pirot"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "ATP"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Barije"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Berilovac"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Đeram"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Četvrt"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Jatagan Mala"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Kale"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Nova Mala"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Novi Zavoj"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Tigrovo Naselje"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Pazar"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Pirotski Kej"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Prisjansko Naselje"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Provalija"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Prčevac"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Radin Do"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Rogoz"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Sarlah"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Senjak"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Staro Tigrovo Naselje"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Tanasko Rajić"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Tijabara"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Cin Cin Kladenac"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Češalj"
    },
    {
        "grad": "Pirot",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Pirot",
        "opstina": "Bazovik",
        "lokacija": "Bazovik"
    },
    {
        "grad": "Pirot",
        "opstina": "Barje Čiflik",
        "lokacija": "Barje Čiflik"
    },
    {
        "grad": "Pirot",
        "opstina": "Basara",
        "lokacija": "Basara"
    },
    {
        "grad": "Pirot",
        "opstina": "Bela",
        "lokacija": "Bela"
    },
    {
        "grad": "Pirot",
        "opstina": "Belo Polje",
        "lokacija": "Belo Polje"
    },
    {
        "grad": "Pirot",
        "opstina": "Berovica",
        "lokacija": "Berovica"
    },
    {
        "grad": "Pirot",
        "opstina": "Blato",
        "lokacija": "Blato"
    },
    {
        "grad": "Pirot",
        "opstina": "Brlog",
        "lokacija": "Brlog"
    },
    {
        "grad": "Pirot",
        "opstina": "Velika Lukanja",
        "lokacija": "Velika Lukanja"
    },
    {
        "grad": "Pirot",
        "opstina": "Veliki Jovanovac",
        "lokacija": "Veliki Jovanovac"
    },
    {
        "grad": "Pirot",
        "opstina": "Veliki Suvodol",
        "lokacija": "Veliki Suvodol"
    },
    {
        "grad": "Pirot",
        "opstina": "Veliko Selo",
        "lokacija": "Veliko Selo"
    },
    {
        "grad": "Pirot",
        "opstina": "Visočka Ržana",
        "lokacija": "Visočka Ržana"
    },
    {
        "grad": "Pirot",
        "opstina": "Vlasi",
        "lokacija": "Vlasi"
    },
    {
        "grad": "Pirot",
        "opstina": "Vojnegovac",
        "lokacija": "Vojnegovac"
    },
    {
        "grad": "Pirot",
        "opstina": "Vranište",
        "lokacija": "Vranište"
    },
    {
        "grad": "Pirot",
        "opstina": "Gnjilan",
        "lokacija": "Gnjilan"
    },
    {
        "grad": "Pirot",
        "opstina": "Gornja Držina",
        "lokacija": "Gornja Držina"
    },
    {
        "grad": "Pirot",
        "opstina": "Gostuša",
        "lokacija": "Gostuša"
    },
    {
        "grad": "Pirot",
        "opstina": "gradašnica",
        "lokacija": "gradašnica"
    },
    {
        "grad": "Pirot",
        "opstina": "gradište",
        "lokacija": "gradište"
    },
    {
        "grad": "Pirot",
        "opstina": "Dobri Do",
        "lokacija": "Dobri Do"
    },
    {
        "grad": "Pirot",
        "opstina": "Dojkinci",
        "lokacija": "Dojkinci"
    },
    {
        "grad": "Pirot",
        "opstina": "Držina",
        "lokacija": "Držina"
    },
    {
        "grad": "Pirot",
        "opstina": "Zavoj",
        "lokacija": "Zavoj"
    },
    {
        "grad": "Pirot",
        "opstina": "Zavojsko Jezero",
        "lokacija": "Zavojsko Jezero"
    },
    {
        "grad": "Pirot",
        "opstina": "Zaskovci",
        "lokacija": "Zaskovci"
    },
    {
        "grad": "Pirot",
        "opstina": "Izvor",
        "lokacija": "Izvor"
    },
    {
        "grad": "Pirot",
        "opstina": "Jalbotina",
        "lokacija": "Jalbotina"
    },
    {
        "grad": "Pirot",
        "opstina": "Jelovica",
        "lokacija": "Jelovica"
    },
    {
        "grad": "Pirot",
        "opstina": "Kamik",
        "lokacija": "Kamik"
    },
    {
        "grad": "Pirot",
        "opstina": "Koprivštica",
        "lokacija": "Koprivštica"
    },
    {
        "grad": "Pirot",
        "opstina": "Kostur",
        "lokacija": "Kostur"
    },
    {
        "grad": "Pirot",
        "opstina": "Krupac",
        "lokacija": "Krupac"
    },
    {
        "grad": "Pirot",
        "opstina": "Kumanovo",
        "lokacija": "Kumanovo"
    },
    {
        "grad": "Pirot",
        "opstina": "Mali Jovanovac",
        "lokacija": "Mali Jovanovac"
    },
    {
        "grad": "Pirot",
        "opstina": "Mali Suvodol",
        "lokacija": "Mali Suvodol"
    },
    {
        "grad": "Pirot",
        "opstina": "Milojkovac",
        "lokacija": "Milojkovac"
    },
    {
        "grad": "Pirot",
        "opstina": "Mirkovci",
        "lokacija": "Mirkovci"
    },
    {
        "grad": "Pirot",
        "opstina": "Nišor",
        "lokacija": "Nišor"
    },
    {
        "grad": "Pirot",
        "opstina": "Obrenovac",
        "lokacija": "Obrenovac"
    },
    {
        "grad": "Pirot",
        "opstina": "Oreovica",
        "lokacija": "Oreovica"
    },
    {
        "grad": "Pirot",
        "opstina": "Orlja",
        "lokacija": "Orlja"
    },
    {
        "grad": "Pirot",
        "opstina": "Osmakova",
        "lokacija": "Osmakova"
    },
    {
        "grad": "Pirot",
        "opstina": "Pakleštica",
        "lokacija": "Pakleštica"
    },
    {
        "grad": "Pirot",
        "opstina": "Pasjač",
        "lokacija": "Pasjač"
    },
    {
        "grad": "Pirot",
        "opstina": "Petrovac",
        "lokacija": "Petrovac"
    },
    {
        "grad": "Pirot",
        "opstina": "Planinica",
        "lokacija": "Planinica"
    },
    {
        "grad": "Pirot",
        "opstina": "Pokrevenik",
        "lokacija": "Pokrevenik"
    },
    {
        "grad": "Pirot",
        "opstina": "Poljska Ržana",
        "lokacija": "Poljska Ržana"
    },
    {
        "grad": "Pirot",
        "opstina": "Ponor",
        "lokacija": "Ponor"
    },
    {
        "grad": "Pirot",
        "opstina": "Prisjan",
        "lokacija": "Prisjan"
    },
    {
        "grad": "Pirot",
        "opstina": "Ragodeš",
        "lokacija": "Ragodeš"
    },
    {
        "grad": "Pirot",
        "opstina": "Rasnica",
        "lokacija": "Rasnica"
    },
    {
        "grad": "Pirot",
        "opstina": "Rosomač",
        "lokacija": "Rosomač"
    },
    {
        "grad": "Pirot",
        "opstina": "Rsovci",
        "lokacija": "Rsovci"
    },
    {
        "grad": "Pirot",
        "opstina": "Rudinje",
        "lokacija": "Rudinje"
    },
    {
        "grad": "Pirot",
        "opstina": "Sinja Glava",
        "lokacija": "Sinja Glava"
    },
    {
        "grad": "Pirot",
        "opstina": "Slavinja",
        "lokacija": "Slavinja"
    },
    {
        "grad": "Pirot",
        "opstina": "Sopot",
        "lokacija": "Sopot"
    },
    {
        "grad": "Pirot",
        "opstina": "Srećkovac",
        "lokacija": "Srećkovac"
    },
    {
        "grad": "Pirot",
        "opstina": "Staničenje",
        "lokacija": "Staničenje"
    },
    {
        "grad": "Pirot",
        "opstina": "Stara Planina",
        "lokacija": "Stara Planina"
    },
    {
        "grad": "Pirot",
        "opstina": "Sukovo",
        "lokacija": "Sukovo"
    },
    {
        "grad": "Pirot",
        "opstina": "Temska",
        "lokacija": "Temska"
    },
    {
        "grad": "Pirot",
        "opstina": "Topli Do",
        "lokacija": "Topli Do"
    },
    {
        "grad": "Pirot",
        "opstina": "Trnjana",
        "lokacija": "Trnjana"
    },
    {
        "grad": "Pirot",
        "opstina": "Cerev Del",
        "lokacija": "Cerev Del"
    },
    {
        "grad": "Pirot",
        "opstina": "Cerova",
        "lokacija": "Cerova"
    },
    {
        "grad": "Pirot",
        "opstina": "Crvenčevo",
        "lokacija": "Crvenčevo"
    },
    {
        "grad": "Pirot",
        "opstina": "Crnoklište",
        "lokacija": "Crnoklište"
    },
    {
        "grad": "Pirot",
        "opstina": "Činiglavci",
        "lokacija": "Činiglavci"
    },
    {
        "grad": "Pirot",
        "opstina": "Šugrin",
        "lokacija": "Šugrin"
    },
    {
        "grad": "Plandište",
        "opstina": "Plandište",
        "lokacija": "Plandište"
    },
    {
        "grad": "Plandište",
        "opstina": "Gradska lokacija",
        "lokacija": "Mariolana"
    },
    {
        "grad": "Plandište",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Plandište",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Plandište",
        "opstina": "Banatski Sokolac",
        "lokacija": "Banatski Sokolac"
    },
    {
        "grad": "Plandište",
        "opstina": "Barice",
        "lokacija": "Barice"
    },
    {
        "grad": "Plandište",
        "opstina": "Velika Greda",
        "lokacija": "Velika Greda"
    },
    {
        "grad": "Plandište",
        "opstina": "Veliki Gaj",
        "lokacija": "Veliki Gaj"
    },
    {
        "grad": "Plandište",
        "opstina": "Dužine",
        "lokacija": "Dužine"
    },
    {
        "grad": "Plandište",
        "opstina": "Jermenovci",
        "lokacija": "Jermenovci"
    },
    {
        "grad": "Plandište",
        "opstina": "Kupinik",
        "lokacija": "Kupinik"
    },
    {
        "grad": "Plandište",
        "opstina": "Laudonovac",
        "lokacija": "Laudonovac"
    },
    {
        "grad": "Plandište",
        "opstina": "Margita",
        "lokacija": "Margita"
    },
    {
        "grad": "Plandište",
        "opstina": "Markovićevo",
        "lokacija": "Markovićevo"
    },
    {
        "grad": "Plandište",
        "opstina": "Miletićevo",
        "lokacija": "Miletićevo"
    },
    {
        "grad": "Plandište",
        "opstina": "Stari Lec",
        "lokacija": "Stari Lec"
    },
    {
        "grad": "Plandište",
        "opstina": "Hajdučica",
        "lokacija": "Hajdučica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Podujevo",
        "lokacija": "Podujevo"
    },
    {
        "grad": "Podujevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Podujevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Podujevo",
        "opstina": "Alabak",
        "lokacija": "Alabak"
    },
    {
        "grad": "Podujevo",
        "opstina": "Bajčina",
        "lokacija": "Bajčina"
    },
    {
        "grad": "Podujevo",
        "opstina": "Balovac",
        "lokacija": "Balovac"
    },
    {
        "grad": "Podujevo",
        "opstina": "Baraina",
        "lokacija": "Baraina"
    },
    {
        "grad": "Podujevo",
        "opstina": "Batlava",
        "lokacija": "Batlava"
    },
    {
        "grad": "Podujevo",
        "opstina": "Belo Polje",
        "lokacija": "Belo Polje"
    },
    {
        "grad": "Podujevo",
        "opstina": "Blato",
        "lokacija": "Blato"
    },
    {
        "grad": "Podujevo",
        "opstina": "Bradaš",
        "lokacija": "Bradaš"
    },
    {
        "grad": "Podujevo",
        "opstina": "Braina",
        "lokacija": "Braina"
    },
    {
        "grad": "Podujevo",
        "opstina": "Brevnik",
        "lokacija": "Brevnik"
    },
    {
        "grad": "Podujevo",
        "opstina": "Brece",
        "lokacija": "Brece"
    },
    {
        "grad": "Podujevo",
        "opstina": "Burince",
        "lokacija": "Burince"
    },
    {
        "grad": "Podujevo",
        "opstina": "Velika Reka",
        "lokacija": "Velika Reka"
    },
    {
        "grad": "Podujevo",
        "opstina": "Glavnik",
        "lokacija": "Glavnik"
    },
    {
        "grad": "Podujevo",
        "opstina": "Godišnjak",
        "lokacija": "Godišnjak"
    },
    {
        "grad": "Podujevo",
        "opstina": "Gornja Dubnica",
        "lokacija": "Gornja Dubnica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Gornja Lapaštica",
        "lokacija": "Gornja Lapaštica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Gornja Pakaštica",
        "lokacija": "Gornja Pakaštica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Gornje Ljupče",
        "lokacija": "Gornje Ljupče"
    },
    {
        "grad": "Podujevo",
        "opstina": "Gornji Sibovac",
        "lokacija": "Gornji Sibovac"
    },
    {
        "grad": "Podujevo",
        "opstina": "Grdovac",
        "lokacija": "Grdovac"
    },
    {
        "grad": "Podujevo",
        "opstina": "Dvorište",
        "lokacija": "Dvorište"
    },
    {
        "grad": "Podujevo",
        "opstina": "Dobri Do",
        "lokacija": "Dobri Do"
    },
    {
        "grad": "Podujevo",
        "opstina": "Dobrotin",
        "lokacija": "Dobrotin"
    },
    {
        "grad": "Podujevo",
        "opstina": "Donja Dubnica",
        "lokacija": "Donja Dubnica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Donja Lapaštica",
        "lokacija": "Donja Lapaštica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Donja Pakaštica",
        "lokacija": "Donja Pakaštica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Donje Ljupče",
        "lokacija": "Donje Ljupče"
    },
    {
        "grad": "Podujevo",
        "opstina": "Donji Sibovac",
        "lokacija": "Donji Sibovac"
    },
    {
        "grad": "Podujevo",
        "opstina": "Duz",
        "lokacija": "Duz"
    },
    {
        "grad": "Podujevo",
        "opstina": "Dumoš",
        "lokacija": "Dumoš"
    },
    {
        "grad": "Podujevo",
        "opstina": "Žitinje",
        "lokacija": "Žitinje"
    },
    {
        "grad": "Podujevo",
        "opstina": "Zakut",
        "lokacija": "Zakut"
    },
    {
        "grad": "Podujevo",
        "opstina": "Kaljatica",
        "lokacija": "Kaljatica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Kačibeg",
        "lokacija": "Kačibeg"
    },
    {
        "grad": "Podujevo",
        "opstina": "Kisela Banja",
        "lokacija": "Kisela Banja"
    },
    {
        "grad": "Podujevo",
        "opstina": "Konjuševac",
        "lokacija": "Konjuševac"
    },
    {
        "grad": "Podujevo",
        "opstina": "Krpimej",
        "lokacija": "Krpimej"
    },
    {
        "grad": "Podujevo",
        "opstina": "Kruševica",
        "lokacija": "Kruševica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Ladovac",
        "lokacija": "Ladovac"
    },
    {
        "grad": "Podujevo",
        "opstina": "Lauša",
        "lokacija": "Lauša"
    },
    {
        "grad": "Podujevo",
        "opstina": "Letance",
        "lokacija": "Letance"
    },
    {
        "grad": "Podujevo",
        "opstina": "Livadica",
        "lokacija": "Livadica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Lug",
        "lokacija": "Lug"
    },
    {
        "grad": "Podujevo",
        "opstina": "Lužane",
        "lokacija": "Lužane"
    },
    {
        "grad": "Podujevo",
        "opstina": "Mazap",
        "lokacija": "Mazap"
    },
    {
        "grad": "Podujevo",
        "opstina": "Majance",
        "lokacija": "Majance"
    },
    {
        "grad": "Podujevo",
        "opstina": "Medregovac",
        "lokacija": "Medregovac"
    },
    {
        "grad": "Podujevo",
        "opstina": "Merdare",
        "lokacija": "Merdare"
    },
    {
        "grad": "Podujevo",
        "opstina": "Metohija",
        "lokacija": "Metohija"
    },
    {
        "grad": "Podujevo",
        "opstina": "Mirovac",
        "lokacija": "Mirovac"
    },
    {
        "grad": "Podujevo",
        "opstina": "Murgula",
        "lokacija": "Murgula"
    },
    {
        "grad": "Podujevo",
        "opstina": "Obrandža",
        "lokacija": "Obrandža"
    },
    {
        "grad": "Podujevo",
        "opstina": "Orlane",
        "lokacija": "Orlane"
    },
    {
        "grad": "Podujevo",
        "opstina": "Palatna",
        "lokacija": "Palatna"
    },
    {
        "grad": "Podujevo",
        "opstina": "Penduha",
        "lokacija": "Penduha"
    },
    {
        "grad": "Podujevo",
        "opstina": "Perane",
        "lokacija": "Perane"
    },
    {
        "grad": "Podujevo",
        "opstina": "Popovo",
        "lokacija": "Popovo"
    },
    {
        "grad": "Podujevo",
        "opstina": "potok",
        "lokacija": "potok"
    },
    {
        "grad": "Podujevo",
        "opstina": "Prepolac",
        "lokacija": "Prepolac"
    },
    {
        "grad": "Podujevo",
        "opstina": "Radujevac",
        "lokacija": "Radujevac"
    },
    {
        "grad": "Podujevo",
        "opstina": "Rakinica",
        "lokacija": "Rakinica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Revuće",
        "lokacija": "Revuće"
    },
    {
        "grad": "Podujevo",
        "opstina": "Repa",
        "lokacija": "Repa"
    },
    {
        "grad": "Podujevo",
        "opstina": "Rečica",
        "lokacija": "Rečica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Svetlje",
        "lokacija": "Svetlje"
    },
    {
        "grad": "Podujevo",
        "opstina": "Siljevica",
        "lokacija": "Siljevica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Podujevo",
        "opstina": "Surdula",
        "lokacija": "Surdula"
    },
    {
        "grad": "Podujevo",
        "opstina": "Surkiš",
        "lokacija": "Surkiš"
    },
    {
        "grad": "Podujevo",
        "opstina": "Trnava",
        "lokacija": "Trnava"
    },
    {
        "grad": "Podujevo",
        "opstina": "Trnavica",
        "lokacija": "Trnavica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Turučica",
        "lokacija": "Turučica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Hrtica",
        "lokacija": "Hrtica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Šajkovac",
        "lokacija": "Šajkovac"
    },
    {
        "grad": "Podujevo",
        "opstina": "Šakovica",
        "lokacija": "Šakovica"
    },
    {
        "grad": "Podujevo",
        "opstina": "Štedim",
        "lokacija": "Štedim"
    },
    {
        "grad": "Požarevac",
        "opstina": "Požarevac",
        "lokacija": "Požarevac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "27. Aprila"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Bulevar Bože Dimitrijevića"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Burjan"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Busije"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Varoško Brdo"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Gornja Mala"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "gradištanski Put"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Đurino Naselje"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Železnička Stanica"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Zabela Naselje"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kostolački Put"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Lamela"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Ljubičevo"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Meminac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Pionirski Trg"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Radna Mala"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Sopot"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Tabačka Čaršija"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Tulba"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Čačalica"
    },
    {
        "grad": "Požarevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Požarevac",
        "opstina": "Bare",
        "lokacija": "Bare"
    },
    {
        "grad": "Požarevac",
        "opstina": "Batovac",
        "lokacija": "Batovac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Beranje",
        "lokacija": "Beranje"
    },
    {
        "grad": "Požarevac",
        "opstina": "Bradarac",
        "lokacija": "Bradarac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Bratinac",
        "lokacija": "Bratinac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Brežane",
        "lokacija": "Brežane"
    },
    {
        "grad": "Požarevac",
        "opstina": "Bubušinac",
        "lokacija": "Bubušinac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Dragovac",
        "lokacija": "Dragovac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Drmno",
        "lokacija": "Drmno"
    },
    {
        "grad": "Požarevac",
        "opstina": "Dubravica",
        "lokacija": "Dubravica"
    },
    {
        "grad": "Požarevac",
        "opstina": "Živica",
        "lokacija": "Živica"
    },
    {
        "grad": "Požarevac",
        "opstina": "Kasidol",
        "lokacija": "Kasidol"
    },
    {
        "grad": "Požarevac",
        "opstina": "Kličevac",
        "lokacija": "Kličevac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Kostolac",
        "lokacija": "Kostolac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Kostolac",
        "lokacija": "Kostolac - gradska Plaža"
    },
    {
        "grad": "Požarevac",
        "opstina": "Kostolac",
        "lokacija": "Kostolac - Dunav"
    },
    {
        "grad": "Požarevac",
        "opstina": "Kostolac",
        "lokacija": "Kostolac - Klenovnik"
    },
    {
        "grad": "Požarevac",
        "opstina": "Kostolac",
        "lokacija": "Kostolac - Ostrovo"
    },
    {
        "grad": "Požarevac",
        "opstina": "Kostolac",
        "lokacija": "Kostolac - Petka"
    },
    {
        "grad": "Požarevac",
        "opstina": "Kostolac",
        "lokacija": "Kostolac - Selo Kostolac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Lučica",
        "lokacija": "Lučica"
    },
    {
        "grad": "Požarevac",
        "opstina": "Maljurevac",
        "lokacija": "Maljurevac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Nabrđe",
        "lokacija": "Nabrđe"
    },
    {
        "grad": "Požarevac",
        "opstina": "Poljana",
        "lokacija": "Poljana"
    },
    {
        "grad": "Požarevac",
        "opstina": "Popovac",
        "lokacija": "Popovac"
    },
    {
        "grad": "Požarevac",
        "opstina": "Prugovo",
        "lokacija": "Prugovo"
    },
    {
        "grad": "Požarevac",
        "opstina": "Rečica",
        "lokacija": "Rečica"
    },
    {
        "grad": "Požarevac",
        "opstina": "Trnjane",
        "lokacija": "Trnjane"
    },
    {
        "grad": "Požarevac",
        "opstina": "Ćirikovac",
        "lokacija": "Ćirikovac"
    },
    {
        "grad": "Požega",
        "opstina": "Požega",
        "lokacija": "Požega"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Bakionica"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Borjak"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Zelenac"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Kotarski Grm"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Lisište"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Marijanovića Brdo"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Milovića Livade"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Radovina"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Savinac"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Tatojevica"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Požega",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Požega",
        "opstina": "Velika Ježevica",
        "lokacija": "Velika Ježevica"
    },
    {
        "grad": "Požega",
        "opstina": "Visibaba",
        "lokacija": "Visibaba"
    },
    {
        "grad": "Požega",
        "opstina": "Vranjani",
        "lokacija": "Vranjani"
    },
    {
        "grad": "Požega",
        "opstina": "Glumač",
        "lokacija": "Glumač"
    },
    {
        "grad": "Požega",
        "opstina": "Godovik",
        "lokacija": "Godovik"
    },
    {
        "grad": "Požega",
        "opstina": "Gornja Dobrinja",
        "lokacija": "Gornja Dobrinja"
    },
    {
        "grad": "Požega",
        "opstina": "Gorobilje",
        "lokacija": "Gorobilje"
    },
    {
        "grad": "Požega",
        "opstina": "Gugalj",
        "lokacija": "Gugalj"
    },
    {
        "grad": "Požega",
        "opstina": "Donja Dobrinja",
        "lokacija": "Donja Dobrinja"
    },
    {
        "grad": "Požega",
        "opstina": "Dražinovići",
        "lokacija": "Dražinovići"
    },
    {
        "grad": "Požega",
        "opstina": "Duškovci",
        "lokacija": "Duškovci"
    },
    {
        "grad": "Požega",
        "opstina": "Zaselje",
        "lokacija": "Zaselje"
    },
    {
        "grad": "Požega",
        "opstina": "Zdravčići",
        "lokacija": "Zdravčići"
    },
    {
        "grad": "Požega",
        "opstina": "Jelen Do",
        "lokacija": "Jelen Do"
    },
    {
        "grad": "Požega",
        "opstina": "Kalenići",
        "lokacija": "Kalenići"
    },
    {
        "grad": "Požega",
        "opstina": "Lopaš",
        "lokacija": "Lopaš"
    },
    {
        "grad": "Požega",
        "opstina": "Loret",
        "lokacija": "Loret"
    },
    {
        "grad": "Požega",
        "opstina": "Ljutice",
        "lokacija": "Ljutice"
    },
    {
        "grad": "Požega",
        "opstina": "Mađer",
        "lokacija": "Mađer"
    },
    {
        "grad": "Požega",
        "opstina": "Mala Ježevica",
        "lokacija": "Mala Ježevica"
    },
    {
        "grad": "Požega",
        "opstina": "Milićevo Selo",
        "lokacija": "Milićevo Selo"
    },
    {
        "grad": "Požega",
        "opstina": "Mršelji",
        "lokacija": "Mršelji"
    },
    {
        "grad": "Požega",
        "opstina": "Otanj",
        "lokacija": "Otanj"
    },
    {
        "grad": "Požega",
        "opstina": "Papratište",
        "lokacija": "Papratište"
    },
    {
        "grad": "Požega",
        "opstina": "Pilatovići",
        "lokacija": "Pilatovići"
    },
    {
        "grad": "Požega",
        "opstina": "Prijanovići",
        "lokacija": "Prijanovići"
    },
    {
        "grad": "Požega",
        "opstina": "Prilipac",
        "lokacija": "Prilipac"
    },
    {
        "grad": "Požega",
        "opstina": "Radovci",
        "lokacija": "Radovci"
    },
    {
        "grad": "Požega",
        "opstina": "Rasna",
        "lokacija": "Rasna"
    },
    {
        "grad": "Požega",
        "opstina": "Rečice",
        "lokacija": "Rečice"
    },
    {
        "grad": "Požega",
        "opstina": "Roge",
        "lokacija": "Roge"
    },
    {
        "grad": "Požega",
        "opstina": "Rupeljevo",
        "lokacija": "Rupeljevo"
    },
    {
        "grad": "Požega",
        "opstina": "Svračkovo",
        "lokacija": "Svračkovo"
    },
    {
        "grad": "Požega",
        "opstina": "Srednja Dobrinja",
        "lokacija": "Srednja Dobrinja"
    },
    {
        "grad": "Požega",
        "opstina": "Tabanovići",
        "lokacija": "Tabanovići"
    },
    {
        "grad": "Požega",
        "opstina": "Tvrdići",
        "lokacija": "Tvrdići"
    },
    {
        "grad": "Požega",
        "opstina": "Tometino Polje",
        "lokacija": "Tometino Polje"
    },
    {
        "grad": "Požega",
        "opstina": "Tučkovo",
        "lokacija": "Tučkovo"
    },
    {
        "grad": "Požega",
        "opstina": "Uzići",
        "lokacija": "Uzići"
    },
    {
        "grad": "Požega",
        "opstina": "Čestobrodica",
        "lokacija": "Čestobrodica"
    },
    {
        "grad": "Preševo",
        "opstina": "Preševo",
        "lokacija": "Preševo"
    },
    {
        "grad": "Preševo",
        "opstina": "Gradska lokacija",
        "lokacija": "Železnička Stanica"
    },
    {
        "grad": "Preševo",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Preševo",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Preševo",
        "opstina": "Aliđerce",
        "lokacija": "Aliđerce"
    },
    {
        "grad": "Preševo",
        "opstina": "Berčevac",
        "lokacija": "Berčevac"
    },
    {
        "grad": "Preševo",
        "opstina": "Bujić",
        "lokacija": "Bujić"
    },
    {
        "grad": "Preševo",
        "opstina": "Bukarevac",
        "lokacija": "Bukarevac"
    },
    {
        "grad": "Preševo",
        "opstina": "Bukovac",
        "lokacija": "Bukovac"
    },
    {
        "grad": "Preševo",
        "opstina": "Buštranje",
        "lokacija": "Buštranje"
    },
    {
        "grad": "Preševo",
        "opstina": "Gare",
        "lokacija": "Gare"
    },
    {
        "grad": "Preševo",
        "opstina": "Golemi Dol",
        "lokacija": "Golemi Dol"
    },
    {
        "grad": "Preševo",
        "opstina": "Gornja Šušaja",
        "lokacija": "Gornja Šušaja"
    },
    {
        "grad": "Preševo",
        "opstina": "Gospođince",
        "lokacija": "Gospođince"
    },
    {
        "grad": "Preševo",
        "opstina": "Depce",
        "lokacija": "Depce"
    },
    {
        "grad": "Preševo",
        "opstina": "Donja Šušaja",
        "lokacija": "Donja Šušaja"
    },
    {
        "grad": "Preševo",
        "opstina": "Žujince",
        "lokacija": "Žujince"
    },
    {
        "grad": "Preševo",
        "opstina": "Ilince",
        "lokacija": "Ilince"
    },
    {
        "grad": "Preševo",
        "opstina": "Kurbalija",
        "lokacija": "Kurbalija"
    },
    {
        "grad": "Preševo",
        "opstina": "Ljanik",
        "lokacija": "Ljanik"
    },
    {
        "grad": "Preševo",
        "opstina": "Mađare",
        "lokacija": "Mađare"
    },
    {
        "grad": "Preševo",
        "opstina": "Miratovac",
        "lokacija": "Miratovac"
    },
    {
        "grad": "Preševo",
        "opstina": "Norča",
        "lokacija": "Norča"
    },
    {
        "grad": "Preševo",
        "opstina": "Oraovica",
        "lokacija": "Oraovica"
    },
    {
        "grad": "Preševo",
        "opstina": "Pečeno",
        "lokacija": "Pečeno"
    },
    {
        "grad": "Preševo",
        "opstina": "Rajince",
        "lokacija": "Rajince"
    },
    {
        "grad": "Preševo",
        "opstina": "Ranatovce",
        "lokacija": "Ranatovce"
    },
    {
        "grad": "Preševo",
        "opstina": "Reljan",
        "lokacija": "Reljan"
    },
    {
        "grad": "Preševo",
        "opstina": "Svinjište",
        "lokacija": "Svinjište"
    },
    {
        "grad": "Preševo",
        "opstina": "Sefer",
        "lokacija": "Sefer"
    },
    {
        "grad": "Preševo",
        "opstina": "Slavujevac",
        "lokacija": "Slavujevac"
    },
    {
        "grad": "Preševo",
        "opstina": "Stanevce",
        "lokacija": "Stanevce"
    },
    {
        "grad": "Preševo",
        "opstina": "Strezovce",
        "lokacija": "Strezovce"
    },
    {
        "grad": "Preševo",
        "opstina": "Trnava",
        "lokacija": "Trnava"
    },
    {
        "grad": "Preševo",
        "opstina": "Cakanovac",
        "lokacija": "Cakanovac"
    },
    {
        "grad": "Preševo",
        "opstina": "Cerevajka",
        "lokacija": "Cerevajka"
    },
    {
        "grad": "Preševo",
        "opstina": "Crnotince",
        "lokacija": "Crnotince"
    },
    {
        "grad": "Preševo",
        "opstina": "Čukarka",
        "lokacija": "Čukarka"
    },
    {
        "grad": "Priboj",
        "opstina": "Priboj",
        "lokacija": "Priboj"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Banjski Čamac"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Železnička Stanica"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Zelenac"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Jarkovac"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Jarmovac"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Lim"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Luka"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Mostina"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Novi Priboj"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Poljice"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Stari grad"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Čitluk"
    },
    {
        "grad": "Priboj",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Priboj",
        "opstina": "Banja",
        "lokacija": "Banja"
    },
    {
        "grad": "Priboj",
        "opstina": "Banja",
        "lokacija": "Banja - Orašac"
    },
    {
        "grad": "Priboj",
        "opstina": "Banja",
        "lokacija": "Banja - Potpeć"
    },
    {
        "grad": "Priboj",
        "opstina": "Banja",
        "lokacija": "Banja - Radovići"
    },
    {
        "grad": "Priboj",
        "opstina": "Banja",
        "lokacija": "Banja - Ćirkovići"
    },
    {
        "grad": "Priboj",
        "opstina": "Batkovići",
        "lokacija": "Batkovići"
    },
    {
        "grad": "Priboj",
        "opstina": "Brezna",
        "lokacija": "Brezna"
    },
    {
        "grad": "Priboj",
        "opstina": "Bučje",
        "lokacija": "Bučje"
    },
    {
        "grad": "Priboj",
        "opstina": "Dobrilovići",
        "lokacija": "Dobrilovići"
    },
    {
        "grad": "Priboj",
        "opstina": "Živinice",
        "lokacija": "Živinice"
    },
    {
        "grad": "Priboj",
        "opstina": "Zabrđe",
        "lokacija": "Zabrđe"
    },
    {
        "grad": "Priboj",
        "opstina": "Zabrnjica",
        "lokacija": "Zabrnjica"
    },
    {
        "grad": "Priboj",
        "opstina": "Zagradina",
        "lokacija": "Zagradina"
    },
    {
        "grad": "Priboj",
        "opstina": "Zaostro",
        "lokacija": "Zaostro"
    },
    {
        "grad": "Priboj",
        "opstina": "Jelača",
        "lokacija": "Jelača"
    },
    {
        "grad": "Priboj",
        "opstina": "Kalafati",
        "lokacija": "Kalafati"
    },
    {
        "grad": "Priboj",
        "opstina": "Kaluđerovići",
        "lokacija": "Kaluđerovići"
    },
    {
        "grad": "Priboj",
        "opstina": "Kasidoli",
        "lokacija": "Kasidoli"
    },
    {
        "grad": "Priboj",
        "opstina": "Kratovo",
        "lokacija": "Kratovo"
    },
    {
        "grad": "Priboj",
        "opstina": "Krnjača",
        "lokacija": "Krnjača"
    },
    {
        "grad": "Priboj",
        "opstina": "Kukurovići",
        "lokacija": "Kukurovići"
    },
    {
        "grad": "Priboj",
        "opstina": "Mažići",
        "lokacija": "Mažići"
    },
    {
        "grad": "Priboj",
        "opstina": "Miliješ",
        "lokacija": "Miliješ"
    },
    {
        "grad": "Priboj",
        "opstina": "Mramorje",
        "lokacija": "Mramorje"
    },
    {
        "grad": "Priboj",
        "opstina": "Plašće",
        "lokacija": "Plašće"
    },
    {
        "grad": "Priboj",
        "opstina": "Požegrmac",
        "lokacija": "Požegrmac"
    },
    {
        "grad": "Priboj",
        "opstina": "Pribojska Goleša",
        "lokacija": "Pribojska Goleša"
    },
    {
        "grad": "Priboj",
        "opstina": "Pribojske Čelice",
        "lokacija": "Pribojske Čelice"
    },
    {
        "grad": "Priboj",
        "opstina": "Rača",
        "lokacija": "Rača"
    },
    {
        "grad": "Priboj",
        "opstina": "Ritošići",
        "lokacija": "Ritošići"
    },
    {
        "grad": "Priboj",
        "opstina": "Sjeverin",
        "lokacija": "Sjeverin"
    },
    {
        "grad": "Priboj",
        "opstina": "Sočice",
        "lokacija": "Sočice"
    },
    {
        "grad": "Priboj",
        "opstina": "Strmac",
        "lokacija": "Strmac"
    },
    {
        "grad": "Priboj",
        "opstina": "Hercegovačka Goleša",
        "lokacija": "Hercegovačka Goleša"
    },
    {
        "grad": "Priboj",
        "opstina": "Crnugovići",
        "lokacija": "Crnugovići"
    },
    {
        "grad": "Priboj",
        "opstina": "Crnuzi",
        "lokacija": "Crnuzi"
    },
    {
        "grad": "Prizren",
        "opstina": "Prizren",
        "lokacija": "Prizren"
    },
    {
        "grad": "Prizren",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Prizren",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Prizren",
        "opstina": "Atmađa",
        "lokacija": "Atmađa"
    },
    {
        "grad": "Prizren",
        "opstina": "Belobrod",
        "lokacija": "Belobrod"
    },
    {
        "grad": "Prizren",
        "opstina": "Biluša",
        "lokacija": "Biluša"
    },
    {
        "grad": "Prizren",
        "opstina": "Bljač",
        "lokacija": "Bljač"
    },
    {
        "grad": "Prizren",
        "opstina": "Brezna",
        "lokacija": "Brezna"
    },
    {
        "grad": "Prizren",
        "opstina": "Brodosavce",
        "lokacija": "Brodosavce"
    },
    {
        "grad": "Prizren",
        "opstina": "Brut",
        "lokacija": "Brut"
    },
    {
        "grad": "Prizren",
        "opstina": "Buzec",
        "lokacija": "Buzec"
    },
    {
        "grad": "Prizren",
        "opstina": "Buča",
        "lokacija": "Buča"
    },
    {
        "grad": "Prizren",
        "opstina": "Veleža",
        "lokacija": "Veleža"
    },
    {
        "grad": "Prizren",
        "opstina": "Vlašnja",
        "lokacija": "Vlašnja"
    },
    {
        "grad": "Prizren",
        "opstina": "Vrbičane",
        "lokacija": "Vrbičane"
    },
    {
        "grad": "Prizren",
        "opstina": "Vrbnica",
        "lokacija": "Vrbnica"
    },
    {
        "grad": "Prizren",
        "opstina": "Gornja Srbica",
        "lokacija": "Gornja Srbica"
    },
    {
        "grad": "Prizren",
        "opstina": "Gornje Ljubinje",
        "lokacija": "Gornje Ljubinje"
    },
    {
        "grad": "Prizren",
        "opstina": "Gornje Selo",
        "lokacija": "Gornje Selo"
    },
    {
        "grad": "Prizren",
        "opstina": "Gorožup",
        "lokacija": "Gorožup"
    },
    {
        "grad": "Prizren",
        "opstina": "Graždanik",
        "lokacija": "Graždanik"
    },
    {
        "grad": "Prizren",
        "opstina": "Grnčare",
        "lokacija": "Grnčare"
    },
    {
        "grad": "Prizren",
        "opstina": "Dedaj",
        "lokacija": "Dedaj"
    },
    {
        "grad": "Prizren",
        "opstina": "Dobrušte",
        "lokacija": "Dobrušte"
    },
    {
        "grad": "Prizren",
        "opstina": "Dojnice",
        "lokacija": "Dojnice"
    },
    {
        "grad": "Prizren",
        "opstina": "Donja Srbica",
        "lokacija": "Donja Srbica"
    },
    {
        "grad": "Prizren",
        "opstina": "Donje Ljubinje",
        "lokacija": "Donje Ljubinje"
    },
    {
        "grad": "Prizren",
        "opstina": "Drajčići",
        "lokacija": "Drajčići"
    },
    {
        "grad": "Prizren",
        "opstina": "Dušanovo",
        "lokacija": "Dušanovo"
    },
    {
        "grad": "Prizren",
        "opstina": "Đonaj",
        "lokacija": "Đonaj"
    },
    {
        "grad": "Prizren",
        "opstina": "Živinjane",
        "lokacija": "Živinjane"
    },
    {
        "grad": "Prizren",
        "opstina": "Žur",
        "lokacija": "Žur"
    },
    {
        "grad": "Prizren",
        "opstina": "Zaplužje",
        "lokacija": "Zaplužje"
    },
    {
        "grad": "Prizren",
        "opstina": "Zgatar",
        "lokacija": "Zgatar"
    },
    {
        "grad": "Prizren",
        "opstina": "Zjum Opoljski",
        "lokacija": "Zjum Opoljski"
    },
    {
        "grad": "Prizren",
        "opstina": "Zjum Has",
        "lokacija": "Zjum Has"
    },
    {
        "grad": "Prizren",
        "opstina": "Zojić",
        "lokacija": "Zojić"
    },
    {
        "grad": "Prizren",
        "opstina": "Zrze",
        "lokacija": "Zrze"
    },
    {
        "grad": "Prizren",
        "opstina": "Jablanica",
        "lokacija": "Jablanica"
    },
    {
        "grad": "Prizren",
        "opstina": "Ješkovo",
        "lokacija": "Ješkovo"
    },
    {
        "grad": "Prizren",
        "opstina": "Kabaš",
        "lokacija": "Kabaš"
    },
    {
        "grad": "Prizren",
        "opstina": "Kabaš Has",
        "lokacija": "Kabaš Has"
    },
    {
        "grad": "Prizren",
        "opstina": "Kapra",
        "lokacija": "Kapra"
    },
    {
        "grad": "Prizren",
        "opstina": "Karašinđerđ",
        "lokacija": "Karašinđerđ"
    },
    {
        "grad": "Prizren",
        "opstina": "Kobanja",
        "lokacija": "Kobanja"
    },
    {
        "grad": "Prizren",
        "opstina": "Kojuš",
        "lokacija": "Kojuš"
    },
    {
        "grad": "Prizren",
        "opstina": "Koriša",
        "lokacija": "Koriša"
    },
    {
        "grad": "Prizren",
        "opstina": "Kosovce",
        "lokacija": "Kosovce"
    },
    {
        "grad": "Prizren",
        "opstina": "Krajk",
        "lokacija": "Krajk"
    },
    {
        "grad": "Prizren",
        "opstina": "Kuklibeg",
        "lokacija": "Kuklibeg"
    },
    {
        "grad": "Prizren",
        "opstina": "Kukovce",
        "lokacija": "Kukovce"
    },
    {
        "grad": "Prizren",
        "opstina": "Kušnin",
        "lokacija": "Kušnin"
    },
    {
        "grad": "Prizren",
        "opstina": "Kuštendil",
        "lokacija": "Kuštendil"
    },
    {
        "grad": "Prizren",
        "opstina": "Landovica",
        "lokacija": "Landovica"
    },
    {
        "grad": "Prizren",
        "opstina": "Lez",
        "lokacija": "Lez"
    },
    {
        "grad": "Prizren",
        "opstina": "Leskovac",
        "lokacija": "Leskovac"
    },
    {
        "grad": "Prizren",
        "opstina": "Lokvica",
        "lokacija": "Lokvica"
    },
    {
        "grad": "Prizren",
        "opstina": "Ljubižda",
        "lokacija": "Ljubižda"
    },
    {
        "grad": "Prizren",
        "opstina": "Ljubižda Has",
        "lokacija": "Ljubižda Has"
    },
    {
        "grad": "Prizren",
        "opstina": "Ljubičevo",
        "lokacija": "Ljubičevo"
    },
    {
        "grad": "Prizren",
        "opstina": "Ljukinaj",
        "lokacija": "Ljukinaj"
    },
    {
        "grad": "Prizren",
        "opstina": "Ljutoglav",
        "lokacija": "Ljutoglav"
    },
    {
        "grad": "Prizren",
        "opstina": "Mazrek",
        "lokacija": "Mazrek"
    },
    {
        "grad": "Prizren",
        "opstina": "Mala Kruša",
        "lokacija": "Mala Kruša"
    },
    {
        "grad": "Prizren",
        "opstina": "Mamuša",
        "lokacija": "Mamuša"
    },
    {
        "grad": "Prizren",
        "opstina": "Manastirica",
        "lokacija": "Manastirica"
    },
    {
        "grad": "Prizren",
        "opstina": "Medvece",
        "lokacija": "Medvece"
    },
    {
        "grad": "Prizren",
        "opstina": "Miljaj",
        "lokacija": "Miljaj"
    },
    {
        "grad": "Prizren",
        "opstina": "Muradem",
        "lokacija": "Muradem"
    },
    {
        "grad": "Prizren",
        "opstina": "Mušnikovo",
        "lokacija": "Mušnikovo"
    },
    {
        "grad": "Prizren",
        "opstina": "Našec",
        "lokacija": "Našec"
    },
    {
        "grad": "Prizren",
        "opstina": "Nebregošte",
        "lokacija": "Nebregošte"
    },
    {
        "grad": "Prizren",
        "opstina": "Nova Šumadija",
        "lokacija": "Nova Šumadija"
    },
    {
        "grad": "Prizren",
        "opstina": "Novake",
        "lokacija": "Novake"
    },
    {
        "grad": "Prizren",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Prizren",
        "opstina": "Petrovo Selo",
        "lokacija": "Petrovo Selo"
    },
    {
        "grad": "Prizren",
        "opstina": "Pirane",
        "lokacija": "Pirane"
    },
    {
        "grad": "Prizren",
        "opstina": "Plava",
        "lokacija": "Plava"
    },
    {
        "grad": "Prizren",
        "opstina": "Plajnik",
        "lokacija": "Plajnik"
    },
    {
        "grad": "Prizren",
        "opstina": "Planeja",
        "lokacija": "Planeja"
    },
    {
        "grad": "Prizren",
        "opstina": "Planjane",
        "lokacija": "Planjane"
    },
    {
        "grad": "Prizren",
        "opstina": "Poslište",
        "lokacija": "Poslište"
    },
    {
        "grad": "Prizren",
        "opstina": "Pousko",
        "lokacija": "Pousko"
    },
    {
        "grad": "Prizren",
        "opstina": "Randubrava",
        "lokacija": "Randubrava"
    },
    {
        "grad": "Prizren",
        "opstina": "Rence",
        "lokacija": "Rence"
    },
    {
        "grad": "Prizren",
        "opstina": "Rečane",
        "lokacija": "Rečane"
    },
    {
        "grad": "Prizren",
        "opstina": "Romaja",
        "lokacija": "Romaja"
    },
    {
        "grad": "Prizren",
        "opstina": "Skorobište",
        "lokacija": "Skorobište"
    },
    {
        "grad": "Prizren",
        "opstina": "Smać",
        "lokacija": "Smać"
    },
    {
        "grad": "Prizren",
        "opstina": "Sredska",
        "lokacija": "Sredska"
    },
    {
        "grad": "Prizren",
        "opstina": "Stružje",
        "lokacija": "Stružje"
    },
    {
        "grad": "Prizren",
        "opstina": "Trepetinca",
        "lokacija": "Trepetinca"
    },
    {
        "grad": "Prizren",
        "opstina": "Tupec",
        "lokacija": "Tupec"
    },
    {
        "grad": "Prizren",
        "opstina": "Hoča Zagradska",
        "lokacija": "Hoča Zagradska"
    },
    {
        "grad": "Prizren",
        "opstina": "Caparce",
        "lokacija": "Caparce"
    },
    {
        "grad": "Prizren",
        "opstina": "Šajinovac",
        "lokacija": "Šajinovac"
    },
    {
        "grad": "Prizren",
        "opstina": "Škoza",
        "lokacija": "Škoza"
    },
    {
        "grad": "Prizren",
        "opstina": "Špinadija",
        "lokacija": "Špinadija"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Prijepolje",
        "lokacija": "Prijepolje"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gradska lokacija",
        "lokacija": "Vakuf"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gradska lokacija",
        "lokacija": "Jezdovića Kosa"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gradska lokacija",
        "lokacija": "Kolovrat"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gradska lokacija",
        "lokacija": "Lim"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gradska lokacija",
        "lokacija": "Luke"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gradska lokacija",
        "lokacija": "Raišnjeva"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gradska lokacija",
        "lokacija": "Suvodo"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gradska lokacija",
        "lokacija": "Šehovića Polje"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Aljinovići",
        "lokacija": "Aljinovići"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Balići",
        "lokacija": "Balići"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Bare",
        "lokacija": "Bare"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Biskupići",
        "lokacija": "Biskupići"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Bjelahova",
        "lokacija": "Bjelahova"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Brajkovac",
        "lokacija": "Brajkovac"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Brvine",
        "lokacija": "Brvine"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Brodarevo",
        "lokacija": "Brodarevo"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Bukovik",
        "lokacija": "Bukovik"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Vinicka",
        "lokacija": "Vinicka"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Vrbovo",
        "lokacija": "Vrbovo"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gojakovići",
        "lokacija": "Gojakovići"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gornje Babine",
        "lokacija": "Gornje Babine"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gornje Goračiće",
        "lokacija": "Gornje Goračiće"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gornji Stranjani",
        "lokacija": "Gornji Stranjani"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gostun",
        "lokacija": "Gostun"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Gračanica",
        "lokacija": "Gračanica"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Grobnice",
        "lokacija": "Grobnice"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Divci",
        "lokacija": "Divci"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Donje Babine",
        "lokacija": "Donje Babine"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Donji Stranjani",
        "lokacija": "Donji Stranjani"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Drenova",
        "lokacija": "Drenova"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Dušmanići",
        "lokacija": "Dušmanići"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Đurašići",
        "lokacija": "Đurašići"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Zabrdnji Toci",
        "lokacija": "Zabrdnji Toci"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Zavinograđe",
        "lokacija": "Zavinograđe"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Zalug",
        "lokacija": "Zalug"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Zastup",
        "lokacija": "Zastup"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Zvijezd",
        "lokacija": "Zvijezd"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Ivanje",
        "lokacija": "Ivanje"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Ivezići",
        "lokacija": "Ivezići"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Izbičanj",
        "lokacija": "Izbičanj"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Jabuka",
        "lokacija": "Jabuka"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Junčevići",
        "lokacija": "Junčevići"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Kamena Gora",
        "lokacija": "Kamena Gora"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Karaula",
        "lokacija": "Karaula"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Karoševina",
        "lokacija": "Karoševina"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Kaćevo",
        "lokacija": "Kaćevo"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Kašice",
        "lokacija": "Kašice"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Kovačevac",
        "lokacija": "Kovačevac"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Koprivna",
        "lokacija": "Koprivna"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Kosatica",
        "lokacija": "Kosatica"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Koševine",
        "lokacija": "Koševine"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Kruševo",
        "lokacija": "Kruševo"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Kučin",
        "lokacija": "Kučin"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Lučice",
        "lokacija": "Lučice"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Mataruge",
        "lokacija": "Mataruge"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Međani",
        "lokacija": "Međani"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Mijani",
        "lokacija": "Mijani"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Mijoska",
        "lokacija": "Mijoska"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Milakovići",
        "lokacija": "Milakovići"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Mileševo",
        "lokacija": "Mileševo"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Milošev Do",
        "lokacija": "Milošev Do"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Miljevići",
        "lokacija": "Miljevići"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Mrčkovina",
        "lokacija": "Mrčkovina"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Muškovina",
        "lokacija": "Muškovina"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Oraovac",
        "lokacija": "Oraovac"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Orašac",
        "lokacija": "Orašac"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Osoje",
        "lokacija": "Osoje"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Oštra Stijena",
        "lokacija": "Oštra Stijena"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Potkrš",
        "lokacija": "Potkrš"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Potok",
        "lokacija": "Potok"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Pravoševo",
        "lokacija": "Pravoševo"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Pranjci",
        "lokacija": "Pranjci"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Rasno",
        "lokacija": "Rasno"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Ratajska",
        "lokacija": "Ratajska"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Sedobro",
        "lokacija": "Sedobro"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Seljane",
        "lokacija": "Seljane"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Seljašnica",
        "lokacija": "Seljašnica"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Skokuće",
        "lokacija": "Skokuće"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Sopotnica",
        "lokacija": "Sopotnica"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Taševo",
        "lokacija": "Taševo"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Hisardžik",
        "lokacija": "Hisardžik"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Hrta",
        "lokacija": "Hrta"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Crkveni Toci",
        "lokacija": "Crkveni Toci"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Čadinje",
        "lokacija": "Čadinje"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Čauševići",
        "lokacija": "Čauševići"
    },
    {
        "grad": "Prijepolje",
        "opstina": "Džurovo",
        "lokacija": "Džurovo"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Prokuplje",
        "lokacija": "Prokuplje"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Borovnjak"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Garić"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Gornja Draganja"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Đurevačko Naselje"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Jabukar"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Kasarna"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Lipar"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Naselje"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Ozrensko Naselje"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Pojate"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Sokićev Bulevar"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Hisar"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Arbanaška",
        "lokacija": "Arbanaška"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Babin Potok",
        "lokacija": "Babin Potok"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Babotinac",
        "lokacija": "Babotinac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Bajčince",
        "lokacija": "Bajčince"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Balinovac",
        "lokacija": "Balinovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Balčak",
        "lokacija": "Balčak"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Bace",
        "lokacija": "Bace"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Bela Voda",
        "lokacija": "Bela Voda"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Beli Kamen",
        "lokacija": "Beli Kamen"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Belogoš",
        "lokacija": "Belogoš"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Beloljin",
        "lokacija": "Beloljin"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Berilje",
        "lokacija": "Berilje"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Bogujevac",
        "lokacija": "Bogujevac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Bregovina",
        "lokacija": "Bregovina"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Bresnik",
        "lokacija": "Bresnik"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Breničić",
        "lokacija": "Breničić"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Bublica",
        "lokacija": "Bublica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Bukuloram",
        "lokacija": "Bukuloram"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Bulatovac",
        "lokacija": "Bulatovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Bučince",
        "lokacija": "Bučince"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Velika Plana",
        "lokacija": "Velika Plana"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Vidovača",
        "lokacija": "Vidovača"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Viča",
        "lokacija": "Viča"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Vlasovo",
        "lokacija": "Vlasovo"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Vodice",
        "lokacija": "Vodice"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Glasovik",
        "lokacija": "Glasovik"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gojinovac",
        "lokacija": "Gojinovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gornja Bejašnica",
        "lokacija": "Gornja Bejašnica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gornja Bresnica",
        "lokacija": "Gornja Bresnica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gornja Konjuša",
        "lokacija": "Gornja Konjuša"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gornja Rečica",
        "lokacija": "Gornja Rečica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gornja Stražava",
        "lokacija": "Gornja Stražava"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gornja Toponica",
        "lokacija": "Gornja Toponica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gornja Trnava",
        "lokacija": "Gornja Trnava"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gornje Kordince",
        "lokacija": "Gornje Kordince"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gornji Statovac",
        "lokacija": "Gornji Statovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Grabovac",
        "lokacija": "Grabovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Gubetin",
        "lokacija": "Gubetin"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Dobrotić",
        "lokacija": "Dobrotić"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Donja Bejašnica",
        "lokacija": "Donja Bejašnica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Donja Bresnica",
        "lokacija": "Donja Bresnica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Donja Konjuša",
        "lokacija": "Donja Konjuša"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Donja Rečica",
        "lokacija": "Donja Rečica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Donja Stražava",
        "lokacija": "Donja Stražava"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Donja Toponica",
        "lokacija": "Donja Toponica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Donja Trnava",
        "lokacija": "Donja Trnava"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Donje Kordince",
        "lokacija": "Donje Kordince"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Donji Statovac",
        "lokacija": "Donji Statovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Dragi Deo",
        "lokacija": "Dragi Deo"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Drenovac",
        "lokacija": "Drenovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Đurovac",
        "lokacija": "Đurovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Đušnica",
        "lokacija": "Đušnica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Žitni Potok",
        "lokacija": "Žitni Potok"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Zdravinje",
        "lokacija": "Zdravinje"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Zlata",
        "lokacija": "Zlata"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Jabučevo",
        "lokacija": "Jabučevo"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Jovine Livade",
        "lokacija": "Jovine Livade"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Jugovac",
        "lokacija": "Jugovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Kaludra",
        "lokacija": "Kaludra"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Klisurica",
        "lokacija": "Klisurica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Kožince",
        "lokacija": "Kožince"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Končić",
        "lokacija": "Končić"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Kondželj",
        "lokacija": "Kondželj"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Kostenica",
        "lokacija": "Kostenica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Krnji grad",
        "lokacija": "Krnji grad"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Kruševica",
        "lokacija": "Kruševica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Mađere",
        "lokacija": "Mađere"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Mala Plana",
        "lokacija": "Mala Plana"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Mačina",
        "lokacija": "Mačina"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Merovac",
        "lokacija": "Merovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Mikulovac",
        "lokacija": "Mikulovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Miljkovica",
        "lokacija": "Miljkovica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Mrljak",
        "lokacija": "Mrljak"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Mršelj",
        "lokacija": "Mršelj"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Nova Božurna",
        "lokacija": "Nova Božurna"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Novi Đurovac",
        "lokacija": "Novi Đurovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Obrtince",
        "lokacija": "Obrtince"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Pasjača",
        "lokacija": "Pasjača"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Pašinac",
        "lokacija": "Pašinac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Pestiš",
        "lokacija": "Pestiš"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Petrovac",
        "lokacija": "Petrovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Piskalje",
        "lokacija": "Piskalje"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Pločnik",
        "lokacija": "Pločnik"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Potočić",
        "lokacija": "Potočić"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Prekadin",
        "lokacija": "Prekadin"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Prekašnica",
        "lokacija": "Prekašnica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Prekopuce",
        "lokacija": "Prekopuce"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Rankova Reka",
        "lokacija": "Rankova Reka"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Rastovnica",
        "lokacija": "Rastovnica"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Rgaje",
        "lokacija": "Rgaje"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Reljinac",
        "lokacija": "Reljinac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Resinac",
        "lokacija": "Resinac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Selište",
        "lokacija": "Selište"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Smrdan",
        "lokacija": "Smrdan"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Srednji Statovac",
        "lokacija": "Srednji Statovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Stari Đurovac",
        "lokacija": "Stari Đurovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Staro Selo",
        "lokacija": "Staro Selo"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Tovrljane",
        "lokacija": "Tovrljane"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Trnovi Laz",
        "lokacija": "Trnovi Laz"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Tulare",
        "lokacija": "Tulare"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Ćukovac",
        "lokacija": "Ćukovac"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Džigolj",
        "lokacija": "Džigolj"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Ševiš",
        "lokacija": "Ševiš"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Široke Njive",
        "lokacija": "Široke Njive"
    },
    {
        "grad": "Prokuplje",
        "opstina": "Šišmanovac",
        "lokacija": "Šišmanovac"
    },
    {
        "grad": "Ražanj",
        "opstina": "Ražanj",
        "lokacija": "Ražanj"
    },
    {
        "grad": "Ražanj",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Ražanj",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Ražanj",
        "opstina": "Braljina",
        "lokacija": "Braljina"
    },
    {
        "grad": "Ražanj",
        "opstina": "Varoš",
        "lokacija": "Varoš"
    },
    {
        "grad": "Ražanj",
        "opstina": "Vitoševac",
        "lokacija": "Vitoševac"
    },
    {
        "grad": "Ražanj",
        "opstina": "Grabovo",
        "lokacija": "Grabovo"
    },
    {
        "grad": "Ražanj",
        "opstina": "Lipovac",
        "lokacija": "Lipovac"
    },
    {
        "grad": "Ražanj",
        "opstina": "Mađere",
        "lokacija": "Mađere"
    },
    {
        "grad": "Ražanj",
        "opstina": "Maletina",
        "lokacija": "Maletina"
    },
    {
        "grad": "Ražanj",
        "opstina": "Maćija",
        "lokacija": "Maćija"
    },
    {
        "grad": "Ražanj",
        "opstina": "Novi Bračin",
        "lokacija": "Novi Bračin"
    },
    {
        "grad": "Ražanj",
        "opstina": "Pardik",
        "lokacija": "Pardik"
    },
    {
        "grad": "Ražanj",
        "opstina": "Podgorac",
        "lokacija": "Podgorac"
    },
    {
        "grad": "Ražanj",
        "opstina": "Poslon",
        "lokacija": "Poslon"
    },
    {
        "grad": "Ražanj",
        "opstina": "Praskovče",
        "lokacija": "Praskovče"
    },
    {
        "grad": "Ražanj",
        "opstina": "Pretrkovac",
        "lokacija": "Pretrkovac"
    },
    {
        "grad": "Ražanj",
        "opstina": "Rujište",
        "lokacija": "Rujište"
    },
    {
        "grad": "Ražanj",
        "opstina": "Skorica",
        "lokacija": "Skorica"
    },
    {
        "grad": "Ražanj",
        "opstina": "Smilovac",
        "lokacija": "Smilovac"
    },
    {
        "grad": "Ražanj",
        "opstina": "Stari Bračin",
        "lokacija": "Stari Bračin"
    },
    {
        "grad": "Ražanj",
        "opstina": "Cerovo",
        "lokacija": "Cerovo"
    },
    {
        "grad": "Ražanj",
        "opstina": "Crni Kao",
        "lokacija": "Crni Kao"
    },
    {
        "grad": "Ražanj",
        "opstina": "Čubura",
        "lokacija": "Čubura"
    },
    {
        "grad": "Ražanj",
        "opstina": "Šetka",
        "lokacija": "Šetka"
    },
    {
        "grad": "Rača",
        "opstina": "Rača",
        "lokacija": "Rača"
    },
    {
        "grad": "Rača",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Rača",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Rača",
        "opstina": "Adrovac",
        "lokacija": "Adrovac"
    },
    {
        "grad": "Rača",
        "opstina": "Borci",
        "lokacija": "Borci"
    },
    {
        "grad": "Rača",
        "opstina": "Bošnjane",
        "lokacija": "Bošnjane"
    },
    {
        "grad": "Rača",
        "opstina": "Veliko Krčmare",
        "lokacija": "Veliko Krčmare"
    },
    {
        "grad": "Rača",
        "opstina": "Viševac",
        "lokacija": "Viševac"
    },
    {
        "grad": "Rača",
        "opstina": "Vojinovac",
        "lokacija": "Vojinovac"
    },
    {
        "grad": "Rača",
        "opstina": "Vučić",
        "lokacija": "Vučić"
    },
    {
        "grad": "Rača",
        "opstina": "Donja Rača",
        "lokacija": "Donja Rača"
    },
    {
        "grad": "Rača",
        "opstina": "Donje Jarušice",
        "lokacija": "Donje Jarušice"
    },
    {
        "grad": "Rača",
        "opstina": "Đurđevo",
        "lokacija": "Đurđevo"
    },
    {
        "grad": "Rača",
        "opstina": "Malo Krčmare",
        "lokacija": "Malo Krčmare"
    },
    {
        "grad": "Rača",
        "opstina": "Miraševac",
        "lokacija": "Miraševac"
    },
    {
        "grad": "Rača",
        "opstina": "Popović",
        "lokacija": "Popović"
    },
    {
        "grad": "Rača",
        "opstina": "Saranovo",
        "lokacija": "Saranovo"
    },
    {
        "grad": "Rača",
        "opstina": "Sepci",
        "lokacija": "Sepci"
    },
    {
        "grad": "Rača",
        "opstina": "Sipić",
        "lokacija": "Sipić"
    },
    {
        "grad": "Rača",
        "opstina": "Trska",
        "lokacija": "Trska"
    },
    {
        "grad": "Raška",
        "opstina": "Raška",
        "lokacija": "Raška"
    },
    {
        "grad": "Raška",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Raška",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Raška",
        "opstina": "Badanj",
        "lokacija": "Badanj"
    },
    {
        "grad": "Raška",
        "opstina": "Baljevac",
        "lokacija": "Baljevac"
    },
    {
        "grad": "Raška",
        "opstina": "Bela Stena",
        "lokacija": "Bela Stena"
    },
    {
        "grad": "Raška",
        "opstina": "Belo Polje",
        "lokacija": "Belo Polje"
    },
    {
        "grad": "Raška",
        "opstina": "Beoci",
        "lokacija": "Beoci"
    },
    {
        "grad": "Raška",
        "opstina": "Biljanovac",
        "lokacija": "Biljanovac"
    },
    {
        "grad": "Raška",
        "opstina": "Biniće",
        "lokacija": "Biniće"
    },
    {
        "grad": "Raška",
        "opstina": "Biočin",
        "lokacija": "Biočin"
    },
    {
        "grad": "Raška",
        "opstina": "Boroviće",
        "lokacija": "Boroviće"
    },
    {
        "grad": "Raška",
        "opstina": "Boće",
        "lokacija": "Boće"
    },
    {
        "grad": "Raška",
        "opstina": "Brvenik",
        "lokacija": "Brvenik"
    },
    {
        "grad": "Raška",
        "opstina": "Brvenik Naselje",
        "lokacija": "Brvenik Naselje"
    },
    {
        "grad": "Raška",
        "opstina": "Brvenica",
        "lokacija": "Brvenica"
    },
    {
        "grad": "Raška",
        "opstina": "Varevo",
        "lokacija": "Varevo"
    },
    {
        "grad": "Raška",
        "opstina": "Vojmilovići",
        "lokacija": "Vojmilovići"
    },
    {
        "grad": "Raška",
        "opstina": "Vrtine",
        "lokacija": "Vrtine"
    },
    {
        "grad": "Raška",
        "opstina": "Gnjilica",
        "lokacija": "Gnjilica"
    },
    {
        "grad": "Raška",
        "opstina": "Gostiradiće",
        "lokacija": "Gostiradiće"
    },
    {
        "grad": "Raška",
        "opstina": "gradac",
        "lokacija": "gradac"
    },
    {
        "grad": "Raška",
        "opstina": "Draganići",
        "lokacija": "Draganići"
    },
    {
        "grad": "Raška",
        "opstina": "Žerađe",
        "lokacija": "Žerađe"
    },
    {
        "grad": "Raška",
        "opstina": "Žutice",
        "lokacija": "Žutice"
    },
    {
        "grad": "Raška",
        "opstina": "Zarevo",
        "lokacija": "Zarevo"
    },
    {
        "grad": "Raška",
        "opstina": "Jošanička Banja",
        "lokacija": "Jošanička Banja"
    },
    {
        "grad": "Raška",
        "opstina": "Kaznoviće",
        "lokacija": "Kaznoviće"
    },
    {
        "grad": "Raška",
        "opstina": "Karadak",
        "lokacija": "Karadak"
    },
    {
        "grad": "Raška",
        "opstina": "Kovači",
        "lokacija": "Kovači"
    },
    {
        "grad": "Raška",
        "opstina": "Kopaonik",
        "lokacija": "Kopaonik"
    },
    {
        "grad": "Raška",
        "opstina": "Korlaće",
        "lokacija": "Korlaće"
    },
    {
        "grad": "Raška",
        "opstina": "Kraviće",
        "lokacija": "Kraviće"
    },
    {
        "grad": "Raška",
        "opstina": "Kremiće",
        "lokacija": "Kremiće"
    },
    {
        "grad": "Raška",
        "opstina": "Kruševica",
        "lokacija": "Kruševica"
    },
    {
        "grad": "Raška",
        "opstina": "Kurići",
        "lokacija": "Kurići"
    },
    {
        "grad": "Raška",
        "opstina": "Kućane",
        "lokacija": "Kućane"
    },
    {
        "grad": "Raška",
        "opstina": "Lisina",
        "lokacija": "Lisina"
    },
    {
        "grad": "Raška",
        "opstina": "Lukovo",
        "lokacija": "Lukovo"
    },
    {
        "grad": "Raška",
        "opstina": "Milatkoviće",
        "lokacija": "Milatkoviće"
    },
    {
        "grad": "Raška",
        "opstina": "Mure",
        "lokacija": "Mure"
    },
    {
        "grad": "Raška",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Raška",
        "opstina": "Nosoljin",
        "lokacija": "Nosoljin"
    },
    {
        "grad": "Raška",
        "opstina": "Orahovo",
        "lokacija": "Orahovo"
    },
    {
        "grad": "Raška",
        "opstina": "Pavlica",
        "lokacija": "Pavlica"
    },
    {
        "grad": "Raška",
        "opstina": "Panojeviće",
        "lokacija": "Panojeviće"
    },
    {
        "grad": "Raška",
        "opstina": "Piskanja",
        "lokacija": "Piskanja"
    },
    {
        "grad": "Raška",
        "opstina": "Plavkovo",
        "lokacija": "Plavkovo"
    },
    {
        "grad": "Raška",
        "opstina": "Plešin",
        "lokacija": "Plešin"
    },
    {
        "grad": "Raška",
        "opstina": "Pobrđe",
        "lokacija": "Pobrđe"
    },
    {
        "grad": "Raška",
        "opstina": "Pokrvenik",
        "lokacija": "Pokrvenik"
    },
    {
        "grad": "Raška",
        "opstina": "Pocesje",
        "lokacija": "Pocesje"
    },
    {
        "grad": "Raška",
        "opstina": "Radošiće",
        "lokacija": "Radošiće"
    },
    {
        "grad": "Raška",
        "opstina": "Rakovac",
        "lokacija": "Rakovac"
    },
    {
        "grad": "Raška",
        "opstina": "Rvati",
        "lokacija": "Rvati"
    },
    {
        "grad": "Raška",
        "opstina": "Rudnica",
        "lokacija": "Rudnica"
    },
    {
        "grad": "Raška",
        "opstina": "Sebimilje",
        "lokacija": "Sebimilje"
    },
    {
        "grad": "Raška",
        "opstina": "Semeteš",
        "lokacija": "Semeteš"
    },
    {
        "grad": "Raška",
        "opstina": "Supnje",
        "lokacija": "Supnje"
    },
    {
        "grad": "Raška",
        "opstina": "Tiodže",
        "lokacija": "Tiodže"
    },
    {
        "grad": "Raška",
        "opstina": "Trnava",
        "lokacija": "Trnava"
    },
    {
        "grad": "Raška",
        "opstina": "Crna Glava",
        "lokacija": "Crna Glava"
    },
    {
        "grad": "Raška",
        "opstina": "Šipačina",
        "lokacija": "Šipačina"
    },
    {
        "grad": "Rekovac",
        "opstina": "Rekovac",
        "lokacija": "Rekovac"
    },
    {
        "grad": "Rekovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Rekovac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Rekovac",
        "opstina": "Bare",
        "lokacija": "Bare"
    },
    {
        "grad": "Rekovac",
        "opstina": "Belušić",
        "lokacija": "Belušić"
    },
    {
        "grad": "Rekovac",
        "opstina": "Beočić",
        "lokacija": "Beočić"
    },
    {
        "grad": "Rekovac",
        "opstina": "Bogalinac",
        "lokacija": "Bogalinac"
    },
    {
        "grad": "Rekovac",
        "opstina": "Brajinovac",
        "lokacija": "Brajinovac"
    },
    {
        "grad": "Rekovac",
        "opstina": "Velika Kruševica",
        "lokacija": "Velika Kruševica"
    },
    {
        "grad": "Rekovac",
        "opstina": "Vukmanovac",
        "lokacija": "Vukmanovac"
    },
    {
        "grad": "Rekovac",
        "opstina": "Dobroselica",
        "lokacija": "Dobroselica"
    },
    {
        "grad": "Rekovac",
        "opstina": "Dragovo",
        "lokacija": "Dragovo"
    },
    {
        "grad": "Rekovac",
        "opstina": "Županjevac",
        "lokacija": "Županjevac"
    },
    {
        "grad": "Rekovac",
        "opstina": "Kavadar",
        "lokacija": "Kavadar"
    },
    {
        "grad": "Rekovac",
        "opstina": "Kalenićki Prnjavor",
        "lokacija": "Kalenićki Prnjavor"
    },
    {
        "grad": "Rekovac",
        "opstina": "Kaludra",
        "lokacija": "Kaludra"
    },
    {
        "grad": "Rekovac",
        "opstina": "Komarane",
        "lokacija": "Komarane"
    },
    {
        "grad": "Rekovac",
        "opstina": "Lepojević",
        "lokacija": "Lepojević"
    },
    {
        "grad": "Rekovac",
        "opstina": "Lomnica",
        "lokacija": "Lomnica"
    },
    {
        "grad": "Rekovac",
        "opstina": "Loćika",
        "lokacija": "Loćika"
    },
    {
        "grad": "Rekovac",
        "opstina": "Maleševo",
        "lokacija": "Maleševo"
    },
    {
        "grad": "Rekovac",
        "opstina": "Motrić",
        "lokacija": "Motrić"
    },
    {
        "grad": "Rekovac",
        "opstina": "Nadrlje",
        "lokacija": "Nadrlje"
    },
    {
        "grad": "Rekovac",
        "opstina": "Oparić",
        "lokacija": "Oparić"
    },
    {
        "grad": "Rekovac",
        "opstina": "Prevešt",
        "lokacija": "Prevešt"
    },
    {
        "grad": "Rekovac",
        "opstina": "Rabenovac",
        "lokacija": "Rabenovac"
    },
    {
        "grad": "Rekovac",
        "opstina": "Ratković",
        "lokacija": "Ratković"
    },
    {
        "grad": "Rekovac",
        "opstina": "Sekurič",
        "lokacija": "Sekurič"
    },
    {
        "grad": "Rekovac",
        "opstina": "Sibnica",
        "lokacija": "Sibnica"
    },
    {
        "grad": "Rekovac",
        "opstina": "Siljevica",
        "lokacija": "Siljevica"
    },
    {
        "grad": "Rekovac",
        "opstina": "Tečić",
        "lokacija": "Tečić"
    },
    {
        "grad": "Rekovac",
        "opstina": "Ursule",
        "lokacija": "Ursule"
    },
    {
        "grad": "Rekovac",
        "opstina": "Cikot",
        "lokacija": "Cikot"
    },
    {
        "grad": "Rekovac",
        "opstina": "Šljivica",
        "lokacija": "Šljivica"
    },
    {
        "grad": "Ruma",
        "opstina": "Ruma",
        "lokacija": "Ruma"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Barunovac"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Berak"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Borkovac"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Breg"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Vrbare"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Igralište"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Katanića Sokak"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Kudoš"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Sodol"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Tivol"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Cerje"
    },
    {
        "grad": "Ruma",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Ruma",
        "opstina": "Buđanovci",
        "lokacija": "Buđanovci"
    },
    {
        "grad": "Ruma",
        "opstina": "Vitojevci",
        "lokacija": "Vitojevci"
    },
    {
        "grad": "Ruma",
        "opstina": "Voganj",
        "lokacija": "Voganj"
    },
    {
        "grad": "Ruma",
        "opstina": "Grabovci",
        "lokacija": "Grabovci"
    },
    {
        "grad": "Ruma",
        "opstina": "Dobrinci",
        "lokacija": "Dobrinci"
    },
    {
        "grad": "Ruma",
        "opstina": "Donji Petrovci",
        "lokacija": "Donji Petrovci"
    },
    {
        "grad": "Ruma",
        "opstina": "Žarkovac",
        "lokacija": "Žarkovac"
    },
    {
        "grad": "Ruma",
        "opstina": "Klenak",
        "lokacija": "Klenak"
    },
    {
        "grad": "Ruma",
        "opstina": "Kraljevci",
        "lokacija": "Kraljevci"
    },
    {
        "grad": "Ruma",
        "opstina": "Mali Radinci",
        "lokacija": "Mali Radinci"
    },
    {
        "grad": "Ruma",
        "opstina": "Nikinci",
        "lokacija": "Nikinci"
    },
    {
        "grad": "Ruma",
        "opstina": "Pavlovci",
        "lokacija": "Pavlovci"
    },
    {
        "grad": "Ruma",
        "opstina": "Platičevo",
        "lokacija": "Platičevo"
    },
    {
        "grad": "Ruma",
        "opstina": "Putinci",
        "lokacija": "Putinci"
    },
    {
        "grad": "Ruma",
        "opstina": "Stejanovci",
        "lokacija": "Stejanovci"
    },
    {
        "grad": "Ruma",
        "opstina": "Hrtkovci",
        "lokacija": "Hrtkovci"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Svilajnac",
        "lokacija": "Svilajnac"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Gradska lokacija",
        "lokacija": "Velika Morava"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Vračar"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Gradska lokacija",
        "lokacija": "Resava"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Gradska lokacija",
        "lokacija": "Sinđelićeva"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Bobovo",
        "lokacija": "Bobovo"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Bresje",
        "lokacija": "Bresje"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Vojska",
        "lokacija": "Vojska"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Vrlane",
        "lokacija": "Vrlane"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Gložane",
        "lokacija": "Gložane"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Grabovac",
        "lokacija": "Grabovac"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Dublje",
        "lokacija": "Dublje"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Dubnica",
        "lokacija": "Dubnica"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Đurinac",
        "lokacija": "Đurinac"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Kupinovac",
        "lokacija": "Kupinovac"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Kušiljevo",
        "lokacija": "Kušiljevo"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Lukovica",
        "lokacija": "Lukovica"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Mačevac",
        "lokacija": "Mačevac"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Proštinac",
        "lokacija": "Proštinac"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Radošin",
        "lokacija": "Radošin"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Roanda",
        "lokacija": "Roanda"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Roćevac",
        "lokacija": "Roćevac"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Sedlare",
        "lokacija": "Sedlare"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Subotica",
        "lokacija": "Subotica"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Troponje",
        "lokacija": "Troponje"
    },
    {
        "grad": "Svilajnac",
        "opstina": "Crkvenac",
        "lokacija": "Crkvenac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Svrljig",
        "lokacija": "Svrljig"
    },
    {
        "grad": "Svrljig",
        "opstina": "Gradska lokacija",
        "lokacija": "Lukavica"
    },
    {
        "grad": "Svrljig",
        "opstina": "Gradska lokacija",
        "lokacija": "Magovac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Gradska lokacija",
        "lokacija": "Saraj"
    },
    {
        "grad": "Svrljig",
        "opstina": "Gradska lokacija",
        "lokacija": "Trs"
    },
    {
        "grad": "Svrljig",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Svrljig",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Svrljig",
        "opstina": "Beloinje",
        "lokacija": "Beloinje"
    },
    {
        "grad": "Svrljig",
        "opstina": "Burdimo",
        "lokacija": "Burdimo"
    },
    {
        "grad": "Svrljig",
        "opstina": "Bučum",
        "lokacija": "Bučum"
    },
    {
        "grad": "Svrljig",
        "opstina": "Varoš",
        "lokacija": "Varoš"
    },
    {
        "grad": "Svrljig",
        "opstina": "Vlahovo",
        "lokacija": "Vlahovo"
    },
    {
        "grad": "Svrljig",
        "opstina": "Galibabinac",
        "lokacija": "Galibabinac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Gojmanovac",
        "lokacija": "Gojmanovac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Grbavče",
        "lokacija": "Grbavče"
    },
    {
        "grad": "Svrljig",
        "opstina": "Gulijan",
        "lokacija": "Gulijan"
    },
    {
        "grad": "Svrljig",
        "opstina": "Guševac",
        "lokacija": "Guševac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Davidovac",
        "lokacija": "Davidovac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Drajinac",
        "lokacija": "Drajinac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Đurinac",
        "lokacija": "Đurinac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Željevo",
        "lokacija": "Željevo"
    },
    {
        "grad": "Svrljig",
        "opstina": "Izvor",
        "lokacija": "Izvor"
    },
    {
        "grad": "Svrljig",
        "opstina": "Kopajkošara",
        "lokacija": "Kopajkošara"
    },
    {
        "grad": "Svrljig",
        "opstina": "Labukovo",
        "lokacija": "Labukovo"
    },
    {
        "grad": "Svrljig",
        "opstina": "Lalinac",
        "lokacija": "Lalinac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Lozan",
        "lokacija": "Lozan"
    },
    {
        "grad": "Svrljig",
        "opstina": "Lukovo",
        "lokacija": "Lukovo"
    },
    {
        "grad": "Svrljig",
        "opstina": "Manojlica",
        "lokacija": "Manojlica"
    },
    {
        "grad": "Svrljig",
        "opstina": "Merdželat",
        "lokacija": "Merdželat"
    },
    {
        "grad": "Svrljig",
        "opstina": "Mečji Do",
        "lokacija": "Mečji Do"
    },
    {
        "grad": "Svrljig",
        "opstina": "Niševac",
        "lokacija": "Niševac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Okolište",
        "lokacija": "Okolište"
    },
    {
        "grad": "Svrljig",
        "opstina": "Okruglica",
        "lokacija": "Okruglica"
    },
    {
        "grad": "Svrljig",
        "opstina": "Palilula",
        "lokacija": "Palilula"
    },
    {
        "grad": "Svrljig",
        "opstina": "Periš",
        "lokacija": "Periš"
    },
    {
        "grad": "Svrljig",
        "opstina": "Pirkovac",
        "lokacija": "Pirkovac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Plužina",
        "lokacija": "Plužina"
    },
    {
        "grad": "Svrljig",
        "opstina": "Popšica",
        "lokacija": "Popšica"
    },
    {
        "grad": "Svrljig",
        "opstina": "Prekonoga",
        "lokacija": "Prekonoga"
    },
    {
        "grad": "Svrljig",
        "opstina": "Radmirovac",
        "lokacija": "Radmirovac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Ribare",
        "lokacija": "Ribare"
    },
    {
        "grad": "Svrljig",
        "opstina": "Slivje",
        "lokacija": "Slivje"
    },
    {
        "grad": "Svrljig",
        "opstina": "Tijovac",
        "lokacija": "Tijovac"
    },
    {
        "grad": "Svrljig",
        "opstina": "Crnoljevica",
        "lokacija": "Crnoljevica"
    },
    {
        "grad": "Svrljig",
        "opstina": "Šljivovik",
        "lokacija": "Šljivovik"
    },
    {
        "grad": "Senta",
        "opstina": "Senta",
        "lokacija": "Senta"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Alveg"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Kolonija"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Makoš"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Mali Rit"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Pana"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Pesak"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Tisa"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Topartski duž"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Čarda"
    },
    {
        "grad": "Senta",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Senta",
        "opstina": "Bogaraš",
        "lokacija": "Bogaraš"
    },
    {
        "grad": "Senta",
        "opstina": "Gornji Breg",
        "lokacija": "Gornji Breg"
    },
    {
        "grad": "Senta",
        "opstina": "Kevi",
        "lokacija": "Kevi"
    },
    {
        "grad": "Senta",
        "opstina": "Tornjoš",
        "lokacija": "Tornjoš"
    },
    {
        "grad": "Sečanj",
        "opstina": "Sečanj",
        "lokacija": "Sečanj"
    },
    {
        "grad": "Sečanj",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Sečanj",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Sečanj",
        "opstina": "Banatska Dubica",
        "lokacija": "Banatska Dubica"
    },
    {
        "grad": "Sečanj",
        "opstina": "Boka",
        "lokacija": "Boka"
    },
    {
        "grad": "Sečanj",
        "opstina": "Busenje",
        "lokacija": "Busenje"
    },
    {
        "grad": "Sečanj",
        "opstina": "Jarkovac",
        "lokacija": "Jarkovac"
    },
    {
        "grad": "Sečanj",
        "opstina": "Jaša Tomić",
        "lokacija": "Jaša Tomić"
    },
    {
        "grad": "Sečanj",
        "opstina": "Konak",
        "lokacija": "Konak"
    },
    {
        "grad": "Sečanj",
        "opstina": "Krajišnik",
        "lokacija": "Krajišnik"
    },
    {
        "grad": "Sečanj",
        "opstina": "Neuzina",
        "lokacija": "Neuzina"
    },
    {
        "grad": "Sečanj",
        "opstina": "Sutjeska",
        "lokacija": "Sutjeska"
    },
    {
        "grad": "Sečanj",
        "opstina": "Šurjan",
        "lokacija": "Šurjan"
    },
    {
        "grad": "Sjenica",
        "opstina": "Sjenica",
        "lokacija": "Sjenica"
    },
    {
        "grad": "Sjenica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Sjenica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Sjenica",
        "opstina": "Aliveroviće",
        "lokacija": "Aliveroviće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Bagačiće",
        "lokacija": "Bagačiće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Bare",
        "lokacija": "Bare"
    },
    {
        "grad": "Sjenica",
        "opstina": "Bačija",
        "lokacija": "Bačija"
    },
    {
        "grad": "Sjenica",
        "opstina": "Bioc",
        "lokacija": "Bioc"
    },
    {
        "grad": "Sjenica",
        "opstina": "Blato",
        "lokacija": "Blato"
    },
    {
        "grad": "Sjenica",
        "opstina": "Boguti",
        "lokacija": "Boguti"
    },
    {
        "grad": "Sjenica",
        "opstina": "Božov Potok",
        "lokacija": "Božov Potok"
    },
    {
        "grad": "Sjenica",
        "opstina": "Boljare",
        "lokacija": "Boljare"
    },
    {
        "grad": "Sjenica",
        "opstina": "Borišiće",
        "lokacija": "Borišiće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Boroviće",
        "lokacija": "Boroviće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Breza",
        "lokacija": "Breza"
    },
    {
        "grad": "Sjenica",
        "opstina": "Brnjica",
        "lokacija": "Brnjica"
    },
    {
        "grad": "Sjenica",
        "opstina": "Buđevo",
        "lokacija": "Buđevo"
    },
    {
        "grad": "Sjenica",
        "opstina": "Vapa",
        "lokacija": "Vapa"
    },
    {
        "grad": "Sjenica",
        "opstina": "Veskoviće",
        "lokacija": "Veskoviće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Visočka",
        "lokacija": "Visočka"
    },
    {
        "grad": "Sjenica",
        "opstina": "Višnjeva",
        "lokacija": "Višnjeva"
    },
    {
        "grad": "Sjenica",
        "opstina": "Višnjice",
        "lokacija": "Višnjice"
    },
    {
        "grad": "Sjenica",
        "opstina": "Vrapci",
        "lokacija": "Vrapci"
    },
    {
        "grad": "Sjenica",
        "opstina": "Vrbnica",
        "lokacija": "Vrbnica"
    },
    {
        "grad": "Sjenica",
        "opstina": "Vrsjenice",
        "lokacija": "Vrsjenice"
    },
    {
        "grad": "Sjenica",
        "opstina": "Goluban",
        "lokacija": "Goluban"
    },
    {
        "grad": "Sjenica",
        "opstina": "Gornje Lopiže",
        "lokacija": "Gornje Lopiže"
    },
    {
        "grad": "Sjenica",
        "opstina": "Goševo",
        "lokacija": "Goševo"
    },
    {
        "grad": "Sjenica",
        "opstina": "Grabovica",
        "lokacija": "Grabovica"
    },
    {
        "grad": "Sjenica",
        "opstina": "gradac",
        "lokacija": "gradac"
    },
    {
        "grad": "Sjenica",
        "opstina": "Grgaje",
        "lokacija": "Grgaje"
    },
    {
        "grad": "Sjenica",
        "opstina": "Doliće",
        "lokacija": "Doliće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Donje Goračiće",
        "lokacija": "Donje Goračiće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Donje Lopiže",
        "lokacija": "Donje Lopiže"
    },
    {
        "grad": "Sjenica",
        "opstina": "Dragojloviće",
        "lokacija": "Dragojloviće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Draževiće",
        "lokacija": "Draževiće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Družiniće",
        "lokacija": "Družiniće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Dubnica",
        "lokacija": "Dubnica"
    },
    {
        "grad": "Sjenica",
        "opstina": "Duga Poljana",
        "lokacija": "Duga Poljana"
    },
    {
        "grad": "Sjenica",
        "opstina": "Dujke",
        "lokacija": "Dujke"
    },
    {
        "grad": "Sjenica",
        "opstina": "Dunišiće",
        "lokacija": "Dunišiće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Žabren",
        "lokacija": "Žabren"
    },
    {
        "grad": "Sjenica",
        "opstina": "Žitniće",
        "lokacija": "Žitniće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Zabrđe",
        "lokacija": "Zabrđe"
    },
    {
        "grad": "Sjenica",
        "opstina": "Zaječiće",
        "lokacija": "Zaječiće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Zahumsko",
        "lokacija": "Zahumsko"
    },
    {
        "grad": "Sjenica",
        "opstina": "Jevik",
        "lokacija": "Jevik"
    },
    {
        "grad": "Sjenica",
        "opstina": "Jezero",
        "lokacija": "Jezero"
    },
    {
        "grad": "Sjenica",
        "opstina": "Kalipolje",
        "lokacija": "Kalipolje"
    },
    {
        "grad": "Sjenica",
        "opstina": "Kamešnica",
        "lokacija": "Kamešnica"
    },
    {
        "grad": "Sjenica",
        "opstina": "Kanjevina",
        "lokacija": "Kanjevina"
    },
    {
        "grad": "Sjenica",
        "opstina": "Karajukića Bunari",
        "lokacija": "Karajukića Bunari"
    },
    {
        "grad": "Sjenica",
        "opstina": "Kijevci",
        "lokacija": "Kijevci"
    },
    {
        "grad": "Sjenica",
        "opstina": "Kladnica",
        "lokacija": "Kladnica"
    },
    {
        "grad": "Sjenica",
        "opstina": "Kneževac",
        "lokacija": "Kneževac"
    },
    {
        "grad": "Sjenica",
        "opstina": "Koznik",
        "lokacija": "Koznik"
    },
    {
        "grad": "Sjenica",
        "opstina": "Kokošiće",
        "lokacija": "Kokošiće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Krajinoviće",
        "lokacija": "Krajinoviće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Krivaja",
        "lokacija": "Krivaja"
    },
    {
        "grad": "Sjenica",
        "opstina": "Krnja Jela",
        "lokacija": "Krnja Jela"
    },
    {
        "grad": "Sjenica",
        "opstina": "Krstac",
        "lokacija": "Krstac"
    },
    {
        "grad": "Sjenica",
        "opstina": "Krće",
        "lokacija": "Krće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Lijeva Reka",
        "lokacija": "Lijeva Reka"
    },
    {
        "grad": "Sjenica",
        "opstina": "Ljutaje",
        "lokacija": "Ljutaje"
    },
    {
        "grad": "Sjenica",
        "opstina": "Mašoviće",
        "lokacija": "Mašoviće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Medare",
        "lokacija": "Medare"
    },
    {
        "grad": "Sjenica",
        "opstina": "Međugor",
        "lokacija": "Međugor"
    },
    {
        "grad": "Sjenica",
        "opstina": "Milići",
        "lokacija": "Milići"
    },
    {
        "grad": "Sjenica",
        "opstina": "Papiće",
        "lokacija": "Papiće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Petrovo Polje",
        "lokacija": "Petrovo Polje"
    },
    {
        "grad": "Sjenica",
        "opstina": "Plana",
        "lokacija": "Plana"
    },
    {
        "grad": "Sjenica",
        "opstina": "Poda",
        "lokacija": "Poda"
    },
    {
        "grad": "Sjenica",
        "opstina": "Ponorac",
        "lokacija": "Ponorac"
    },
    {
        "grad": "Sjenica",
        "opstina": "Pralja",
        "lokacija": "Pralja"
    },
    {
        "grad": "Sjenica",
        "opstina": "Raždaginja",
        "lokacija": "Raždaginja"
    },
    {
        "grad": "Sjenica",
        "opstina": "Rasno",
        "lokacija": "Rasno"
    },
    {
        "grad": "Sjenica",
        "opstina": "Raspoganče",
        "lokacija": "Raspoganče"
    },
    {
        "grad": "Sjenica",
        "opstina": "Rastenoviće",
        "lokacija": "Rastenoviće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Raškoviće",
        "lokacija": "Raškoviće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Skradnik",
        "lokacija": "Skradnik"
    },
    {
        "grad": "Sjenica",
        "opstina": "Strajiniće",
        "lokacija": "Strajiniće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Stup",
        "lokacija": "Stup"
    },
    {
        "grad": "Sjenica",
        "opstina": "Sugubine",
        "lokacija": "Sugubine"
    },
    {
        "grad": "Sjenica",
        "opstina": "Sušica",
        "lokacija": "Sušica"
    },
    {
        "grad": "Sjenica",
        "opstina": "Trešnjevica",
        "lokacija": "Trešnjevica"
    },
    {
        "grad": "Sjenica",
        "opstina": "Trijebine",
        "lokacija": "Trijebine"
    },
    {
        "grad": "Sjenica",
        "opstina": "Tuzinje",
        "lokacija": "Tuzinje"
    },
    {
        "grad": "Sjenica",
        "opstina": "Tutiće",
        "lokacija": "Tutiće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Uvac",
        "lokacija": "Uvac"
    },
    {
        "grad": "Sjenica",
        "opstina": "Ugao",
        "lokacija": "Ugao"
    },
    {
        "grad": "Sjenica",
        "opstina": "Ursule",
        "lokacija": "Ursule"
    },
    {
        "grad": "Sjenica",
        "opstina": "Ušak",
        "lokacija": "Ušak"
    },
    {
        "grad": "Sjenica",
        "opstina": "Fijulj",
        "lokacija": "Fijulj"
    },
    {
        "grad": "Sjenica",
        "opstina": "Caričina",
        "lokacija": "Caričina"
    },
    {
        "grad": "Sjenica",
        "opstina": "Cetanoviće",
        "lokacija": "Cetanoviće"
    },
    {
        "grad": "Sjenica",
        "opstina": "Crvsko",
        "lokacija": "Crvsko"
    },
    {
        "grad": "Sjenica",
        "opstina": "Crčevo",
        "lokacija": "Crčevo"
    },
    {
        "grad": "Sjenica",
        "opstina": "Čedovo",
        "lokacija": "Čedovo"
    },
    {
        "grad": "Sjenica",
        "opstina": "Čipalje",
        "lokacija": "Čipalje"
    },
    {
        "grad": "Sjenica",
        "opstina": "Čitluk",
        "lokacija": "Čitluk"
    },
    {
        "grad": "Sjenica",
        "opstina": "Šare",
        "lokacija": "Šare"
    },
    {
        "grad": "Sjenica",
        "opstina": "Štavalj",
        "lokacija": "Štavalj"
    },
    {
        "grad": "Sjenica",
        "opstina": "Šušure",
        "lokacija": "Šušure"
    },
    {
        "grad": "Smederevo",
        "opstina": "Smederevo",
        "lokacija": "Smederevo"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "25. Maj"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Buline Vode"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Godomin"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Gornja Vaga"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Donji grad"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Dunav"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Zlatno Brdo"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Jugovo"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Karađorđev Dud"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Karađorđevo Brdo"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Kovačićevo"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Ladna Voda"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Leštar"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Papazovac"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Plavinac"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Provalija"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Sveti Sava"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Senjak"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Slavija"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Carina"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Smederevo",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Smederevo",
        "opstina": "Badljevica",
        "lokacija": "Badljevica"
    },
    {
        "grad": "Smederevo",
        "opstina": "Binovac",
        "lokacija": "Binovac"
    },
    {
        "grad": "Smederevo",
        "opstina": "Vodanj",
        "lokacija": "Vodanj"
    },
    {
        "grad": "Smederevo",
        "opstina": "Vranovo",
        "lokacija": "Vranovo"
    },
    {
        "grad": "Smederevo",
        "opstina": "Vrbovac",
        "lokacija": "Vrbovac"
    },
    {
        "grad": "Smederevo",
        "opstina": "Vučak",
        "lokacija": "Vučak"
    },
    {
        "grad": "Smederevo",
        "opstina": "Dobri Do",
        "lokacija": "Dobri Do"
    },
    {
        "grad": "Smederevo",
        "opstina": "Drugovac",
        "lokacija": "Drugovac"
    },
    {
        "grad": "Smederevo",
        "opstina": "Kolari",
        "lokacija": "Kolari"
    },
    {
        "grad": "Smederevo",
        "opstina": "Kulič",
        "lokacija": "Kulič"
    },
    {
        "grad": "Smederevo",
        "opstina": "Landol",
        "lokacija": "Landol"
    },
    {
        "grad": "Smederevo",
        "opstina": "Lipe",
        "lokacija": "Lipe"
    },
    {
        "grad": "Smederevo",
        "opstina": "Lugavčina",
        "lokacija": "Lugavčina"
    },
    {
        "grad": "Smederevo",
        "opstina": "Lunjevac",
        "lokacija": "Lunjevac"
    },
    {
        "grad": "Smederevo",
        "opstina": "Mala Krsna",
        "lokacija": "Mala Krsna"
    },
    {
        "grad": "Smederevo",
        "opstina": "Malo Orašje",
        "lokacija": "Malo Orašje"
    },
    {
        "grad": "Smederevo",
        "opstina": "Mihajlovac",
        "lokacija": "Mihajlovac"
    },
    {
        "grad": "Smederevo",
        "opstina": "Osipaonica",
        "lokacija": "Osipaonica"
    },
    {
        "grad": "Smederevo",
        "opstina": "Petrijevo",
        "lokacija": "Petrijevo"
    },
    {
        "grad": "Smederevo",
        "opstina": "Radinac",
        "lokacija": "Radinac"
    },
    {
        "grad": "Smederevo",
        "opstina": "Ralja",
        "lokacija": "Ralja"
    },
    {
        "grad": "Smederevo",
        "opstina": "Saraorci",
        "lokacija": "Saraorci"
    },
    {
        "grad": "Smederevo",
        "opstina": "Seone",
        "lokacija": "Seone"
    },
    {
        "grad": "Smederevo",
        "opstina": "Skobalj",
        "lokacija": "Skobalj"
    },
    {
        "grad": "Smederevo",
        "opstina": "Suvodol",
        "lokacija": "Suvodol"
    },
    {
        "grad": "Smederevo",
        "opstina": "Udovice",
        "lokacija": "Udovice"
    },
    {
        "grad": "Smederevo",
        "opstina": "Šalinac",
        "lokacija": "Šalinac"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Smederevska Palanka",
        "lokacija": "Smederevska Palanka"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Vlajića Brdo"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Gorčine"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Ivak"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Kiseljak"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Kolonija"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Mali Ključ"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Mikulja"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Rudine"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Taš"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Hajdučki Potok"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Azanja",
        "lokacija": "Azanja"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Baničina",
        "lokacija": "Baničina"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Bačinac",
        "lokacija": "Bačinac"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Bašin",
        "lokacija": "Bašin"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Vlaški Do",
        "lokacija": "Vlaški Do"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Vodice",
        "lokacija": "Vodice"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Glibovac",
        "lokacija": "Glibovac"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Golobok",
        "lokacija": "Golobok"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Grčac",
        "lokacija": "Grčac"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Kusadak",
        "lokacija": "Kusadak"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Mala Plana",
        "lokacija": "Mala Plana"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Mramorac",
        "lokacija": "Mramorac"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Pridvorice",
        "lokacija": "Pridvorice"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Ratari",
        "lokacija": "Ratari"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Selevac",
        "lokacija": "Selevac"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Stojačak",
        "lokacija": "Stojačak"
    },
    {
        "grad": "Smederevska Palanka",
        "opstina": "Cerovac",
        "lokacija": "Cerovac"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Sokobanja",
        "lokacija": "Sokobanja"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Gradska lokacija",
        "lokacija": "Banjica"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Gradska lokacija",
        "lokacija": "Vrelo Borići"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Gradska lokacija",
        "lokacija": "gradašnica"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Gradska lokacija",
        "lokacija": "Jabukar"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Gradska lokacija",
        "lokacija": "Ozren"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Gradska lokacija",
        "lokacija": "Podina"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Gradska lokacija",
        "lokacija": "Čair"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Gradska lokacija",
        "lokacija": "Čuka 2"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Gradska lokacija",
        "lokacija": "Šetalište"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Beli Potok",
        "lokacija": "Beli Potok"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Blendija",
        "lokacija": "Blendija"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Bogdinac",
        "lokacija": "Bogdinac"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Vrbovac",
        "lokacija": "Vrbovac"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Vrelo",
        "lokacija": "Vrelo"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Vrmdža",
        "lokacija": "Vrmdža"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Dugo Polje",
        "lokacija": "Dugo Polje"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Žučkovac",
        "lokacija": "Žučkovac"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Jezero",
        "lokacija": "Jezero"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Jošanica",
        "lokacija": "Jošanica"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Levovik",
        "lokacija": "Levovik"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Milušinac",
        "lokacija": "Milušinac"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Mužinac",
        "lokacija": "Mužinac"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Nikolinac",
        "lokacija": "Nikolinac"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Poružnica",
        "lokacija": "Poružnica"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Radenkovac",
        "lokacija": "Radenkovac"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Resnik",
        "lokacija": "Resnik"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Rujevica",
        "lokacija": "Rujevica"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Sesalac",
        "lokacija": "Sesalac"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Trgovište",
        "lokacija": "Trgovište"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Trubarevac",
        "lokacija": "Trubarevac"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Cerovica",
        "lokacija": "Cerovica"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Čitluk",
        "lokacija": "Čitluk"
    },
    {
        "grad": "Sokobanja",
        "opstina": "Šarbanovac",
        "lokacija": "Šarbanovac"
    },
    {
        "grad": "Sombor",
        "opstina": "Sombor",
        "lokacija": "Sombor"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Venac"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Goge"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Gornja Varoš"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Železnička Stanica"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Josićko Naselje"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Mlake"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Nenadić"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Rokovci"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Selenča"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Trepča Naselje"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Crvenka"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Čvorak"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Šikara"
    },
    {
        "grad": "Sombor",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Sombor",
        "opstina": "Aleksa Šantić",
        "lokacija": "Aleksa Šantić"
    },
    {
        "grad": "Sombor",
        "opstina": "Bački Breg",
        "lokacija": "Bački Breg"
    },
    {
        "grad": "Sombor",
        "opstina": "Bački Monoštor",
        "lokacija": "Bački Monoštor"
    },
    {
        "grad": "Sombor",
        "opstina": "Bezdan",
        "lokacija": "Bezdan"
    },
    {
        "grad": "Sombor",
        "opstina": "Bilić",
        "lokacija": "Bilić"
    },
    {
        "grad": "Sombor",
        "opstina": "Bukovački Salaši",
        "lokacija": "Bukovački Salaši"
    },
    {
        "grad": "Sombor",
        "opstina": "Gakovo",
        "lokacija": "Gakovo"
    },
    {
        "grad": "Sombor",
        "opstina": "gradina",
        "lokacija": "gradina"
    },
    {
        "grad": "Sombor",
        "opstina": "Doroslovo",
        "lokacija": "Doroslovo"
    },
    {
        "grad": "Sombor",
        "opstina": "Žarkovac",
        "lokacija": "Žarkovac"
    },
    {
        "grad": "Sombor",
        "opstina": "Kljajićevo",
        "lokacija": "Kljajićevo"
    },
    {
        "grad": "Sombor",
        "opstina": "Kolut",
        "lokacija": "Kolut"
    },
    {
        "grad": "Sombor",
        "opstina": "Kruševlje",
        "lokacija": "Kruševlje"
    },
    {
        "grad": "Sombor",
        "opstina": "Lenija",
        "lokacija": "Lenija"
    },
    {
        "grad": "Sombor",
        "opstina": "Lugovo",
        "lokacija": "Lugovo"
    },
    {
        "grad": "Sombor",
        "opstina": "Lugomerci",
        "lokacija": "Lugomerci"
    },
    {
        "grad": "Sombor",
        "opstina": "Milčić",
        "lokacija": "Milčić"
    },
    {
        "grad": "Sombor",
        "opstina": "Obziri",
        "lokacija": "Obziri"
    },
    {
        "grad": "Sombor",
        "opstina": "Radojevići",
        "lokacija": "Radojevići"
    },
    {
        "grad": "Sombor",
        "opstina": "Rančevo",
        "lokacija": "Rančevo"
    },
    {
        "grad": "Sombor",
        "opstina": "Rastina",
        "lokacija": "Rastina"
    },
    {
        "grad": "Sombor",
        "opstina": "Riđica",
        "lokacija": "Riđica"
    },
    {
        "grad": "Sombor",
        "opstina": "Svetozar Miletić",
        "lokacija": "Svetozar Miletić"
    },
    {
        "grad": "Sombor",
        "opstina": "Stanišić",
        "lokacija": "Stanišić"
    },
    {
        "grad": "Sombor",
        "opstina": "Stapar",
        "lokacija": "Stapar"
    },
    {
        "grad": "Sombor",
        "opstina": "Telečka",
        "lokacija": "Telečka"
    },
    {
        "grad": "Sombor",
        "opstina": "Čičovi",
        "lokacija": "Čičovi"
    },
    {
        "grad": "Sombor",
        "opstina": "Čonoplja",
        "lokacija": "Čonoplja"
    },
    {
        "grad": "Sombor",
        "opstina": "Šaponje",
        "lokacija": "Šaponje Salaši"
    },
    {
        "grad": "Srbica",
        "opstina": "Srbica",
        "lokacija": "Srbica"
    },
    {
        "grad": "Srbica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Srbica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Srbica",
        "opstina": "Baks",
        "lokacija": "Baks"
    },
    {
        "grad": "Srbica",
        "opstina": "Banja",
        "lokacija": "Banja"
    },
    {
        "grad": "Srbica",
        "opstina": "Broćna",
        "lokacija": "Broćna"
    },
    {
        "grad": "Srbica",
        "opstina": "Vitak",
        "lokacija": "Vitak"
    },
    {
        "grad": "Srbica",
        "opstina": "Voćnjak",
        "lokacija": "Voćnjak"
    },
    {
        "grad": "Srbica",
        "opstina": "Gornja Klina",
        "lokacija": "Gornja Klina"
    },
    {
        "grad": "Srbica",
        "opstina": "Gornje Prekaze",
        "lokacija": "Gornje Prekaze"
    },
    {
        "grad": "Srbica",
        "opstina": "Gornji Obilić",
        "lokacija": "Gornji Obilić"
    },
    {
        "grad": "Srbica",
        "opstina": "Donja Klina",
        "lokacija": "Donja Klina"
    },
    {
        "grad": "Srbica",
        "opstina": "Donje Obrinje",
        "lokacija": "Donje Obrinje"
    },
    {
        "grad": "Srbica",
        "opstina": "Donje Prekaze",
        "lokacija": "Donje Prekaze"
    },
    {
        "grad": "Srbica",
        "opstina": "Donji Obilić",
        "lokacija": "Donji Obilić"
    },
    {
        "grad": "Srbica",
        "opstina": "Doševac",
        "lokacija": "Doševac"
    },
    {
        "grad": "Srbica",
        "opstina": "Izbica",
        "lokacija": "Izbica"
    },
    {
        "grad": "Srbica",
        "opstina": "Kladernica",
        "lokacija": "Kladernica"
    },
    {
        "grad": "Srbica",
        "opstina": "Kožica",
        "lokacija": "Kožica"
    },
    {
        "grad": "Srbica",
        "opstina": "Kostrc",
        "lokacija": "Kostrc"
    },
    {
        "grad": "Srbica",
        "opstina": "Kotore",
        "lokacija": "Kotore"
    },
    {
        "grad": "Srbica",
        "opstina": "Krasalić",
        "lokacija": "Krasalić"
    },
    {
        "grad": "Srbica",
        "opstina": "Krasmirovac",
        "lokacija": "Krasmirovac"
    },
    {
        "grad": "Srbica",
        "opstina": "Kruševac",
        "lokacija": "Kruševac"
    },
    {
        "grad": "Srbica",
        "opstina": "Kućica",
        "lokacija": "Kućica"
    },
    {
        "grad": "Srbica",
        "opstina": "Lauša",
        "lokacija": "Lauša"
    },
    {
        "grad": "Srbica",
        "opstina": "Leočina",
        "lokacija": "Leočina"
    },
    {
        "grad": "Srbica",
        "opstina": "Likovac",
        "lokacija": "Likovac"
    },
    {
        "grad": "Srbica",
        "opstina": "Ljubovac",
        "lokacija": "Ljubovac"
    },
    {
        "grad": "Srbica",
        "opstina": "Makrmalj",
        "lokacija": "Makrmalj"
    },
    {
        "grad": "Srbica",
        "opstina": "Marina",
        "lokacija": "Marina"
    },
    {
        "grad": "Srbica",
        "opstina": "Mikušnica",
        "lokacija": "Mikušnica"
    },
    {
        "grad": "Srbica",
        "opstina": "Murga",
        "lokacija": "Murga"
    },
    {
        "grad": "Srbica",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Srbica",
        "opstina": "Ovčarevo",
        "lokacija": "Ovčarevo"
    },
    {
        "grad": "Srbica",
        "opstina": "Padalište",
        "lokacija": "Padalište"
    },
    {
        "grad": "Srbica",
        "opstina": "Plužina",
        "lokacija": "Plužina"
    },
    {
        "grad": "Srbica",
        "opstina": "Poljance",
        "lokacija": "Poljance"
    },
    {
        "grad": "Srbica",
        "opstina": "Prelovac",
        "lokacija": "Prelovac"
    },
    {
        "grad": "Srbica",
        "opstina": "Radiševo",
        "lokacija": "Radiševo"
    },
    {
        "grad": "Srbica",
        "opstina": "Rakitnica",
        "lokacija": "Rakitnica"
    },
    {
        "grad": "Srbica",
        "opstina": "Rezala",
        "lokacija": "Rezala"
    },
    {
        "grad": "Srbica",
        "opstina": "Rudnik",
        "lokacija": "Rudnik"
    },
    {
        "grad": "Srbica",
        "opstina": "Srednja Klina",
        "lokacija": "Srednja Klina"
    },
    {
        "grad": "Srbica",
        "opstina": "Suvo Grlo",
        "lokacija": "Suvo Grlo"
    },
    {
        "grad": "Srbica",
        "opstina": "Tica",
        "lokacija": "Tica"
    },
    {
        "grad": "Srbica",
        "opstina": "Trnavce",
        "lokacija": "Trnavce"
    },
    {
        "grad": "Srbica",
        "opstina": "Turićevac",
        "lokacija": "Turićevac"
    },
    {
        "grad": "Srbica",
        "opstina": "Tušilje",
        "lokacija": "Tušilje"
    },
    {
        "grad": "Srbica",
        "opstina": "Ćirez",
        "lokacija": "Ćirez"
    },
    {
        "grad": "Srbica",
        "opstina": "Čitak",
        "lokacija": "Čitak"
    },
    {
        "grad": "Srbica",
        "opstina": "Čubrelj",
        "lokacija": "Čubrelj"
    },
    {
        "grad": "Srbobran",
        "opstina": "Srbobran",
        "lokacija": "Srbobran"
    },
    {
        "grad": "Srbobran",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Naselje"
    },
    {
        "grad": "Srbobran",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Srbobran",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Srbobran",
        "opstina": "Nadalj",
        "lokacija": "Nadalj"
    },
    {
        "grad": "Srbobran",
        "opstina": "Turija",
        "lokacija": "Turija"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Sremska Mitrovica",
        "lokacija": "Sremska Mitrovica"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "22. Avgust"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "29. Novembar"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Aleja"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Autobuska Stanica"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Blok B"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Gajeva"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Dekanske Bašte"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Dudara"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Žitopromet"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "K.P. Dom"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "M.P. Kamenjar"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Maksima Gorkog"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Matije Huđi"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Miloš Obilić"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje 25. Maj"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Nikola Tesla"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Orao - Poljostroj"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Palanka"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Pejton"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Radinački Put"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Sava"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Severno od Planinske"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Slobodan Bajić - Paja"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Spomen Groblje"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Stari Most"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Stevan Sremac"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Sutjeska"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Crvena Česma"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Bešenovački Prnjavor",
        "lokacija": "Bešenovački Prnjavor"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Bešenovo",
        "lokacija": "Bešenovo"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Bosut",
        "lokacija": "Bosut"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Veliki Radinci",
        "lokacija": "Veliki Radinci"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Grgurevci",
        "lokacija": "Grgurevci"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Divoš",
        "lokacija": "Divoš"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Zasavica I",
        "lokacija": "Zasavica 1"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Zasavica II",
        "lokacija": "Zasavica 2"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Jarak",
        "lokacija": "Jarak"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Kuzmin",
        "lokacija": "Kuzmin"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Laćarak",
        "lokacija": "Laćarak"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Ležimir",
        "lokacija": "Ležimir"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Manđelos",
        "lokacija": "Manđelos"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Martinci",
        "lokacija": "Martinci"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Mačvanska Mitrovica",
        "lokacija": "Mačvanska Mitrovica"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Mačvanska Mitrovica",
        "lokacija": "Mačvanska Mitrovica - Brodogradilište"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Mačvanska Mitrovica",
        "lokacija": "Mačvanska Mitrovica - Krivaja"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Mačvanska Mitrovica",
        "lokacija": "Mačvanska Mitrovica - Modran"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Mačvanska Mitrovica",
        "lokacija": "Mačvanska Mitrovica - Sava"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Noćaj",
        "lokacija": "Noćaj"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Ravnje",
        "lokacija": "Ravnje"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Radenković",
        "lokacija": "Radenković"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Salaš Noćajski",
        "lokacija": "Salaš Noćajski"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Sremska Rača",
        "lokacija": "Sremska Rača"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Stara Bingula",
        "lokacija": "Stara Bingula"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Čalma",
        "lokacija": "Čalma"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Šašinci",
        "lokacija": "Šašinci"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Šišatovac",
        "lokacija": "Šišatovac"
    },
    {
        "grad": "Sremska Mitrovica",
        "opstina": "Šuljam",
        "lokacija": "Šuljam"
    },
    {
        "grad": "Sremski Karlovci",
        "opstina": "Sremski Karlovci",
        "lokacija": "Sremski Karlovci"
    },
    {
        "grad": "Sremski Karlovci",
        "opstina": "Gradska lokacija",
        "lokacija": "Belilo"
    },
    {
        "grad": "Sremski Karlovci",
        "opstina": "Gradska lokacija",
        "lokacija": "Gornji Kraj"
    },
    {
        "grad": "Sremski Karlovci",
        "opstina": "Gradska lokacija",
        "lokacija": "Doka"
    },
    {
        "grad": "Sremski Karlovci",
        "opstina": "Gradska lokacija",
        "lokacija": "Dudara"
    },
    {
        "grad": "Sremski Karlovci",
        "opstina": "Gradska lokacija",
        "lokacija": "Pivara"
    },
    {
        "grad": "Sremski Karlovci",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Sremski Karlovci",
        "opstina": "Gradska lokacija",
        "lokacija": "Čerat"
    },
    {
        "grad": "Sremski Karlovci",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Sremski Karlovci",
        "opstina": "Fruška Gora",
        "lokacija": "Fruška Gora"
    },
    {
        "grad": "Stara Pazova",
        "opstina": "Stara Pazova",
        "lokacija": "Stara Pazova"
    },
    {
        "grad": "Stara Pazova",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Stara Pazova",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Stara Pazova",
        "opstina": "Belegiš",
        "lokacija": "Belegiš"
    },
    {
        "grad": "Stara Pazova",
        "opstina": "Vojka",
        "lokacija": "Vojka"
    },
    {
        "grad": "Stara Pazova",
        "opstina": "Golubinci",
        "lokacija": "Golubinci"
    },
    {
        "grad": "Stara Pazova",
        "opstina": "Krnješevci",
        "lokacija": "Krnješevci"
    },
    {
        "grad": "Stara Pazova",
        "opstina": "Nova Pazova",
        "lokacija": "Nova Pazova"
    },
    {
        "grad": "Stara Pazova",
        "opstina": "Novi Banovci",
        "lokacija": "Novi Banovci"
    },
    {
        "grad": "Stara Pazova",
        "opstina": "Stari Banovci",
        "lokacija": "Stari Banovci"
    },
    {
        "grad": "Stara Pazova",
        "opstina": "Surduk",
        "lokacija": "Surduk"
    },
    {
        "grad": "Subotica",
        "opstina": "Subotica",
        "lokacija": "Subotica"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Aleksandrovo"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Bajnat"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Bolnica"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Veliki Radanovac"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Vinogradi"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Gat"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Gornji grad"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Dudova Šuma"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Željezničko Naselje"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Zorka"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Jasibara"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Ker"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Kertvaroš"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Makova Sedmica"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Mali Bajmok"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Mali Radanovac"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Novi grad"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Peščara"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Prozivka"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Radanovac"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Radijalac"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Srpski Šor"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Teslino Naselje"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Tokio"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar 1"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar 2"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar 3"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Crveno Selo"
    },
    {
        "grad": "Subotica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Subotica",
        "opstina": "Bajmok",
        "lokacija": "Bajmok"
    },
    {
        "grad": "Subotica",
        "opstina": "Bački Vinogradi",
        "lokacija": "Bački Vinogradi"
    },
    {
        "grad": "Subotica",
        "opstina": "Bačko Dušanovo",
        "lokacija": "Bačko Dušanovo"
    },
    {
        "grad": "Subotica",
        "opstina": "Bikovo",
        "lokacija": "Bikovo"
    },
    {
        "grad": "Subotica",
        "opstina": "Višnjevac",
        "lokacija": "Višnjevac"
    },
    {
        "grad": "Subotica",
        "opstina": "Gornji Tavankut",
        "lokacija": "Gornji Tavankut"
    },
    {
        "grad": "Subotica",
        "opstina": "Donji Tavankut",
        "lokacija": "Donji Tavankut"
    },
    {
        "grad": "Subotica",
        "opstina": "Đurđin",
        "lokacija": "Đurđin"
    },
    {
        "grad": "Subotica",
        "opstina": "Kelebija",
        "lokacija": "Kelebija"
    },
    {
        "grad": "Subotica",
        "opstina": "Ljutovo",
        "lokacija": "Ljutovo"
    },
    {
        "grad": "Subotica",
        "opstina": "Mala Bosna",
        "lokacija": "Mala Bosna"
    },
    {
        "grad": "Subotica",
        "opstina": "Mišićevo",
        "lokacija": "Mišićevo"
    },
    {
        "grad": "Subotica",
        "opstina": "Novi Žednik",
        "lokacija": "Novi Žednik"
    },
    {
        "grad": "Subotica",
        "opstina": "Palić",
        "lokacija": "Palić"
    },
    {
        "grad": "Subotica",
        "opstina": "Palićko Jezero",
        "lokacija": "Palićko Jezero"
    },
    {
        "grad": "Subotica",
        "opstina": "Stari žednik",
        "lokacija": "Stari žednik"
    },
    {
        "grad": "Subotica",
        "opstina": "Hajdukovo",
        "lokacija": "Hajdukovo"
    },
    {
        "grad": "Subotica",
        "opstina": "Čantavir",
        "lokacija": "Čantavir"
    },
    {
        "grad": "Subotica",
        "opstina": "Šupljak",
        "lokacija": "Šupljak"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Suva Reka",
        "lokacija": "Suva Reka"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Banja",
        "lokacija": "Banja"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Belanica",
        "lokacija": "Belanica"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Blace",
        "lokacija": "Blace"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Budakovo",
        "lokacija": "Budakovo"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Bukoš",
        "lokacija": "Bukoš"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Vranić",
        "lokacija": "Vranić"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Vrševce",
        "lokacija": "Vrševce"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Geljance",
        "lokacija": "Geljance"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Gornja Krušica",
        "lokacija": "Gornja Krušica"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Grejkovce",
        "lokacija": "Grejkovce"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Grejčevce",
        "lokacija": "Grejčevce"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Guncat",
        "lokacija": "Guncat"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Dvorane",
        "lokacija": "Dvorane"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Delovce",
        "lokacija": "Delovce"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Dobrodeljane",
        "lokacija": "Dobrodeljane"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Donja Krušica",
        "lokacija": "Donja Krušica"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Dubrava",
        "lokacija": "Dubrava"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Dulje",
        "lokacija": "Dulje"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Đinovce",
        "lokacija": "Đinovce"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Javor",
        "lokacija": "Javor"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Kostrce",
        "lokacija": "Kostrce"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Kravoserija",
        "lokacija": "Kravoserija"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Ladrovac",
        "lokacija": "Ladrovac"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Ladrović",
        "lokacija": "Ladrović"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Lešane",
        "lokacija": "Lešane"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Lužnica",
        "lokacija": "Lužnica"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Mačitevo",
        "lokacija": "Mačitevo"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Movljane",
        "lokacija": "Movljane"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Mušutište",
        "lokacija": "Mušutište"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Neprebište",
        "lokacija": "Neprebište"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Nišor",
        "lokacija": "Nišor"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Papaz",
        "lokacija": "Papaz"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Pećane",
        "lokacija": "Pećane"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Popovljane",
        "lokacija": "Popovljane"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Raštane",
        "lokacija": "Raštane"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Rečane",
        "lokacija": "Rečane"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Savrovo",
        "lokacija": "Savrovo"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Samodraža",
        "lokacija": "Samodraža"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Selogražde",
        "lokacija": "Selogražde"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Semetište",
        "lokacija": "Semetište"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Senik",
        "lokacija": "Senik"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Slapužane",
        "lokacija": "Slapužane"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Sopina",
        "lokacija": "Sopina"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Stara Vučina",
        "lokacija": "Stara Vučina"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Studenčane",
        "lokacija": "Studenčane"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Topličane",
        "lokacija": "Topličane"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Trnje",
        "lokacija": "Trnje"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Tumičina",
        "lokacija": "Tumičina"
    },
    {
        "grad": "Suva Reka",
        "opstina": "Čajdrak",
        "lokacija": "Čajdrak"
    },
    {
        "grad": "Surdulica",
        "opstina": "Surdulica",
        "lokacija": "Surdulica"
    },
    {
        "grad": "Surdulica",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Surdulica",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Surdulica",
        "opstina": "Alakince",
        "lokacija": "Alakince"
    },
    {
        "grad": "Surdulica",
        "opstina": "Bacijevce",
        "lokacija": "Bacijevce"
    },
    {
        "grad": "Surdulica",
        "opstina": "Belo Polje",
        "lokacija": "Belo Polje"
    },
    {
        "grad": "Surdulica",
        "opstina": "Binovce",
        "lokacija": "Binovce"
    },
    {
        "grad": "Surdulica",
        "opstina": "Bitvrđa",
        "lokacija": "Bitvrđa"
    },
    {
        "grad": "Surdulica",
        "opstina": "Božica",
        "lokacija": "Božica"
    },
    {
        "grad": "Surdulica",
        "opstina": "Vlasina Okruglica",
        "lokacija": "Vlasina Okruglica"
    },
    {
        "grad": "Surdulica",
        "opstina": "Vlasina Rid",
        "lokacija": "Vlasina Rid"
    },
    {
        "grad": "Surdulica",
        "opstina": "Vlasina Stojkovićeva",
        "lokacija": "Vlasina Stojkovićeva"
    },
    {
        "grad": "Surdulica",
        "opstina": "Vlasinsko Jezero",
        "lokacija": "Vlasinsko Jezero"
    },
    {
        "grad": "Surdulica",
        "opstina": "Vučadelce",
        "lokacija": "Vučadelce"
    },
    {
        "grad": "Surdulica",
        "opstina": "Gornja Koznica",
        "lokacija": "Gornja Koznica"
    },
    {
        "grad": "Surdulica",
        "opstina": "Gornje Romanovce",
        "lokacija": "Gornje Romanovce"
    },
    {
        "grad": "Surdulica",
        "opstina": "Groznatovci",
        "lokacija": "Groznatovci"
    },
    {
        "grad": "Surdulica",
        "opstina": "Danjino Selo",
        "lokacija": "Danjino Selo"
    },
    {
        "grad": "Surdulica",
        "opstina": "Dikava",
        "lokacija": "Dikava"
    },
    {
        "grad": "Surdulica",
        "opstina": "Donje Romanovce",
        "lokacija": "Donje Romanovce"
    },
    {
        "grad": "Surdulica",
        "opstina": "Drajinci",
        "lokacija": "Drajinci"
    },
    {
        "grad": "Surdulica",
        "opstina": "Dugi Del",
        "lokacija": "Dugi Del"
    },
    {
        "grad": "Surdulica",
        "opstina": "Dugojnica",
        "lokacija": "Dugojnica"
    },
    {
        "grad": "Surdulica",
        "opstina": "Zagužanje",
        "lokacija": "Zagužanje"
    },
    {
        "grad": "Surdulica",
        "opstina": "Jelašnica",
        "lokacija": "Jelašnica"
    },
    {
        "grad": "Surdulica",
        "opstina": "Kalabovce",
        "lokacija": "Kalabovce"
    },
    {
        "grad": "Surdulica",
        "opstina": "Kijevac",
        "lokacija": "Kijevac"
    },
    {
        "grad": "Surdulica",
        "opstina": "Klisura",
        "lokacija": "Klisura"
    },
    {
        "grad": "Surdulica",
        "opstina": "Kolunica",
        "lokacija": "Kolunica"
    },
    {
        "grad": "Surdulica",
        "opstina": "Konjarnik",
        "lokacija": "Konjarnik"
    },
    {
        "grad": "Surdulica",
        "opstina": "Kopčini",
        "lokacija": "Kopčini"
    },
    {
        "grad": "Surdulica",
        "opstina": "Kostroševci",
        "lokacija": "Kostroševci"
    },
    {
        "grad": "Surdulica",
        "opstina": "Krstinci",
        "lokacija": "Krstinci"
    },
    {
        "grad": "Surdulica",
        "opstina": "Leskova Bara",
        "lokacija": "Leskova Bara"
    },
    {
        "grad": "Surdulica",
        "opstina": "Lokva",
        "lokacija": "Lokva"
    },
    {
        "grad": "Surdulica",
        "opstina": "Masurica",
        "lokacija": "Masurica"
    },
    {
        "grad": "Surdulica",
        "opstina": "Mačkatica",
        "lokacija": "Mačkatica"
    },
    {
        "grad": "Surdulica",
        "opstina": "Mašinci",
        "lokacija": "Mašinci"
    },
    {
        "grad": "Surdulica",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Surdulica",
        "opstina": "Palja",
        "lokacija": "Palja"
    },
    {
        "grad": "Surdulica",
        "opstina": "Rđavica",
        "lokacija": "Rđavica"
    },
    {
        "grad": "Surdulica",
        "opstina": "Stajkovce",
        "lokacija": "Stajkovce"
    },
    {
        "grad": "Surdulica",
        "opstina": "Strezimirovci",
        "lokacija": "Strezimirovci"
    },
    {
        "grad": "Surdulica",
        "opstina": "Suvojnica",
        "lokacija": "Suvojnica"
    },
    {
        "grad": "Surdulica",
        "opstina": "Suhi Dol",
        "lokacija": "Suhi Dol"
    },
    {
        "grad": "Surdulica",
        "opstina": "Topli Do",
        "lokacija": "Topli Do"
    },
    {
        "grad": "Surdulica",
        "opstina": "Topli Dol",
        "lokacija": "Topli Dol"
    },
    {
        "grad": "Surdulica",
        "opstina": "Troskač",
        "lokacija": "Troskač"
    },
    {
        "grad": "Surdulica",
        "opstina": "Ćurkovica",
        "lokacija": "Ćurkovica"
    },
    {
        "grad": "Temerin",
        "opstina": "Temerin",
        "lokacija": "Temerin"
    },
    {
        "grad": "Temerin",
        "opstina": "Gradska lokacija",
        "lokacija": "Blok 18"
    },
    {
        "grad": "Temerin",
        "opstina": "Gradska lokacija",
        "lokacija": "Blok 22"
    },
    {
        "grad": "Temerin",
        "opstina": "Gradska lokacija",
        "lokacija": "Vašarište"
    },
    {
        "grad": "Temerin",
        "opstina": "Gradska lokacija",
        "lokacija": "Kolonija"
    },
    {
        "grad": "Temerin",
        "opstina": "Gradska lokacija",
        "lokacija": "Kudeljara"
    },
    {
        "grad": "Temerin",
        "opstina": "Gradska lokacija",
        "lokacija": "Staro Đurđevo"
    },
    {
        "grad": "Temerin",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Temerin",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Temerin",
        "opstina": "Bački Jarak",
        "lokacija": "Bački Jarak"
    },
    {
        "grad": "Temerin",
        "opstina": "Kamendin",
        "lokacija": "Kamendin"
    },
    {
        "grad": "Temerin",
        "opstina": "Sirig",
        "lokacija": "Sirig"
    },
    {
        "grad": "Titel",
        "opstina": "Titel",
        "lokacija": "Titel"
    },
    {
        "grad": "Titel",
        "opstina": "Gradska lokacija",
        "lokacija": "Tisa"
    },
    {
        "grad": "Titel",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Titel",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Titel",
        "opstina": "Vilovo",
        "lokacija": "Vilovo"
    },
    {
        "grad": "Titel",
        "opstina": "Gardinovci",
        "lokacija": "Gardinovci"
    },
    {
        "grad": "Titel",
        "opstina": "Lok",
        "lokacija": "Lok"
    },
    {
        "grad": "Titel",
        "opstina": "Mošorin",
        "lokacija": "Mošorin"
    },
    {
        "grad": "Titel",
        "opstina": "Šajkaš",
        "lokacija": "Šajkaš"
    },
    {
        "grad": "Topola",
        "opstina": "Topola",
        "lokacija": "Topola"
    },
    {
        "grad": "Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Industrijska Zona"
    },
    {
        "grad": "Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Jezero Topola"
    },
    {
        "grad": "Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Ljube Selo"
    },
    {
        "grad": "Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Meterize"
    },
    {
        "grad": "Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Mitrovčić"
    },
    {
        "grad": "Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Oplenac"
    },
    {
        "grad": "Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Ravnica"
    },
    {
        "grad": "Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Topola",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Topola",
        "opstina": "Belosavci",
        "lokacija": "Belosavci"
    },
    {
        "grad": "Topola",
        "opstina": "Blaznava",
        "lokacija": "Blaznava"
    },
    {
        "grad": "Topola",
        "opstina": "Božurnja",
        "lokacija": "Božurnja"
    },
    {
        "grad": "Topola",
        "opstina": "Vinča",
        "lokacija": "Vinča"
    },
    {
        "grad": "Topola",
        "opstina": "Vojkovci",
        "lokacija": "Vojkovci"
    },
    {
        "grad": "Topola",
        "opstina": "Gornja Trnava",
        "lokacija": "Gornja Trnava"
    },
    {
        "grad": "Topola",
        "opstina": "Gornja Šatornja",
        "lokacija": "Gornja Šatornja"
    },
    {
        "grad": "Topola",
        "opstina": "Gorovič",
        "lokacija": "Gorovič"
    },
    {
        "grad": "Topola",
        "opstina": "Guriševci",
        "lokacija": "Guriševci"
    },
    {
        "grad": "Topola",
        "opstina": "Donja Trešnjevica",
        "lokacija": "Donja Trešnjevica"
    },
    {
        "grad": "Topola",
        "opstina": "Donja Trnava",
        "lokacija": "Donja Trnava"
    },
    {
        "grad": "Topola",
        "opstina": "Donja Šatornja",
        "lokacija": "Donja Šatornja"
    },
    {
        "grad": "Topola",
        "opstina": "Žabare",
        "lokacija": "Žabare"
    },
    {
        "grad": "Topola",
        "opstina": "Zagorica",
        "lokacija": "Zagorica"
    },
    {
        "grad": "Topola",
        "opstina": "Jarmenovci",
        "lokacija": "Jarmenovci"
    },
    {
        "grad": "Topola",
        "opstina": "Jelenac",
        "lokacija": "Jelenac"
    },
    {
        "grad": "Topola",
        "opstina": "Junkovac",
        "lokacija": "Junkovac"
    },
    {
        "grad": "Topola",
        "opstina": "Kloka",
        "lokacija": "Kloka"
    },
    {
        "grad": "Topola",
        "opstina": "Krćevac",
        "lokacija": "Krćevac"
    },
    {
        "grad": "Topola",
        "opstina": "Lipovac",
        "lokacija": "Lipovac"
    },
    {
        "grad": "Topola",
        "opstina": "Manojlovci",
        "lokacija": "Manojlovci"
    },
    {
        "grad": "Topola",
        "opstina": "Maskar",
        "lokacija": "Maskar"
    },
    {
        "grad": "Topola",
        "opstina": "Natalinci",
        "lokacija": "Natalinci"
    },
    {
        "grad": "Topola",
        "opstina": "Ovsište",
        "lokacija": "Ovsište"
    },
    {
        "grad": "Topola",
        "opstina": "Pavlovac",
        "lokacija": "Pavlovac"
    },
    {
        "grad": "Topola",
        "opstina": "Plaskovac",
        "lokacija": "Plaskovac"
    },
    {
        "grad": "Topola",
        "opstina": "Rajkovac",
        "lokacija": "Rajkovac"
    },
    {
        "grad": "Topola",
        "opstina": "Svetlić",
        "lokacija": "Svetlić"
    },
    {
        "grad": "Topola",
        "opstina": "Topola (selo)",
        "lokacija": "Topola (selo)"
    },
    {
        "grad": "Topola",
        "opstina": "Šume",
        "lokacija": "Šume"
    },
    {
        "grad": "Trgovište",
        "opstina": "Trgovište",
        "lokacija": "Trgovište"
    },
    {
        "grad": "Trgovište",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Trgovište",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Trgovište",
        "opstina": "Babina Poljana",
        "lokacija": "Babina Poljana"
    },
    {
        "grad": "Trgovište",
        "opstina": "Barbace",
        "lokacija": "Barbace"
    },
    {
        "grad": "Trgovište",
        "opstina": "Vladovce",
        "lokacija": "Vladovce"
    },
    {
        "grad": "Trgovište",
        "opstina": "Goločevac",
        "lokacija": "Goločevac"
    },
    {
        "grad": "Trgovište",
        "opstina": "Gornovac",
        "lokacija": "Gornovac"
    },
    {
        "grad": "Trgovište",
        "opstina": "Gornja Trnica",
        "lokacija": "Gornja Trnica"
    },
    {
        "grad": "Trgovište",
        "opstina": "Gornji Kozji Dol",
        "lokacija": "Gornji Kozji Dol"
    },
    {
        "grad": "Trgovište",
        "opstina": "Gornji Stajevac",
        "lokacija": "Gornji Stajevac"
    },
    {
        "grad": "Trgovište",
        "opstina": "Dejance",
        "lokacija": "Dejance"
    },
    {
        "grad": "Trgovište",
        "opstina": "Donja Trnica",
        "lokacija": "Donja Trnica"
    },
    {
        "grad": "Trgovište",
        "opstina": "Donji Kozji Dol",
        "lokacija": "Donji Kozji Dol"
    },
    {
        "grad": "Trgovište",
        "opstina": "Donji Stajevac",
        "lokacija": "Donji Stajevac"
    },
    {
        "grad": "Trgovište",
        "opstina": "Dumbija",
        "lokacija": "Dumbija"
    },
    {
        "grad": "Trgovište",
        "opstina": "Đerekarce",
        "lokacija": "Đerekarce"
    },
    {
        "grad": "Trgovište",
        "opstina": "Zladovce",
        "lokacija": "Zladovce"
    },
    {
        "grad": "Trgovište",
        "opstina": "Kalovo",
        "lokacija": "Kalovo"
    },
    {
        "grad": "Trgovište",
        "opstina": "Lesnica",
        "lokacija": "Lesnica"
    },
    {
        "grad": "Trgovište",
        "opstina": "Mala Reka",
        "lokacija": "Mala Reka"
    },
    {
        "grad": "Trgovište",
        "opstina": "Margance",
        "lokacija": "Margance"
    },
    {
        "grad": "Trgovište",
        "opstina": "Mezdraja",
        "lokacija": "Mezdraja"
    },
    {
        "grad": "Trgovište",
        "opstina": "Novi Glog",
        "lokacija": "Novi Glog"
    },
    {
        "grad": "Trgovište",
        "opstina": "Novo Selo",
        "lokacija": "Novo Selo"
    },
    {
        "grad": "Trgovište",
        "opstina": "Petrovac",
        "lokacija": "Petrovac"
    },
    {
        "grad": "Trgovište",
        "opstina": "Prolesje",
        "lokacija": "Prolesje"
    },
    {
        "grad": "Trgovište",
        "opstina": "Radovnica",
        "lokacija": "Radovnica"
    },
    {
        "grad": "Trgovište",
        "opstina": "Rajčevce",
        "lokacija": "Rajčevce"
    },
    {
        "grad": "Trgovište",
        "opstina": "Surlica",
        "lokacija": "Surlica"
    },
    {
        "grad": "Trgovište",
        "opstina": "Crveni grad",
        "lokacija": "Crveni grad"
    },
    {
        "grad": "Trgovište",
        "opstina": "Crna Reka",
        "lokacija": "Crna Reka"
    },
    {
        "grad": "Trgovište",
        "opstina": "Crnovce",
        "lokacija": "Crnovce"
    },
    {
        "grad": "Trgovište",
        "opstina": "Šajince",
        "lokacija": "Šajince"
    },
    {
        "grad": "Trgovište",
        "opstina": "Šaprance",
        "lokacija": "Šaprance"
    },
    {
        "grad": "Trgovište",
        "opstina": "Široka Planina",
        "lokacija": "Široka Planina"
    },
    {
        "grad": "Trgovište",
        "opstina": "Šumata Trnica",
        "lokacija": "Šumata Trnica"
    },
    {
        "grad": "Trstenik",
        "opstina": "Trstenik",
        "lokacija": "Trstenik"
    },
    {
        "grad": "Trstenik",
        "opstina": "Gradska lokacija",
        "lokacija": "Zapadna Morava"
    },
    {
        "grad": "Trstenik",
        "opstina": "Gradska lokacija",
        "lokacija": "Pejovac"
    },
    {
        "grad": "Trstenik",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Trstenik",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Trstenik",
        "opstina": "Bogdanje",
        "lokacija": "Bogdanje"
    },
    {
        "grad": "Trstenik",
        "opstina": "Božurevac",
        "lokacija": "Božurevac"
    },
    {
        "grad": "Trstenik",
        "opstina": "Brezovica",
        "lokacija": "Brezovica"
    },
    {
        "grad": "Trstenik",
        "opstina": "Bresno Polje",
        "lokacija": "Bresno Polje"
    },
    {
        "grad": "Trstenik",
        "opstina": "Bučje",
        "lokacija": "Bučje"
    },
    {
        "grad": "Trstenik",
        "opstina": "Velika Drenova",
        "lokacija": "Velika Drenova"
    },
    {
        "grad": "Trstenik",
        "opstina": "Veluće",
        "lokacija": "Veluće"
    },
    {
        "grad": "Trstenik",
        "opstina": "Golubovac",
        "lokacija": "Golubovac"
    },
    {
        "grad": "Trstenik",
        "opstina": "Gornja Omašnica",
        "lokacija": "Gornja Omašnica"
    },
    {
        "grad": "Trstenik",
        "opstina": "Gornja Crnišava",
        "lokacija": "Gornja Crnišava"
    },
    {
        "grad": "Trstenik",
        "opstina": "Gornji Dubič",
        "lokacija": "Gornji Dubič"
    },
    {
        "grad": "Trstenik",
        "opstina": "Gornji Ribnik",
        "lokacija": "Gornji Ribnik"
    },
    {
        "grad": "Trstenik",
        "opstina": "Grabovac",
        "lokacija": "Grabovac"
    },
    {
        "grad": "Trstenik",
        "opstina": "Donja Omašnica",
        "lokacija": "Donja Omašnica"
    },
    {
        "grad": "Trstenik",
        "opstina": "Donja Crnišava",
        "lokacija": "Donja Crnišava"
    },
    {
        "grad": "Trstenik",
        "opstina": "Donji Dubič",
        "lokacija": "Donji Dubič"
    },
    {
        "grad": "Trstenik",
        "opstina": "Donji Ribnik",
        "lokacija": "Donji Ribnik"
    },
    {
        "grad": "Trstenik",
        "opstina": "Dublje",
        "lokacija": "Dublje"
    },
    {
        "grad": "Trstenik",
        "opstina": "Jasikovica",
        "lokacija": "Jasikovica"
    },
    {
        "grad": "Trstenik",
        "opstina": "Kamenjača",
        "lokacija": "Kamenjača"
    },
    {
        "grad": "Trstenik",
        "opstina": "Levići",
        "lokacija": "Levići"
    },
    {
        "grad": "Trstenik",
        "opstina": "Loboder",
        "lokacija": "Loboder"
    },
    {
        "grad": "Trstenik",
        "opstina": "Lozna",
        "lokacija": "Lozna"
    },
    {
        "grad": "Trstenik",
        "opstina": "Lopaš",
        "lokacija": "Lopaš"
    },
    {
        "grad": "Trstenik",
        "opstina": "Mala Drenova",
        "lokacija": "Mala Drenova"
    },
    {
        "grad": "Trstenik",
        "opstina": "Mala Sugubina",
        "lokacija": "Mala Sugubina"
    },
    {
        "grad": "Trstenik",
        "opstina": "Medveđa",
        "lokacija": "Medveđa"
    },
    {
        "grad": "Trstenik",
        "opstina": "Mijajlovac",
        "lokacija": "Mijajlovac"
    },
    {
        "grad": "Trstenik",
        "opstina": "Milutovac",
        "lokacija": "Milutovac"
    },
    {
        "grad": "Trstenik",
        "opstina": "Okruglica",
        "lokacija": "Okruglica"
    },
    {
        "grad": "Trstenik",
        "opstina": "Osaonica",
        "lokacija": "Osaonica"
    },
    {
        "grad": "Trstenik",
        "opstina": "Odžaci",
        "lokacija": "Odžaci"
    },
    {
        "grad": "Trstenik",
        "opstina": "Pajsak",
        "lokacija": "Pajsak"
    },
    {
        "grad": "Trstenik",
        "opstina": "Planinica",
        "lokacija": "Planinica"
    },
    {
        "grad": "Trstenik",
        "opstina": "Poljna",
        "lokacija": "Poljna"
    },
    {
        "grad": "Trstenik",
        "opstina": "Popina",
        "lokacija": "Popina"
    },
    {
        "grad": "Trstenik",
        "opstina": "Počekovina",
        "lokacija": "Počekovina"
    },
    {
        "grad": "Trstenik",
        "opstina": "Prnjavor",
        "lokacija": "Prnjavor"
    },
    {
        "grad": "Trstenik",
        "opstina": "Rajinac",
        "lokacija": "Rajinac"
    },
    {
        "grad": "Trstenik",
        "opstina": "Riđevštica",
        "lokacija": "Riđevštica"
    },
    {
        "grad": "Trstenik",
        "opstina": "Riljac",
        "lokacija": "Riljac"
    },
    {
        "grad": "Trstenik",
        "opstina": "Rujišnik",
        "lokacija": "Rujišnik"
    },
    {
        "grad": "Trstenik",
        "opstina": "Selište",
        "lokacija": "Selište"
    },
    {
        "grad": "Trstenik",
        "opstina": "Stari Trstenik",
        "lokacija": "Stari Trstenik"
    },
    {
        "grad": "Trstenik",
        "opstina": "Stopanja",
        "lokacija": "Stopanja"
    },
    {
        "grad": "Trstenik",
        "opstina": "Stragari",
        "lokacija": "Stragari"
    },
    {
        "grad": "Trstenik",
        "opstina": "Stublica",
        "lokacija": "Stublica"
    },
    {
        "grad": "Trstenik",
        "opstina": "Tobolac",
        "lokacija": "Tobolac"
    },
    {
        "grad": "Trstenik",
        "opstina": "Ugljarevo",
        "lokacija": "Ugljarevo"
    },
    {
        "grad": "Trstenik",
        "opstina": "Čairi",
        "lokacija": "Čairi"
    },
    {
        "grad": "Tutin",
        "opstina": "Tutin",
        "lokacija": "Tutin"
    },
    {
        "grad": "Tutin",
        "opstina": "Gradska lokacija",
        "lokacija": "gradac"
    },
    {
        "grad": "Tutin",
        "opstina": "Gradska lokacija",
        "lokacija": "Lukavica"
    },
    {
        "grad": "Tutin",
        "opstina": "Gradska lokacija",
        "lokacija": "Severni Kočarnik"
    },
    {
        "grad": "Tutin",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Tutin",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Tutin",
        "opstina": "Arapoviće",
        "lokacija": "Arapoviće"
    },
    {
        "grad": "Tutin",
        "opstina": "Baljen",
        "lokacija": "Baljen"
    },
    {
        "grad": "Tutin",
        "opstina": "Batrage",
        "lokacija": "Batrage"
    },
    {
        "grad": "Tutin",
        "opstina": "Baćica",
        "lokacija": "Baćica"
    },
    {
        "grad": "Tutin",
        "opstina": "Biohane",
        "lokacija": "Biohane"
    },
    {
        "grad": "Tutin",
        "opstina": "Blaca",
        "lokacija": "Blaca"
    },
    {
        "grad": "Tutin",
        "opstina": "Bovanj",
        "lokacija": "Bovanj"
    },
    {
        "grad": "Tutin",
        "opstina": "Boroštica",
        "lokacija": "Boroštica"
    },
    {
        "grad": "Tutin",
        "opstina": "Braćak",
        "lokacija": "Braćak"
    },
    {
        "grad": "Tutin",
        "opstina": "Bregovi",
        "lokacija": "Bregovi"
    },
    {
        "grad": "Tutin",
        "opstina": "Brniševo",
        "lokacija": "Brniševo"
    },
    {
        "grad": "Tutin",
        "opstina": "Bujkoviće",
        "lokacija": "Bujkoviće"
    },
    {
        "grad": "Tutin",
        "opstina": "Velje Polje",
        "lokacija": "Velje Polje"
    },
    {
        "grad": "Tutin",
        "opstina": "Veseniće",
        "lokacija": "Veseniće"
    },
    {
        "grad": "Tutin",
        "opstina": "Vrapče",
        "lokacija": "Vrapče"
    },
    {
        "grad": "Tutin",
        "opstina": "Vrba",
        "lokacija": "Vrba"
    },
    {
        "grad": "Tutin",
        "opstina": "Glogovik",
        "lokacija": "Glogovik"
    },
    {
        "grad": "Tutin",
        "opstina": "Gluhavica",
        "lokacija": "Gluhavica"
    },
    {
        "grad": "Tutin",
        "opstina": "Gnila",
        "lokacija": "Gnila"
    },
    {
        "grad": "Tutin",
        "opstina": "Godovo",
        "lokacija": "Godovo"
    },
    {
        "grad": "Tutin",
        "opstina": "Gornji Crniš",
        "lokacija": "Gornji Crniš"
    },
    {
        "grad": "Tutin",
        "opstina": "Gujiće",
        "lokacija": "Gujiće"
    },
    {
        "grad": "Tutin",
        "opstina": "Gurdijelje",
        "lokacija": "Gurdijelje"
    },
    {
        "grad": "Tutin",
        "opstina": "Guceviće",
        "lokacija": "Guceviće"
    },
    {
        "grad": "Tutin",
        "opstina": "Devreč",
        "lokacija": "Devreč"
    },
    {
        "grad": "Tutin",
        "opstina": "Delimeđe",
        "lokacija": "Delimeđe"
    },
    {
        "grad": "Tutin",
        "opstina": "Detane",
        "lokacija": "Detane"
    },
    {
        "grad": "Tutin",
        "opstina": "Dobri Dub",
        "lokacija": "Dobri Dub"
    },
    {
        "grad": "Tutin",
        "opstina": "Dobrinje",
        "lokacija": "Dobrinje"
    },
    {
        "grad": "Tutin",
        "opstina": "Dolovo",
        "lokacija": "Dolovo"
    },
    {
        "grad": "Tutin",
        "opstina": "Draga",
        "lokacija": "Draga"
    },
    {
        "grad": "Tutin",
        "opstina": "Dubovo",
        "lokacija": "Dubovo"
    },
    {
        "grad": "Tutin",
        "opstina": "Dulebe",
        "lokacija": "Dulebe"
    },
    {
        "grad": "Tutin",
        "opstina": "Đerekare",
        "lokacija": "Đerekare"
    },
    {
        "grad": "Tutin",
        "opstina": "Ervenice",
        "lokacija": "Ervenice"
    },
    {
        "grad": "Tutin",
        "opstina": "Žirče",
        "lokacija": "Žirče"
    },
    {
        "grad": "Tutin",
        "opstina": "Župa",
        "lokacija": "Župa"
    },
    {
        "grad": "Tutin",
        "opstina": "Žuče",
        "lokacija": "Žuče"
    },
    {
        "grad": "Tutin",
        "opstina": "Zapadni Mojstir",
        "lokacija": "Zapadni Mojstir"
    },
    {
        "grad": "Tutin",
        "opstina": "Izrok",
        "lokacija": "Izrok"
    },
    {
        "grad": "Tutin",
        "opstina": "Istočni Mojstir",
        "lokacija": "Istočni Mojstir"
    },
    {
        "grad": "Tutin",
        "opstina": "Jablanica",
        "lokacija": "Jablanica"
    },
    {
        "grad": "Tutin",
        "opstina": "Jarebice",
        "lokacija": "Jarebice"
    },
    {
        "grad": "Tutin",
        "opstina": "Jezgroviće",
        "lokacija": "Jezgroviće"
    },
    {
        "grad": "Tutin",
        "opstina": "Jeliće",
        "lokacija": "Jeliće"
    },
    {
        "grad": "Tutin",
        "opstina": "Južni Kočarnik",
        "lokacija": "Južni Kočarnik"
    },
    {
        "grad": "Tutin",
        "opstina": "Kovači",
        "lokacija": "Kovači"
    },
    {
        "grad": "Tutin",
        "opstina": "Koniče",
        "lokacija": "Koniče"
    },
    {
        "grad": "Tutin",
        "opstina": "Leskova",
        "lokacija": "Leskova"
    },
    {
        "grad": "Tutin",
        "opstina": "Lipica",
        "lokacija": "Lipica"
    },
    {
        "grad": "Tutin",
        "opstina": "Melaje",
        "lokacija": "Melaje"
    },
    {
        "grad": "Tutin",
        "opstina": "Mitrova",
        "lokacija": "Mitrova"
    },
    {
        "grad": "Tutin",
        "opstina": "Morani",
        "lokacija": "Morani"
    },
    {
        "grad": "Tutin",
        "opstina": "Naboje",
        "lokacija": "Naboje"
    },
    {
        "grad": "Tutin",
        "opstina": "Nadumce",
        "lokacija": "Nadumce"
    },
    {
        "grad": "Tutin",
        "opstina": "Namga",
        "lokacija": "Namga"
    },
    {
        "grad": "Tutin",
        "opstina": "Noćaje",
        "lokacija": "Noćaje"
    },
    {
        "grad": "Tutin",
        "opstina": "Oraše",
        "lokacija": "Oraše"
    },
    {
        "grad": "Tutin",
        "opstina": "Orlje",
        "lokacija": "Orlje"
    },
    {
        "grad": "Tutin",
        "opstina": "Ostrovica",
        "lokacija": "Ostrovica"
    },
    {
        "grad": "Tutin",
        "opstina": "Paljevo",
        "lokacija": "Paljevo"
    },
    {
        "grad": "Tutin",
        "opstina": "Piskopovce",
        "lokacija": "Piskopovce"
    },
    {
        "grad": "Tutin",
        "opstina": "Plenibabe",
        "lokacija": "Plenibabe"
    },
    {
        "grad": "Tutin",
        "opstina": "Pokrvenik",
        "lokacija": "Pokrvenik"
    },
    {
        "grad": "Tutin",
        "opstina": "Pope",
        "lokacija": "Pope"
    },
    {
        "grad": "Tutin",
        "opstina": "Popiće",
        "lokacija": "Popiće"
    },
    {
        "grad": "Tutin",
        "opstina": "Potreb",
        "lokacija": "Potreb"
    },
    {
        "grad": "Tutin",
        "opstina": "Pružanj",
        "lokacija": "Pružanj"
    },
    {
        "grad": "Tutin",
        "opstina": "Raduhovce",
        "lokacija": "Raduhovce"
    },
    {
        "grad": "Tutin",
        "opstina": "Raduša",
        "lokacija": "Raduša"
    },
    {
        "grad": "Tutin",
        "opstina": "Ramoševo",
        "lokacija": "Ramoševo"
    },
    {
        "grad": "Tutin",
        "opstina": "Reževiće",
        "lokacija": "Reževiće"
    },
    {
        "grad": "Tutin",
        "opstina": "Ribariće",
        "lokacija": "Ribariće"
    },
    {
        "grad": "Tutin",
        "opstina": "Rudnica",
        "lokacija": "Rudnica"
    },
    {
        "grad": "Tutin",
        "opstina": "Ruđa",
        "lokacija": "Ruđa"
    },
    {
        "grad": "Tutin",
        "opstina": "Saš",
        "lokacija": "Saš"
    },
    {
        "grad": "Tutin",
        "opstina": "Smoluća",
        "lokacija": "Smoluća"
    },
    {
        "grad": "Tutin",
        "opstina": "Starčeviće",
        "lokacija": "Starčeviće"
    },
    {
        "grad": "Tutin",
        "opstina": "Strumce",
        "lokacija": "Strumce"
    },
    {
        "grad": "Tutin",
        "opstina": "Suvi Do",
        "lokacija": "Suvi Do"
    },
    {
        "grad": "Tutin",
        "opstina": "Točilovo",
        "lokacija": "Točilovo"
    },
    {
        "grad": "Tutin",
        "opstina": "Ćulije",
        "lokacija": "Ćulije"
    },
    {
        "grad": "Tutin",
        "opstina": "Crkvine",
        "lokacija": "Crkvine"
    },
    {
        "grad": "Tutin",
        "opstina": "Čarovina",
        "lokacija": "Čarovina"
    },
    {
        "grad": "Tutin",
        "opstina": "Čmanjke",
        "lokacija": "Čmanjke"
    },
    {
        "grad": "Tutin",
        "opstina": "Čukote",
        "lokacija": "Čukote"
    },
    {
        "grad": "Tutin",
        "opstina": "Šaronje",
        "lokacija": "Šaronje"
    },
    {
        "grad": "Tutin",
        "opstina": "Šipče",
        "lokacija": "Šipče"
    },
    {
        "grad": "Tutin",
        "opstina": "Špiljani",
        "lokacija": "Špiljani"
    },
    {
        "grad": "Ćićevac",
        "opstina": "Ćićevac",
        "lokacija": "Ćićevac"
    },
    {
        "grad": "Ćićevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Ćićevac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Ćićevac",
        "opstina": "Braljina",
        "lokacija": "Braljina"
    },
    {
        "grad": "Ćićevac",
        "opstina": "grad Stalać",
        "lokacija": "grad Stalać"
    },
    {
        "grad": "Ćićevac",
        "opstina": "Lučina",
        "lokacija": "Lučina"
    },
    {
        "grad": "Ćićevac",
        "opstina": "Mojsinje",
        "lokacija": "Mojsinje"
    },
    {
        "grad": "Ćićevac",
        "opstina": "Mrzenica",
        "lokacija": "Mrzenica"
    },
    {
        "grad": "Ćićevac",
        "opstina": "Pločnik",
        "lokacija": "Pločnik"
    },
    {
        "grad": "Ćićevac",
        "opstina": "Pojate",
        "lokacija": "Pojate"
    },
    {
        "grad": "Ćićevac",
        "opstina": "Stalać",
        "lokacija": "Stalać"
    },
    {
        "grad": "Ćićevac",
        "opstina": "Trubarevo",
        "lokacija": "Trubarevo"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Ćuprija",
        "lokacija": "Ćuprija"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Ada"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Bolnica"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Visoka Medicinska Škola"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Dom Zdravlja"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Železnička Stanica"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Zmić"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Ludo Polje"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Moravski Park"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Minel"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Ordište"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Rasputnica"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Selište"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Skelino Polje"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Tonja"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Cernica"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Batinac",
        "lokacija": "Batinac"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Bigrenica",
        "lokacija": "Bigrenica"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Virine",
        "lokacija": "Virine"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Vlaška",
        "lokacija": "Vlaška"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Dvorica",
        "lokacija": "Dvorica"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Dobričevo",
        "lokacija": "Dobričevo"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Ivankovac",
        "lokacija": "Ivankovac"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Isakovo",
        "lokacija": "Isakovo"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Jovac",
        "lokacija": "Jovac"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Kovanica",
        "lokacija": "Kovanica"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Krušar",
        "lokacija": "Krušar"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Mijatovac",
        "lokacija": "Mijatovac"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Ostrikovac",
        "lokacija": "Ostrikovac"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Paljane",
        "lokacija": "Paljane"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Senje",
        "lokacija": "Senje"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Staro Selo",
        "lokacija": "Staro Selo"
    },
    {
        "grad": "Ćuprija",
        "opstina": "Supska",
        "lokacija": "Supska"
    },
    {
        "grad": "Ub",
        "opstina": "Ub",
        "lokacija": "Ub"
    },
    {
        "grad": "Ub",
        "opstina": "Gradska lokacija",
        "lokacija": "Vučjak"
    },
    {
        "grad": "Ub",
        "opstina": "Gradska lokacija",
        "lokacija": "Talovi"
    },
    {
        "grad": "Ub",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Ub",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centrar"
    },
    {
        "grad": "Ub",
        "opstina": "Banjani",
        "lokacija": "Banjani"
    },
    {
        "grad": "Ub",
        "opstina": "Bogdanovica",
        "lokacija": "Bogdanovica"
    },
    {
        "grad": "Ub",
        "opstina": "Brgule",
        "lokacija": "Brgule"
    },
    {
        "grad": "Ub",
        "opstina": "Brezovica",
        "lokacija": "Brezovica"
    },
    {
        "grad": "Ub",
        "opstina": "Vrelo",
        "lokacija": "Vrelo"
    },
    {
        "grad": "Ub",
        "opstina": "Vrhovine",
        "lokacija": "Vrhovine"
    },
    {
        "grad": "Ub",
        "opstina": "Vukona",
        "lokacija": "Vukona"
    },
    {
        "grad": "Ub",
        "opstina": "Gvozdenović",
        "lokacija": "Gvozdenović"
    },
    {
        "grad": "Ub",
        "opstina": "Gunjevac",
        "lokacija": "Gunjevac"
    },
    {
        "grad": "Ub",
        "opstina": "Dokmir",
        "lokacija": "Dokmir"
    },
    {
        "grad": "Ub",
        "opstina": "Zvizdar",
        "lokacija": "Zvizdar"
    },
    {
        "grad": "Ub",
        "opstina": "Joševa",
        "lokacija": "Joševa"
    },
    {
        "grad": "Ub",
        "opstina": "Kalenić",
        "lokacija": "Kalenić"
    },
    {
        "grad": "Ub",
        "opstina": "Kalinovac",
        "lokacija": "Kalinovac"
    },
    {
        "grad": "Ub",
        "opstina": "Kožuar",
        "lokacija": "Kožuar"
    },
    {
        "grad": "Ub",
        "opstina": "Kršna Glava",
        "lokacija": "Kršna Glava"
    },
    {
        "grad": "Ub",
        "opstina": "Liso Polje",
        "lokacija": "Liso Polje"
    },
    {
        "grad": "Ub",
        "opstina": "Lončanik",
        "lokacija": "Lončanik"
    },
    {
        "grad": "Ub",
        "opstina": "Milorci",
        "lokacija": "Milorci"
    },
    {
        "grad": "Ub",
        "opstina": "Murgaš",
        "lokacija": "Murgaš"
    },
    {
        "grad": "Ub",
        "opstina": "Novaci",
        "lokacija": "Novaci"
    },
    {
        "grad": "Ub",
        "opstina": "Paljuvi",
        "lokacija": "Paljuvi"
    },
    {
        "grad": "Ub",
        "opstina": "Pambukovica",
        "lokacija": "Pambukovica"
    },
    {
        "grad": "Ub",
        "opstina": "Radljevo",
        "lokacija": "Radljevo"
    },
    {
        "grad": "Ub",
        "opstina": "Raduša",
        "lokacija": "Raduša"
    },
    {
        "grad": "Ub",
        "opstina": "Ruklada",
        "lokacija": "Ruklada"
    },
    {
        "grad": "Ub",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Ub",
        "opstina": "Sovljak",
        "lokacija": "Sovljak"
    },
    {
        "grad": "Ub",
        "opstina": "Stublenica",
        "lokacija": "Stublenica"
    },
    {
        "grad": "Ub",
        "opstina": "Takovo",
        "lokacija": "Takovo"
    },
    {
        "grad": "Ub",
        "opstina": "Tvrdojevac",
        "lokacija": "Tvrdojevac"
    },
    {
        "grad": "Ub",
        "opstina": "Trlić",
        "lokacija": "Trlić"
    },
    {
        "grad": "Ub",
        "opstina": "Trnjaci",
        "lokacija": "Trnjaci"
    },
    {
        "grad": "Ub",
        "opstina": "Tulari",
        "lokacija": "Tulari"
    },
    {
        "grad": "Ub",
        "opstina": "Crvena Jabuka",
        "lokacija": "Crvena Jabuka"
    },
    {
        "grad": "Ub",
        "opstina": "Čučuge",
        "lokacija": "Čučuge"
    },
    {
        "grad": "Ub",
        "opstina": "Šarbane",
        "lokacija": "Šarbane"
    },
    {
        "grad": "Užice",
        "opstina": "Užice",
        "lokacija": "Užice"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Begluk"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Bela Zemlja"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Belo Groblje"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Gluvaći"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Dovarje"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Zabučje"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Koštica"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Krčagovo"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Lipa"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Malo Zabučje"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Pora"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Rakijska Pijaca"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Rosulje"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Senjak"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Stari grad"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Terazije"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Turica"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Carina"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Užice",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Užice",
        "opstina": "Bioska",
        "lokacija": "Bioska"
    },
    {
        "grad": "Užice",
        "opstina": "Bjelotići",
        "lokacija": "Bjelotići"
    },
    {
        "grad": "Užice",
        "opstina": "Buar",
        "lokacija": "Buar"
    },
    {
        "grad": "Užice",
        "opstina": "Vitasi",
        "lokacija": "Vitasi"
    },
    {
        "grad": "Užice",
        "opstina": "Volujac",
        "lokacija": "Volujac"
    },
    {
        "grad": "Užice",
        "opstina": "Vrutci",
        "lokacija": "Vrutci"
    },
    {
        "grad": "Užice",
        "opstina": "Gorjani",
        "lokacija": "Gorjani"
    },
    {
        "grad": "Užice",
        "opstina": "Gostinica",
        "lokacija": "Gostinica"
    },
    {
        "grad": "Užice",
        "opstina": "Gubin Do",
        "lokacija": "Gubin Do"
    },
    {
        "grad": "Užice",
        "opstina": "Dobrodo",
        "lokacija": "Dobrodo"
    },
    {
        "grad": "Užice",
        "opstina": "Drežnik",
        "lokacija": "Drežnik"
    },
    {
        "grad": "Užice",
        "opstina": "Drijetanj",
        "lokacija": "Drijetanj"
    },
    {
        "grad": "Užice",
        "opstina": "Duboko",
        "lokacija": "Duboko"
    },
    {
        "grad": "Užice",
        "opstina": "Zbojštica",
        "lokacija": "Zbojštica"
    },
    {
        "grad": "Užice",
        "opstina": "Zlakusa",
        "lokacija": "Zlakusa"
    },
    {
        "grad": "Užice",
        "opstina": "Kamenica",
        "lokacija": "Kamenica"
    },
    {
        "grad": "Užice",
        "opstina": "Karan",
        "lokacija": "Karan"
    },
    {
        "grad": "Užice",
        "opstina": "Kačer",
        "lokacija": "Kačer"
    },
    {
        "grad": "Užice",
        "opstina": "Keserovina",
        "lokacija": "Keserovina"
    },
    {
        "grad": "Užice",
        "opstina": "Kotroman",
        "lokacija": "Kotroman"
    },
    {
        "grad": "Užice",
        "opstina": "Krvavci",
        "lokacija": "Krvavci"
    },
    {
        "grad": "Užice",
        "opstina": "Kremna",
        "lokacija": "Kremna"
    },
    {
        "grad": "Užice",
        "opstina": "Kršanje",
        "lokacija": "Kršanje"
    },
    {
        "grad": "Užice",
        "opstina": "Lelići",
        "lokacija": "Lelići"
    },
    {
        "grad": "Užice",
        "opstina": "Ljubanje",
        "lokacija": "Ljubanje"
    },
    {
        "grad": "Užice",
        "opstina": "Mokra Gora",
        "lokacija": "Mokra Gora"
    },
    {
        "grad": "Užice",
        "opstina": "Nikojevići",
        "lokacija": "Nikojevići"
    },
    {
        "grad": "Užice",
        "opstina": "Panjak",
        "lokacija": "Panjak"
    },
    {
        "grad": "Užice",
        "opstina": "Pear",
        "lokacija": "Pear"
    },
    {
        "grad": "Užice",
        "opstina": "Ponikovica",
        "lokacija": "Ponikovica"
    },
    {
        "grad": "Užice",
        "opstina": "Potočanje",
        "lokacija": "Potočanje"
    },
    {
        "grad": "Užice",
        "opstina": "Potpeće",
        "lokacija": "Potpeće"
    },
    {
        "grad": "Užice",
        "opstina": "Ravni",
        "lokacija": "Ravni"
    },
    {
        "grad": "Užice",
        "opstina": "Raduša",
        "lokacija": "Raduša"
    },
    {
        "grad": "Užice",
        "opstina": "Ribaševina",
        "lokacija": "Ribaševina"
    },
    {
        "grad": "Užice",
        "opstina": "Sevojno",
        "lokacija": "Sevojno"
    },
    {
        "grad": "Užice",
        "opstina": "Skržuti",
        "lokacija": "Skržuti"
    },
    {
        "grad": "Užice",
        "opstina": "Stapari",
        "lokacija": "Stapari"
    },
    {
        "grad": "Užice",
        "opstina": "Strmac",
        "lokacija": "Strmac"
    },
    {
        "grad": "Užice",
        "opstina": "Trnava",
        "lokacija": "Trnava"
    },
    {
        "grad": "Uroševac",
        "opstina": "Uroševac",
        "lokacija": "Uroševac"
    },
    {
        "grad": "Uroševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Uroševac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Uroševac",
        "opstina": "Babljak",
        "lokacija": "Babljak"
    },
    {
        "grad": "Uroševac",
        "opstina": "Balić",
        "lokacija": "Balić"
    },
    {
        "grad": "Uroševac",
        "opstina": "Biba",
        "lokacija": "Biba"
    },
    {
        "grad": "Uroševac",
        "opstina": "Burnik",
        "lokacija": "Burnik"
    },
    {
        "grad": "Uroševac",
        "opstina": "Varoš Selo",
        "lokacija": "Varoš Selo"
    },
    {
        "grad": "Uroševac",
        "opstina": "Gatnje",
        "lokacija": "Gatnje"
    },
    {
        "grad": "Uroševac",
        "opstina": "Gornje Nerodimlje",
        "lokacija": "Gornje Nerodimlje"
    },
    {
        "grad": "Uroševac",
        "opstina": "Grebno",
        "lokacija": "Grebno"
    },
    {
        "grad": "Uroševac",
        "opstina": "Grlica",
        "lokacija": "Grlica"
    },
    {
        "grad": "Uroševac",
        "opstina": "Doganjevo",
        "lokacija": "Doganjevo"
    },
    {
        "grad": "Uroševac",
        "opstina": "Donje Nerodimlje",
        "lokacija": "Donje Nerodimlje"
    },
    {
        "grad": "Uroševac",
        "opstina": "Dramnjak",
        "lokacija": "Dramnjak"
    },
    {
        "grad": "Uroševac",
        "opstina": "Zaskok",
        "lokacija": "Zaskok"
    },
    {
        "grad": "Uroševac",
        "opstina": "Zlatare",
        "lokacija": "Zlatare"
    },
    {
        "grad": "Uroševac",
        "opstina": "Jezerce",
        "lokacija": "Jezerce"
    },
    {
        "grad": "Uroševac",
        "opstina": "Jerli Prelez",
        "lokacija": "Jerli Prelez"
    },
    {
        "grad": "Uroševac",
        "opstina": "Jerli Talinovac",
        "lokacija": "Jerli Talinovac"
    },
    {
        "grad": "Uroševac",
        "opstina": "Kamena Glava",
        "lokacija": "Kamena Glava"
    },
    {
        "grad": "Uroševac",
        "opstina": "Kosin",
        "lokacija": "Kosin"
    },
    {
        "grad": "Uroševac",
        "opstina": "Košare",
        "lokacija": "Košare"
    },
    {
        "grad": "Uroševac",
        "opstina": "Laškobare",
        "lokacija": "Laškobare"
    },
    {
        "grad": "Uroševac",
        "opstina": "Manastirce",
        "lokacija": "Manastirce"
    },
    {
        "grad": "Uroševac",
        "opstina": "Mirosavlje",
        "lokacija": "Mirosavlje"
    },
    {
        "grad": "Uroševac",
        "opstina": "Muhadžer Prelez",
        "lokacija": "Muhadžer Prelez"
    },
    {
        "grad": "Uroševac",
        "opstina": "Muhadžer Talinovac",
        "lokacija": "Muhadžer Talinovac"
    },
    {
        "grad": "Uroševac",
        "opstina": "Muhovce",
        "lokacija": "Muhovce"
    },
    {
        "grad": "Uroševac",
        "opstina": "Nekodim",
        "lokacija": "Nekodim"
    },
    {
        "grad": "Uroševac",
        "opstina": "Novi Miraš",
        "lokacija": "Novi Miraš"
    },
    {
        "grad": "Uroševac",
        "opstina": "Papaz",
        "lokacija": "Papaz"
    },
    {
        "grad": "Uroševac",
        "opstina": "Plešina",
        "lokacija": "Plešina"
    },
    {
        "grad": "Uroševac",
        "opstina": "Pojatište",
        "lokacija": "Pojatište"
    },
    {
        "grad": "Uroševac",
        "opstina": "Raka",
        "lokacija": "Raka"
    },
    {
        "grad": "Uroševac",
        "opstina": "Rahovica",
        "lokacija": "Rahovica"
    },
    {
        "grad": "Uroševac",
        "opstina": "Sazlija",
        "lokacija": "Sazlija"
    },
    {
        "grad": "Uroševac",
        "opstina": "Svrčina",
        "lokacija": "Svrčina"
    },
    {
        "grad": "Uroševac",
        "opstina": "Slivovo",
        "lokacija": "Slivovo"
    },
    {
        "grad": "Uroševac",
        "opstina": "Sojevo",
        "lokacija": "Sojevo"
    },
    {
        "grad": "Uroševac",
        "opstina": "Softović",
        "lokacija": "Softović"
    },
    {
        "grad": "Uroševac",
        "opstina": "Srpski Babuš",
        "lokacija": "Srpski Babuš"
    },
    {
        "grad": "Uroševac",
        "opstina": "Stari Miraš",
        "lokacija": "Stari Miraš"
    },
    {
        "grad": "Uroševac",
        "opstina": "Staro Selo",
        "lokacija": "Staro Selo"
    },
    {
        "grad": "Uroševac",
        "opstina": "Stojković",
        "lokacija": "Stojković"
    },
    {
        "grad": "Uroševac",
        "opstina": "Tankosić",
        "lokacija": "Tankosić"
    },
    {
        "grad": "Uroševac",
        "opstina": "Trn",
        "lokacija": "Trn"
    },
    {
        "grad": "Uroševac",
        "opstina": "Crnilo",
        "lokacija": "Crnilo"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Crna Trava",
        "lokacija": "Crna Trava"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Bajinci",
        "lokacija": "Bajinci"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Bankovci",
        "lokacija": "Bankovci"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Bistrica",
        "lokacija": "Bistrica"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Brod",
        "lokacija": "Brod"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Vus",
        "lokacija": "Vus"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Gornje Gare",
        "lokacija": "Gornje Gare"
    },
    {
        "grad": "Crna Trava",
        "opstina": "gradska",
        "lokacija": "gradska"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Darkovce",
        "lokacija": "Darkovce"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Dobro Polje",
        "lokacija": "Dobro Polje"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Zlatance",
        "lokacija": "Zlatance"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Jabukovik",
        "lokacija": "Jabukovik"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Jovanovce",
        "lokacija": "Jovanovce"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Kalna",
        "lokacija": "Kalna"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Krivi Del",
        "lokacija": "Krivi Del"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Krstićevo",
        "lokacija": "Krstićevo"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Mlačište",
        "lokacija": "Mlačište"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Obradovce",
        "lokacija": "Obradovce"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Ostrozub",
        "lokacija": "Ostrozub"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Pavličina",
        "lokacija": "Pavličina"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Preslap",
        "lokacija": "Preslap"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Rajčetine",
        "lokacija": "Rajčetine"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Ruplje",
        "lokacija": "Ruplje"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Sastav Reka",
        "lokacija": "Sastav Reka"
    },
    {
        "grad": "Crna Trava",
        "opstina": "Čuka",
        "lokacija": "Čuka"
    },
    {
        "grad": "Čajetina",
        "opstina": "Čajetina",
        "lokacija": "Čajetina"
    },
    {
        "grad": "Čajetina",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Čajetina",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Čajetina",
        "opstina": "Alin Potok",
        "lokacija": "Alin Potok"
    },
    {
        "grad": "Čajetina",
        "opstina": "Branešci",
        "lokacija": "Branešci"
    },
    {
        "grad": "Čajetina",
        "opstina": "Golovo",
        "lokacija": "Golovo"
    },
    {
        "grad": "Čajetina",
        "opstina": "Gostilje",
        "lokacija": "Gostilje"
    },
    {
        "grad": "Čajetina",
        "opstina": "Dobroselica",
        "lokacija": "Dobroselica"
    },
    {
        "grad": "Čajetina",
        "opstina": "Drenova",
        "lokacija": "Drenova"
    },
    {
        "grad": "Čajetina",
        "opstina": "Željine",
        "lokacija": "Željine"
    },
    {
        "grad": "Čajetina",
        "opstina": "Zlatibor",
        "lokacija": "Zlatibor"
    },
    {
        "grad": "Čajetina",
        "opstina": "Jablanica",
        "lokacija": "Jablanica"
    },
    {
        "grad": "Čajetina",
        "opstina": "Kriva Reka",
        "lokacija": "Kriva Reka"
    },
    {
        "grad": "Čajetina",
        "opstina": "Ljubiš",
        "lokacija": "Ljubiš"
    },
    {
        "grad": "Čajetina",
        "opstina": "Mačkat",
        "lokacija": "Mačkat"
    },
    {
        "grad": "Čajetina",
        "opstina": "Mušvete",
        "lokacija": "Mušvete"
    },
    {
        "grad": "Čajetina",
        "opstina": "Oko",
        "lokacija": "Oko"
    },
    {
        "grad": "Čajetina",
        "opstina": "Rakovica",
        "lokacija": "Rakovica"
    },
    {
        "grad": "Čajetina",
        "opstina": "Rožanstvo",
        "lokacija": "Rožanstvo"
    },
    {
        "grad": "Čajetina",
        "opstina": "Rudine",
        "lokacija": "Rudine"
    },
    {
        "grad": "Čajetina",
        "opstina": "Sainovina",
        "lokacija": "Sainovina"
    },
    {
        "grad": "Čajetina",
        "opstina": "Semegnjevo",
        "lokacija": "Semegnjevo"
    },
    {
        "grad": "Čajetina",
        "opstina": "Sirogojno",
        "lokacija": "Sirogojno"
    },
    {
        "grad": "Čajetina",
        "opstina": "Stublo",
        "lokacija": "Stublo"
    },
    {
        "grad": "Čajetina",
        "opstina": "Tripkova",
        "lokacija": "Tripkova"
    },
    {
        "grad": "Čajetina",
        "opstina": "Trnava",
        "lokacija": "Trnava"
    },
    {
        "grad": "Čajetina",
        "opstina": "Šljivovica",
        "lokacija": "Šljivovica"
    },
    {
        "grad": "Čačak",
        "opstina": "Čačak",
        "lokacija": "Čačak"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "3. Decembar"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Alvadžinica"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Avenija 1"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Avenija 2"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Avenija Lipa"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Beljina"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Velika Kolonija"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Vinara"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Gvožđar"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Jezdinsko Polje"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Kaluđerice"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Kasarna Ratko Mitrović"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Kej"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Ključ"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Košutnjak"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Kulinovačko Polje"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Lozničko Polje"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Lugovi"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Ljubić"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Ljubić Kej"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Medicinska Škola"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Palilula"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Park"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Pridvoračko Polje"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Sajmište"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Stari Autoprevoz"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Stari grad"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Tanasko Rajić"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Turski Potok"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Hotel Morava"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Čačak",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Čačak",
        "opstina": "Atenica",
        "lokacija": "Atenica"
    },
    {
        "grad": "Čačak",
        "opstina": "Atomska Banja",
        "lokacija": "Atomska Banja"
    },
    {
        "grad": "Čačak",
        "opstina": "Baluga (Ljubićska)",
        "lokacija": "Baluga (Ljubićska)"
    },
    {
        "grad": "Čačak",
        "opstina": "Baluga (Trnavska)",
        "lokacija": "Baluga (Trnavska)"
    },
    {
        "grad": "Čačak",
        "opstina": "Banjica",
        "lokacija": "Banjica"
    },
    {
        "grad": "Čačak",
        "opstina": "Beljina",
        "lokacija": "Beljina"
    },
    {
        "grad": "Čačak",
        "opstina": "Bečanj",
        "lokacija": "Bečanj"
    },
    {
        "grad": "Čačak",
        "opstina": "Brezovica",
        "lokacija": "Brezovica"
    },
    {
        "grad": "Čačak",
        "opstina": "Bresnica",
        "lokacija": "Bresnica"
    },
    {
        "grad": "Čačak",
        "opstina": "Vapa",
        "lokacija": "Vapa"
    },
    {
        "grad": "Čačak",
        "opstina": "Vidova",
        "lokacija": "Vidova"
    },
    {
        "grad": "Čačak",
        "opstina": "Viljuša",
        "lokacija": "Viljuša"
    },
    {
        "grad": "Čačak",
        "opstina": "Vranići",
        "lokacija": "Vranići"
    },
    {
        "grad": "Čačak",
        "opstina": "Vrnčani",
        "lokacija": "Vrnčani"
    },
    {
        "grad": "Čačak",
        "opstina": "Vujetinci",
        "lokacija": "Vujetinci"
    },
    {
        "grad": "Čačak",
        "opstina": "Goričani",
        "lokacija": "Goričani"
    },
    {
        "grad": "Čačak",
        "opstina": "Gornja Gorevnica",
        "lokacija": "Gornja Gorevnica"
    },
    {
        "grad": "Čačak",
        "opstina": "Gornja Trepča",
        "lokacija": "Gornja Trepča"
    },
    {
        "grad": "Čačak",
        "opstina": "Donja Gorevnica",
        "lokacija": "Donja Gorevnica"
    },
    {
        "grad": "Čačak",
        "opstina": "Donja Trepča",
        "lokacija": "Donja Trepča"
    },
    {
        "grad": "Čačak",
        "opstina": "Žaočani",
        "lokacija": "Žaočani"
    },
    {
        "grad": "Čačak",
        "opstina": "Zablaće",
        "lokacija": "Zablaće"
    },
    {
        "grad": "Čačak",
        "opstina": "Jančići",
        "lokacija": "Jančići"
    },
    {
        "grad": "Čačak",
        "opstina": "Ježevica",
        "lokacija": "Ježevica"
    },
    {
        "grad": "Čačak",
        "opstina": "Jezdina",
        "lokacija": "Jezdina"
    },
    {
        "grad": "Čačak",
        "opstina": "Katrga",
        "lokacija": "Katrga"
    },
    {
        "grad": "Čačak",
        "opstina": "Kačulice",
        "lokacija": "Kačulice"
    },
    {
        "grad": "Čačak",
        "opstina": "Konjevići",
        "lokacija": "Konjevići"
    },
    {
        "grad": "Čačak",
        "opstina": "Kukići",
        "lokacija": "Kukići"
    },
    {
        "grad": "Čačak",
        "opstina": "Kulinovci",
        "lokacija": "Kulinovci"
    },
    {
        "grad": "Čačak",
        "opstina": "Lipnica",
        "lokacija": "Lipnica"
    },
    {
        "grad": "Čačak",
        "opstina": "Loznica",
        "lokacija": "Loznica"
    },
    {
        "grad": "Čačak",
        "opstina": "Ljubić",
        "lokacija": "Ljubić"
    },
    {
        "grad": "Čačak",
        "opstina": "Međuvršje",
        "lokacija": "Međuvršje"
    },
    {
        "grad": "Čačak",
        "opstina": "Milićevci",
        "lokacija": "Milićevci"
    },
    {
        "grad": "Čačak",
        "opstina": "Miokovci",
        "lokacija": "Miokovci"
    },
    {
        "grad": "Čačak",
        "opstina": "Mojsinje",
        "lokacija": "Mojsinje"
    },
    {
        "grad": "Čačak",
        "opstina": "Mrčajevci",
        "lokacija": "Mrčajevci"
    },
    {
        "grad": "Čačak",
        "opstina": "Mršinci",
        "lokacija": "Mršinci"
    },
    {
        "grad": "Čačak",
        "opstina": "Ovčar Banja",
        "lokacija": "Ovčar Banja"
    },
    {
        "grad": "Čačak",
        "opstina": "Ostra",
        "lokacija": "Ostra"
    },
    {
        "grad": "Čačak",
        "opstina": "Pakovraće",
        "lokacija": "Pakovraće"
    },
    {
        "grad": "Čačak",
        "opstina": "Parmenac",
        "lokacija": "Parmenac"
    },
    {
        "grad": "Čačak",
        "opstina": "Petnica",
        "lokacija": "Petnica"
    },
    {
        "grad": "Čačak",
        "opstina": "Preljina",
        "lokacija": "Preljina"
    },
    {
        "grad": "Čačak",
        "opstina": "Premeća",
        "lokacija": "Premeća"
    },
    {
        "grad": "Čačak",
        "opstina": "Pridvorica",
        "lokacija": "Pridvorica"
    },
    {
        "grad": "Čačak",
        "opstina": "Prijevor",
        "lokacija": "Prijevor"
    },
    {
        "grad": "Čačak",
        "opstina": "Prislonica",
        "lokacija": "Prislonica"
    },
    {
        "grad": "Čačak",
        "opstina": "Rajac",
        "lokacija": "Rajac"
    },
    {
        "grad": "Čačak",
        "opstina": "Rakova",
        "lokacija": "Rakova"
    },
    {
        "grad": "Čačak",
        "opstina": "Riđage",
        "lokacija": "Riđage"
    },
    {
        "grad": "Čačak",
        "opstina": "Rošci",
        "lokacija": "Rošci"
    },
    {
        "grad": "Čačak",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Čačak",
        "opstina": "Sokolići",
        "lokacija": "Sokolići"
    },
    {
        "grad": "Čačak",
        "opstina": "Stančići",
        "lokacija": "Stančići"
    },
    {
        "grad": "Čačak",
        "opstina": "Trbušani",
        "lokacija": "Trbušani"
    },
    {
        "grad": "Čačak",
        "opstina": "Trnava",
        "lokacija": "Trnava"
    },
    {
        "grad": "Čoka",
        "opstina": "Čoka",
        "lokacija": "Čoka"
    },
    {
        "grad": "Čoka",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Čoka",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Čoka",
        "opstina": "Banatski Monoštor",
        "lokacija": "Banatski Monoštor"
    },
    {
        "grad": "Čoka",
        "opstina": "Vrbica",
        "lokacija": "Vrbica"
    },
    {
        "grad": "Čoka",
        "opstina": "Jazovo",
        "lokacija": "Jazovo"
    },
    {
        "grad": "Čoka",
        "opstina": "Ostojićevo",
        "lokacija": "Ostojićevo"
    },
    {
        "grad": "Čoka",
        "opstina": "Padej",
        "lokacija": "Padej"
    },
    {
        "grad": "Čoka",
        "opstina": "Sanad",
        "lokacija": "Sanad"
    },
    {
        "grad": "Čoka",
        "opstina": "Crna Bara",
        "lokacija": "Crna Bara"
    },
    {
        "grad": "Šabac",
        "opstina": "Šabac",
        "lokacija": "Šabac"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Bair"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Benska Bara"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Donji Šor"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Živinarnik"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Žika Popović"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kamenjak"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kamičak"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Kasarske Livade"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Letnjikovac"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Letnjikovačka Kosa"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Preki Šor"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Sava"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Trijangla"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Trkalište"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Šipurske Livade"
    },
    {
        "grad": "Šabac",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Šabac",
        "opstina": "Bela Reka",
        "lokacija": "Bela Reka"
    },
    {
        "grad": "Šabac",
        "opstina": "Bogosavac",
        "lokacija": "Bogosavac"
    },
    {
        "grad": "Šabac",
        "opstina": "Bojić",
        "lokacija": "Bojić"
    },
    {
        "grad": "Šabac",
        "opstina": "Bukor",
        "lokacija": "Bukor"
    },
    {
        "grad": "Šabac",
        "opstina": "Varna",
        "lokacija": "Varna"
    },
    {
        "grad": "Šabac",
        "opstina": "Vulujac",
        "lokacija": "Vulujac"
    },
    {
        "grad": "Šabac",
        "opstina": "Gornja Vranjska",
        "lokacija": "Gornja Vranjska"
    },
    {
        "grad": "Šabac",
        "opstina": "Grušić",
        "lokacija": "Grušić"
    },
    {
        "grad": "Šabac",
        "opstina": "Dvorište",
        "lokacija": "Dvorište"
    },
    {
        "grad": "Šabac",
        "opstina": "Desić",
        "lokacija": "Desić"
    },
    {
        "grad": "Šabac",
        "opstina": "Dobrić",
        "lokacija": "Dobrić"
    },
    {
        "grad": "Šabac",
        "opstina": "Drenovac",
        "lokacija": "Drenovac"
    },
    {
        "grad": "Šabac",
        "opstina": "Duvanište",
        "lokacija": "Duvanište"
    },
    {
        "grad": "Šabac",
        "opstina": "Žabar",
        "lokacija": "Žabar"
    },
    {
        "grad": "Šabac",
        "opstina": "Zablaće",
        "lokacija": "Zablaće"
    },
    {
        "grad": "Šabac",
        "opstina": "Zminjak",
        "lokacija": "Zminjak"
    },
    {
        "grad": "Šabac",
        "opstina": "Jevremovac",
        "lokacija": "Jevremovac"
    },
    {
        "grad": "Šabac",
        "opstina": "Jelenča",
        "lokacija": "Jelenča"
    },
    {
        "grad": "Šabac",
        "opstina": "Korman",
        "lokacija": "Korman"
    },
    {
        "grad": "Šabac",
        "opstina": "Krivaja",
        "lokacija": "Krivaja"
    },
    {
        "grad": "Šabac",
        "opstina": "Lipolist",
        "lokacija": "Lipolist"
    },
    {
        "grad": "Šabac",
        "opstina": "Majur",
        "lokacija": "Majur"
    },
    {
        "grad": "Šabac",
        "opstina": "Mala Vranjska",
        "lokacija": "Mala Vranjska"
    },
    {
        "grad": "Šabac",
        "opstina": "Maovi",
        "lokacija": "Maovi"
    },
    {
        "grad": "Šabac",
        "opstina": "Mačvanski Pričinović",
        "lokacija": "Mačvanski Pričinović"
    },
    {
        "grad": "Šabac",
        "opstina": "Metlić",
        "lokacija": "Metlić"
    },
    {
        "grad": "Šabac",
        "opstina": "Miloševac",
        "lokacija": "Miloševac"
    },
    {
        "grad": "Šabac",
        "opstina": "Miokus",
        "lokacija": "Miokus"
    },
    {
        "grad": "Šabac",
        "opstina": "Mišar",
        "lokacija": "Mišar"
    },
    {
        "grad": "Šabac",
        "opstina": "Mrđenovac",
        "lokacija": "Mrđenovac"
    },
    {
        "grad": "Šabac",
        "opstina": "Nakučani",
        "lokacija": "Nakučani"
    },
    {
        "grad": "Šabac",
        "opstina": "Orašac",
        "lokacija": "Orašac"
    },
    {
        "grad": "Šabac",
        "opstina": "Orid",
        "lokacija": "Orid"
    },
    {
        "grad": "Šabac",
        "opstina": "Petkovica",
        "lokacija": "Petkovica"
    },
    {
        "grad": "Šabac",
        "opstina": "Petlovača",
        "lokacija": "Petlovača"
    },
    {
        "grad": "Šabac",
        "opstina": "Pocerski Metković",
        "lokacija": "Pocerski Metković"
    },
    {
        "grad": "Šabac",
        "opstina": "Pocerski Pričinović",
        "lokacija": "Pocerski Pričinović"
    },
    {
        "grad": "Šabac",
        "opstina": "Predvorica",
        "lokacija": "Predvorica"
    },
    {
        "grad": "Šabac",
        "opstina": "Prnjavor",
        "lokacija": "Prnjavor"
    },
    {
        "grad": "Šabac",
        "opstina": "Radovašnica",
        "lokacija": "Radovašnica"
    },
    {
        "grad": "Šabac",
        "opstina": "Ribari",
        "lokacija": "Ribari"
    },
    {
        "grad": "Šabac",
        "opstina": "Rumska",
        "lokacija": "Rumska"
    },
    {
        "grad": "Šabac",
        "opstina": "Sinošević",
        "lokacija": "Sinošević"
    },
    {
        "grad": "Šabac",
        "opstina": "Skrađani",
        "lokacija": "Skrađani"
    },
    {
        "grad": "Šabac",
        "opstina": "Slatina",
        "lokacija": "Slatina"
    },
    {
        "grad": "Šabac",
        "opstina": "Slepčević",
        "lokacija": "Slepčević"
    },
    {
        "grad": "Šabac",
        "opstina": "Tabanović",
        "lokacija": "Tabanović"
    },
    {
        "grad": "Šabac",
        "opstina": "Cerovac",
        "lokacija": "Cerovac"
    },
    {
        "grad": "Šabac",
        "opstina": "Culjković",
        "lokacija": "Culjković"
    },
    {
        "grad": "Šabac",
        "opstina": "Ševarice",
        "lokacija": "Ševarice"
    },
    {
        "grad": "Šabac",
        "opstina": "Štitar",
        "lokacija": "Štitar"
    },
    {
        "grad": "Šid",
        "opstina": "Šid",
        "lokacija": "Šid"
    },
    {
        "grad": "Šid",
        "opstina": "Gradska lokacija",
        "lokacija": "Vračar"
    },
    {
        "grad": "Šid",
        "opstina": "Gradska lokacija",
        "lokacija": "G2 Naselje"
    },
    {
        "grad": "Šid",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Istok"
    },
    {
        "grad": "Šid",
        "opstina": "Gradska lokacija",
        "lokacija": "Naselje Jelice Stanivuković"
    },
    {
        "grad": "Šid",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Šid",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Šid",
        "opstina": "Adaševci",
        "lokacija": "Adaševci"
    },
    {
        "grad": "Šid",
        "opstina": "Batrovci",
        "lokacija": "Batrovci"
    },
    {
        "grad": "Šid",
        "opstina": "Bačinci",
        "lokacija": "Bačinci"
    },
    {
        "grad": "Šid",
        "opstina": "Berkasovo",
        "lokacija": "Berkasovo"
    },
    {
        "grad": "Šid",
        "opstina": "Bikić Do",
        "lokacija": "Bikić Do"
    },
    {
        "grad": "Šid",
        "opstina": "Bingula",
        "lokacija": "Bingula"
    },
    {
        "grad": "Šid",
        "opstina": "Vašica",
        "lokacija": "Vašica"
    },
    {
        "grad": "Šid",
        "opstina": "Višnjićevo",
        "lokacija": "Višnjićevo"
    },
    {
        "grad": "Šid",
        "opstina": "Gibarac",
        "lokacija": "Gibarac"
    },
    {
        "grad": "Šid",
        "opstina": "Erdevik",
        "lokacija": "Erdevik"
    },
    {
        "grad": "Šid",
        "opstina": "Ilinci",
        "lokacija": "Ilinci"
    },
    {
        "grad": "Šid",
        "opstina": "Jamena",
        "lokacija": "Jamena"
    },
    {
        "grad": "Šid",
        "opstina": "Kukujevci",
        "lokacija": "Kukujevci"
    },
    {
        "grad": "Šid",
        "opstina": "Ljuba",
        "lokacija": "Ljuba"
    },
    {
        "grad": "Šid",
        "opstina": "Molovin",
        "lokacija": "Molovin"
    },
    {
        "grad": "Šid",
        "opstina": "Morović",
        "lokacija": "Morović"
    },
    {
        "grad": "Šid",
        "opstina": "Privina Glava",
        "lokacija": "Privina Glava"
    },
    {
        "grad": "Šid",
        "opstina": "Sot",
        "lokacija": "Sot"
    },
    {
        "grad": "Štimlje",
        "opstina": "Štimlje",
        "lokacija": "Štimlje"
    },
    {
        "grad": "Štimlje",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Štimlje",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Štimlje",
        "opstina": "Belince",
        "lokacija": "Belince"
    },
    {
        "grad": "Štimlje",
        "opstina": "Vojinovce",
        "lokacija": "Vojinovce"
    },
    {
        "grad": "Štimlje",
        "opstina": "Gornje Godance",
        "lokacija": "Gornje Godance"
    },
    {
        "grad": "Štimlje",
        "opstina": "Davidovce",
        "lokacija": "Davidovce"
    },
    {
        "grad": "Štimlje",
        "opstina": "Devetak",
        "lokacija": "Devetak"
    },
    {
        "grad": "Štimlje",
        "opstina": "Donje Godance",
        "lokacija": "Donje Godance"
    },
    {
        "grad": "Štimlje",
        "opstina": "Duga",
        "lokacija": "Duga"
    },
    {
        "grad": "Štimlje",
        "opstina": "Đurkovce",
        "lokacija": "Đurkovce"
    },
    {
        "grad": "Štimlje",
        "opstina": "Zborce",
        "lokacija": "Zborce"
    },
    {
        "grad": "Štimlje",
        "opstina": "Karačica",
        "lokacija": "Karačica"
    },
    {
        "grad": "Štimlje",
        "opstina": "Lanište",
        "lokacija": "Lanište"
    },
    {
        "grad": "Štimlje",
        "opstina": "Malopoljce",
        "lokacija": "Malopoljce"
    },
    {
        "grad": "Štimlje",
        "opstina": "Mužičane",
        "lokacija": "Mužičane"
    },
    {
        "grad": "Štimlje",
        "opstina": "Petraštica",
        "lokacija": "Petraštica"
    },
    {
        "grad": "Štimlje",
        "opstina": "Petrović",
        "lokacija": "Petrović"
    },
    {
        "grad": "Štimlje",
        "opstina": "Petrovo",
        "lokacija": "Petrovo"
    },
    {
        "grad": "Štimlje",
        "opstina": "Rance",
        "lokacija": "Rance"
    },
    {
        "grad": "Štimlje",
        "opstina": "Račak",
        "lokacija": "Račak"
    },
    {
        "grad": "Štimlje",
        "opstina": "Rašince",
        "lokacija": "Rašince"
    },
    {
        "grad": "Štimlje",
        "opstina": "Topilo",
        "lokacija": "Topilo"
    },
    {
        "grad": "Štimlje",
        "opstina": "Crnoljevo",
        "lokacija": "Crnoljevo"
    },
    {
        "grad": "Štrpce",
        "opstina": "Štrpce",
        "lokacija": "Štrpce"
    },
    {
        "grad": "Štrpce",
        "opstina": "Gradska lokacija",
        "lokacija": "Centar"
    },
    {
        "grad": "Štrpce",
        "opstina": "Gradska lokacija",
        "lokacija": "Širi Centar"
    },
    {
        "grad": "Štrpce",
        "opstina": "Berevce",
        "lokacija": "Berevce"
    },
    {
        "grad": "Štrpce",
        "opstina": "Brezovica",
        "lokacija": "Brezovica"
    },
    {
        "grad": "Štrpce",
        "opstina": "Brod",
        "lokacija": "Brod"
    },
    {
        "grad": "Štrpce",
        "opstina": "Viča",
        "lokacija": "Viča"
    },
    {
        "grad": "Štrpce",
        "opstina": "Vrbeštica",
        "lokacija": "Vrbeštica"
    },
    {
        "grad": "Štrpce",
        "opstina": "Gornja Bitinja",
        "lokacija": "Gornja Bitinja"
    },
    {
        "grad": "Štrpce",
        "opstina": "Gotovuša",
        "lokacija": "Gotovuša"
    },
    {
        "grad": "Štrpce",
        "opstina": "Donja Bitinja",
        "lokacija": "Donja Bitinja"
    },
    {
        "grad": "Štrpce",
        "opstina": "Drajkovce",
        "lokacija": "Drajkovce"
    },
    {
        "grad": "Štrpce",
        "opstina": "Ižance",
        "lokacija": "Ižance"
    },
    {
        "grad": "Štrpce",
        "opstina": "Jažince",
        "lokacija": "Jažince"
    },
    {
        "grad": "Štrpce",
        "opstina": "Koštanjevo",
        "lokacija": "Koštanjevo"
    },
    {
        "grad": "Štrpce",
        "opstina": "Sevce",
        "lokacija": "Sevce"
    },
    {
        "grad": "Štrpce",
        "opstina": "Sušiće",
        "lokacija": "Sušiće"
    },
    {
        "grad": "Štrpce",
        "opstina": "Firaje",
        "lokacija": "Firaje"
    }
]

    for l in locations:
        try:
            Location.objects.create(city=l['grad'], municipality=l['opstina'], area=l['lokacija'])
        except:
            self.stdout.write(self.style.SUCCESS('Already exists'))


    self.stdout.write(self.style.SUCCESS('Successfully seeded data for locations'))
