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
        f = open("list.txt","r");
        link = raw_input("masukan website: ")
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
       
       Space(7);  print "[®]********* SCANNING WEB VULN *********[®]"
       Space(7);  print "[©]*************MR.W4HYU****************[©]"
       Space(7);  print "[®]******indonesian error system********[®]"
       Space(7);  print "[™]=====================================[™]"
       Space(7);  print         "|_______||V. 10 ||______|"
       space(7);  print                 "||______||" 
Desktop()
Search()
