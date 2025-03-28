class Film:
    def __init__(self, name, genre, duration: int, regiccer, main_actor):
        self.name = name
        self.genre = genre
        self.duration = duration
        self.regiccer = regiccer
        self.main_actor = main_actor
    
    def play(self):
        return 'меняются кадры, испытываются эмоции, раскрывается драмматургия: мы смотрим фильм'
    
film_hisnik = Film('Hishnik', 'triller', 90, 'Stiven_Spilberg', 'Arnold_Schwarzenegger')
print(film_hisnik.play(), film_hisnik.name, f'а все потому что это {film_hisnik.genre} и в главной роли там {film_hisnik.main_actor}')