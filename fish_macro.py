import os
from time import sleep
from tkinter import ttk

import tk as tk
from pynput import keyboard
import pyautogui
from PIL import ImageTk, Image
from pynput import mouse
from tkinter import *
import PIL.Image
from threading import Thread
import threading
e = threading.Event()
valor = []


class Th(Thread):
    def __init__(self, is_loop=True):
        Thread.__init__(self)
        self.is_loop = is_loop

    def stop(self):
        self.is_loop = False
        return

    def get_stop(self):
        return self.is_loop

    def setFisher(self):
        if self.is_loop:
            pyautogui.keyDown('ctrl')
            pyautogui.press('z')
            pyautogui.keyUp('ctrl')
            sleep(0.5)

    def setFisherClick(self):
        if self.is_loop:
            pyautogui.keyDown('ctrl')
            pyautogui.press('z')
            pyautogui.keyUp('ctrl')
            pyautogui.moveTo(valor[0], valor[1])
            pyautogui.click(valor[0], valor[1])

    def atack(self):
        atacks = Lb1.get(0, last=Lb1.size())
        for atack in atacks:
            if self.is_loop:
                pyautogui.write(atack)
                pyautogui.press("ENTER")
                sleep(1)

    def run(self):
      print('oie', self.is_loop)
      while (self.is_loop):
        bubble = pyautogui.locateOnScreen('target_fish.png',confidence=0.80, region=(valor[0], valor[1], 50, 50))
        print(bubble)
        if bubble != None and self.is_loop != False:
            self.setFisher()
            self.atack()
            self.setFisherClick()
            pyautogui.moveTo(valor[0], valor[1], 1)
            pyautogui.click(valor[0], valor[1])


def on_press(event, timeout, a):
    print("Started thread but waiting for event...")
    event_set = event.wait(timeout)
    if event_set:
        print('eniejaotjao')
        a.stop()
    else:
        a.stop()


def press(key):
    print(key)
    if key == keyboard.Key.esc:
        e.set()
        janela.deiconify()
        # listener.join()
        print('key', key)
        return
listener = keyboard.Listener(on_press=press)
listener.start()  # start to listen on a separate thread


def create_fish_picture(mouseX, mouseY):
    format_x = mouseX - 25
    format_y = mouseY - 25
    myScreenshot = pyautogui.screenshot(region=(format_x, format_y, 50, 50))
    path = os.path.dirname(__file__) + '/target_fish.png'
    myScreenshot.save(path)
    open_img = PIL.Image.open(path)
    img = ImageTk.PhotoImage(open_img)
    lbl_path = Label(janela, image=img)
    lbl_path.image = img
    lbl_path.place(x=235, y=10)
    janela.deiconify()
    valor.append(format_x)
    valor.append(format_y)
    return myScreenshot

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        fish_image = create_fish_picture(x, y)

        return False

janela = Tk()

def getBubble():
    janela.withdraw()
    listener = mouse.Listener(
        on_click=on_click)
    listener.start()

def start():
    # janela.withdraw()
    a = Th(True)
    a.start()
    thread1 = threading.Thread(name='Event-Blocking-Thread', target=on_press, args=(e, 99999, a))
    thread1.start()

def set():
    list_select = Lb1.curselection()
    atack_current = combo_atacks.get()
    if (list_select == ()):
        Lb1.insert(END, atack_current)
        return
    Lb1.insert(list_select, atack_current)

def set_all():
    array =[
        "m1",
        "m2",
        "m3",
        "m4",
        "m5",
        "m6",
        "m7",
        "m8",
        "m9",
        "m10",
        "m11",
        "m12"]
    for i in array:
        Lb1.insert(END, i)

def del_atack():
    dele = Lb1.curselection()
    Lb1.delete(dele)

def del_all():
    for i in range(Lb1.size()):
        Lb1.delete(0)


combo_atacks = ttk.Combobox(janela,state='readonly',
                            values=[
                                    "m1",
                                    "m2",
                                    "m3",
                                    "m4",
                                    "m5",
                                    "m6",
                                    "m7",
                                    "m8",
                                    "m9",
                                    "m10",
                                    "m11",
                                    "m12"]
                                    )
combo_atacks.current(0)
combo_atacks.place(x=10, y=80, width=50)
Lb1 = Listbox(janela, selectmode=EXTENDED)
Lb1.place(x=100, y=80, width=50)
set_attack = Button(janela, font=("Arial Bold", 10), width=25, text="Set Attack", command=set)
set_attack.place(x=10, y=110, width=80)
set_all = Button(janela, font=("Arial Bold", 10), width=25, text="Set All", command=set_all)
set_all.place(x=10, y=140, width=80)
del_attack = Button(janela, font=("Arial Bold", 10), width=25, text="Del Attack", command=del_atack)
del_attack.place(x=10, y=170, width=80)
del_all = Button(janela, font=("Arial Bold", 10), width=25, text="Del All", command=del_all)
del_all.place(x=10, y=200, width=80)
bt_select_opt = Button(janela, font=("Arial Bold", 10), width=25, text="Select Bubble Fish Target", command=getBubble)
bt_select_opt.place(x=10, y=10)
bt_select_opt = Button(janela, font=("Arial Bold", 10), width=25, text="Start Fish", command=start)
bt_select_opt.place(x=10, y=48)


janela.geometry("300x250+250+250")
janela.mainloop()
