import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
host = "https://*****.server.co.za:5001/#/login"
user = "admin"
passwd = "whatever"
pbx_type = ""
ext = '1011'
mac = '805ec0bwwwwwww'
model = 'SIP-T23P'
def importerACS(mac,ext,model,host):
        #3: Open and read the text file and convert to a Python dictonary format that we can use to import into the ACS.
    ##We use pandas DataFrame to keep structure(colunms) required for importing
    export_dir = '/home/user/Documents/LocalDir/Client/extensions/Client-jhb'
    macs_dir = '/home/user/Documents/LocalDir/Client/macs'
    try:
        #self.export_dir = directory
        tmpl = 'yourtemplate.ph.xml'
        df = pd.read_csv('%s/extensions.csv' % export_dir)
        macdf = df.loc[df['Number'] == int(ext)]
        #macdf = df.loc[df['Number'] == 1011]
        print(ext)
        print(macdf)
        macdf.loc[macdf["Number"] == ext, "MAC_0"] = mac
        macdf.loc[macdf["Number"] == ext, "PhoneModel14"] = model
        macdf.loc[macdf["Number"] == ext, "PhoneTemplate14"] = tmpl
        #macdf.to_csv('%s%s.csv' % (self.macs_dir,mac),encoding='utf-8',index=False)
        macdf.to_csv('%s%s.csv' % (macs_dir,mac))
        status = {"code": 200,"msg": "Export, OK"}
        
        ##For testing purpose, return mac csv content
        with open('%s%s.csv' % (macs_dir,mac),'r') as f:
            csvtext = f.readlines()
        #self.csvtext = csvtext
    except Exception as e:
        status = {"code": 404,"msg": "Export file not found"}
        csvtext = e
    print(csvtext)
importerACS(mac, ext, model, host)