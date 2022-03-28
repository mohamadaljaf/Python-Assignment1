import sound

def rem_vocals(snd):
    '''Return a copy of snd that contains no vocals'''
    
    new_snd = sound.copy(snd)
    
    for samp in new_snd:
        left = sound.get_left(samp)
        right = sound.get_right(samp)
        value = (left-right) / 2.0
        value = int(value)
        sound.set_right(samp, value)
        sound.set_left(samp, value)
    return new_snd

def fade_in(snd, fade_length):
    '''Return a copy of snd that fades in with
    fade length amount'''

    new_snd = sound.copy(snd)
    
    for samp in new_snd:
        index = sound.get_index(samp)
        value = (1.0 / fade_length) * index
        if index <= fade_length:
            sound.set_values(samp, int(value * sound.get_left(samp)), \
                                      int(value * sound.get_right(samp)))
    return new_snd

def fade_out(snd, fade_length):
    '''Return a copy of snd that fades out with
    fade length amount'''

    new_snd = sound.copy(snd)
    fade_init = 1.0 / fade_length
    fade_length = len(new_snd) - fade_length
    
    for samp in new_snd:
        index = sound.get_index(samp)
        if index >= fade_length:
            value = fade_init * (len(new_snd) - index)
            sound.set_values(samp, int(value * sound.get_left(samp)), \
                                      int(value * sound.get_right(samp)))
    return new_snd

def fade(snd, fade_length):
    '''Return a copy of snd that fades in and out with
    fade length amount'''
    
    new_snd = sound.copy(snd)
    new_snd = fade_in(new_snd, fade_length)
    new_snd = fade_out(new_snd, fade_length)
    
    return new_snd

def left_to_right(snd, pan_length):
    '''Return a copy of snd that fades out the left
    channel and fades in the right channel by
    fade length amount'''
    
    new_snd = sound.copy(snd)
           
    for samp in new_snd:
        index = sound.get_index(samp)
        if index <= pan_length:
            value_left = (1.0 / pan_length) * (pan_length - index)
            value_right = (1.0 / pan_length) * index                
            sound.set_values(samp, int(value_left * sound.get_left(samp)), \
                                      int(value_right * sound.get_right(samp)))            
    return new_snd

if __name__ == "__main__":
    snd = sound.load_sound("airplane.wav")
    sound.play(left_to_right(snd, 88200))