from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

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
        update.message.reply_text("enter animalia")
        self.go_back(update)

    def on_exit_animalia(self, update):
        print('exit animalia')

    def on_enter_plantae(self, update):
        update.message.reply_text("enter plantae")
        self.go_back(update)

    def on_exit_plantae(self, update):
        print('exit plantae')
