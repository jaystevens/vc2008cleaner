#!/usr/bin/env python2.7

#  Copyright(c) 2015-2015 Jason Stevens
#  All Rights Reserved
#
#  These coded instructions, statements, and computer programs
#  contain unpublished proprietary information written by
#  Jason Stevens, and are protected by Federal copyright law.  They may
#  not be disclosed to third parties or copied or duplicated
#  in any form, in whole or in part, without the prior written consent
#  of Jason Stevens
#


import os
import traceback
import win32api

myVersion = '1.0.1'
timeout = 10  # time to wait in seconds


# noinspection PyBroadException
def cleanup():
    files_to_clean = ['eula.1028.txt', 'eula.1031.txt', 'eula.1033.txt', 'eula.1036.txt', 'eula.1040.txt',
                      'eula.1041.txt', 'eula.1042.txt', 'eula.2052.txt', 'eula.3082.txt', 'globdata.ini',
                      'install.exe', 'install.ini', 'install.res.1028.dll', 'install.res.1031.dll',
                      'install.res.1033.dll', 'install.res.1036.dll', 'install.res.1040.dll',
                      'install.res.1041.dll', 'install.res.1042.dll', 'install.res.2052.dll',
                      'install.res.3082.dll', 'VC_RED.cab', 'VC_RED.MSI', 'vcredist.bmp']

    try:
        drives = win32api.GetLogicalDriveStrings().split("\x00")

        for drive in drives:
            if drive == '':
                continue
            for filez in files_to_clean:
                if os.path.exists(os.path.join(drive, filez)):
                    try:
                        print('removing {0}'.format(os.path.join(drive, filez)))
                        os.remove(os.path.join(drive, filez))
                    except:
                        traceback.print_exc()
    except Exception:
        traceback.print_exc()


if __name__ == '__main__':
    print('\nvc2008cleaner version: {0}\nCopyright (c) 2015-2015 Jason Stevens'.format(myVersion))
    cleanup()
