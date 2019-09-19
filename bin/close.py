# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Creado por: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# Main: Programa cierra el siestema.
import os
import signal
import shutil


PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
# Face
DIR_FACES = os.path.join(os.path.join(
    PATH_DIR, "recognizerVideo"), "recognizer")
DIR_FACES = os.path.join(os.path.join(DIR_FACES, "att_faces"), "tmp_faces")
# Temporal Face
DIR_IMAGES = os.path.join(PATH_DIR, "..")
DIR_IMAGES = os.path.join(DIR_IMAGES, "public")
DIR_IMAGES = os.path.join(DIR_IMAGES, "video")
DIR_IMAGES = os.path.join(DIR_IMAGES, "images")
# Dir temp
DIR_TMP = os.path.join(PATH_DIR, "tmp")
# Temporal process
PID_FILE = os.path.join(os.path.join(PATH_DIR, "tmp"), "mydaemon.PID")
# PID_FILE2 = os.path.join(os.path.join(PATH_DIR, "tmp"), "pass.PID")
# PID_FILE3 = os.path.join(os.path.join(PATH_DIR, "tmp"), "fin.PID")
# FILE_PROCESS = os.path.join(os.path.join(PATH_DIR, "tmp"), "process.PID")

pid = 1

def exist_pid(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True
try:
    if os.path.isfile(PID_FILE):
        pid = open(PID_FILE, "r").read()
        if exist_pid(int(pid)):
            os.kill(int(pid), signal.SIGTERM)
        os.unlink(PID_FILE)

    if os.path.isdir(DIR_TMP) != True:
        os.makedirs(DIR_TMP)
        os.makedirs(DIR_FACES)
        os.makedirs(DIR_IMAGES)
    else:
        shutil.rmtree(DIR_IMAGES)
        shutil.rmtree(DIR_FACES)
        shutil.rmtree(DIR_TMP)

        os.makedirs(DIR_TMP)
        os.makedirs(DIR_FACES)
        os.makedirs(DIR_IMAGES)
    # b print("Close All")
except Exception as e:
    print(e)
