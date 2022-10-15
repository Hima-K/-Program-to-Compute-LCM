{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Python Program to find the L.C.M. of two input number\
\
def compute_lcm(x, y):\
\
   # choose the greater number\
   if x > y:\
       greater = x\
   else:\
       greater = y\
\
   while(True):\
       if((greater % x == 0) and (greater % y == 0)):\
           lcm = greater\
           break\
       greater += 1\
\
   return lcm\
\
num1 = 54\
num2 = 24\
\
print("The L.C.M. is", compute_lcm(num1, num2))}