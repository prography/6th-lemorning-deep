import os
import logging
from subprocess import check_output, CalledProcessError, STDOUT


def getstatusoutput(cmd):
    try:
        data = check_output(cmd, shell=True, universal_newlines=True, stderr=STDOUT)
        status = 0
    except CalledProcessError as ex:
        data = ex.output
        status = ex.returncode
    if data[-1:] == '\n':
        data = data[:-1]
    return status, data

if __name__ == '__main__':
    outputdir = os.path("./wav_output")
    for root, dirs, files in os.walk("./data/audio/m4a/"):
        for f in files:
            path = os.path.join(root, f)
            base, ext = os.path.splitext(f)
            outputpath = os.path.join(outputdir, base + ".wav")
            if ext == '.m4a':
                print('converting %s to %s' % (path, outputpath))
                status, output = getstatusoutput('ffmpeg -i "%s" "%s"' % (path, outputpath))
                if status:
                    logging.error (output)