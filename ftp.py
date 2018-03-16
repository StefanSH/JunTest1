import ftputil

dir = '2New'
path_to_file = 'C:\\Sandbox\\JunTest\\testFile.txt'

def copy(host, login, password, dir, path_to_file):
    file_name = path_to_file.split('\\')[-1]
    try:
        ftp = ftputil.FTPHost(host, login, password)
    except ftputil.error.PermanentError:
        print('Login Incorrect')
    except ftputil.error.FTPOSError:
        print('Invalid adress')

    try:
        ftp.upload(path_to_file, dir + '/' + file_name)
    except ftputil.error.FTPIOError:
        c = input('This directory doesn\'t exist. Do you want to create it? Y/n \n')
        if (c == 'y' or c == 'Y'):
            ftp.makedirs(dir)
            ftp.upload(path_to_file, dir + '/' + file_name)
    except OSError:
        print(path_to_file + ' ' + 'doesn\'t exist')
