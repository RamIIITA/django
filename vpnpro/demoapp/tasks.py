from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os

@shared_task(name = "print_msg_with_name")
def print_message(name, *args, **kwargs):
  print("Celery is working!! {} have implemented it correctly.".format(name))

@shared_task(name = "add_2_numbers")
def add(x, y):
  print("Add function has been called!! with params {}, {}".format(x, y))
  return x+y


i=1
@shared_task(name="change_vpn")
def change_vpn():
  global i
  lst=["Croatia","Iceland","Netherlands","South_Korea"]
  n = len(lst)
  country = lst[(i%n)]
  os.system('nordvpn connect '+country)
  print(country)
  i+=1