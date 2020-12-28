from moviepy.editor import *
import pygame

def p():
    clip = VideoFileClip(r"ДЛЯ ЗАСТАВКИ.mp4")
    clip.preview()
    pygame.display.quit()