######################################################################################
# Black Viper Table to Script Converter
#
# 1. Go to http://www.blackviper.com/service-configurations/ and select Configuration
# 2. Copy and paste Table into textfile "configuration.txt"
# 3. execute script in same folder
#
######################################################################################


filename = "configuration.txt"
with open(filename) as f:
  lis = [x.split("\t") for x in f]

info = [line for line in zip(*lis)]

for line in info[2:]:
    fileOutName = "%s - %s.ps1" % (filename.split(".")[0], line[0].replace("\n", ""))
    scriptOut = open(fileOutName, "w")
    for regEntry, mode in zip(info[1][1:], line[1:]):
        if mode.startswith("Manual"):
            mode = "Manual"
        if mode.startswith("Not Installed"):
            continue
        if mode.startswith("Automatic"):
            mode = "Automatic"
        if mode.startswith("Disabled"):
            mode = "Disabled"
        if mode.startswith("Uninstalled"):
            continue

        out = 'Set-Service "%s" -StartupType %s \n' % (regEntry, mode)
        scriptOut.write(out)
    scriptOut.close()