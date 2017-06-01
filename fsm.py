from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def to_help(self, update):
        text = update.message.text
        return text.lower() == 'help'

    def on_enter_help(self, update):
        update.message.reply_text("Biological Classification Bot\n"
                                  "\nThis program demonstrate the "
                                  "hierarchy of the following 7 "
                                  "ranks:\n\tkingdom(界)\n\t"
                                  "phylum(門)\n\tclass(綱)\n\t"
                                  "order(目)\n\tfamily(科)\n\t"
                                  "genus(屬)\n\tspecies(種)\n\n"
                                  "Please type any English name "
                                  "of a kingdom to begin\n"
                                  "e.g. animalia, plantae, "
                                  "bacteria\n\n"
                                  "NOTE: you will not be able to "
                                  "start a new search until you "
                                  "have finished your previous "
                                  "search\n\n"
                                  "NOTE: this biological data base"
                                  " is not yet complete, there "
                                  "will be missing species\n"
                                  "For performing a proper search,"
                                  " please type only the provided "
                                  "name of each state\n\n"
                                  "Have Fun!")
        self.go_back(update)

    def to_animalia(self, update):
        text = update.message.text
        return text.lower() == 'animalia'

    def to_chordata(self, update):
        text = update.message.text
        return text.lower() == 'chordata'

    def to_mammalia(self, update):
        text = update.message.text
        return text.lower() == 'mammalia'

    def to_primates(self, update):
        text = update.message.text
        return text.lower() == 'primates'

    def to_hominidae(self, update):
        text = update.message.text
        return text.lower() == 'hominidae'

    def to_homo(self, update):
        text = update.message.text
        return text.lower() == 'homo'

    def to_sapiens(self, update):
        text = update.message.text
        return text.lower() == 'sapiens'

    def to_plantae(self, update):
        text = update.message.text
        return text.lower() == 'plantae'

    def to_angiosperms(self, update):
        text = update.message.text
        return text.lower() == 'angiosperms'

    def to_sapindales(self, update):
        text = update.message.text
        return text.lower() == 'sapindales'

    def to_anacardiaceae(self, update):
        text = update.message.text
        return text.lower() == 'anacardiaceae'

    def to_mangifera(self, update):
        text = update.message.text
        return text.lower() == 'mangifera'

    def to_indica(self, update):
        text = update.message.text
        return text.lower() == 'indica'

    def to_bacteria(self, update):
        text = update.message.text
        return text.lower() == 'bacteria'

    def to_firmicutes(self, update):
        text = update.message.text
        return text.lower() == 'firmicutes'

    def to_bacilli(self, update):
        text = update.message.text
        return text.lower() == 'bacilli'

    def to_lactobacillales(self, update):
        text = update.message.text
        return text.lower() == 'lactobacillales'

    def to_lactobacillaceae(self, update):
        text = update.message.text
        return text.lower() == 'lactobacillaceae'

    def to_lactobacillus(self, update):
        text = update.message.text
        return text.lower() == 'lactobacillus'

    def to_acidophilus(self, update):
        text = update.message.text
        return text.lower() == 'acidophilus'

    def on_enter_animalia(self, update):
        update.message.reply_text("動物界 Animalia:\n"
                                  "\t脊索動物門 Chordata\n"
                                  "\nUnder Construction:\n"
                                  "\t直泳動物門 Orthonectida()\n"
                                  "\t直泳動物門 Orthonectida()\n"
                                  "\t菱形動物門 Rhombozoa\n"
                                  "\t單胚動物門 Monoblastozoa\n"
                                  "\t櫛水母動物門 Ctenophora\n"
                                  "\t刺胞動物門 Cnidaria\n"
                                  "\t三裂動物門 Trilobozoa\n"
                                  "\t盾形動物門 Proarticulata\n"
                                  "\t無腔動物門 Acoelomorpha\n"
                                  "\t異渦動物門 Xenoturbellida\n"
                                  "\t棘皮動物門 Echinodermata\n"
                                  "\t古蟲動物門 Vetulicolia\n"
                                  "\t半索動物門 Hemichordata\n"
                                  "\t蛻皮動物門 Ecdysozoa\n"
                                  "\t扁蟲動物門 Platyzoa\n"
                                  "\t冠輪動物門 Lophotrochozoa\n"
                                  "\t毛顎動物門 Chaetognatha\n")

    def on_enter_chordata(self, update):
        update.message.reply_text("脊索動物門 Chordata:\n"
                                  "\t哺乳綱 Mammalia\n"
                                  "\nUnder Construction:\n"
                                  "\t盾皮魚綱 Placodermi\n"
                                  "\t軟骨魚綱 Chondrichthyes\n"
                                  "\t棘魚綱 Acanthodii\n"
                                  "\t硬骨魚綱 Osteichthyes\n"
                                  "\t兩生綱 Amphibia\n"
                                  "\t鳥綱 Aves\n")

    def on_enter_mammalia(self, update):
        update.message.reply_text("哺乳綱 Mammalia:\n"
                                  "\t靈長目 Primates\n"
                                  "\nUnder Construction:\n"
                                  "\t三尖齒獸目 Triconodonta\n"
                                  "\t美洲有袋目 Ameridelphia\n"
                                  "\t澳洲有袋目 Australidelphia\n"
                                  "\t非洲獸目 Afrotheria\n"
                                  "\t勞亞獸目 Laurasiatheria\n"
                                  "\t異關節目 Xenarthra\n")

    def on_enter_primates(self, update):
        update.message.reply_text("靈長目 Primates:\n"
                                  "\t人科 Hominidae\n"
                                  "\nUnder Construction:\n"
                                  "\t鼠狐猴科 Cheirogaleidae\n"
                                  "\t狐猴科 Lemuridae\n"
                                  "\t嬉猴科 Lepilemuridae\n"
                                  "\t大狐猴科 Indriidae\n"
                                  "\t指猴科 Daubentoniidae\n"
                                  "\t懶猴科 Lorisidae\n"
                                  "\t嬰猴科 Galagidae\n"
                                  "\t眼鏡猴科 Tarsiidae\n"
                                  "\t捲尾猴科 Cebidae\n"
                                  "\t青猴科 Aotidae\n"
                                  "\t僧面猴科 Pitheciidae\n"
                                  "\t蜘蛛猴科 Atelidae\n"
                                  "\t猴科 Cercopithecidae\n"
                                  "\t長臂猿科 Hylobatidae\n")

    def on_enter_hominidae(self, update):
        update.message.reply_text("人科 Hominidae:\n"
                                  "\t人屬 Homo\n"
                                  "\nUnder Construction:\n"
                                  "\t猩猩屬 Pongo\n"
                                  "\t大猩猩屬 Gorilla\n"
                                  "\t黑猩猩屬 Pan\n")

    def on_enter_homo(self, update):
        update.message.reply_text("人屬 Homo:\n"
                                  "\t智人 H. sapiens\n"
                                  "\nUnder Construction:\n"
                                  "\t魯道夫人 H. rudolfensis\n"
                                  "\t巧人 H. habilis\n"
                                  "\t直立人 H. erectus\n"
                                  "\t先驅人 H. antecessor\n"
                                  "\t匠人 H. ergaster\n"
                                  "\t海德堡人 H. heidelbergensis\n"
                                  "\t羅德西亞人 H. rhodesiensis\n"
                                  "\t西布蘭諾人 H. cepranensis\n"
                                  "\t格魯及亞人 H. georgicus\n"
                                  "\t豪登人 H. gautengensis\n"
                                  "\t納勒迪人 H. naledi\n"
                                  "\t尼安德塔人 H. neanderthalensis\n"
                                  "\t佛羅勒斯人 H. floresiensis\n"
                                  "\t泰昌人 H. tsaichangensis\n")

    def on_enter_sapiens(self, update):
        update.message.reply_text("人種(智人) H. Sapiens\n\n"
                                  "Human, that's you and me!")
        self.go_back(update)

    def on_enter_plantae(self, update):
        update.message.reply_text("植物界 Plantae\n"
                                  "\t被子植物門 Angiosperms\n"
                                  "\nUnder Construction:\n"
                                  "\t輪藻門 Charophyta\n"
                                  "\t綠藻門 Chlorophyta\n"
                                  "\t地錢門 Marchantiophyta\n"
                                  "\t角苔門 Anthocerotophyta\n"
                                  "\t苔蘚植物門 Bryophyta\n"
                                  "\t萊尼蕨門 Rhyniophyta\n"
                                  "\t工蕨門 Zosterophyllophyta\n"
                                  "\t石松門 Lycopodiophyta\n"
                                  "\t三向蕨門 Trimerophytophyta\n"
                                  "\t蕨類植物門 Pteridophyta\n"
                                  "\t前裸子植物門 Progymnospermophyta\n"
                                  "\t種子蕨門 Pteridospermatophyta\n"
                                  "\t松柏門 Pinophyta\n"
                                  "\t蘇鐵門 Cycadophyta\n"
                                  "\t銀杏門 Ginkgophyta\n"
                                  "\t買麻藤門 Gnetophyta\n")

    def on_enter_angiosperms(self, update):
        update.message.reply_text("被子植物門 Angiosperms:\n"
                                  "\t無患子目 Sapindales\n"
                                  "\nUnder Construction:\n"
                                  "\t無油樟目 Amborellaceae\n"
                                  "\t金粟蘭目 Chloranthaceae\n"
                                  "\t睡蓮目 Nymphaeaceae\n"
                                  "\t木蘭藤目 Austrobaileyales\n"
                                  "\t金魚藻目 Ceratophyllales\n"
                                  "\t白桂皮目 Canellales\n"
                                  "\t樟目 Laurales\n"
                                  "\t木蘭目 Magnoliales\n"
                                  "\t胡椒目 Piperales\n"
                                  "\t山龍眼目 Proteales\n"
                                  "\t毛茛目 Ranunculales\n"
                                  "\t洋二仙草目 Gunnerales\n"
                                  "\t石竹目 Caryophyllales\n"
                                  "\t檀香目 Santalales\n"
                                  "\t虎耳草目 Saxifragales\n"
                                  "\t葫蘆目 Cucurbitales\n"
                                  "\t豆目 Fabales\n"
                                  "\t殼斗目 Fagales\n"
                                  "\t金虎尾目 Malpighiales\n"
                                  "\t酢漿草目 Oxalidales\n"
                                  "\t薔薇目 Rosales\n"
                                  "\t白花菜目 Brassicales\n"
                                  "\t錦葵目 Malvales\n"
                                  "\t山茱萸目 Cornales\n"
                                  "\t杜鵑花目 Ericales\n"
                                  "\t絞木目 Garryales\n"
                                  "\t龍膽目 Gentianales\n"
                                  "\t唇形目 Lamiales\n"
                                  "\t茄目 Solanales\n"
                                  "\t傘形目 Apiales\n"
                                  "\t冬青目 Aquifoliales\n"
                                  "\t菊目 Asterales\n")

    def on_enter_sapindales(self, update):
        update.message.reply_text("無患子目 Sapindales:\n"
                                  "\t漆樹科 Anacardiaceae\n"
                                  "\nUnder Construction:\n"
                                  "\t熏倒牛科 Biebersteiniaceae\n"
                                  "\t白刺科 Nitrariaceae\n"
                                  "\t四合椿科 Kirkiaceae\n"
                                  "\t橄欖科 Burseraceae\n"
                                  "\t無患子科 Sapindaceae\n"
                                  "\t芸香科 Rutaceae\n"
                                  "\t苦木科 Simaroubaceae\n"
                                  "\t楝科 Meliaceae\n")

    def on_enter_anacardiaceae(self, update):
        update.message.reply_text("漆樹科 Anacardiaceae:\n"
                                  "\t芒果屬 Mangifera\n"
                                  "\nUnder Construction:\n"
                                  "\t腰果屬 Anacardium\n"
                                  "\t波漆屬 Bouea\n"
                                  "\t山檨子屬 Buchanania\n"
                                  "\t坎諾漆屬 Campnosperma\n"
                                  "\t南酸棗屬 Choerospondias\n"
                                  "\t黃櫨屬 Cotinus\n"
                                  "\t人面子屬 Dracontomelon\n"
                                  "\t辛果漆屬 Drimycarpus\n"
                                  "\t藤漆屬 Pegia\n"
                                  "\t黃連木屬 Pistacia\n"
                                  "\t鹽膚木屬 Rhus\n"
                                  "\t肖乳香屬 Schinus\n"
                                  "\t肉托果屬 Semecarpus\n"
                                  "\t檳榔青屬 Spondias）\n"
                                  "\t漆屬 Toxicodendron\n"
                                  "\t厚皮樹屬 Lannea\n")

    def on_enter_mangifera(self, update):
        update.message.reply_text("杧果屬 Mangifera:\n"
                                  "\t芒果 M. indica\n")

    def on_enter_indica(self, update):
        update.message.reply_text("芒果 M. Indica\n"
                                  "\nSweet!")
        self.go_back(update)

    def on_enter_bacteria(self, update):
        update.message.reply_text("細菌界 Bacteria:\n"
                                  "\t厚壁菌門 Firmicutes\n"
                                  "\nUnder Construction:\n"
                                  "\t放線菌門 Actinobacteria\n"
                                  "\t產水菌門 Aquificae\n"
                                  "\t梭桿菌門 Fusobacteria\n"
                                  "\t芽單胞菌門 Gemmatimonadetes\n"
                                  "\t變形菌門 Proteobacteria\n"
                                  "\t螺旋體門 Spirochaetes\n"
                                  "\t酸桿菌門 Acidobacteria\n"
                                  "\t綠彎菌門 Chloroflexi\n"
                                  "\t產金菌門 Chrysiogenetes\n"
                                  "\t藍藻門 Cyanobacteria\n"
                                  "\t脫鐵桿菌門 Deferribacteres\n"
                                  "\t網團菌門 Dictyoglomi\n"
                                  "\t熱脫硫桿菌門 Thermodesulfobacteria\n"
                                  "\t熱袍菌門 Thermotogae\n")

    def on_enter_firmicutes(self, update):
        update.message.reply_text("厚壁菌門 Firmicutes:\n"
                                  "\t芽孢桿菌綱 Bacilli\n"
                                  "\nUnder Construction:\n"
                                  "\t丹毒絲菌綱（Erysipelotrichia\n"
                                  "\t柔膜菌綱（Mollicutes\n")

    def on_enter_bacilli(self, update):
        update.message.reply_text("芽孢桿菌綱 Bacilli:\n"
                                  "\t乳桿菌目 Lactobacillales\n"
                                  "\nUnder Construction:\n"
                                  "\t芽孢桿菌目 Bacillales\n")

    def on_enter_lactobacillales(self, update):
        update.message.reply_text("乳桿菌目 Lactobacillales:\n"
                                  "\t乳桿菌科 Lactobacillaceae\n"
                                  "\nUnder Construction:\n"
                                  "\tAcetoanaerobium\n"
                                  "\tAerococcaceae\n"
                                  "\tCarnobacteriaceae\n"
                                  "\tEnterococcaceae\n"
                                  "\tLeuconostocaceae\n"
                                  "\tStreptococcaceae\n")

    def on_enter_lactobacillaceae(self, update):
        update.message.reply_text("乳桿菌科 Lactobacillaceae:\n"
                                  "\t乳桿菌屬 Lactobacillus\n"
                                  "\nUnder Construction:\n"
                                  "\tAlloiococcus\n"
                                  "\tParalactobacillus\n"
                                  "\tPediococcus\n"
                                  "\tSharpea\n")

    def on_enter_lactobacillus(self, update):
        update.message.reply_text("乳桿菌屬 Lactobacillus:\n"
                                  "\t嗜酸乳酸桿菌 L. acidophilus\n"
                                  "\nUnder Construction:\n"
                                  "\t短乳酸桿菌（L. brevis\n"
                                  "\t乾酪乳酸桿菌 L. casei\n"
                                  "\t德氏乳酸桿菌 L. delbrueckii\n"
                                  "\t鼠李糖乳桿菌 L. rhamnosus\n"
                                  "\t唾液乳桿菌 L. salivarius\n")

    def on_enter_acidophilus(self, update):
        update.message.reply_text("嗜酸乳桿菌 L. Acidophilus\n"
                                  "\nMake more cheese and yogurt!")
        self.go_back(update)

    def on_exit_animalia(self, update):
        print('exit animalia')

    def on_exit_plantae(self, update):
        print('exit plantae')

    def on_exit_bacteria(self, update):
        print('exit bacteria')
