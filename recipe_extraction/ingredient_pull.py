import nltk, nltk.data, nltk.tag
import sys, pdb
class init(object):
    #This function sets the variables and initializes the n-gram taggers.
    def __init__(self):
        self._UNIGRAM_TRAIN_SETS=[
            [
                ("teaspoon", "QT"),
                ("tablespoon", "QT"),
                ("lbs", "QT"),
                ("g", "QT"), 
                ("grams", "QT"),
                ("pounds", "QT"),
                ("cups", "QT"),
                ("whole", "QT"),
                ("chopped", "QT"),
                ("medium", "QT"),
                ("size", "QT"),
                #ingredients
                ("flour", "ING"),
                ("water", "ING"),
                ("salt", "ING"),
                ("sugar", "ING"),
                ("pepper", "ING"),
                ("oil","ING"),
                ("beef", "ING"),
                ("butter", "ING"),
                ("mushrooms", "ING"), 
                ("onions", "ING"),
                ("wine", "ING"),
                ("stock","ING"),
                ("chives", "ING"),
                ("paneer", "ING"),
                ("capsicum", "ING"),
                ("ghee", "ING"), 
                ("tomatoes", "ING"), 
                ("coriander", "ING"),
                ("chillies", "ING"),
                ("garlic", "ING"),
                ("ginger", "ING"),
                ("fenugreek", "ING"),
                ("red", "ING"),
                ("green", "ING"),
                ("yellow", "ING"),
                ("Avocadoes", "ING"),
                ("Beans", "ING"),
                ("Cheese", "ING"),
                ("chipotles", "ING"),
                ("chocolate", "ING"),
                ("limes", "ING"),
                ("oregano", "ING"),
                ("pickles", "ING"),
                ("limes", "ING"),
                ("lemon", "ING"),
                ("tomatoes", "ING"),
                ("bell pepper", "ING"),
                ("capsicum", "ING"),
                ("eggplant", "ING"),
                ("lentils", "ING"),
                ("basil", "ING"),
                ("thyme", "ING"),
                ("Parsley", "ING"),
                ("Mint", "ING"),
                ("rosemary", "ING"),
                ("sage", "ING"),
                ("chives", "ING"),
                ("dill", "ING"),
                ("cilantro", "ING"),
                ("Tarragon", "ING"),
                ("saffron", "ING"),
                ("cardamom", "ING"),
                ("cinnamon", "ING"),
                ("cloves", "ING"),
                ("cumin", "ING"),
            ]
        ]
        self._BIGRAM_TRAIN_SETS = [
            [("coriander","ING"), ("seeds", "ING")],
            [("garlic","ING" ), ("paste", "ING")],
            [("green", "ING"), ("chillies", "ING")],
            [("chopped", "ING"), ("ginger", "ING")], 
            [("fenugreek", "ING"), ("leaves", "ING")],
            [("size", "ING"), ("tomatoes", "ING")],
            [("red","ING"), ("chillies", "ING")],
        ]
        self._TRIGRAM_TRAIN_SETS = [
            [("whole", "ING"), ("red","ING"), ("chillies", "ING")],
            [("chopped", "ING"), ("green", "ING"), ("chillies", "ING")],
            [("medium", "ING"), ("size", "ING"), ("tomatoes", "ING")],

        ]
        self._default_tagger = nltk.data.load(nltk.tag._POS_TAGGER)
        self._uni_tagger = nltk.UnigramTagger(self._UNIGRAM_TRAIN_SETS, backoff=self._default_tagger)
        self._bi_tagger = nltk.BigramTagger(self._BIGRAM_TRAIN_SETS, backoff=self._uni_tagger)
        self._tri_tagger = nltk.TrigramTagger(self._TRIGRAM_TRAIN_SETS, backoff=self._bi_tagger)
    
    # This function is the default nltk pos_tag
    def my_pos_tag(self, sentence):
        """Insert the Sentence you want tagged according to the ingredient(ING) and measurement(QT)"""
        self._pos_sentence = sentence
        return nltk.pos_tag(nltk.word_tokenize(self._pos_sentence))
    
    #This function is my customized unigram tagger.
    def my_unigram_tag(self, sentence):
        self._uni_sentence = sentence
        return self._uni_tagger.tag(nltk.word_tokenize(self._uni_sentence))
    
    #This function is my customized bigram tagger.
    def my_bigram_tag(self, sentence):
        self._bi_sentence = sentence
        return self._bi_tagger.tag(nltk.word_tokenize(self._bi_sentence))
    
    #This function is my customized trigram tagger.
    def my_trigram_tag(self, sentence):
        self._tri_sentence = sentence
        return self._tri_tagger.tag(nltk.word_tokenize(self._tri_sentence))
    
    #this function parses the tagged content and returns the output.
    def chunk(self, tagged_list):
        """Insert already the tagged list you receive from the tag function. This will chunk the ingredient entities."""
        self._tagged_list = tagged_list
        self._grammar = """NG : {<CD><QT>?<IN>?<ING>*}
                            NG : {<ING>*<CD>?<QT>?}
                            NG : {<CD><QT>*?<IN>?<ING>*}
                            NG : {<CD><NN>?<VBD>?<ING>*}"""
                            #{<ING>.*<CD><QT>}
                            #{<LS><QT>.*<ING>}
                            #{<LS><``><CD><QT>.*<ING>}
                            #{<CD><``><CD><QT>.*<ING>}
                            #{<LS><``><LS><QT>.*<ING>}
                            #{<CD><``><LS><QT>.*<ING>}
                            #{<LS><QT>?.*<ING>}
        self._cp = nltk.RegexpParser(self._grammar)
        return self.output(self._cp.parse(self._tagged_list))
    
    #collection of all functions to handle files
    def get_ingredients_file(self, filename, tagger='trigram'):
        self._filename = filename
        self._file_tagger = tagger
        self._file = open(self._filename)
        self._file_recipe = self._file.read()
        if self._file_tagger == 'bigram':
            self._file_tagged = self.my_bigram_tag(self._file_recipe)
        elif self._file_tagger == 'unigram':
            self._file_tagged = self.my_unigram_tag(self._file_recipe)
        elif self._file_tagger == 'trigram':
            self._file_tagged = self.my_trigram_tag(self._file_recipe)
        self._file_ingredients = self.chunk(self._file_tagged)
        return self._file_ingredients
        print (self._file_ingredients)
    
    #this is the collection of all funtions to handle string input.
    def get_ingredients_string(self, recipe, tagger="trigram"):
        self._string_recipe = recipe
        self._string_tagger = tagger
        if self._string_tagger == 'bigram':
            self._string_tagged = self.my_bigram_tag(self._string_recipe)
        elif self._string_tagger == 'unigram':
            self._string_tagged = self.my_unigram_tag(self._string_recipe)
        elif self._string_tagger == 'trigram':
            self._string_tagged = self.my_trigram_tag(self._string_recipe)
        self._string_ingredients = self.chunk(self._string_tagged)
        return self._string_ingredients
    
    # this is the output function that returns the printed content.
    def output(self, tree): 
        self.ingredients = []
        self._tree = tree
        self._subtrees = []
        for subtree in self._tree.subtrees():
            self._subtrees.append(subtree.leaves())
        self._subtrees.remove(self._subtrees[0])
        for o in self._subtrees:
            if len(o) > 2: 
                self.ingredients.append([u[0] for u in o])
        self._final_output = """
            """
        for ing in self.ingredients:
            for ou in ing:
                self._final_output += ou + " "
            self._final_output += """,
            """
        return self._final_output