import webbrowser
import BillingSystem
import second
import sqlite3
from reportlab.pdfgen import canvas
from datetime import date
import datetime

def rightalingn(pdf,string,left,right,ycoordinate):
  length=len(string)
  totalLength=(right-left)/7
  print(totalLength)
  spaces=int(totalLength-length)
  print(spaces)
  pdf.drawString(right,ycoordinate," "*spaces)
  left=left+(7*spaces)
  pdf.drawString(left,ycoordinate,string)

def header(pdf):
  #pdf.setTitle(header.date+"Invoice")
  # logo="logo.jpeg"
  # pdf.drawInlineImage(logo,190,253)

  pdf.line(30,820,550,820)
  pdf.setFont("Courier-Bold",20)
  pdf.drawString(260,800,"Shop Name")
  pdf.setFont("Courier-Bold",11)
  pdf.drawString(266,785,"Address Line1,")
  pdf.drawString(266,770,"Address Line2,")
  pdf.drawString(215,755,"Pincode. Phone: Contact Number")
  

  pdf.line(30,750,550,750)
  
  today = date.today()
  today = today.strftime("%d %b %Y")

  now = datetime.datetime.now()

  pdf.drawString(30,735,"Invoice Number: "+ str(int(BillingSystem.current_bill)))
  pdf.drawString(30,720,"Date: "+ str(today))
  pdf.drawString(30,705,"Time: "+ str(now.strftime("%I:%M:%S %p")))
  pdf.drawString(30,690,"Bill Generated by: "+ str(second.currentEmpName))

  pdf.line(315,745,315,682) #centre line

  pdf.drawString(325,735,"Customer Name: "+ str(BillingSystem.customer_Name))
  pdf.drawString(325,720,"Customer Contact: "+ str(BillingSystem.Customer_contact))


def middle(pdf):
  pdf.line(30,677,550,677)
  pdf.drawString(32,668,"Sr.No.")
  pdf.drawString(75,668,"Product Name")
  pdf.drawString(220,668,"Quantity")
  pdf.drawString(317,668,"Rate")
  pdf.drawString(430,668,"Amount")
  
  pdf.line(30,662,550,662)

  pdf.line(30,677,30,100)
  pdf.line(73,677,73,100)
  pdf.line(218,677,218,100)
  pdf.line(315,677,315,100)
  pdf.line(428,677,428,100)
  pdf.line(550,677,550,100)

def additem(product,pdf,ycoordinate):
  while(len(product.name)>18):
    pdf.drawString(75,ycoordinate,product.name[:18]+"-")
    product.name=product.name[18:]
    ycoordinate=ycoordinate-15
  
  pdf.drawString(75,ycoordinate,product.name)
  pdf.drawString(222,ycoordinate,str(product.quantity))
  pdf.drawString(319,ycoordinate,str(product.rate))
  pdf.drawString(432,ycoordinate,str(product.amount))
  return (ycoordinate-15)

def footer(pdf,list):
  pdf.line(30,100,550,100)
  pdf.drawString(352,88,"Grand Total: ")
  pdf.drawString(434,88,"Rs " + f"{BillingSystem.Total}")
  pdf.drawString(400,50,"Authorized Signatory")
  pdf.setFont("Courier-Bold",7)