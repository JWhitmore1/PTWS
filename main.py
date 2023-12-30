'''
Personalised Thunderstorm Warning System

Author: Joshua Whitmore
'''

import re
import os
import asyncio
from ftplib import FTP

async def get_images():
    # clear old images
    local_files = os.listdir('images')
    for file in local_files:
        os.remove('./images/' + file)

    ftp = FTP('ftp.bom.gov.au')
    ftp.login()
    ftp.cwd('anon/gen/radar')
    remote_files = ftp.nlst()
    for file in remote_files:
        if re.search("^IDR1053.*png$", file):
            # print("Download: " + file.split('.', 2)[2])
            try:
                ftp.retrbinary("RETR " + file, open("./images/" + file.split('.', 2)[2], 'wb').write)
            except EOFError:    # To avoid EOF errors.
                pass

async def analyse():
    '''
    https://www.baeldung.com/cs/peak-detection-2d
    crop image banner?

    turn image into matrix mapping rainfall colour to int

    chunk and average
    
    find clumps of high intensity
     - find highest value chunks
     - scan surrounding chunks
     - create bounds to clump with intensity cuttof (+ smooth?)

    look for overlaping forms in multiple frames

    generate direction and speed
    
    extrapolate
    '''

    pass

async def main():
    images = await asyncio.gather(get_images())
    print('Saved radar stills')

if __name__ == '__main__':
    asyncio.run(main())