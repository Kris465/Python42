class Film:
    def __init__(self, name, genre, duration: int, regiccer, main_actor):
        self.name = name
        self.genre = genre
        self.duration = duration
        self.regiccer = regiccer
        self.main_actor = main_actor
    
    def play(self):
        return 'меняются кадры, испытываются эмоции, раскрывается драмматургия: мы смотрим фильм'
    
# film_hisnik = Film('Hishnik', 'triller', 90, 'Stiven_Spilberg', 'Arnold_Schwarzenegger')
# print(film_hisnik.play(), film_hisnik.name, f'а все потому что это {film_hisnik.genre} и в главной роли там {film_hisnik.main_actor}')

class Cinematograf(Film): # подумать)
    def __init__(self, name, genre, duration, regiccer, main_actor):
        super().__init__(name, genre, duration, regiccer, main_actor)
    
    def play(self):
        return 'меняются жанры, собирательные образыглавных героев, драмматургия принимает новые формы и вилки событий, мы имеем дело с развитием кинемотографа: '

cinema_alens_vs_predator = Cinematograf('alens_vs_predator', 'triller_2', 120, 'Stiven_Spilberg', 'Aaaay_Arnold_!')
print(cinema_alens_vs_predator.play(), cinema_alens_vs_predator.name, f'а все потому что это {cinema_alens_vs_predator.genre} и в главной роли там {cinema_alens_vs_predator.main_actor}')

# class Cinema:
    

