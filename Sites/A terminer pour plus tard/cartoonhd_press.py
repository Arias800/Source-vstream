#-*- coding: utf-8 -*-
Site bugger donc a finir si il est plus'
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
# Votre nom ou pseudo
from resources.lib.gui.hoster import cHosterGui #systeme de recherche pour l'hote
from resources.lib.gui.gui import cGui #systeme d'affichage pour xbmc
from resources.lib.handler.inputParameterHandler import cInputParameterHandler #entree des parametres
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler #sortie des parametres
from resources.lib.handler.requestHandler import cRequestHandler #requete url
from resources.lib.parser import cParser #recherche de code
from resources.lib.comaddon import progress, VSlog #import du dialog progress

#from resources.lib.util import cUtil #outils pouvant etre utiles

#Si vous créez une source et la deposez dans le dossier "sites" elle sera directement visible sous xbmc

SITE_IDENTIFIER = 'cartoonhd_press' #identifant (nom de votre fichier) remplacez les espaces et les . par _ AUCUN CARACTERE SPECIAL
SITE_NAME = 'cartoonhd.press' #nom que xbmc affiche
SITE_DESC = 'films en streaming, streaming hd, streaming 720p, Films/séries, récent en vo' #description courte de votre source

URL_MAIN = 'http://cartoonhd.press' #url de votre source

#definis les url pour les catégories principale, ceci est automatique, si la definition est présente elle sera affichee.
#LA RECHERCHE GLOBAL N'UTILE PAS showSearch MAIS DIRECTEMENT LA FONCTION INSCRITE DANS LA VARIABLE URL_SEARCH_*
URL_SEARCH = (URL_MAIN + '?s=', 'showMovies')
#recherche global films
URL_SEARCH_MOVIES = (URL_MAIN + '?s=', 'showMovies')
#recherche global serie, manga
URL_SEARCH_SERIES = (URL_MAIN + '?s=', 'showMovies')
#recherche global divers
URL_SEARCH_MISC = (URL_MAIN + '?s=', 'showMovies')
#
FUNCTION_SEARCH = 'showMovies'

# menu films existant dans l'acceuil (Home)
MOVIE_NEWS = (URL_MAIN + '/recent-movies', 'showMovies') #films (derniers ajouts = trie par date)
MOVIE_VIEWS = (URL_MAIN + '/films/favorites', 'showMovies2') #films (les plus vus = populaire)
MOVIE_GENRES = (True, 'showGenres') #films genres
MOVIE_ANNEES = (False, 'showMovieYears') #films (par années)

# menu serie existant dans l'acceuil (Home)
SERIE_NEWS = (URL_MAIN + '/latest-episodes', 'showMovies') #news.png ou series.png | séries (derniers ajouts = trie par date)
SERIE_GENRES = (True, 'showGenres') #séries genres
SERIE_ANNEES = (False, 'showSerieYears') #séries (par années)

SPORT_SPORTS = (URL_MAIN + 'url', 'showMovies') #sport


def load(): #fonction chargee automatiquement par l'addon l'index de votre navigation.
    oGui = cGui() #ouvre l'affichage

    oOutputParameterHandler = cOutputParameterHandler() #appelle la fonction pour sortir un parametre
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/') # sortie du parametres siteUrl n'oubliez pas la Majuscule
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)
    #Ajoute lien dossier (identifant, function a attendre, nom, icone, parametre de sortie)
    #Puisque nous ne voulons pas atteindre une url on peut mettre ce qu'on veut dans le parametre siteUrl

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films (Derniers ajouts)', 'news.png', oOutputParameterHandler)
    #ici la function showMovies a besoin d'une url ici le racourci MOVIE_NEWS

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films (Genres)', 'genres.png', oOutputParameterHandler)
    #showGenres n'a pas besoin d'une url pour cette methode

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ANNEES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_ANNEES[1], 'Films (Par Années)', 'annees.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_VIEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_VIEWS[1], 'Films (Les plus vus)', 'views.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Séries (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Séries (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_ANNEES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_ANNEES[1], 'Séries (Par Années)', 'annees.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SPORT_SPORTS[0])
    oGui.addDir(SITE_IDENTIFIER, SPORT_SPORTS[1], 'Sport en direct', 'sport.png', oOutputParameterHandler)

    oGui.setEndOfDirectory() #ferme l'affichage

def showSearch(): #fonction de recherche
    oGui = cGui()

    sSearchText = oGui.showKeyBoard() #appelle le clavier xbmc
    if (sSearchText != False):
        sUrl = URL_SEARCH[0] + sSearchText #modifie l'url de recherche
        showMovies(sUrl) #appelle la fonction qui pourra lire la page de resultats
        oGui.setEndOfDirectory()
        return


def showGenres(): #affiche les genres
    oGui = cGui()

    #juste a entrer les categories et les liens qui vont bien
    liste = []
    liste.append( ['Action', URL_MAIN + 'action/'] )
    liste.append( ['Animation', URL_MAIN + 'animation/'] )
    liste.append( ['Arts Martiaux', URL_MAIN + 'arts-martiaux/'] )
    liste.append( ['Aventure', URL_MAIN + 'aventure/'] )
    liste.append( ['Biopic', URL_MAIN + 'biopic/'] )
    liste.append( ['Comédie', URL_MAIN + 'comedie/'] )
    liste.append( ['Comédie Dramatique', URL_MAIN + 'comedie-dramatique/'] )
    liste.append( ['Comédie Musicale', URL_MAIN + 'comedie-musicale/'] )
    liste.append( ['Documentaire', URL_MAIN + 'documentaire/'] )
    liste.append( ['Drame', URL_MAIN + 'drame/'] )
    liste.append( ['Epouvante Horreur', URL_MAIN + 'epouvante-horreur/'] )
    liste.append( ['Erotique', URL_MAIN + 'erotique'] )
    liste.append( ['Espionnage', URL_MAIN + 'espionnage/'] )
    liste.append( ['Famille', URL_MAIN + 'famille/'] )
    liste.append( ['Fantastique', URL_MAIN + 'fantastique/'] )
    liste.append( ['Guerre', URL_MAIN + 'guerre/'] )
    liste.append( ['Historique', URL_MAIN + 'historique/'] )
    liste.append( ['Musical', URL_MAIN + 'musical/'] )
    liste.append( ['Policier', URL_MAIN + 'policier/'] )
    liste.append( ['Péplum', URL_MAIN + 'peplum/'] )
    liste.append( ['Romance', URL_MAIN + 'romance/'] )
    liste.append( ['Science Fiction', URL_MAIN + 'science-fiction/'] )
    liste.append( ['Spectacle', URL_MAIN + 'spectacle/'] )
    liste.append( ['Thriller', URL_MAIN + 'thriller/'] )
    liste.append( ['Western', URL_MAIN + 'western/'] )
    liste.append( ['Divers', URL_MAIN + 'divers/'] )

    for sTitle, sUrl in liste: #boucle

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl) #sortie de l'url en parametre
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
        #ajouter un dossier vers la fonction showMovies avec le titre de chaque categorie.

    oGui.setEndOfDirectory()


def showMovieYears():#creer une liste inversée d'annees
    oGui = cGui()

    for i in reversed (xrange(1913, 2019)):
        Year = str(i)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + 'films/annee-' + Year)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', Year, 'annees.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSerieYears():
    oGui = cGui()

    for i in reversed (xrange(1936, 2019)):
        Year = str(i)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + 'series/annee-' + Year)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', Year, 'annees.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovies(sSearch = ''):
    oGui = cGui() #ouvre l'affichage
    if sSearch: #si une url et envoyer directement grace a la fonction showSearch
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl') #recupere l'url sortie en parametre

    oRequestHandler = cRequestHandler(sUrl) #envoye une requete a l'url
    sHtmlContent = oRequestHandler.request() #requete aussi

    #sHtmlContent = sHtmlContent.replace('<span class="likeThis">', '').replace('</span>', '')
    #la fonction replace est pratique pour supprimer un code du resultat

    sPattern = '<img src="([^"]+)"\s*alt=".+?"\s*"background-color: #717171;" />\s*<div id=".+?"></div>\s*</div>\s*<div class=".+?"\s*data-ajax=".+?"\s*data-id=".+?"\s*data-type=".+?"\s*data-upcoming="false">\s*<a href="([^"]+)">([^<>]+)</a>'
    #pour faire simple recherche ce bout de code dans le code source de l'url
    #- "([^"]+)" je veux cette partie de code qui se trouve entre guillemets mais pas de guillemets dans la chaine
    #- .+? je ne veux pas cette partie et peux importe ceux qu'elle contient
    #- >(.+?)< je veux cette partie de code qui se trouve entre < et > mais il peut y avoir n'inporte quoi entre les 2.
    #- (https*://[^"]) je veux l'adresse qui commence par https ou http jusqu'au prochain guillemet.
    #
    #Pour tester vos Regex, vous pouvez utiliser le site https://regex101.com/ en mettant dans les modifiers "gmis"

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    #le plus simple et de faire un  VSlog(str(aResult))
    #dans le fichier log d'xbmc vous pourrez voir un array de ce que recupere le script
    #et modifier sPattern si besoin
    VSlog(str(aResult)) #Commenter ou supprimer cette ligne une fois fini

    #affiche une information si aucun resulat
    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        total = len(aResult[1])
        #dialog barre de progression
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total) #dialog update
            if progress_.iscanceled():
                break

            #L'array affiche vos info dans l'orde de sPattern en commencant a 0, attention dans ce cas la on recupere 6 information
            #Mais selon votre regex il ne peut y en avoir que 2 ou 3.
            sTitle = str(aEntry[2])
            sUrl2 = str(aEntry[1])
            sThumb = str(aEntry[0])
            #sLang = str(aEntry[3])
            #sQual = str(aEntry[4])
            #sHoster = str(aEntry[5])
            sDesc = ''

            #sTitle = sTitle.replace('En streaming', '')

            #Si vous avez des information dans aEntry Qualiter lang organiser un peux vos titre exemple.
            #Si vous pouvez la langue et la Qualite en MAJ ".upper()" vostfr.upper() = VOSTFR
            #sTitle = ('%s [%s] (%s) [COLOR coral]%s[/COLOR]') % (sTitle, sQual, sLang.upper(), sHoster)
            #mettre les information de streaming entre [] et le reste entre () vstream s'occupe de la couleur automatiquement.

        #Utile que si les liens recuperer ne commence pas par (http://www.nomdusite.com/)
            #sUrl2 = URL_MAIN + sUrl2

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2) #sortie de l'url
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle) #sortie du titre
            oOutputParameterHandler.addParameter('sThumb', sThumb) #sortie du poster

            if '/series' in sUrl:
                oGui.addTV(SITE_IDENTIFIER, 'ShowSerieSaisonEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
                #addTV pour sortir les series tv (identifiant, function, titre, icon, poster, description, sortie parametre)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
                #addMovies pour sortir les films (identifiant, function, titre, icon, poster, description, sortie parametre)

            #il existe aussi addMisc(identifiant, function, titre, icon, poster, description, sortie parametre)
            #la difference et pour les metadonner serie, films ou sans

        progress_.VSclose(progress_) #fin du dialog

        sNextPage = __checkForNextPage(sHtmlContent) #cherche la page suivante
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addNext(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', oOutputParameterHandler)
            #Ajoute une entree pour le lien Next | pas de addMisc pas de poster et de description inutile donc

    if not sSearch:
        oGui.setEndOfDirectory() #ferme l'affichage

def showMovies2(sSearch = ''):
    oGui = cGui() #ouvre l'affichage
    if sSearch: #si une url et envoyer directement grace a la fonction showSearch
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl') #recupere l'url sortie en parametre

    oRequestHandler = cRequestHandler(sUrl) #envoye une requete a l'url
    sHtmlContent = oRequestHandler.request() #requete aussi

    #sHtmlContent = sHtmlContent.replace('<span class="likeThis">', '').replace('</span>', '')
    #la fonction replace est pratique pour supprimer un code du resultat

    sPattern = '<img src="([^"]+)"\s*alt=".+?"\s*"/>\s*</div>\s*<div class=".+?"\s*data-ajax=".+?"\s*data-id=".+?"\s*data-type=".+?"\s*<a href="([^"]+)"\s*title=".+?">([^<>]+)</a>'
    #pour faire simple recherche ce bout de code dans le code source de l'url
    #- "([^"]+)" je veux cette partie de code qui se trouve entre guillemets mais pas de guillemets dans la chaine
    #- .+? je ne veux pas cette partie et peux importe ceux qu'elle contient
    #- >(.+?)< je veux cette partie de code qui se trouve entre < et > mais il peut y avoir n'inporte quoi entre les 2.
    #- (https*://[^"]) je veux l'adresse qui commence par https ou http jusqu'au prochain guillemet.
    #
    #Pour tester vos Regex, vous pouvez utiliser le site https://regex101.com/ en mettant dans les modifiers "gmis"

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    #le plus simple et de faire un  VSlog(str(aResult))
    #dans le fichier log d'xbmc vous pourrez voir un array de ce que recupere le script
    #et modifier sPattern si besoin
    VSlog(str(aResult)) #Commenter ou supprimer cette ligne une fois fini

    #affiche une information si aucun resulat
    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        total = len(aResult[1])
        #dialog barre de progression
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total) #dialog update
            if progress_.iscanceled():
                break

            #L'array affiche vos info dans l'orde de sPattern en commencant a 0, attention dans ce cas la on recupere 6 information
            #Mais selon votre regex il ne peut y en avoir que 2 ou 3.
            sTitle = str(aEntry[2])
            sUrl2 = str(aEntry[1])
            sThumb = str(aEntry[0])
            #sLang = str(aEntry[3])
            #sQual = str(aEntry[4])
            #sHoster = str(aEntry[5])
            sDesc = ''

            #sTitle = sTitle.replace('En streaming', '')

            #Si vous avez des information dans aEntry Qualiter lang organiser un peux vos titre exemple.
            #Si vous pouvez la langue et la Qualite en MAJ ".upper()" vostfr.upper() = VOSTFR
            #sTitle = ('%s [%s] (%s) [COLOR coral]%s[/COLOR]') % (sTitle, sQual, sLang.upper(), sHoster)
            #mettre les information de streaming entre [] et le reste entre () vstream s'occupe de la couleur automatiquement.

        #Utile que si les liens recuperer ne commence pas par (http://www.nomdusite.com/)
            #sUrl2 = URL_MAIN + sUrl2

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2) #sortie de l'url
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle) #sortie du titre
            oOutputParameterHandler.addParameter('sThumb', sThumb) #sortie du poster

            if '/series' in sUrl:
                oGui.addTV(SITE_IDENTIFIER, 'ShowSerieSaisonEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
                #addTV pour sortir les series tv (identifiant, function, titre, icon, poster, description, sortie parametre)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
                #addMovies pour sortir les films (identifiant, function, titre, icon, poster, description, sortie parametre)

            #il existe aussi addMisc(identifiant, function, titre, icon, poster, description, sortie parametre)
            #la difference et pour les metadonner serie, films ou sans

        progress_.VSclose(progress_) #fin du dialog

        sNextPage = __checkForNextPage(sHtmlContent) #cherche la page suivante
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addNext(SITE_IDENTIFIER, 'showMovies2', '[COLOR teal]Next >>>[/COLOR]', oOutputParameterHandler)
            #Ajoute une entree pour le lien Next | pas de addMisc pas de poster et de description inutile donc

    if not sSearch:
        oGui.setEndOfDirectory() #ferme l'affichage


def __checkForNextPage(sHtmlContent): #cherche la page suivante
    oParser = cParser()
    sPattern = '<div class="navigation".+? <span.+? <a href="(.+?)">'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        return aResult[1][0]

    return False


def showHosters(): #recherche et affiche les hotes
    oGui = cGui() #ouvre l'affichage
    oInputParameterHandler = cInputParameterHandler() #apelle l'entree de parametre
    sUrl = oInputParameterHandler.getValue('siteUrl') #apelle siteUrl
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle') #appelle le titre
    sThumb = oInputParameterHandler.getValue('sThumb') #appelle le poster

    oRequestHandler = cRequestHandler(sUrl) #requete sur l'url
    sHtmlContent = oRequestHandler.request() #requete sur l'url

    oParser = cParser()
    sPattern = '<iframe.+?src="(.+?)"'
    #ici nous cherchons toute les sources iframe

    aResult = oParser.parse(sHtmlContent, sPattern)
    #pensez a faire un VSlog(str(aResult)) pour verifier

    #si un lien ne s'affiche pas peux etre que l'hote n'est pas supporte par l'addon
    if (aResult[0] == True):
        for aEntry in aResult[1]:

            sHosterUrl = str(aEntry)
            oHoster = cHosterGui().checkHoster(sHosterUrl) #recherche l'hote dans l'addon
            if (oHoster != False):
                oHoster.setDisplayName(sMovieTitle) #nom affiche
                oHoster.setFileName(sMovieTitle) #idem
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
                #affiche le lien (oGui, oHoster, url du lien, poster)

    oGui.setEndOfDirectory() #fin

#Pour les series, il y a generalement une etape en plus pour la selection des episodes ou saisons.
def ShowSerieSaisonEpisodes():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '?????????????????????'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])

        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break

            sTitle = sMovieTitle + str(aEntry[1])
            sUrl2 = str(aEntry[2])

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addTV(SITE_IDENTIFIER, 'seriesHosters', sTitle, '', sThumb, '', oOutputParameterHandler)

        progress_.VSclose(progress_)

    oGui.setEndOfDirectory()

def seriesHosters(): #cherche les episodes de series
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<dd><a href="([^<]+)" class="zoombox.+?" title="(.+?)"><button class="btn">.+?</button></a></dd>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:

            sHosterUrl = str(aEntry[0])
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if (oHoster != False):
                oHoster.setDisplayName(aEntry[1])
                oHoster.setFileName(aEntry[1])
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()

#Voila c'est un peux brouillon mais ça devrait aider un peu, n'hesitez pas a poser vos questions et meme a partager vos sources.
