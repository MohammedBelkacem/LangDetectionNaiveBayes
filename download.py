## Ce programme permet de télécharger des corpus de phrases à partie de la plateforme Tatoeba.
## Pour ajouter une langue, insérer son code iso 639-3 dans le tableau ci-dessous
#wali tutlayin yellan deg tatoeba akken ad tessadre tigrummiwin n yisefka. Rnu tangalt n tutlayt-a ddaw-a
#tingalin iso 639-3
import wget
import bz2
import os

if not os.path.exists('data_downloaded'):
 os.makedirs('data_downloaded')
if not os.path.exists('data_raw'):
 os.makedirs('data_raw')
if not os.path.exists('data_test'):
 os.makedirs('data_test')
if not os.path.exists('data_traning'):
 os.makedirs('data_traning')


#16 langues
tutlayin=['kab','eng','fra','ita','eus','cat','por','spa','deu','nld','swe','est','srp','tur','hun','rus']

#Téléchargement des corpus à partir de tatoeba
for i in tutlayin:
    wget.download('https://downloads.tatoeba.org/exports/per_language/'+str(i)+'/'+str(i)+'_sentences.tsv.bz2','data_downloaded')


#ce programme permet de  dézipper les fichiers de langues


for tutlayt in tutlayin:
    filename= tutlayt+"_sentences.tsv.bz2"
    dirpath='data_downloaded'

    archive_path = os.path.join(dirpath,filename)
    outfile_path = os.path.join(dirpath, filename[:-4])
    with open(archive_path, 'rb') as source, open(outfile_path, 'wb') as dest:
        dest.write(bz2.decompress(source.read()))

#Suppression des fichiers zipés

for tutlayt in tutlayin:
    afaylu_arewway= 'data_downloaded/'+tutlayt+"_sentences.tsv.bz2"
    os.remove(afaylu_arewway)


#ce programme permet d'extraire uniquement les phrases du corpus téléchargé sans les autres informations contenues dans ces fichiers


for tutlayt in tutlayin:
    afaylu_arewway= open('data_downloaded/'+tutlayt+"_sentences.tsv",encoding='utf-8')
    afaylu_zeddigen=open('data_raw/'+tutlayt+"_sentences.txt","w+",encoding='utf-8')

    for adur in afaylu_arewway:
     adur=adur.replace("\ufeff","")
     azalen = adur.split("\t")
     afaylu_zeddigen.write(azalen[2])
    afaylu_arewway.close()
    afaylu_zeddigen.close()

# Ce programme permet d'extraire 2000 phrase de chaque fichier de langue . Il servira à entrainer l'algorithme et générer le modele de langue

limit=1000
i=0
afaylu_yemmden= open("data_traning/LanguageDetection.csv","w+",encoding='utf-8')
afaylu_yemmden.write("sentence"+'\t'+"language"+'\r')
for tutlayt in tutlayin:
    i=0
    afaylu_zeddigen=open("data_raw/"+tutlayt+"_sentences.txt",encoding='utf-8')
    for sentence in afaylu_zeddigen:
        if len(sentence) > 15:
            afaylu_yemmden.write(sentence.replace("\n","")+'\t'+tutlayt+'\r')
            i=i+1
            if limit!=0 and i>=limit:
                afaylu_zeddigen.close()
                break
    afaylu_zeddigen.close()
afaylu_yemmden.close()

#Ce programme permet d'extraire 100 phrase de chaque fichier de langue à partir de la phrase numéro 5000
#du corpus téléchargé pour former un seul corpus mélangé pour tester la classification

limit=200
from_=8000
i=0
afaylu_yemmden= open("data_test/Brut.csv","w+",encoding='utf-8')
for tutlayt in tutlayin:
    i=0
    afaylu_zeddigen=open("data_raw/"+tutlayt+"_sentences.txt",encoding='utf-8')
    for sentence in afaylu_zeddigen:
        if len(sentence) > 15:
            if i>5000:
             afaylu_yemmden.write(sentence.replace("\n","").replace('\r',"")+'\r')
            i=i+1
            if limit!=0 and i>=limit+from_:
                afaylu_zeddigen.close()
                break

    afaylu_zeddigen.close()
afaylu_yemmden.close()
print("finished")
