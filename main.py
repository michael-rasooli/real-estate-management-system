import os
import sys
import tkinter as tk
import classes as cl


def get_app_folder():
    if getattr(sys, "frozen", False):
     
        if sys.platform == "darwin" and ".app/Contents/MacOS" in sys.executable:
            return os.path.abspath(
                os.path.join(os.path.dirname(sys.executable), "../../..")
            )

        
        return os.path.dirname(sys.executable)

    
    return os.path.dirname(os.path.abspath(__file__))


app_folder = get_app_folder()
db_path = os.path.join(app_folder, "amlak.db")

db = cl.Database(db_path)
service = cl.ServiceLogic(db)

root = tk.Tk()
view = cl.View(root, service)

try:
    root.mainloop()
finally:
    db.close()