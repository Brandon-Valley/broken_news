import uberduckapi as ud
import os
my_duck = ud.UberDuck(os.environ['UBERDUCK_Key'], os.environ['UBERDUCK_Secret'])
# sponge = my_duck.get_voice('fish-head', "Breaking news! Hey everyone I'm alive")
# sponge = my_duck.get_voice('fish-head', "test test test ... ... ... Breaking news! Russian customs officials said they had detained a star American basketball player after finding hashish oil in her luggage at an airport near Moscow. The Russian news agency has identified the player as Brittney Griner.")
sponge = my_duck.get_voice('fish-head', "... Breaking news! Russian customs officials said they had detained a star American basketball player after finding hashish oil in her luggage at an airport near Moscow. ... ... The Russian news agency has identified the player as Brittney Griner.")

# if the request went through
if sponge:
    # sponge.play_voice()
    sponge.save('fish.mp4') # also works with .wav
    
    
print('done')