import collections

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s) == 1:
        #     return 0
        # elif len(set(s)) in [0, 1]:
        #     return -1

        # ss = list(set(s))
        # ss.sort(key =s.index)
        # for i in ss:
        #     if s.count(i) == 1:
        #         return s.index(i)
        # return -1
        l = list(s)

        dic = collections.Counter(l)
        print(dic)

        for i, v in enumerate(s):
            if (dic[v] == 1):
                return i

        return -1

# s = "loveleetcode"

s ='"rcxfqsiahvghboalaotgiqeongprpkrrfrdkafibklraovwpbqrfraoivcvbocllvxvnnewgriubjqwjrtqxdxdjxconptbpakexogmhgoglsrobbjktffctrxdwtofmoukadsqljdqvkxxwabvcicfmnxmuqrgtxmfhmklcqbcqqcbbwtsdkhsedmbgavdemcwusfvgvwldmsejtwjhfkkujmcfddfouonamlnupenhwpapqekfrvfdbboaxjukqijtlmfxxcgmxjelvemgmwldkcwaorixxauuoidmmxhjoqruqwjkaxervxcmacqgbguufpiwofixuehkldpquhxhracftdwwwkskicmlwlbnxnogfbpijnovgvwtrwaihuwhqxollbkujdniorquwdxluovvrcpddmhduhiafxcdkhghhlujlakpudbeeptblthfutapuncdjhhepqrsjmruvmqxbnthvpmnjrhsbtcugfrpoobnoxtiirtpaebxlcpuslfblssfjxegnxksvjxtucjdbetbfsichxkesqcwdpqedbmsdcwxrquuvfkebjhpjxvchgjrkeexaorvckajpjsbthgjrvubpkalrnilrfbafeasbkfuxomlulxqfiwdjhrajdhxvupwbvibiquvaqkkwpmitrodqirjfcokaqwkeacmifxpkvmnlepbniujlepnpafhrjgdhvgrqkuiwpcftdoukfaoclnnoptebhhkbediafmqlftjuccjdijsfvratgcrxsqokfdkjihajpqkqdkphrbmncfhfmqitcsqkauwssuiqerphmaxgawvrkxjetwovpvisnxvdsvxjwobxpsqinbusgxxrsmwgrrfrmehncqodepiclsdoqcsgehbtrbvfjwaxvtlxrgehwdthqgaxjbppvggkqgwcnlavjesjhpcumuthgwgdrncfslpgxmpowbgsgwldmtisoqprnuvtwimobxlipbainabxgchwqrvbfaanfxwgcqmeustpgvciriccpagjlcbkptvlwgrudosxreodnsfprrjvtapffovuvdpeisnodjavkmfvehiuxcfaqckbwvbhqwvhdddlqtuawlhemtmpkvwbqnjfopemwvavpadtesohmcvalxqjbincsdrjgehsraaefduxoxxtgxpsllfjwukknkegelkjpheplkwgwsxtdkebkocxiavcltcljnekccflcgkqmlfxdvffcsitxgeblndawsfeaaskthifhsrxwobxsfxgtukhvcggrswxtkulffxosofmuxbgcaopedferqdumfpucikghaqssawvoofkklwxclnjpqlcochcnsndlxsciiptkdmubgonwmefacorwchjeantitwnuoovjqokrbprggpbcoligvgrhrbwoemdgkdtdtuhbtattablwmdxflndohskmctmhdhnrwgqkvcuodhfflnotemgrixrendrndcujpdpcxvlnpepvucoaxcdivjsvmfbbqtxfxudcbiakmwpppjwughaefhohqbmmtlodnqekdtedkvpmeuhhxealssddsgtvebsvtitlmqwcikpddahktbiwcrlhpvflkwbshuptnewoavvllhrtcfcoovwmcosqobwckdqtocupanlgfbcldrfrowtccistrdgmuvhephjnjtbtjnmchvjjkdksgdwejedkvetfqouxkofkhewrhaxucvdkxqocgdulvnufqnohvhjlhfqorcnevdhunhixkrkxtddwjmwmanugirdlvewiegngqposlvuwilppjfehmjxduiopfgpipvvcprhmtakrmqiabfagrtisjbbrpxcuorhxmmmtqbmgxiprbxdcxsblqfelnqoubkenvbdqlrlojtkkqqudoxcgbtqmfaeiphultqwdlhgjrtudqdecvjkudmfmiilqsbnlwivecunqrvsmpojnfjjtahbdfpdmiprmnbwuoijbhugvwrfggwpmgfwjwwmmskpokvtjqkjwmvxonvqlibnqwvlorfxaxbqjlbmfqtvnpdfhtsqwtkkviajsptdbbvsnbihgokgakmbjkhhvwqwvlgwnirqfwvxtepgwjadglickivesllspbgupuoxnhchjmjreduehdiaegtqeqvekirtbkdpseujqqeoicpkkcuuvmkktwthirgsbmxqkfkfjkixrxbdjilvxjrchnaiimoraadlpknlcqwdrcjctnwtiprjaucbcbiihpxxqcmeflglhsiuqimhkucvgmrbwxnimrsufgaxqcpolrnlacgimbdbbgojeavhbnftfwamnpkenfboudtowgfsjabimchifnxlskfuliongptnktmkadpcwkrgogdiihjedsxnjxekmpmjtcrkcqkabwgtldtrjmkoavfkjkmkafejxxbbumneqckirlussudkjfiqsrfvcqkgxmneoijxmilmrejmcxdpwipjmgaelbowrxevamwigwjxmihgbetoqptuxpegrqjdpixlcatxuufkqfjixntfnjlslgjlwndvpjfwneafamoehdnkmaswoaababruqqlcljxxhhwrrfnfxuenrobrucbewrsarbcusxefrkntwwswcxvimopunapagvehipicuufiufverqmoptaegknbdsshopisndevqakrwamsrlufobhhiqsauabaxvfixnoeadkhjlfighblprxtqbhhccflsqnjqnphlngkenodqderjctqhnealpnjvivfxtxgbfflgipvhjnwogrmwmqlrikbkvxnugncceirrkknlpdtgljruodotnllixdiphckpspuemmmmwopxcmpishdbwbaonjprwnxghrexgpatnxkstkumjrjttmhoiijitpqadgcchldwoomhwsspeerjtdqhaagngqfnvhvnbifwxsogdfibigktiptrfkoaohwgougikfmmsmpqjcpkihujixjuposcnumromeldcsofmhdrkostapleubanlbjbrgqnqpomqxgbihbtffjqbestnufiklhdlmrtxpkehbkfloaxcepqbkuhljlacjkkvxwqknnvgsulluknbmudrjkgnacvmsuafvwtbajngklrbcwetuibasnrejcphoullrrntiuvopximxloimurxmtaifmfmobuqaooaoifptxqnddjxvgnfxolatojtavddmhokbteqvnrlpfojoidteuknlkrdhhqouteobxecwqshsjeopqejkxmgooweiplgjckppllnfinqexvvrqawrgsedmqafvdfcvgdcgcasvipfppodwgcsjuokkwunjbdpkbcskjefieegjtcnmihdakvmcctrtfqqslfpgaahpjgonbbajmchlmjqdsthupdwfmmsshfptwoferklmlotkbjofperkhmiedgconcvnvleedgghnbrvlowijphwvmonbtasliktmwcogmcjjtiuipjehuabqljrovlgbxvguwqllnnsbnjhrvorlcmbbiabcrdthwwxfumrcqkkthsgnxoptktqqmdevkahvnwfgaasdwwrqqfkwwaoilfmvotbowttsfepjrmuwplqaasbsbegsodhphhkxfdaxwipmxgjssifdrxusrsxbcnapwxggaammxduitaqiinbjjougolceargwmevmhtrrruwnnjjaatnrappohgfeibdkjewbblnwmdvtnktctrxehqxkfdjsjugtuctepikchirjjkqoipbcftlrhthmldplnttxithpkucbmjxeagjdehtmovosivwigjhivtttwoajmpatlfjhrnwdrbvofcdmelvqvaahdptcjfluquhfgmogbqwwvsofcbgprknlandufsjhpmnotukvgbilgoimgmcurskwwkionpaukescpwkpxecfanxqitkjexpsfodkusrcouwrdaoombgeeautrpumdcenmicgxvndgebdhnoixrdqcvqtbgbgfskqdipdbqkfantpckdwvlbajgbjhckxthhdloajqrkbuwmhejtxbqqgcdbvmlwpejevmsxamkthdqujpjxfjxjimcwxxxmvrrbafvlxgtxovslgicqovacpqvcorqodjoxshhlxwkuqjmbncfetwtmcfddejvdxgquerobilbmligpqcbnmmrxlmvtxqhtcnqkoueekghwirrtvlgrjwbeqfcbagffeafpxhamfwnsxfmxotnkcfljspsfhcxluphfrldjbmcaqlhrrsvooqaibtwpdnveerxdcqutnxwqsmllgbwhwixhvaehgoajsxujlftcciskxapdxiqukuiinxhfogxihrgwetagaheovwdlkwencfectxmjmedcdgfenjexxdgefgqcbeckwtcufrvtardhngckwawgwnauwrmqkratnnkimmbmsuxapsmiwpwrxmjpcpkeogqibdefabisrhplhsuhwpnkabjtpqpieljrqpjlralogpejwfjfwicpklirxcfloptodgicoqjbjwndemtlojvkvlxkiqlvcshabtksaccrcukarosrocpjjjvecicpbvenuuwdpvxqrqtxumhanmhwnesbhsixdilgsrewlkxfgtrspwrwmxvikmpagaioaskmudmjuikxafmqataetckobtsrohhepmtvkkxvjarqivsjqmvlkgvkhggdqkpkkooduvmtucthgtnfwahcrlotpaqaeopwxprucnlrtnqmsqetepwihqnjixcpkgpshxoclrnrpsqxemaoillpwfturldaraaucxemacrbqimqdoqlecmomlpudnudserghpmkrxhlfqdpixulouunsccrwfmigdkpiwfewjqnibgelwmgxkqmabtmsslqkndwlnxshadbhelxembmwesdnrsdpebrrjvvrtcedtiwdqvblbkwvjrclchhenhecqitkjpsusammgjqhepckrojictbcderejsiwhnmqpjtjornsvjcwohqnenpboqjanvueufcahwtupebsopernxhsgvtjhekoeihvigetvumtscsimbctjtowrmtkvxwwvtbcmqdtpfopwuklcacdifolmrjtbruiqxkqilfgvarqmrqfflokkevhieuwdtddgllctadfinwgtjdeqsnbqanluvubkmfbhqkxwggqavtiuufrbwhwccuxrvrvxmracuqobnuxmhrpptfeafujprucgtsrjlhjabwikoxknlbdlvlvwkuuqftoeajxbcxtqxsnuioqccjujlhulchvuptrddvvxabitmonfdbsuldsqurqwpfwefdekeheswvobsqawhhqkgwfjijsaiofpkthklfmsttgrbkfgnkkverelpplbfscgdlkkranixdauplfoerqvugaxcdixxjxjklntfaxucferwtifvurbwejmiomvnmlhgdpuiwjffbkrvbouxdxbddpmkoojirnjadroaqmepajlvxpsswaxrlkeounuosoggdtqhqijaqcinmsaoovatmjowjcvrfohtlvmvmvcrtnhviboejfhggwkstfmruntmmpxqotkbxkjvmcllqkcubxhqmotencllualsmjhaobgwwoidesrmfewklmqesopxujqcqbkxxjnhxvmntgfwkxxhprtqccwqfcvjrbkvblxbxoqaxoglrhbqcdnbvdqpfldgxkqkohtchtlewcdsaluellggtmotwekjkllpvnkufcokkknmjerdcqfxmuqmpnblcgmswflxterjbftpcsagxecuasncxfaspjkgbhpjhqlbfeovfvqtcfpwxpggifiarogagsomdivlnxnnqusndvrerldijvrficasfpphwtwwjorqfjnjcsthwgtwcvcamapdgwsthixkrjkvlksbhntfgigktembwxmtshbhaqhpnxxecqrecnjbcqnleuwiugglpbrdadhofcigslrkuuoqqaasnlbohxgkgonahqowjaxksckudqsusoonocvkaqtbqmtvfbfarkbinpfrbsemotiwhjbmfrggdudscmmsopjaiisbmcfaoovfjxwvauhdboghocspgjflmgivwieiijorcoduaiviqbmvbdiucwnirbaunlcfgcdkdurrueilcxmtmhvltpcpxrsolfopxkdifcpvojroogojnwcdpemjpffuhmjedjxuxaownpiaexeqvhgmavcnxxrvjjdgshwfionxjwvktkuhntspucneanhrbmteuuidstvnkfwtnpwodkwsnceedapahukpjxpguqgkanoljnlwjmjisgipwpatllpgbrjxvfxndxdshgcofitglgiutulbnptrmsggpcrhdrvriamojqgwqkfebnxlfrfaccxjbpdgrdwxkmrhukhxbkxwqmnidbwmljecleomlptngcaqwxrkwnvchxvqpxneqgeivibbklpbmjkbpxsgxnhbqgodssdahlhuxevdhjhnnkocxkkdmixcslqckdijsgherireixobhwnmoxcbvxcnnvvmrcdwhibseuwupwsdutpouicbsjdcrtkbvpvpqqqwwaebkndfksljrdrkuaakpgscqsvnlashqtcntoshdcrmfjaebcrufgcgadmpkopflgbajhhpnvkpqjgisixbmsvvxjsvelqqfraqmjjpkjwksnunqckpmujxefghrpfjquixturojhugmdrtjijagkgvxhiwbsnxsxjeiawfshfkemgtxcfmqvfxqprcuubsfksakertvbbwuqdujhvbevglpfbjkmqsaetsbsjakmptshhgpqcbqcqduahvlttqcgnsvixvbbxaqrkcaftuwmuwpbmvxbblniaaxhtqkjcffvvhogjqfkbuiqxjgwtuaclvfxudnbitqvifalupmvqohnrcicrstthqipdgsmirdhteotdqfvrleakpoecvgflrjrpqcjlpntefiiguhslmaabbofpfbgqbgdrjdhqfolopoqpkseoprpowsghdvpghagarhhiewwpdbetcgkewjlciiedwaiutakvbmrstfdqxxtfmlnsbwfnoccshtitgfwiaufqlldqvjxdrjntgsugrwxfmwjkpwmqwvlptiopnionqjsmhtswqokupsbcwncfejcrtfehgcrmcbuamlnvtbugafjsejjjapugliuopbqivktvdjwclpndfbrtikbjnwpfecimtdlatnwtwvfvpafuamrmsqsiiauxvuosxcsfmqoluwsppmtrbaigcttelmctgmxxfuegwmtfwgfadlrrgmhrbdwnfctsqmlmvdkulsfatmnhuffvrqougqrehsvusdrbfwmwlrlftrmnrkifjtfpksvjiebquqlvpfsneqhuwdajtckqhhemljktajpphvhjciurqbptfdbuqflwkdtbdvxcpxparbwexhbjwlefxjrosmkishjochoagxreveqpfkdfxowquwpwrniopuhuxfvtmjucaonsujqpscmffakuucfpcqvkcbndjgbdepmuuujuppqtbidsljrusudbtrwjwmqgqhgfwuvxoficqxsfwueniijjkxxmcvrefglxrxggaenulexafroqkngbaksvfaefrethnokbemppbwjrbkwikjdcnbvuqmaqwjoadkkrdoglcpcikgnlanatpgrqsdgoewuxcjgwlqjrhgagonlssknnaqwsdegwcbuxkfghwtcapletxhiekpcqxpujdpajqlpoeucvmqxskvnguudkadxlfddwdeuwgnfmpqbxdfjmqonhwuwlkqlorusrctsgvfwcdaewnehqsvtqdxpikvpclkkrbejjdfkibmljctdoxkwgwvpixsdhdfdoxxsodmifhegrautwaoxmewomshxukfvbmevvsjbkqqfgboixepwapdlusukcxthkalsakgfgjqxhujdjdwcsgcixpbwacftqeniuskekumgmsfbvvdvdjulnrojxunxuhajudfwgiuahkcnldpntjsvqbluhubuwjftvmxsboqonmqfsmitrvkwowixpklcetvpsvasduqpjqpldaaxofwgpjfbqxjjjmwfrwqmnunfjppvvanjbkvueidmbcfilmkutqarpgvofiqubtjidlwcunagcdgqdeigpcwrqirdoeshojdgladwqqwqnldbqthrnvdtrecmeboindlbsrtjiptciboldrroxxpqccoroscfwpisihotdmjedvgwdxffsslbcqpsfeapqqmbujutcpovhhdsrddwrgvmrqugajwwldonhifluwuwuqfweqtasrhrakfgqxwsrsgiiljbsdkxrhudftfvnnikpujkmbgdhmeqisawtniawnrjuwjltchnvqckfmaiqsjwwfskqvwrvrkqqipdegoulvpwlstckclclnaurkekulqqcbqfpdenquafflxbfodeobagvussdddibkkqvibjflfjdntnkwjlqrdwnlasdcujwkoofwnhkngiwkrgragargkvaqgsdhbdasnvaeabohmlobidrgqlaxddpcukmsugaafgocsfbdnrdtrvdarewuaqjktkwmdswgiboqdumqcuuocegmhlswidxgrbieqgjmevaptoxwecbumalueqvmkwbipidckdjqdufwctbwjelvhbjihkgwipgiohwwrkxeumvfrslptscqlojgacgvjxommocbvblppgpfonubaefvrrlqwivafgdwdfhknqvsekenkkfvccmuhionlmcxmdkwseektrlmsaeogkochdroxmcgggwsgiokqsbqhcintpowrfgabisspfbkhfqcttemhipuxusfxqcpscoaxjharsqbokbwdvxlgwoouhjvmebqtdfajgriunctlvahogfivufxglxuljdsdwmtxxitqevbxowtvvgcmbnofabduphmrucgrttruijkindmwuujdxvucfsixqgghnilxekikbhwpjockrenkeohdthffshrmbnjragsrgxwfmhlkvahrribkktkuwttaxcqxahgrjijaepbuaigioksvcufoejpdiprktnnkidxkcgmssudicuawlcqruskfftdqlxnemxbjftkdktmhxivdugthowghehhkonaifnohhpvocvlottqgpieprukhfcdbfqgmluwlosnvitqohqkwkpvapnogsfjtaaojnnkedtapnvjntvstomfewqlnbhbsxmiimqjewcamqsqvhcqnconkhwastjjmsuupjudchiuudtvvsaneioecrgvoidtdactarsrognfxmpwenhxaodkeobdkqmogkmebxbbasibvnpvuqwqrvoqqupbvlntvikhuscvqnstwesbudvahnxeouxxoinracffarufwvkicrrtuwwokwfqogrohanahaueufiqdcjksomcebocdqruqspvhemrcbjhcwnwnohquskwelimiksxnawegjdsbxjdbmmhnqlcbmuhencnsfjjthrlekbnuiwcrxneuhnjkvbwupemcjvcmigtjgxslnatswhequpunvccnrprooxlgtntfmfignhpetdpdxodmuotvltniuxltqxuankxosruhmaotanxgrwsvmppxsukrxmvsrhpbsrndcxqswbpsfjgonuhkkgacxtodilragfprmpfhlndcbaqoxrglspgnbnpmrxmugoupurornpdndtoxpxsjtuujgbbtocqtstlwqnksnxillrshiooufqiqtilcfnwpceehbkbjdxjuldtqbfhehjebtrfhhqfhnliixjdowepijikrbuprkppmffqeucntuoolsbrjiibppbwbbmflxtsbadtxddokhnohjlkkxlhrdghsrfrcmntivvwconrogjbtgwxrunbofgwdjwexbunceicmlnfwjjvjhtwppeahxjkmqivqaanvfgwulodcphvavjbshddsxatvacvgxdnkxpsuggccsiwiiratoqcipdbghnckalekmlgllfswqwcjhdktcuwkvrvaobgsrasdsidruedxcriteohimwgwkdorffjqcdagkjigpdgdxrbovdxemxcofaesdjjsvlnuumgsfjcdremktrdncolrqrilcxakbjjepblwghpqwnrporbvneqorojnimohfvnfnkciceoqisawgcmkpabpbgioolrrkwqjmeibrrgfeecnkfrwwthtijtimsthavsxvcpssnhffsgvukkqtvbcwrebcjdtpbdhibojwbkssmuxciwiovpmllklprcuwlernuvifnoccmnbvqggglbjgkgvmkocptmfljvfpilxoqqfvrbkfbqjqtxhslkfaaedmafkmssqhanrrupejedebbfiwetwkkldwcvnlucnsfvpkaiuthtcbcbctpdtesjfcpnifotokgxgrovslaweqgbmqjjfqqgrqgwscifdfndouwnxrpwqvxigenfneddapaqtsirevhjxdxbbuvthcktrajqbsmhirubdvbwriocrarxrfsdsfredmfjkalsseltkcjfchkfekfrannqhxusvqcqrhgnhbvvqlbfqbltaqthmbxcahdfhmawvgqxfabhfoqwraxdvdcxhuhhmxfwkhwsfpxagahkbmgqgkbnlddtavwbcvkuukfedimjrtaveunmarpbcpgcwdlquclxwgungsoroxubpqkbvkkitjcvlpxkroaajaumwvgqunkmawqhpirjmhxdgbcrbjigudeblbdxnvlibanxecmmwcoepbdemtmjwwfufvouahoniujhwhfkscxjoxtekldsjapoedocvsmjpkfsmischxbidsrxtcoqekrwqjmgupnoembnwgdmubveotwppautpeenraisnxqejimsuojrtpcshsreofgmswpbpqbfaqwjvahaodditcjuwptvrbmbnhdmcaaposopakjiuttbmkcrestkwtnnqjhgtkubnhrnjxlroiwefpubpkkdxnsfdceoauwswfwusgndeqgsijxnqrqrcfktwdketxftsvwtcrwggmdsmhmuafmtbmogbeaasdscpqasbgwlmtvnbclgfpxrsbvgumgsxhvbptvrqgpbppscqlturoiupwiuangtbvfpibfrfrgivgfrphnvluqtorwxdnvtptsfmixjbxgjhcmcxjbjsphgjdiphvoadcvskcesupmtoahwaawbibmfxugfcnxeesgwkfdkhllgqliuldeumhhbqehqwfiwsdvsecfdqrjthcmuwdukourrmtmirmcpfmqnqirfrkwrkmgxtawlohcgtamgfdugvxcxgrqwiotajcteisjimhbxvmajrdidskjiolcqpuijdfothigiqopusxabfjdgmwvbqhgkvwutckvnpeeucslntrlpriaiddqjufevjsawfmqbxuecsdotocrbvpuaqaxbkvoivrdkujqpbbofjlqnujdkjfcgbxnhkxbtidwaxdnxudrcvrilwhrpndilagxvvkihsarpoiokajvlxmwgsekkrrggtgatrpjdlplacjmxnnuhifdfsihcfxfxmxgxaguhdjmrbvwxtndwwupamlxhkffpjjjlihctspnuewnjcsvrdrcqkftswkvfmlkxtsdaawwrucbndmhhfdsutfdkkxgbuorbqggnwbghplrtedmqgmkegegpxnpmqsfloulckpgopwvmwgsevcajfcmslrbnsphupnminpowswxxkhbekoesxxxkqolervwnkwpoisfhkkeegesxfqppekmhnlwjvmtvxcmebadkfjpuuovogxbiefwcrhkvodvuwietcrrxvevgcejivnrwxgdsotwxudfkxxwcbvherubcsapfsqiqvwtxlhtqamdisiljqtmdrwjrtaovfrnpxfxrqtapqgovpttroublnfvceohjwqrbdlprvwwufihchinrdannviovxqcifmeachcoccuxhuvoawkrgxjibwullgwtdxnmvcqbhfdrxqjrtpjcjrmurqgkaclagpntsmtjeilrdfclrrtklfprfgfngcljqftxtniobttpftbvqvidfnsioaijfiloxrpawnkaxfdmekwgkthnvhuisniqfconvtdmfehquqvhhjawvsqpuuobkonbgrriisnnhbxnrswaajpvdmebsmxmxugmbehpsanctnlpxejhodfedhtlxoaaxnlkenwqstumlalhuolvbextveeoutinejgkqkovquskwkomkqxbixiaitirhuaeukueoerfmdommknoabduftgfgmxespamjoqrmdmrohqdfkhonsxvqhrbowaidmpnshxauhriwscfravldmfepmkfattuungiptubvaqsmsbuavgnbukbdcjxvrraubelakvngnrxqiqqtjluxvjfebvcdbsfkhsjnwctbhkasuvqqtmjvgphsjgddlfcaihpowulnggukgiuanitlopiwjwungtpnuuxtbdgkcllrvseufidjopogclusetmrsaiuigkadcgnslrkmlipwptuevtatocuemdrtospakuagskekcswgixgxvsrelawiqwcsklpctnawipixurmwsqglsqtxtpphldqulhibpsxfmjiccwsnmikpvnatwopjwcjcrvkfmstcphdvlajmhounoswcdfpwarondffwsfwmajawrhxestdtmoxsdmngcsidrqkmcuhuqprwjuokoopkabcufecitnnenfpgeogsxknnnwmjcxibjtpicehfeapcuuwnxddgeresnntqhpgsqvwobusfnnftbovrdtgiifwxqksofurdvwxftfnivmhrbcwcjxppsvdspeaetibfpxsoigwnvdekhqhxbogutjtukthsslgigxpchhhommworrkcdbthcrxfipwqbeiulwohjbhrkgexpmojopgaigfmrjfnjlqrwupnfcgpjkwukblvsahpehglwimdrqewwkloeveihwmecrboauxlhudqxntasenumhaivxrmevoawditieewjosutpcfmgmdadhfbcfkbmnihxqgrppgjenxtgskogpdaxrtxfaeovhuenrfenjuagcjocrginiepkncijkakhflogdjaxjhnfdbvmqldcwndekuumdhgcignjgcgmwrrqhbqtahpvaqfokhkqdqrhogagcivekilpfhoxxtmpalehmndnsnufrrxoisoxewmlxuxjhhawfprxpmwkrewmpxmqwbbomredmhfaotwfhtdpnvuxooqvccennwnbjbspusfmwwubwbdvvhmmtlchaqstwhsovqxxptcggjcekxamxepcgllktdluimkpxusunusngfknlwdrdsnqbglxkbkxsxcdihmvglfrfhjmjwugbsvgdlmufknnowfsohultbesncbcvxckcmputmtmeiundsbncvtesvxrfvkwfroneanddxdmxkihalgleqrcmjnfnxmrsdpiawessucwwprexrvvfcfnkdohfjgjvpwkwnpkinqrjqwdhuorlrhtcueggtaamdsexotkfbovanqmidqrhgiggmmkgntwbxeerblcjheduwgxkimncjqomlblgxprcfemgofsuqrctkrfwrbdtkgbwarcpqldrujdfvstomntokrfchqnbatbdmmgxsaundlsvnbuqlkuoxfqxrqdonhncqlhhlncoddiihsgiewxjhvenrcdjxbofkggitlhturvnexhhbjerkltfvwhjpbtdsukjujsogfcejfjwiubmsuvnglwinaeekwdjvqmgangvrxudswqmvdaxmbrvqgsqilccvatddmrqltgipjaivnorxcpakctpwmwdfqsoqqlngjruossaafxvplijbfrrkixunjoffbvedcvgblfegrrkdxejwgepmivvfsjbcjgfkwiagmjerbghumuorgdhoubgmecsjfxqleurgnhqaovgskpjjvosxtchmwrbiqgovnirbunakqpwvsfsiknrwwjidbxmrxvfcivqpevuigdxvmxcmvbkemejcvdmkfugaocwhdxmsbjbbpmhoirhrggcbbnsuijcihhdkjkaqqresmutwanoftuthnwvwawhckmxqigrbemiasiuuiwjpmqnosnukgdhghksbvlnwvrwlsxmqwdhijbouakrwsoblxiendknakruldrsbsuqjrhqcgwltlruksowmpcknlstxwpgifjtxmdravakrkdctpvwnmlcvcwujlapfotkfdelofioaovcoxefrqwhseffxruxahbusocednwhhiomlkumatcicufasblvinmrvuwointfqpgabxdjkghvpxatscwrhcdrhowigwgqrmfocwdwhbvfpiwiwnultowfamfsdqqadhmguilcodfssfvnqbwuvjvdqnqmxsxfwxsiivefifglkwxegxdsfsjuhjbomvnijvifomngngragulubglgtrjaujhiarkpgifdnooxvpfbfxcfrxwiwpnabfdkenvddjrlxcipiisgawlhfcnrpegcmudeirwvjhmgsrroviaqpkgcpgxhpxtiwxkomwftilxspceuwpqnsstofmeumrmigfnbimkhhvrrgowbrgboapdtitvwgrcuwpotlsgqiesrgnbwhvtusrnrqmrhxamtmnmnpjbfbqsmrgmrpthnbxsrnwionvcnbwxisijallkjnkhldrmttbibostkrrnbnlikeqaiockatqtmjhsuqabcuqindudjatgnpanvsairlrhvleckkmvnixkwdvxmkgbisjjhgtolfulehatdxesqpagnjuwksgskutdgmltaacitvufbrbsvekocmdkdrrhfgnlksrqhwdvjpartgdftoojfvhcipxdaaqjtjfdjnwkvttgbwjbbmtigmdgxubtdslocjopegtablomttlajxkrgjnpjixbodxjvberjiuwunqljusrshkodmnmgcaejvdcfljlqvomgskelionemmpwueopemvewiktfleslesxjugjawdhgqdqdklsuvcxpgifasuvmmrpunctmtldmvkhxwfrdqfsauevmxmlwgagrnpsumnqimmfrbukiiooqkprijdcjdiurvfepcswqebiasgxfdmrbbilwbjmxtqbmvucovjfmgcsokfpqjhubjxcepxxgvifkefvculfoshsriasslpirbfvlkmnicirctpdrxghvwwxlniptbfdbcjwdlanlbbdgksolxeravrdsruatkaxreleejdxilcmmahukmvnavpvwteukpatqolponolgpdvnfexevibnxbnbuithhnoxqkxqxqrponnjkuotluhpcglbtjvltakhthutwcrbxxtpxmbvomvvpgpabglgcjwghdhhsldnujjbdoqcffvrvrjmfilqnoculfgmudxtkugvhbluqrwrfikoigwbejgdqfkjmsntthrusgcsqhqopcqvrqmawrkbgldqrbofpcugnevtvalqkaelsggompoxlisxuhaavvgdhlmqodwowapoibkefrknktvxfuvnobhkrtxjeiusemphfikxkjhtbegqsblekvhudfwgwiscmeowjdmsshtrbemcovufakosmaconrbxfoctdlcmgsxwrswupigiqwvkvujcbfrjaufvmgdewkuekwgpgddmumsufcmdrucivvgguhptjhijlqldcvktjjgsnbmxffnldkeeklvbpkfnvbvqegkdchcsmjpooaiukkbiouxgrsbchqeglpvuefendlpcufurtfekbbmbhhohcoqfigsiclvlcotrgvcloufjlduuajldocjusgboksgeiclfvparknmxdjxfvrxpcmhekmcvujwaoiomrlinqlrcklgvwpmdxukfisngbaewdhwwrjbfptmdpjxekjrpudchlhtjbpchqpsnvstlahnklulkbbwskaxcmtswdhxdeqsawwnvdgnwotswmwtoausnspdmqidkqlgoulrthisjpovjdaajpnrrwshvxiwmdxgiglgpuwnjwoslvivuovwwpuuprrajgndwnveilxhpvkdmdflppuxmooldwsjijltqicdnetgtjcgevqijhiwdtxvrvmbsldpviaupoduvfpvtrxfeqtjcfhrbgfqhnvaonbfwcoanwqxakfdgkeckuhoskxwpoiemwnpjimbspnumohiaemiebogvbkubpunvtlskporvohmhgpgcpclgmmaskmahxrbrnlhhxthotuojjddetolqfcejwpephpskunmjbttvhpejqgbfpbimcxssetgkppwoxkdafgvbcfnrcfpotbsqolcevgiaojxpxjsecvfelqchicfaqijnxoejbkiaedmtectvrptudxbmjmsbogvdnjahhhiedpvsnovcbvpcckdqoeqjmkwcctgxilhcaucokthmdnjwgsqcpbwslmnclvwbtiulwdtomeldpckqcojmdlekduqsdnrervrptdajtwixmripuxuessckstqlhnvcjlfnpebiodgisemnnlstgxbsdiovcvdrurapdwwdwcfnlcxaueebvjpcmlaiklukbxstpkaksmnxudxrrsbwpb"'


foo = Solution()
n = foo.firstUniqChar(s)
print(n)