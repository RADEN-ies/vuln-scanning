#DATENG MAU RECODE YA
#SAYA MEMANG BELUM PRO TAPI STIDAKNYA SAYA TERUS BERJUANG 
#PESAN SAYA SI ANDA PERLU BELAJAR LAGI 
#wahyu.st021@gmail.com 
from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1
def Search():
        f = open("vuln.txt","r");
        link = raw_input("MASUKAN DOMAIN TARGET: ")
        print "\n\nOUTPUT : \n"
        while True:
                sub_link = f.readline()
                if not sub_link:
                        break
                req_link = "http://"+link+"/"+sub_link
                req = Request(req_link)
                try:
                        response = urlopen(req)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print "FOUND! = ",req_link
def Desktop():
       Space(7);  print "[--------- VULN SCANNING -------]"
       Space(7);  print "[----------- TUAN B4DUT -----------]"
       Space(7);  print "[------- https://cyberline.ml -----]"
Desktop()
Search()
