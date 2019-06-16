# setup.py
# solitaire game

from distutils.core import setup
import py2exe

setup(console=["game.py"]
      name='Solitaire',
      version='1.0',
      packages=[''],
      url='',
      license='',
      author='Andrew Ingram',
      author_email='aingram702@outlook.com',
      description='Simple Solitaire Game',
      data_files=[("bitmaps",
                   ["cards/01c.gif", "cards/01d.gif", "cards/01h.gif", "cards/01s.gif",
                    "cards/02c.gif", "cards/02d.gif", "cards/02h.gif", "cards/02s.gif",
                    "cards/03c.gif", "cards/03d.gif", "cards/03h.gif", "cards/03s.gif",
                    "cards/04c.gif", "cards/04d.gif", "cards/04h.gif", "cards/04s.gif",
                    "cards/05c.gif", "cards/05d.gif", "cards/05h.gif", "cards/05s.gif",
                    "cards/06c.gif", "cards/06d.gif", "cards/06h.gif", "cards/06s.gif",
                    "cards/07c.gif", "cards/07d.gif", "cards/07h.gif", "cards/07s.gif",
                    "cards/08c.gif", "cards/08d.gif", "cards/08h.gif", "cards/08s.gif",
                    "cards/09c.gif", "cards/09d.gif", "cards/09h.gif", "cards/09s.gif",
                    "cards/010c.gif", "cards/010d.gif", "cards/010h.gif", "cards/010s.gif",
                    "cards/011c.gif", "cards/011d.gif", "cards/011h.gif", "cards/011s.gif",
                    "cards/012c.gif", "cards/012d.gif", "cards/012h.gif", "cards/012s.gif",
                    "cards/013c.gif", "cards/013d.gif", "cards/013h.gif", "cards/013s.gif",
                    "cards/back01.gif", "cards/bottom01.gif", "cards/bottom01-n.gif", "cards/bottom02.gif",
                    "cards/bottom02-n.gif", "cards/bottom03.gif", "cards/bottom03-n.gif", "cards/bottom04.gif",
                    "cards/bottom04-n.gif", "cards/bottom05.gif", "cards/bottom05-n.gif", "cards/bottom06.gif",
                    "cards/bottom06-n.gif", "cards/bottom07.gif", "cards/bottom07-n.gif", "cards/bottom04.gif",
                    "cards/l01.gif", "cards/l01-n.gif", "cards/l02.gif", "cards/l02-n.gif", "cards/l03.gif",
                    "cards/l03-n.gif", "cards/l04.gif", "cards/l04-n.gif", "cards/shade.gif", "cards/shadow00.gif",
                    "cards/shadow01.gif", "cards/shadow02.gif", "cards/shadow03.gif", "cards/shadow04.gif",
                    "cards/shadow05.gif", "cards/shadow06.gif", "cards/shadow07.gif", "cards/shadow08.gif",
                    "cards/shadow09.gif", "cards/shadow10.gif", "cards/shadow11.gif", "cards/shadow12.gif",
                    "cards/shadow13.gif", "cards/xshadow01.gif", "cards/xshadow02.gif", "cards/xshadow03.gif",
                    "cards/xshadow04.gif","cards/xshadow05.gif", "cards/xshadow06.gif", "cards/xshadow07.gif", 
                    "cards/xshadow08.gif", "cards/xshadow09.gif", "cards/xshadow10.gif", "cards/xshadow11.gif",
                    "cards/xshadow12.gif", "cards/xshadow13.gif"])])
     
