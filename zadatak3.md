## Injection
- **Injection** napadi obuhvataju slanje podataka, u vidu zlonamernog koda, aplikaciji kako bi se promenilo značenje komande koja treba da se izvrši. Ovi napadi obično iskorišćavaju propuste u mehanizmima validacije unosa, omogućavajući napadačima da manipulišu tokom izvršavanja aplikacije. Primer je SQL injection gde napadač šalje "admin' OR 1=1--" umesto samo "admin" kako bi dobio pristup naloga admina.
- Najveći uticaj uspešnog injection napada može varirati. Međutim, u većini slučajeva, primarni cilj je dobijanje neovlašćenog pristupa osetljivim podacima ili resursima. Na primer, u SQL injection napadima, napadači mogu da izvuku poverljive informacije iz baza podataka, da modifikuju ili obrišu podatke, ili čak da izvrše administrativne komande na osnovnom sistemu.
- Za rešavanje **Login Admin** Juice Shop-a zadatka moguća je primena upita kao što je "admin' OR 1=1--" string na mestu email polja za unos i stringa bilo koje dužine(da bi zadovoljili validaciju neophodnog unosa) u polju za lozinku kako bi dobili pristup nalogu admina. Kako bi došli do baš ovog upita, dovoljno je u email polju uneti karakter ' i pokušati logovanje što će rezultovati u vraćanju greške od strane servera sa dodatnim informacijama koje možemo naći u delu Network Developer  Tools-a. Analizom tela greške, možemo primetiti da nam je server vratio ceo SQL upit koji se vrši prilikom logovanja korisnika i na osnovu njega možemo formirati upit kojim ćemo izvršiti SQL injection napad. Tako isprobavanjem različitih upita, kao što su "**admin' OR 1=1--**" ili "**' or email like '%admin%'--**" možemo dobiti pristup admin nalogu ili ukoliko želimo da pristupimo nalogu korisnika Jim, dovlojno je reč admin zameniti imenom korisnika i iskoristiti upit "**' or email like '%jim%'--**". Kada pristupimo nalogu admina, možemo saznati njegovu email adresu, a vrlo lako i njegovu lozinku, isporbavanjem nekih od najčešće korišćenih lozinki ili vršenjem napada račnikom sa listom mogućih lozinki.
- Ranjivosti koje omogućavaju da injection napadi uspeju često potiču od neadekvatnih validacija unosa. ⁤⁤Uobičajene ranjivosti uključuju:
    - **Nedostatak provere valjanosti unosa**: Neuspešna validacija korisničkih unosa omogućavaju napadačima da ubace zlonamerni kod ili komande u aplikaciju. ⁤
    - **Loše konfigurisane kontrole pristupa**: Nedovoljne kontrole pristupa mogu omogućiti napadačima da iskoriste ranjivosti sistema za dobijanje neovlašćenog pristupa. ⁤
    - **Nebezbedne prakse kodiranja**: Korišćenje dinamičkih SQL upita povezanih sa korisničkim unosima stvaraju mogućnosti za SQL injection napade. ⁤
- Da bi sprečili injection napade, potrebno je primeniti mere bezbednosti na više slojeva aplikaciije. To uključuje:
    - **Validacija korisničkih unosa** na fronend i backend delu aplikacije
    - **Korišćenje parametrizovanih upita** umesto dinamički formiranih SQL upita
    - **Redovne bezbednosne procene i analize koda**

## Broken access control
- Napadi kontrole pristupa su klasa bezbednosnih eksploatacija koje se dešavaju kada je napadač u mogućnosti da zaobiđe ili manipuliše kontrolama pristupa kako bi dobio neovlašćeni pristup resursima ili funkcionalnosti unutar aplikacije ili sistema. Ovi napadi obično uključuju iskorišćavanje nedostataka u dizajnu ili implementaciji mehanizama kontrole pristupa, omogućavajući napadačima da izvrše radnje za koje ne bi trebalo da imaju dozvolu. 
- Najveći uticaj uspešnog iskorišćavanja pokvarene kontrole pristupa može biti ozbiljan, jer često dovodi do neovlašćenog pristupa osetljivim podacima, sticanje privilegija ili neovlašćene modifikacije kritičnih resursa. Na primer, napadači mogu da steknu administrativne privilegije, pristupe poverljivim korisničkim informacijama, menjaju finansijske transakcije ili poremete normalan rad sistema. 
- Za zadatak pronalaska **Easter Egg**-a u oblasti Broken access control prvo je potrebno pronaći stranicu koja sadrži fajlove, među kojima je i **eastere.gg** fajl. Kada pokušamo da ga preuzmemo, dobijamo grešku da je moguće pruzimanje samo *.md* i *.pdf* fajlova i uz to nam ukazuje na to da se u implementaciji koristi *Express ^4.17.1* radni okvir koji ima otkrivene ranjivosti kao što je neadekvatno URL enkodiranje, što se može iskoristiti za rešavanje ovog zadatka. Zato, dodavanjem "%2500.md" na kraju URL-a možemo preuzeti ovaj fajl. U drugim zadacima kao što su pregled tuđe korpe ili forged feedback, dovoljno je analizirati zahteve koji se šalju prilikom pregleda sopstvene korpe ili slanja feedback-a i ponovnim slanjem tih zahteva u okviru Network sekcije Developer Tools-a, sa adekvatno izmenjenim vrednostima kao što su ID korpe ili UserId, može se dobiti pristup tuđe korpe ili poslati feedback u ime nekog drugog korisnika.
- Ranjivosti koje omogućavaju napde kontole pristupa su:
    - **Nedovoljne provere autorizacije**: Nepavilna primena kontrole pristupa može dozvoliti korisnicima da pristupe funkcionalnostima ili resursima bez dgovarajućeg ovlašćenja
    - **Nebezbedno upravljanje sesijom**: Ovo može dovesti do otmice sesije i time našadačima omogućiti lažno predstavljanje kako bi zaobišli kontrolu pristupa
    - **Direktne reference objekata**: Direktno izlaganje internih referenci objekata, kao što su putanje datoteka ili identifikatori baze podataka, bez odgovarajućih provera autorizacije može dozvoliti napadačima da manipulišu ovim referencama kako bi dobili neovlašćeni pristup osetljivim podacima ili funkcionalnosti.
    - **Predvidljivi identifikatori resursa**: Napadači mogu da iskoriste predvidljive obrasce u identifikatorima resursa (npr. sekvencijalni ID-ovi) da pristupe resursima za koje nisu ovlašćeni da pregledaju ili menjaju.
- Odgovarajuće kontramere kako bi se sprečila ova klasa napada:
    - **Kontrola pristupa zasnovana na ulogama (RBAC)**
    - **Bezbedno upravljanje sesijom**
    - **Testiranje kontrole pristupa**

## Broken Anti Automation
- Broken Anti Automation napadi podrazumevaju napade tako da eksploatišu ranjivosti ili nedostatke u merama protiv automatizacije koje implementiraju softverski sistemi kako bi se sprečile automatizovane aktivnosti ili aktivnosti koje uključuju korišćenje botova. Najčešća posledica je narušavanje integriteta sistema, što dovodi do neovlašćenog pristupa, krađe podataka ili oštećenja reputacije. Napadači mogu da iskoriste automatizovane skripte kako bi slali veliku količinu lažnih recenzija, manipulisali onlajn anketama ili izvršili DDoS napade.
- U Juice Shop aplikaciji, za rešavanje **CAPTCHA Bypass** zadatka, koji zahteva slanje 10 ili više feedback-a korisnika u 20 sekundi, je samo potrebno izvršiti slanje jednog istog zahteva preko Network dela Developer Tools-a. 
- Ranjivosti u softveru koje omogućavaju da ovi napadi uspeju su obično slabosti u primeni mera protiv automatizacije:
    - **Neadekvatni CAPTCHA mehanizmi**: Ako su CAPTCHA izazovi slabi ili ih je lako zaobići, napadači mogu automatizovati svoju interakciju sa sistemom
    - **Nedostatak ograničenja brzine**: Potrebno je ograničiti broj zahteva ili radnji koje se mogu izvršiti u određenom vremenskom periodu kako napadači ne bi mogli da preplave sistem sa velikim brojem automatizovanim zahtevima.
    - **Slabo upravljanje sesijama**
    - **Nedovoljna validacija unosa**
- Kako bi se ovo sprečilo, neophodno je uključiti neke od kontramera:
    - **Snažni CAPTCHA izazovi**: CAPTCHA izazovi koje je teško rešiti automatizovanim skriptama, a da pritom budu jednostavni za korisnika ili napredne CAPTCHA tehnike, koje uključuju rad sa slikama ili audio CAPTCHA
    - **Ograničavanje i prigušivanje brzine**: Implementacija mehanizama koji ograničavaju brzinu kako bi ograničili učestalost zahteva sa pojedinačnih IP adresa ili korisničkih naloga.

## Vulnerable Components
- **Vulnerable Components** napadi ciljaju na slabosti third-party ili open-source softverskih komponenti koje se koriste u aplikaciji ili sistemu. Ovi napadi iskorišćavaju poznate ranjivosti u bibliotekama, okvirima ili zavisnostima da bi dobili neovlašćeni pristup, izvršili proizvoljni kod ili ugrozili bezbednost celog sistema.
- Pošto se mnoge aplikacije oslanjaju na third-party komponente, iskorišćavanje ranjivosti u ovim komponentama može dovesti do neovlašćenog pristupa osetljivim informacijama, pristup poverljivim inforamcijama, zastoja sistema ili čak potpune kompromitacije sistema.
- Za rešavanje **Unsigned JWT** zadatka je potrebno iskopirati JWT sa nekog od prethodnih zahteva. Korišćenjem nekih od online alata za analizu JWT-a možemo dobiti strukturu tokena i zatim te informacije iskoristiti za kreiranje novog. Token mora da se sastoji iz tri dela tako da prvi deo možemo zadržati, dok je u drugom delu, koji sadrži email i druge informacije, potrbno postaviti odgovarajući email. Izmenjeni json objekat zatim treba enkodirati u Base64 string i zameniti dobijenu vrednost i dodati kao drugu vrednost tokena. Na osnovu teksta zadatka je očigleno da server može primiti token bez potpisa, poslednji deo tokena nam nije neophodan. Tako formiran token možemo dodati u neki od prethodnih zahteva i zahtev će proći i vratiti odgovarajući odgovor. Uzrok ovoga je korišćenje zastarelih biblioteka ili radnih okvira koji se ne ažuriraju blagovremeno.
- Neki od čestih uzroka za ove napade:
    - **Zastarele ili unpatched komponente**: Nedostatak redovnog ažuriranja i zakrpa third-party komponenti čini sisteme ranjivim na poznate bezbednosne propuste. Ovo se odnosi i na ugnježdene komponente. Napadači mogu da iskoriste ove ranjivosti da ugroze integritet i bezbednost celog sistema.
    - **Neredovno skeniranje i ranjivosti komponenti**
    - **Nebezbedne defaul konfiguracije**: Neke komponente third-party mogu da dolaze sa nesigurnim podrazumevanim konfiguracijama ili podešavanjima koje napadači mogu da iskoriste.
- Kako izbeći ove napade:
    - **Uklanjanje nekorišćenih i nepotrebnih zavisnosti, fajlova...**
    - **Konstantno praćenje izvora** kao što su Common Vulnerability i Exposures (CVE) and National Vulnerability Database (NVD)
    - **Korišćenje poverljivih izvora i repozitorijuma**


## XSS

- XSS napadi su klasa bezbednosnih eksploatacija do kojih dolazi kada napadači ubacuju zlonamerne skripte u veb stranice kojima pristupaju drugi korisnici. Ove skripte mogu da izvrše proizvoljan kod, potencijalno kompromitujući sesiju korisnika, ukradu osetljive informacije ili vrše neovlašćene radnje u ime korisnika.
- Najveći uticaj uspešnog XSS napada može se kretati od krađe osetljivih korisničkih informacija, kao što su kredencijali za prijavu ili lični podaci, do otmice korisničkih sesija ili čak širenja malvera drugim korisnicima. Pošto se XSS napadi dešavaju direktno unutar pretraživača korisnika, oni mogu zaobići tradicionalne bezbednosne mere kao što su firewall i sistemi za otkrivanje upada, što ih čini posebno opasnim.
- Jednostavniji zadaci unutar Juice Shop aplikacije podrazumevaju umetanje html koda u DOM stablo što se može izvršiti unosom u search bar. Sa druge strane **Client-side XSS Protection** zahteva slanje zahteva kao što je registracija tako da se na mesto email-a nalazi zadati html kod. To se može izvršiti na osnovu prethodnog slanja korišćenjem korisničkog interfejsa, a zatim izmena email vrednosti i ponovno slanje zahteva. Time se zaobilazi bezbednosni mehanizam na klijent strani.
- Ranjivosti koje omogućavaju napde su:
    - **Nepravilna validacija unosa** na klijent i server strani. Nepravilna provera korisničkog unosa pre nego što se prikaže na veb stranicama omogućava napadačima da ubace zlonamerne skripte u sadržaj stranice.
    - **Nebezbedne third-party biblioteke ili plugin-i**: Uključivanje third-party biblioteka ili dodataka sa poznatim XSS ranjivostima u kodu aplikacije može ga izložiti eksploataciji.
- Kontramere:
    - **Validacija ulaza i kodiranje izlaza**
    - **Sanitization biblioteke**: sanitization unosa korisnika i uklanjanje potencijalno opasnih znakova
    - **Bezbednosne funkcije pretraživača**: KOrišćenje bezbednosnih funkcija pretraživača, kao što su XSS filteri i ugrađene zaštite od reflektujućih XSS napada
    - **Filtriranje sadržaja i validacija**: Implementacija mehanizama filtriranja sadržaja i validacije kako bi identifikovali i blokirali potencijalno zlonamerni sadržaj, kao što je JavaScript kod, od unosa koje generiše korisnik.


## Unvalidated Redirects

- Unvalidated redirects napadi se dešavaju kada napadač manipuliše URL i šalje ga korisniku. Nakon otvaranja tog URL-a dolazi do redirekcije ka malicioznoj web stranici ili stranici na koju napadač želi da redirektuje korisnika. Kada korisnik klikne na link, aplikacija ga preusmjerava na sajt kontrolisan od strane napadača. Ovi napadi su opasni je mogu navesti korisnike da misle da posjećuju legitiman sajt, što može dovesti do kompromitovanja naloga, krađe podataka ili infekcije malvera. 
- Ranjivosti koje omogućavaju napade su:
    - **Nedostatak validacije unosa** Web aplikacija ne validira pravilno korisnićki unos, uključujući URL-ove korištene za preusmeravanje
    - **Nebezbedni parametri preusmerenja** Aplikacija koristi parametre u URL-i da odredi odredište za preusmerenje, ali ih ne validira adekvatno
    - **Preusmerenje na klijentskoj strani** logika preusmerenja implementirana na klijentskoj strani aplikacije
    - **Session Hijacking** ako napadač preuzme sesiju od korisnika, može preusmjeriti korisnika na zlonamjerne sajtove
- Kontramere:
    - **Validacija unosa** Odbaciti sve URL-ove koji ne zadovoljavaju pčekivani pattern
    - **Implementacija logike preusmerenja na serverskoj strani** ovim ćemo smanjiti rizik od manipulacija klijentskog koda
    - **Kreirati listu dozvoljenih preusmerenja** vršiti preusmerenja isključivo na bezbedne i unapred definisane rute


## Broken Authentication

- Broken Authentication ranjivosti se dešavaju kada napadač ikoristi slabosti u atuentifikaciji da stekne neautorizovan pristup korisničkom nalogu ili osjetljivim podacima. Napadači često pokušavaju brute force napade kako bi pronašli kredencijale korisnika ili koriste prethodno otkrivene kredencijale sa drugih sajtova oslanjajući se na naviku korisnika da koristi iste lozinke. Takođe, veoma često napadač manipuliše sesijom kako bi natjerao korisnika da koristi sesiju kontrolisanu od strane napadača. 
- Ranjivosti koje omogučavaju napade su:
    - **Upotreba slabih lozinki** aplikacija ne zahtijeva od korisnika da koristi složene lozinke odnosno da lozinka sadrži velika slova, mala slova, specijalne karaktere itd.
    - **Nesigurno skladištenje kredencijala** čuvanje kredencijala u slobodnom tekstu i ne korištenje heširanja i šifrovanja u radu sa kredencijalima
    - **Loše upravljanje sesijama** predvidljivi identifikatori sesije, ne korištenje ograničenog vremena validnost sesije itd.
    - **Broj pokušaja za prijavu nije ograničen**
    - **Loš mehanizam za oporavak lozinke** korištenje nesigurne komunikacije za slanje linka za oporavak lozinke
- Kontramere:
    - **Zahtijevati jake lozinke od korisnika**
    - **MFA** koristi multi-faktorsku autentifikaciju kao dodatni sloj zaštite
    - **Koristiti dobre prakse za upravljanje sesijom** koristiti mehanizam kolačića, definisati istek važenja sesije kao i generisati nepredvidive identifikatore sesija
    - **Heširanje lozinki**


## Insecure Deserialization

- Insecure deserialization je tip bezbednosne pretnje koja se dešava kada sistem deserijalizuje maliciozne podatke bez adekvatne validacije. Npadači mogu iskoristiti ovu pretnju izvršavanjem malicioznog koda, izvršavanjem DOS napada itd.

- Ranjivosti koje omogućavaju napade su:
    - **Prihvatanje podatak od nesigurnog izvora** aplikacija prihavata serijalizovane podatke od korisničkog unosa, eksternih fajlova i sl.
    - **Korišćenje neprovjerenih biblioteka**
    - **Pretpostavka da su serializovani objekti uvijek sigurni** samim tim aplikacija preskače validaciju ovih podataka

- Kontramere:
    - **Validacija unosa** 
    - **Koristiti provjerene biblioteke** kako bi se izbjegle česte ranjivosti
    - **Provjera integriteta** kao što je korištenje digitalnih potpisa ili checksum
    - **Ograničenje privilegija** limitirati privilegije procesa deserializacije kako bi se izbjegle nepotrebe operacije sa deserijalizovanim podacima


## Security Misconfiguration

- Security misconfiguration su ranjivosti uzrokovane lošom konfiguracijom softvera, sistema ili mreže. Ove prijetnje su često posljedica nemara, ne predvidnja odredjenih ranjivosti kao i nesvjesnosti ranjivosti koje mogu biti uzrokovane lošom konfiguracijom.
- Ranjivosti koje omogućavaju napade su:
    - **Uobičajeni kredencijali** korištenje default lozinki i korisničkih imena za bazu, mrežu ili softver
    - **Zastareo softver** 
    - **Nepotrebni servisi i portovi** ostavljanje nepotrebnih portova i servisa povećavaju povrišinu napada
    - **Loša kontrola pristupa** loše konfigurisana prava pristupa i permisije mogu rezultovati neautorizovanom pristupu podacima
    - **Otkrivanje konfiguracionih fajlova** može dovesti do otkriavanja pouzdanih informacija o sistemu i izmjena samih konfiguracija
    - **Loša SSL konfiguracija** loše konfigurisan TLS protokol, manipulacija sertifikatima i dr.
- Kontramere:
    - **Ažuriranje softvera** 
    - **Definisanje bezbednosne konfiguracije** koristiti dobre prakse prilikom konfiguracije, isključivanje nepotrebnih portova i servisa 
    - **Alati za automatizovanu konfiguraciju**
    - **Kontrola pristupa i privilegije**
    - **Segmentacija mreže** izolacija kritičnih dijelova aplikacije od ostale mreže


## Cryptographic Issues

- Cryptographic Issues su napadi koji su uzrokovani u ranjivostima kriptografskih algoritama, protokola kako bi se kompromitovalo povjerljivost, integritet ili autentičnost podataka ili komunikacije. Ovi napadi mogu podrazumijevati razne aspekte kriptografije kao sto su enkripcija, digitalni potpisi, heširanje ili upraljvanje ključevima. 
- Ranjivosti koje omogućavaju napade su:
    - **Slabi kriptografski algoritmi** korištenje algoritama sa poznatim ranjivostima kao sto su DES ili MD5
    - **Generisanje slabih ključeva** generisanje jednostavnih ključeva može dovesti do lakog brute force napada ili kripto analize
    - **Nedovoljna dužina ključeva**
    - **Nesigurno skladište ključeva** čuvanje ključeva u tabelama baze podataka ili u memorije u slobodnom obliku
    - **Slab generator nasumičnih brojeva** može dovesti do generisanja slabih ključeva
    - **Korištenje nesigurnih kriptografskih biblioteka**
    - **Loša bezbednosna konfiguracija**
- Kontramere:
    - **Upotreba jakih kriptografskih algoritama** kao što su AES, RSA, ECC za enkripciju i SHA-256 za heširanje
    - **Upotreba preporučene dužine ključeva**
    - **Siguran generator ključeva**
    - **Upotreba sigurnog skladištenja ključeva** koristiti sisteme za upravljanje ključevima ili hardverske bezbednosne sisteme. Ograničiti pristup skladištu
    - **Implementacija jakih mehanizama autentifikacije** čime se štitimo od brute force napada
    - **Redovno ažuriranje kriptografskih biblioteka**


