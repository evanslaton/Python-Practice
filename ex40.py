class Song(object):

  def __init__(self, lyrics):
    self.lyrics = lyrics
  
  def sing_me_a_song(self):
    for line in self.lyrics:
      print(line)
  
  def number_of_lines(self):
    print(len(self.lyrics))

happy_bday = Song(["Happy birthday to you",
                   "I don't want to set sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["they rally around that family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
happy_bday.number_of_lines()

bulls_on_parade.sing_me_a_song()
bulls_on_parade.number_of_lines()