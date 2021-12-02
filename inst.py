import os
from time import sleep, gmtime, strftime
from tkinter import ttk
from datetime import datetime
import tk as tk
import keys_storage
import test
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
a = None

class Th(Thread):
    _instance = None
    def __init__(self, is_loop=True):
        Thread.__init__(self)
        self.is_loop = is_loop
        self.already_started = False
        self.is_schedule = True
        self.set_scizor = False
        self.set_fish = False

    @classmethod
    def instance(self):
        if self._instance is None:
            self._instance = self()
        return self._instance

    def stop(self):
        self.is_loop = False
        return

    def get_loop(self):
        return self.is_loop

    def init(self):
        self.is_loop = True
        return

    def set_already_run(self, boolean):
        self.already_started = boolean
        return

    def already_run(self):
        return self.already_started

    def setFisher(self):
        if self.is_loop:
            test.PressKey(keys_storage.key["CAPS"])
            sleep(0.5)
            test.ReleaseKey(keys_storage.key["CAPS"])

    def logout(self):
        test.PressKey(keys_storage.key['CTROL'])
        sleep(0.5)
        test.PressKey(keys_storage.key['L'])
        sleep(0.5)
        test.ReleaseKey(keys_storage.key['CTROL'])
        sleep(0.5)
        test.ReleaseKey(keys_storage.key['L'])
        sleep(0.5)
        test.PressKey(keys_storage.key['ENTER'])
        sleep(0.5)
        test.ReleaseKey(keys_storage.key['ENTER'])
        print('logout', datetime.now())

    
    def schedule(self):
        if self.is_schedule:
            if datetime.now().strftime('%H:%M') == '08:10':
                self.set_scizor = False
                self.set_fish = False
                self.is_schedule = False
                test.PressKey(keys_storage.key["ENTER"])
                sleep(0.8)
                test.ReleaseKey(keys_storage.key["ENTER"])
                sleep(25)
                test.PressKey(keys_storage.key["ENTER"])
                sleep(0.8)
                test.ReleaseKey(keys_storage.key["ENTER"])
                sleep(1.8)
                while self.set_scizor == False:
                    scizor = pyautogui.locateOnScreen('scizor.png', confidence=0.90)
                    if scizor != None:
                        self.set_scizor = True
                        x, y = pyautogui.center(scizor)   
                        pyautogui.moveTo(x, y)
                        pyautogui.rightClick(x, y)
                while self.set_fish == False:
                    isca = pyautogui.locateOnScreen('isca.png', confidence=0.90)
                    if isca != None:
                        self.set_fish = True
                        x, y = pyautogui.center(isca)   
                        pyautogui.moveTo(x, y)
                        pyautogui.click(x, y)
                self.setFisherClick()

    def setFisherClick(self):
        if self.is_loop:
            sleep(0.8)
            test.PressKey(keys_storage.key["CAPS"])
            sleep(0.8)
            test.ReleaseKey(keys_storage.key["CAPS"])
            pyautogui.moveTo(valor[0], valor[1])
            pyautogui.click(valor[0], valor[1])

    def atack(self):
        # atacks = Lb1.get(0, last=Lb1.size())
        # for atack in atacks:
        for atack in ['F8', 'F6', 'F4', 'F3']:
            if self.is_loop:
                test.PressKey(keys_storage.key[atack])
                sleep(0.5)
                test.ReleaseKey(keys_storage.key[atack])
                sleep(1)

    def msg(self, text, delay):
        pyautogui.write(text)
        sleep(delay)
        test.PressKey(keys_storage.key['ENTER'])
        sleep(0.5)
        test.ReleaseKey(keys_storage.key['ENTER'])

    def pokeball(self, hotkey, location):
        test.PressKey(keys_storage.key[hotkey])
        sleep(0.5)
        test.ReleaseKey(keys_storage.key[hotkey])
        sleep(0.5)
        x, y = pyautogui.center(location)   
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y)
        data = datetime.now()
        print('pokebola vai!!', hotkey, data)

    def delay_to_start(self, delay):
        print('preparando')
        sleep(delay)
        print('go')
        self.init()

    def run(self):
      self.delay_to_start(0.5)
      while (self.get_loop()):
        # self.schedule()
        bubble = pyautogui.locateOnScreen('target_fish.png', confidence=0.92, region=(valor[0], valor[1], 50, 50))
        # anchor = pyautogui.locateOnScreen('anchor.png', confidence=0.83, region=(1039, 500, 73, 81))
        # if anchor == None:
        #     break
        if bubble != None and self.is_loop != False:
            self.setFisher()
            self.setFisherClick()
            self.atack()
            for i in range(25):
                shiny_crabby = pyautogui.locateOnScreen('scrabby.png', confidence=0.88)
                if shiny_crabby != None and self.is_loop != False:
                    self.pokeball('NUNLOCK', shiny_crabby)
                    print('shiny_crabby', shiny_crabby)
                    break
            for i in range(25):
                shiny_tenta = pyautogui.locateOnScreen('shiny_tenta.png', confidence=0.95)
                if shiny_tenta != None and self.is_loop != False:
                    self.pokeball('BACKSPACE', shiny_tenta)
                    print('shiny_tenta', shiny_tenta)
                    break
    #   self.msg('????', 1)
    #   self.msg('to pescando e trabalhando aqui', 1.5)
    #   self.msg('vou precisar sair ja volto ae', 1.3)
    #   self.logout()



def on_press(event, timeout, a):
    print("Started thread but waiting for event...")
    event_set = event.wait(timeout)
    print('event', event_set)
    if event_set:
        a.stop()
        a.set_already_run(True)
    else:
        a.stop()



def press(key):
    if key == keyboard.Key.esc:      
        e.set()
        janela.deiconify()
        # listener.join()
        return
listener = keyboard.Listener(on_press=press)
print('listener', listener)
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
    janela.withdraw()
    a = Th(True).instance()
    if not a.instance().already_run():
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
        "F1",
        "F2",
        "F3",
        "F4",
        "F5",
        "F6",
        "F7",
        "F8",
        "F9",
        "F10",
        "F11",
        "F12"]
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
                                    "F1",
                                    "F2",
                                    "F3",
                                    "F4",
                                    "F5",
                                    "F6",
                                    "F7",
                                    "F8",
                                    "F9",
                                    "F10",
                                    "F11",
                                    "F12"]
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
