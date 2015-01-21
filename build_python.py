#!/usr/local/bin/python2.7

# load basic modules only
import os, sys, platform, shutil, subprocess

def go():
    # check what OS we are on.
    if sys.platform.startswith('win'):
        if os.path.exists('C:\\Program Files (x86)\\'):
            programfiles_path = 'C:\\Program Files (x86)\\'
        else:
            programfiles_path = 'C:\\Program Files\\'

    # get script path.
    script_path = ''
    if hasattr(sys,"frozen"):
        script_path = os.path.dirname(os.path.realpath(sys.executable))
    else:
        script_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(script_path)

    # make build directory to compile python
    if os.path.exists(os.path.join(script_path, 'build')) == True:
        shutil.rmtree(os.path.join(script_path, 'build'))
    if os.path.exists(os.path.join(script_path, 'dist')) == True:
        shutil.rmtree(os.path.join(script_path, 'dist'))

    # Setup pyinstaller to Compile.
    head_projpath, tail = os.path.split(script_path)
    specf = 'vc2008cleaner.spec'
    # try and find pyinstaller location
    if sys.platform.startswith('win'):
        # C:\
        try:
            root_path = os.environ['SystemDrive']
            root_path += os.sep
        except KeyError:
            root_path = 'not found'
        try:
            # C:\Users\jay.stevens
            user_path = os.environ['HOMEDRIVE']
            user_path += os.environ['HOMEPATH']
        except KeyError:
            user_path = 'not found'
    else:  # mac/linux
        # /
        root_path = os.sep
        # /home/jay.stevens
        user_path = os.environ['HOME']
    # root_path pyinstaller
    if os.path.exists(os.path.join(root_path, 'pyinstaller', 'pyinstaller.py')):
        pyinstaller_path = os.path.join(root_path, 'pyinstaller', 'pyinstaller.py')
    # user_path pyinstaller
    elif os.path.exists(os.path.join(user_path, 'pyinstaller', 'pyinstaller.py')):
        pyinstaller_path = os.path.join(user_path, 'pyinstaller', 'pyinstaller.py')
    # head_projpath _pyinstaller
    elif os.path.exists(os.path.join(head_projpath, '_pyinstaller', 'pyinstaller.py')):
        pyinstaller_path = os.path.join(head_projpath, '_pyinstaller', 'pyinstaller.py')
    else:
        print('unable to find pyinstaller.py\nsearch paths:\n%s\n%s\n%s' % (os.path.join(root_path, 'pyinstaller'), os.path.join(user_path, 'pyinstaller'), os.path.join(head_projpath, '_pyinstaller')))
        sys.exit(1)
    # get the version of python we are running
    pyver = '%s.%s' % (sys.version_info[0], sys.version_info[1])
    # compile pyinstaller package using the copy of python that was used to launch this build script
    if sys.platform.startswith('darwin'):
        os.system('/bin/bash -c \'%s%sbin%spython%s %s --noconfirm %s%s%s\'' % (sys.prefix, os.sep, os.sep, pyver, pyinstaller_path, script_path, os.sep, specf))
    elif sys.platform.startswith('lin'):
        os.system('%s%sbin%spython%s %s --noconfirm %s%s%s' % (sys.prefix, os.sep, os.sep, pyver, pyinstaller_path, script_path, os.sep, specf))
    else:
        os.system('%s%spython.exe "%s" --noconfirm "%s%s%s"' % (sys.prefix, os.sep, pyinstaller_path, script_path, os.sep, specf))

    # cleanup build dir
    if os.path.exists('build'):
        shutil.rmtree('build')

    print('end')
    if sys.platform.startswith('win'): os.system('pause')

if __name__ == '__main__':
    go()
