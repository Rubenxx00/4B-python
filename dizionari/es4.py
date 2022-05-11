
def istogramma(diz):
    for lettera in diz:
        print(lettera + ': ', end='')
        num_asterischi = diz[lettera] // 10  # un asterisco ogni 10 occorrenze
        for i in range(num_asterischi):
            print('*', end='') # stampa asterisco el volte senza andare a capo
        print() # a capo

testo = '''Secoli il verita te avremo me grazia. Mani amo lega pel onta col uno. Buone ve fatta se arida ed rotta acqua ci altra. Regge sul ferri diede sei piu avere oblio dir lieto. Sospirare chiederai affluisce chi mia. Solauna tornato nel dov vivente uccelli giu. Muove san mio resto oltre preda veste. Sangue in andate ci re sapete trasse avendo ha. Il ed precisa no mistica perduta un secondo diventi apparve. Pei incertezza nascondere giudichera bel impazienza mai voluttuosa perfezione.

Uno partirmi voi tal inquieta smettere oleandri cenobita. Fai amai tuo tono alta dito dire pure. Tese ambo ha onde oh lana si ti fame. Ho anni dice la al sono arco. Intendeva contenuta parlavate va da puramente chiederai un scacciare. Caduco ch verita te fresca oh da. Perse udi una verra entro gizeh molte col prova.

Ti sollevando agitazione cancellato ed irrequieto ricordarmi ma scomparire. Tu sembri divine so invece impeto essere potrai. La leva orlo lo oggi vedi ma. Travolge uso con finestre migliore seguente immemore sua. Ti aspettero ma al lacerante rivederci. Colui preme gambe ah vi. Smarrito non crudelta ove infinita qui con.

Davanzale statuette vacillavo uno nel imaginato salutarvi. Ha cominciata disconosci un incontrato ed. Indugiare aggiogati sconvolta le or su. Passarono benedetto se ghirlande conquista potessero ma ed. Piu avanza pietro stessa ore finita udi dov invano. So ve venire vostri soffio oh. Usci fimo taci fare alta piu ogni lei fra. Muto da da ai dove rote ho vede atto.

Cadaveri benedico ripeteva ma chirurgo un finestre. Pago lega tair vi limo ambo taci va. Nella poi del mai altra corre. Lei sospirare macchiate poi sei mia aspirarne accendeva ascoltami. Bisogna cuscini fu di la tallone. Vai passare evitato dal lacrime. Soffocato vai approdare ore gli disperato.

Sparvieri mai suo essendosi bordatino talismani subitanea. Ci re giammai passare fascino vi pensavo. Afa dita ero non doni ben ebro nego. Energia pensoso ve insieme pensava caverna se re. Chi pericolosa cambieremo istantanea sai vergognoso. File nudo il po fino anch vi fu vidi. Te petto sarai le mi trovi al. Era noi orribile partirmi paragone una ami.

Parrebbe osi volgendo traversa poi torcesse esercita. Gocce messa tua sue offro. Da svanito piccolo leggera perisce avevano le modella fu ha. Anno fu me bene un orlo onta volo ai tese. Conoscermi di indefinite cominciata seducevano coraggiose sgomentato si. Per rientrarvi sfaldavano sostenendo ore. Te da coraggio tendendo silenzio da. Obliare corrosi confini pollici ve al deposti monella.

Talismani rinnovati un scintilla ah bordatino salutarvi. Avidamente ritornarvi conoscermi il ad volgendosi. So ieri dell moto ed vuoi anno muto. Nari temi uno omai miei urto una dita. Ah speciale el incendio palpebre il permesso ad affinita. Glie puoi fara ti un temo il dara. Non forma torme sui ali pieta parla sul quale amica. Animazione accompagno sue necessario pie conosciuto far indicibili.

Primavera ritrovata no riconosco taciturna un tu. Po dolcemente lo inebriarmi da ti dormissero. Elefantina ed ve tu dormissero ho tranquilla. Da sussulto io se di sbendati scarabei. Mutamenti ma prendesse ah desiderio rifiutare ginocchio. Ritornarvi coraggiose due ama non nascondeva san toglieremo conoscermi. Bonta fende massi sul qui chi una. Concedi tue tre entrare fai tirreno affonda conosco confusa all. Mio siedi altro umida animo chi seppe nel non.

In ah sospiro aiutava cerulea scavata rimasta corrosi da. Contenuti impedisce subitaneo congiunto splendido ve ah. Ora repentina chi pel altissimi abbozzata torturare aspettano dei. Si el mi monumento me comprendi concedono settimane serravano riempiuti. Nevi ma ecco temi el. Ali intendeva deliziose consumato uso. Ne le ve attimi ho fabbro groppa riposi oscure alzati.'''

d = {}

for lettera in testo:
    if lettera.isalpha(): # se è una lettera (no numero, no punteggiatura...)
        lettera = lettera.lower()
        if lettera in d:
            d[lettera] = d[lettera] + 1
        else:
            d[lettera] = 1

print(istogramma(d))