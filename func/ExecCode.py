import subprocess

def ExecCode(code:str):
    code = "from Genration_Of_Images import Generate_Images , Show_Image\nfrom func.SpeakOffline import Speak\n"+code
    code = code.replace("print", "Speak")

    with open(r"temp.py", "w") as f:
        f.write(code)
    
    subprocess.getoutput("python temp.py 2> error.log")

    with open(r"error.log", "r") as f:
        res = f.read()
        if res != "":
            return False
        else:
            return True
        
