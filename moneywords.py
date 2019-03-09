num_dic={0 : "zero",
		1:"one",
		2 : "two",
		3 : "three",
		4 : "four",
		5 : "five",
		6 : "six",
		7 : "seven",
		8 : "eight",
		9 : "nine",
		10 : "ten",
		11 : "eleven",
		12 : "twelve",
		13 : "thirteen",
		14 : "fourteen",
		15 : "fifteen",
		16 : "sixteen",
		17 : "seventeen",
		18 : "eighteen",
		19 : "nineteen",
		20 : "twenty",
		30 : "thirty",
		40 : "forty",
		50 : "fifty",
		60 : "sixty",
		70 : "seventy",
		80 : "eighty",
		90 : "ninety"
		}


x_times={
		1:1,
		2 : 10,
		3 : 100,
		4 : 1000,
		5 : 10000,
		6 : 100000,
		7 : 1000000,
		8 : 10000000,
		9 : 100000000,
}


nameMap={0:"",
		100:"hundred",
		1000:"thousand",
		100000:"lac",
		10000000:"crore"
}



def numberToWords(intnumber):
	main=''
	if(intnumber==0):
		main=num_dic[0]
	while (intnumber!=0):		
			strNumber=str(intnumber)
			lentgh=len(strNumber)
			num=int(strNumber[0])
			x=x_times[lentgh]
			n_times=num*x
			value=intnumber//x
			if(x==10):
				if value==1:
					xx=x+intnumber%x
					string1=num_dic[xx]
					main=main+" "+string1
					intnumber=0
				else:
					string1=num_dic[n_times]
					main=main+" and "+string1
					intnumber=intnumber-n_times
			elif (x==100):
				string=num_dic[num]+ ' '+nameMap[100]
				main=main+" "+string
				intnumber=intnumber-n_times
			elif (x==1000):
				num1=int(strNumber[1])
				if num1==0:
					string=num_dic[num]+ ' '+nameMap[1000]
					main=main+" "+string
					intnumber=intnumber-(value*x_times[4])
			elif(x==10000):
				num1=int(strNumber[1])
				if value==1:
					xx=intnumber//x_times[4]
					string2=num_dic[xx]
					main=main+" "+string2+" "+nameMap[1000]
					intnumber=intnumber-(x_times[4]*xx)
				else:
					if num1==0:
						string2=num_dic[num*10]
						main=main+" "+string2+" "+nameMap[1000]
						intnumber=intnumber-(x*num)
					else:
						string2=num_dic[num*10]
						main=main+" "+string2
						intnumber=intnumber-n_times						
			elif (x==100000):
				string=num_dic[num]+ ' '+nameMap[100000]
				main=main+" "+string
				intnumber=intnumber-n_times
			elif (x==1000000):
				num1=int(strNumber[1])
				if value==1:
					xx=intnumber//x_times[6]
					string3=num_dic[xx]
					main=main+" "+string3+" "+nameMap[100000]
					intnumber=intnumber-(x_times[6]*xx)
				else:
					if num1==0:
						string3=num_dic[num*10]
						main=main+" "+string3+" "+nameMap[100000]
						intnumber=intnumber-(x*num)
					else:
						string3=num_dic[num*10]
						main=main+" "+string3
						intnumber=intnumber-n_times						
			elif(x==10000000):
				string=num_dic[num]+ ' '+nameMap[10000000]
				main=main+" "+string
				intnumber=intnumber-n_times
			elif(x==100000000):
				if value==1:
					xx=intnumber//x_times[8]
					string4=num_dic[xx]
					main=main+" "+string4+" "+nameMap[10000000]
					intnumber=intnumber-(x_times[8]*xx)
				else:
					string4=num_dic[num*10]
					main=main+" "+string4
					intnumber=intnumber-n_times
			else:
				string=num_dic[num]
				main=main+" "+string
				intnumber=intnumber-n_times
	return "{} taka only \n".format(main)

print("Enter the Number :")
Intnumber=int(input())
takaWords=numberToWords(Intnumber)
# print("Printing number   in words .....................")
print(takaWords)



"""this is for testing purpose """

# print("Enter range :\n")
# begin=int(input())
# end=int(input())
# print("Saving taka in words in a text file.....................")
# with open("Output.txt", "w") as text_file:
# 	for i in range(begin,end+1,1):
# 		text_file.write(str(numberToWords(i)))

	
