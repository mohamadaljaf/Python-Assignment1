import sound
import a1

def three_samples():
  '''Return a new sound with three samples.'''
  
  snd = sound.create_sound (3)
  sample = sound.get_sample (snd, 0)
  sound.set_left (sample, 1010)
  sound.set_right (sample, 80)
  sample = sound.get_sample (snd, 1)
  sound.set_left (sample, 1500)
  sound.set_right (sample, -4200)
  sample = sound.get_sample (snd, 2)
  sound.set_left (sample, -65)
  sound.set_right (sample, 28132)
  return snd

def three_samples_rem_vocals():
  '''Return a new sound to which vocal-removal has been applied.'''
  
  snd = sound.create_sound (3)
  sample = sound.get_sample (snd, 0)
  sound.set_left (sample, 465)
  sound.set_right (sample, 465)
  sample = sound.get_sample (snd, 1)
  sound.set_left (sample, 2850)
  sound.set_right (sample, 2850)
  sample = sound.get_sample (snd, 2)
  sound.set_left (sample, -14098)
  sound.set_right (sample, -14098)
  return snd

def four_samples():
  '''Return a new sound with four samples.'''
  
  snd = sound.create_sound (4)
  sample = sound.get_sample (snd, 0)
  sound.set_left (sample, 1010)
  sound.set_right (sample, 80)
  sample = sound.get_sample (snd, 1)
  sound.set_left (sample, 1500)
  sound.set_right (sample, -4200)
  sample = sound.get_sample (snd, 2)
  sound.set_left (sample, 65)
  sound.set_right (sample, 28132)
  sample = sound.get_sample (snd, 3)
  sound.set_left (sample, 150)
  sound.set_right (sample, 150)  
  return snd

def four_samples_fade_in():
  '''Return a new sound to which a fade-in has been applied.'''
  
  snd = sound.create_sound (4)
  sample = sound.get_sample (snd, 0)
  sound.set_left (sample, 0)
  sound.set_right (sample, 0)
  sample = sound.get_sample (snd, 1)
  sound.set_left (sample, 375)
  sound.set_right (sample, -1050)
  sample = sound.get_sample (snd, 2)
  sound.set_left (sample, 32)
  sound.set_right (sample, 14066)
  sample = sound.get_sample (snd, 3)
  sound.set_left (sample, 112)
  sound.set_right (sample, 112)
  return snd

def four_samples_fade_out():
  '''Return a new sound to which fade-out has been applied.'''
  
  snd = sound.create_sound (4)
  sample = sound.get_sample (snd, 0)
  sound.set_left (sample, 757)
  sound.set_right (sample, 60)
  sample = sound.get_sample (snd, 1)
  sound.set_left (sample, 750)
  sound.set_right (sample, -2100)
  sample = sound.get_sample (snd, 2)
  sound.set_left (sample, 16)
  sound.set_right (sample, 7033)
  sample = sound.get_sample (snd, 3)
  sound.set_left (sample, 0)
  sound.set_right (sample, 0)
  return snd

def four_samples_fade():
  '''Return a new sound to which fade has been applied.'''
  
  snd = sound.create_sound (4)
  sample = sound.get_sample (snd, 0)
  sound.set_left (sample, 0)
  sound.set_right (sample, 0)
  sample = sound.get_sample (snd, 1)
  sound.set_left (sample, 750)
  sound.set_right (sample, -2100)
  sample = sound.get_sample (snd, 2)
  sound.set_left (sample, 32)
  sound.set_right (sample, 14066)
  sample = sound.get_sample (snd, 3)
  sound.set_left (sample, 0)
  sound.set_right (sample, 0)
  return snd

def four_samples_left_to_right():
  '''Return a new sound to which panning has been applied.'''
  
  snd = sound.create_sound (4)
  sample = sound.get_sample (snd, 0)
  sound.set_left (sample, 757)
  sound.set_right (sample, 0)
  sample = sound.get_sample (snd, 1)
  sound.set_left (sample, 750)
  sound.set_right (sample, -1050)
  sample = sound.get_sample (snd, 2)
  sound.set_left (sample, 16)
  sound.set_right (sample, 14066)
  sample = sound.get_sample (snd, 3)
  sound.set_left (sample, 0)
  sound.set_right (sample, 112)
  return snd

sound.play(four_samples_fade_in())