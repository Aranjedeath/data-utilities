import re

bad_words_raw = ['2g1c', '2 girls 1 cup', 'acrotomophilia', 'anal', 'anilingus', 'anus', 'arsehole', 'ass', 'asshole', \
 'assmunch', 'auto erotic', 'autoerotic', 'babeland', 'baby batter', 'ball gag', 'ball gravy', 'ball kicking', 'ball licking', \
  'ball sack', 'ball sucking', 'bangbros', 'bareback', 'barely legal', 'barenaked', 'bastardo', 'bastinado', 'bbw', 'bdsm', 'beaver cleaver', \
   'beaver lips', 'bestiality', 'bi curious', 'big black', 'big breasts', 'big knockers', 'big tits', 'bimbos', 'birdlock', 'bitch', 'black cock', \
    'blonde action', 'blonde on blonde action', 'blow j', 'blow your l', 'blue waffle', 'blumpkin', 'bollocks', 'bondage', 'boner', 'boob', 'boobs', \
    'booty call', 'brown showers', 'brunette action', 'bukkake', 'bulldyke', 'bullet vibe', 'bung hole', 'bunghole', 'busty', 'butt', 'buttcheeks', 'butthole', \
     'camel toe', 'camgirl', 'camslut', 'camwhore', 'carpet muncher', 'carpetmuncher', 'chocolate rosebuds', 'circlejerk', 'cleveland steamer', 'clit', 'clitoris', \
      'clover clamps', 'clusterfuck', 'cock', 'cocks', 'coprolagnia', 'coprophilia', 'cornhole', 'cum', 'cumming', 'cunnilingus', 'cunt', 'darkie', 'date rape', 'daterape', \
       'deep throat', 'deepthroat', 'dick', 'dildo', 'dirty pillows', 'dirty sanchez', 'dog style', 'doggie style', 'doggiestyle', 'doggy style', 'doggystyle', 'dolcett', \
        'domination', 'dominatrix', 'dommes', 'donkey punch', 'double dong', 'double penetration', 'dp action', 'eat my ass', 'ecchi', 'ejaculation', 'erotic', 'erotism', \
         'escort', 'ethical slut', 'eunuch', 'faggot', 'fecal', 'felch', 'fellatio', 'feltch', 'female squirting', 'femdom', 'figging', 'fingering', 'fisting', 'foot fetish', \
          'footjob', 'frotting', 'fuck', 'fuck you', 'fuck off', 'fuck of', 'fuckoff', 'fuck-off', 'fucker', 'fuck buttons', 'fudge packer', 'fudgepacker', 'futanari', 'g-spot', \
           'gang bang', 'gay sex', 'genitals', 'giant cock', 'girl on', 'girl on top', 'girls gone wild', 'goatcx', 'goatse', 'gokkun', 'golden shower', 'goo girl', 'goodpoop', \
            'goregasm', 'grope', 'group sex', 'guro', 'hand job', 'handjob', 'hard core', 'hardcore', 'hentai', 'homoerotic', 'honkey', 'hooker', 'hot chick', 'how to kill', \
             'how to murder', 'huge fat', 'humping', 'incest', 'intercourse', 'jack off', 'jail bait', 'jailbait', 'jerk off', 'jigaboo', 'jiggaboo', 'jiggerboo', 'jizz', 'juggs', \
              'kike', 'kinbaku', 'kinkster', 'kinky', 'knobbing', 'leather restraint', 'leather straight jacket', 'lemon party', 'lolita', 'lovemaking', 'make me come', 'male squirting', \
               'masturbate', 'menage a trois', 'milf', 'missionary position', 'motherfucker', 'mound of venus', 'mr hands', 'muff diver', 'muffdiving', 'nambla', 'nawashi', 'negro', \
                'neonazi', 'nig nog', 'nigga', 'nigger', 'nimphomania', 'nipple', 'nipples', 'nsfw images', 'nude', 'nudity', 'nympho', 'nymphomania', 'octopussy', 'omorashi', \
                 'one cup two girls', 'one guy one jar', 'orgasm', 'orgy', 'paedophile', 'panties', 'panty', 'pedobear', 'pedophile', 'pegging', 'penis', 'phone sex', \
                  'piece of shit', 'piss pig', 'pissing', 'pisspig', 'playboy', 'pleasure chest', 'pole smoker', 'ponyplay', 'poof', 'poop chute', 'poopchute', 'porn',  \
                  'porno', 'pornography', 'prince albert piercing', 'pthc', 'pubes', 'pussy', 'queaf', 'raghead', 'raging boner', 'rape', 'raping', 'rapist', 'rectum', \
                   'reverse cowgirl', 'rimjob', 'rimming', 'rosy palm', 'rosy palm and her 5 sisters', 'rusty trombone', 's&m', 'sadism', 'scat', 'schlong', 'scissoring', \
                   'semen', 'sex', 'sexo', 'sexy', 'shaved beaver', 'shaved pussy', 'shemale', 'shibari', 'shit', 'shota', 'shrimping', 'slanteye', 'slut', 'smut', 'snatch', \
                   'snowballing', 'sodomize', 'sodomy', 'spic', 'spooge', 'spread legs', 'strap on', 'strapon', 'strappado', 'strip club', 'style doggy', 'suck', 'sucks', \
                   'suicide girls', 'sultry women', 'swastika', 'swinger', 'tainted love', 'taste my', 'tea bagging', 'threesome', 'throating', 'tied up', 'tight white', \
                   'tit', 'tits', 'titties', 'titty', 'tongue in a', 'topless', 'tosser', 'towelhead', 'tranny', 'tribadism', 'tub girl', 'tubgirl', 'tushy', 'twat', 'twink', \
                   'twinkie', 'two girls one cup', 'undressing', 'upskirt', 'urethra play', 'urophilia', 'vagina', 'venus mound', 'vibrator', 'violet blue', 'violet wand', \
                   'vorarephilia', 'voyeur', 'vulva', 'wank', 'wet dream', 'wetback', 'white power', 'women rapping', 'wrapping men', 'wrinkled starfish', 'xx', 'xxx', 'yaoi', \
                   'yellow showers', 'yiffy', 'zoophilia', 'Lanza', 'Eric Harris', 'EricHarris', 'Dylan Klebold', 'DylanKlebold', 'Seung-Hui Cho', 'Seung-Hui-Cho', 'Seung Hui Cho', \
                   'SeungHuiCho', 'Nidal Malik Hasan', 'NidalMalik Hasan', 'Nidal MalikHasan', 'NidalMalikHasan', 'Jared Loughner', 'JaredLoughner', 'James Holmes', 'JamesHolmes', \
                   'James Eagan Holmes', 'JamesEganHolmes', 'Adam Lanza', 'AdamLanza', 'Dzhokar Tsarnaev', 'DzhokarTsarnaev', 'Tamerlan Tsarnaev', 'TamerlanTsarnaev', 'Tsarnaev', \
                   'Bin laden', 'Osama', 'Osama Bin Laden', 'Zawahiri', 'George Zimmerman', 'T.J. Lane', 'TJLane', 'TJ Lane', 'Anwar al-Awlaki', 'al-Awlaki', 'Awlaki', 'crooked', \
                   'national rifle association', 'ill-informed', 'Mayors Against All Gun', 'dictator', 'Obama', 'Barack', 'Bloomberg', 'Hillary Clinton', 'Wayne Lapierre', 'Joe Biden', \
                   'Blumburg', 'Bloomberg', 'Nanny Bloomberg', 'Nanny', 'Nannystate', 'Gunsdontkill', 'Peopledo', 'Guns', 'Gunsforall', 'Guns4all', 'Stalin', 'Mao', 'Lenin', \
                   'Hitler', 'Mussolini', 'Mugabe', 'Vlad', 'Kim Jong-Il', 'Jong-Il', 'Hirohito', 'Hirota', 'Brezhnev', 'Kai-shek', 'Wilhelm', 'Minh', 'Yakubu', 'Gowon', 'Saddam', \
                   'Charles Manson', 'Hussein', 'Nazi', 'elliot rodger', 'elliott rodger', 'isis']

super_bad_words = ['fuck', 'asshole', 'guns', 'amendment', 'pussy', 'grabbing', 'grabber', 'bloomberg', \
        'cunt', 'gangbanger', 'slut', 'kike', 'nigger', 'nigga', 'cocksucker', 'wingnut', 'dingleberry', 'ballsack', 'idiot', 'scumbag', 'death', 'knife', 'benghazi']

bad_words = set(map(lambda x: x.strip().lower(), bad_words_raw))

def blacklist(word, word_length=30):
    word = word.lower()
    if len(bad_words.intersection(set([word]))) > 0:
        result = True
    elif len(word.replace(' ', '')) > word_length:
        result = True
    else:
        try:
            unicode(word)
            for super_bad_word in super_bad_words:
                if word.find(super_bad_word) >= 0:
                    result = True
                    break
                else:
                    result = False
        except:
            result = True
    return result

def titlecase(row, first_name=0, last_name=1, address=2, city=3, state=4, zip=5):

    def zip_fill(zip):
        if zip == '':
            return ''
        elif len(zip) == 4:
            return zip.zfill(5)
        else:
            return zip

    new_row = [
        row[first_name].title(), row[last_name].title(), row[address].upper(), row[city].title(), row[state].upper(), zip_fill(row[zip])
    ] + row[zip+1:]

    return new_row

