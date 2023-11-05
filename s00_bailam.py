#region debai
"""
--- ma debai / id
greeting(hour_str)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03greetinghourstr

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo trinhduyetweb de kiemtra tep s00_bailam.py, va lay diachi/url aka githubbailamurl

02b dán diachi githubbailamurl theo mẫu ở trang web duoiday
    https://forms.gle/mb6ZrFw4pXW8DqeBA

--- debai / problem
Viết hàm 
  greeting(hour_str)
giúp chat bot in ra câu chào theo buổi sáng/chiều/tối trong ngày 
00:00AM  - 11:59AM Good morning!
12:00PM  - 05:59PM Good afternoon!
06:00PM  - 11:59PM Good evening!

Khi chạy với đầuvào / input  | Kếtquả đẩura / output  | Thứtự mẫuthử 
---------------------------- | ---------------------- | -----------
greeting(hour_str='6am')     | Good morning!          | 00

# AM / PM format
greeting('6am')              | Good morning!          | 01
greeting('6 am')             | Good morning!          | 02
greeting('6AM')              | Good morning!          | 03
greeting('6 AM')             | Good morning!          | 04

greeting('9pm')              | Good evening!          | 05
greeting('0900pm')           | Good evening!          | 06
greeting('09:00pm')          | Good evening!          | 07
greeting('09:00 pm')         | Good evening!          | 08
greeting('09:00 PM')         | Good evening!          | 09

greeting('1pm')              | Good afternoon!        | 10

# 24-hours format
greeting('06:00')            | Good morning!          | 11
greeting('0600')             | Good morning!          | 12
greeting('21:00')            | Good evening!          | 13
greeting('2100')             | Good evening!          | 14

"""
#endregion debai

#region bailam
from re import X, split
def checkam(x):
  if ':' in x:
    x=x.split(":")
    if int(x[0])<12:
      return('Good morning!')
  if int(x)<12:
    return('Good morning!')
#---------------------------#
def checkpm(x):
  if ':' in x:
    x=x.split(":")
    if int(x[0])<6:
      return('Good afternoon!')
    elif int(x[0])>=6:
      return('Good evening!')
  if int(x)>=6:
    return('Good evening!')
  elif int(x)<6:
    return('Good afternoon!')
#---------------------------#
def greeting(hour_str):
  x=''
  if 'pm' in hour_str or 'am' in hour_str or 'PM' in hour_str or 'AM' in hour_str:
    if 'am' in hour_str:
      x= hour_str.split("am")
      return checkam(x[0])
    elif 'AM' in hour_str:
      x= hour_str.split("AM")
      return checkam(x[0])
    elif 'pm' in hour_str:
      x= hour_str.split("pm")
      return checkpm(x[0])
    elif 'PM' in hour_str:
      x= hour_str.split("PM")
      return checkpm(x[0])
  else:
    if ':' in hour_str:
      x=hour_str.split(":")
      if int(x[0])<12:
        return('Good morning!')
      elif int(x[0]) >=12 and int(x[0])<18:
        return('Good afternoon!')
      else:
        return('Good evening!')
    else:
      if int(hour_str[0:2])>=18:
        return('Good evening!')
      elif int(hour_str[0:2]) >=12 and int(hour_str[0:2])<18:
        return('Good afternoon!')
      else:
        return('Good morning!')

if __name__=='__main__':
  pass
#endregion bailam
