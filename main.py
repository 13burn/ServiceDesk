
import threading
import eel
from cefpython3 import cefpython as cef
from time import sleep
#TODO: separate ell and cef modules to their own files... maybe just eel
def eel_start():
    eel.init("web")

    @eel.expose                         # Expose this function to Javascript
    def say_hello_py():
        print('Hello from Python World!')

    eel.start('index.html', mode=False, port=8080, disable_cache=True) #cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])
    
    
def cef_start():
    cef.Initialize()
    cef.CreateBrowserSync(url="http://127.0.0.1:8080", window_title="ok")
    cef.MessageLoop()


if __name__ == '__main__':
    t1 = threading.Thread(target=cef_start)
    t1.start()
    if t1.isAlive:
        eel_start()