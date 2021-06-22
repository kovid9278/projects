import sys
import time
import requests
from bs4 import BeautifulSoup
url = 'https://cameradecision.com/all-Sony-cameras' 
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html     = response.text
soup     = BeautifulSoup(html,'html.parser')
url1 = soup.find_all('div', {'class' : "panel-heading"})
totalurl = len(url1)
data = []
for k in range (totalurl) :
    
    url = url1[k].find('a')['href'] 
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html     = response.text
    soup     = BeautifulSoup(html,'html.parser')
    x = soup.find_all('table', {'class' : 'table-condensed'})[-2]
    y = x.find_all('td')
    z = len(y)
    test = {}
    def check(namex):
        for j in range (z):
            if y[j].text.strip() == namex :
                test[namex] = y[j+1].text
                if test[namex] ==  ''  :
                        try:
                            test[namex] = y[j+1].find('span')['style'].split(':')[1]
                            break
                        except:
                            test[namex] = '-'
                            break
                        break
                break
                    
        else :
            test[namex] = '-'
    test['Name'] = soup.find('h1').text.strip()
    
    check('Brand')
    check('Model')
    check('Announced')
    check('Body Type')
    check('Manual Focus')
    check('Lens Mount')
    check('Number of Lenses')
    check('Focal Length Multiplier')
    check('Macro Focus Range')
    check('Screen Type')
    check('Screen Resolution')
    check('Live View')
    check('Touch Screen')
    check('Viewfinder')
    check('Viewfinder Resolution')
    check('Viewfinder Coverage')
    check('Viewfinder Magnification')
    check('Min Shutter Speed')
    check('Max Mechanical Shutter Speed')
    check('Max Electronic Shutter Speed')
    check('Continuous Shooting')
    check('Shutter Priority')
    check('Aperture Priority')
    check('Manual Exposure Mode')
    check('Exposure Compensation')
    check('Custom White Balance')
    check('Image Stabilization')
    check('Built-in Flash')
    check('Flash Range')
    check('Max Flash Sync')
    check('Flash Modes')
    check('External Flash')
    check('AE Bracketing')
    check('WB Bracketing')
    check('Multi-Segment')
    check('Average')
    check('Spot')
    check('Partial')
    check('AF-Area')
    check('Center Weighted')
    check('DxO Overall Score')
    check('DxO Color Depth')
    check('DxO Dynamic Range')
    check('DxO Low Light ISO')
    
    a = soup.find_all('table', {'class' : 'table-condensed'})[-1]
    b = a.find_all('td')
    c = len(b)
    
    def check2(namex):
        for j in range (c):
            if b[j].text.strip() == namex :
                test[namex] = b[j+1].text
                if test[namex] ==  ''  :
                        try:
                            test[namex] = b[j+1].find('span')['style'].split(':')[1]
                            break
                        except:
                            test[namex] = '-' 
                            break
                        break
                break
                    
        else :
            test[namex] = '-'
    
    check2('Sensor Type')
    check2('Sensor Size')
    check2('Sensor Dimensions')
    check2('Sensor Area')
    check2('Sensor Resolution')
    check2('Max Image Resolution')
    check2('Max Native ISO')
    check2('Max Boosted ISO')
    check2('Min Native ISO')
    check2('Min Boosted ISO')
    check2('RAW Support')
    check2('AF Touch')
    check2('AF Continuous')
    check2('AF Single')
    check2('AF Tracking')
    check2('AF Selective')
    check2('AF Center')
    check2('AF Multi Area')
    check2('AF Live View')
    check2('AF Face Detection')
    check2('AF Contrast Detection')
    check2('AF Phase Detection')
    check2('Number of Focus Points')
    check2('Number of Cross Focus Points')
    check2('Video Resolutions')
    check2('Max Video Resolution')
    check2('Video Formats')
    check2('Microphone Port')
    check2('Headphone Port')
    check2('Wireless Connectivity')
    check2('HDMI')
    check2('USB')
    check2('Environmental Sealing')
    check2('Water Proof')
    check2('Dust Proof')
    check2('Shock Proof')
    check2('Crush Proof')
    check2('Freeze Proof')
    check2('Weight')
    check2('Physical Dimensions')
    check2('Battery Life')
    check2('Battery Type')
    check2('Battery Model')
    check2('Self Timer')
    check2('Timelapse Recording')
    check2('GPS')
    check2('Storage Type')
    check2('Storage Slots')
    data.append(test)
    print('done')
    
import pandas as pd 
db = pd.DataFrame(data)
db.to_csv('Sony.csv')
