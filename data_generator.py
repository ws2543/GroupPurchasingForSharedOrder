
digit = ["0","1","2","3","4","5","6","7","8","9"]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

special_string = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
special = list(special_string)

gender = ["M","F","O"]

import random

def generate_username(n):
	gl = []
	for i in range(n):
		char_length = int(random.choice(digit[1:]))
		digit_length = int(random.choice(digit))

		username_char = "".join(random.sample(alphabet,char_length))
		username_digit = "".join(random.sample(digit,digit_length))

		username = username_char+username_digit

		gl.append(username)

	return gl

def generate_pw(n):
	pwl = []
	f = open("password.txt")
	for line in f:
		if "|" in line:
			continue
		pwl.append(line.strip())
	f.close()

	pwl_re = random.sample(pwl,n)
	return pwl_re

def generate_phone(n):
	phl = []
	f = open("phone.txt")
	for line in f:
		phl.append(line.strip())
	f.close()

	phl_re = random.sample(phl,n)
	return phl_re

def generate_email(n):
	el = []
	f = open("email.txt")
	for line in f:
		el.append(line.strip())
	f.close()
	el_re = random.sample(el,n)
	return el_re

def generate_caddress(n):
	al = []
	f = open("address.txt")
	first = ""
	for line in f:
		if " NY " not in line:
			first = line.strip()
			first+=", "
		else:
			first+=line.strip()
			al.append(first)
			first = ""
	f.close()

	al_re = random.sample(al,n)
	return al_re

def generate_psaddress(n):
	al = []
	f = open("address.txt")
	first = ""
	for line in f:
		if " NY " not in line:
			first = line.strip()
			al.append(first)
		else:
			continue
	f.close()

	al_re = random.sample(al,n)
	return al_re

def generate_int_id(n):
	int_id = list(range(1,n+1))
	return int_id

def get_zip_from_address(address):
	idx = address.find(' NY ')
	zipcode = address[idx+4:]
	return zipcode

def generate_bank(n):
	bl = []
	f = open("bank_account.txt")
	for line in f:
		bl.append(line.strip())

	f.close()
	bl_re = random.sample(bl,n)
	return bl_re

def generate_name(n):
	nl = []
	f = open("name.txt")
	for line in f:
		nl.append(line.strip())

	f.close()
	nl_re = random.sample(nl,n)
	return nl_re

def generate_ssn(n):
	ssnl=[]
	for i in range(n):
		first = "".join(random.choices(digit,k=3))
		second = "".join(random.choices(digit,k=2))
		third = "".join(random.choices(digit,k=4))

		ssn = first+"-"+second+"-"+third
		ssnl.append(ssn)
	return ssnl

def generate_cid(n):
	#5+5
	id10 = []
	for i in range(n):
		first = "".join(random.choices(alphabet,k=5)).upper()
		second = "".join(random.choices(digit,k=5))
		id10.append(first+second)
	return id10


def generate_iid(n):
	#3+7
	id10 = []
	types = ["VEG","FRU","MEA","SEA","FRO","CAN","CER"]#vegetables,fruits,meat,seafood,frozen food, canned food, cereal
	for i in range(n):
		first = random.choice(types).upper()
		second = "".join(random.choices(digit,k=7))
		id10.append(first+second)
	return id10

username = generate_username(30)
password = generate_pw(30)
c_phone = generate_phone(30)
c_email = generate_email(30)
c_address = generate_caddress(30)

f = open("customer_table.csv","w")
f.write("username|password|c_phone|c_email|c_address")
for i in list(zip(username,password,c_phone,c_email,c_address)):
    f.write("\n")
    f.write(str(i[0])+"|"+str(i[1])+"|"+str(i[2])+"|"+str(i[3])+"|"+str(i[4]))
f.close()

mid = list(range(1,31))
names = generate_name(30)
first_name = []
last_name = []

for name in names:
    name = name.strip().split(" ")
    first_name.append(name[0])
    last_name.append(name[1])
ssn = generate_ssn(30)
gender = random.choices(["M","F"],k=28)+["O"]*2
random.shuffle(gender)

phone = generate_phone(30)

emails = generate_email(100)
email = [i for i in emails if i not in c_email]
email = random.sample(email,30)

f = open("manager_table.csv","w")
f.write("mid|first_name|last_name|ssn|gender|phone|email")
for i in list(zip(mid,first_name,last_name,ssn,gender,phone,email)):
    f.write("\n")
    f.write(str(i[0])+"|"+str(i[1])+"|"+str(i[2])+"|"+str(i[3])+"|"+str(i[4])+"|"+str(i[5])+"|"+str(i[6]))
f.close()

cid = generate_cid(30)
f = open("cart_customer_table.csv","w")
f.write("cid|username")
for i in list(zip(cid,username)):
    f.write("\n")
    f.write(str(i[0])+"|"+str(i[1]))
f.close()

ps_id = list(range(1,11))
bank_account = generate_bank(10)
ps_phones = generate_phone(30)
ps_phone = [i for i in ps_phones if i not in phone]

ps_address = ["50 Haven Ave","100 Haven Ave","154 Haven Ave","390 Fort Washington Ave","617 West 168th St."]+["400 W 113th Street","606 West 57th Street","28-16 Jackson Avenue"] + ["47 Claremont Ave","600 West 113th Street","556 West 114th Street"]
detail = ["Mailbox #B-183", "Unit 23D", "Room 610", "","Room 1010"]+["Apt 608","Apt 2510",""]+["Mailbox 204","Apt 20",""]
city = ["New York"]*6 + ["Long Island City"] + ["New York"]*4
state = ["New York"]*11
zip_code = ["10032"]*3 + ["10033"] + ["10032"] + ["10025","10019","11101"]+["10027","10025","10025"]
assert len(ps_address) == len(detail) == len(city) == len(state) == len(zip_code)

f = open("pickupstation.csv","w")
f.write("ps_id|ps_address|detail|city|state|zip_code|bank_account|ps_phone")
for i in list(zip(ps_id,ps_address,detail,city,state,zip_code,bank_account,ps_phone)):
    f.write("\n")
    f.write(str(i[0])+"|"+str(i[1])+"|"+str(i[2])+"|"+str(i[3])+"|"+str(i[4])+"|"+str(i[5])+"|"+str(i[6])+"|"+str(i[7]))
f.close()


iid = generate_iid(30)

def generate_oid(n):
    #char(10)
    #4+6
    id10 = []
    for i in range(n):
        first = "".join(random.choices(alphabet,k=4)).upper()
        second = "".join(random.choices(digit,k=6))
        id10.append(first+second)
    return id10

oid = generate_oid(10)

otime_from = ["2019-10-07 08:00:00","2019-10-07 12:00:00","2019-10-07 16:00:00","2019-10-07 20:00:00","2019-10-08 00:00:00",
             "2019-10-08 08:00:00","2019-10-08 12:00:00","2019-10-08 16:00:00","2019-10-08 20:00:00","2019-10-09 00:00:00"]
otime_to = ["2019-10-07 11:59:59","2019-10-07 15:59:59","2019-10-07 19:59:59","2019-10-07 23:59:59","2019-10-08 07:59:59",
           "2019-10-08 11:59:59","2019-10-08 15:59:59","2019-10-08 19:59:59","2019-10-08 23:59:59","2019-10-09 07:59:59"]

a = list(set(list(zip(join_in_oid,join_in_username))))

import random
import time
from datetime import datetime

def randomDate(start, end):
    frmt = '%d-%m-%Y %H:%M:%S'

    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))

    ptime = stime + random.random() * (etime - stime)
    dt = datetime.fromtimestamp(time.mktime(time.localtime(ptime)))
    return dt

random_datetime = randomDate("20-01-2018 13:30:00", "23-01-2018 04:50:34")

print(random_datetime)

join_time = []
for i in range(8):
    rd = randomDate("07-10-2019 08:00:00", "07-10-2019 11:59:59")
    join_time.append(rd)
for i in range(4):
    rd = randomDate("07-10-2019 12:00:00", "07-10-2019 15:59:59")
    join_time.append(rd)
for i in range(5):
    rd = randomDate("07-10-2019 16:00:00", "07-10-2019 19:59:59")
    join_time.append(rd)
for i in range(4):
    rd = randomDate("07-10-2019 20:00:00", "07-10-2019 23:59:59")
    join_time.append(rd)
for i in range(5):
    rd = randomDate("08-10-2019 00:00:00", "08-10-2019 07:59:59")
    join_time.append(rd)

for i in range(5):
    rd = randomDate("08-10-2019 08:00:00", "08-10-2019 11:59:59")
    join_time.append(rd)
for i in range(4):
    rd = randomDate("08-10-2019 12:00:00", "08-10-2019 15:59:59")
    join_time.append(rd)
for i in range(3):
    rd = randomDate("08-10-2019 16:00:00", "08-10-2019 19:59:59")
    join_time.append(rd)
for i in range(7):
    rd = randomDate("08-10-2019 20:00:00", "08-10-2019 23:59:59")
    join_time.append(rd)
for i in range(2):
    rd = randomDate("09-10-2019 00:00:00", "09-10-2019 07:59:59")
    join_time.append(rd)

f = open("join_in.csv","w")
a = sorted(a,key=lambda x:x[0][0:4])
f.write("oid|username|join_time")
for i in range(47):
    f.write("\n")
    f.write(str(a[i][0])+"|"+str(a[i][1])+"|"+str(join_time[i]))
f.close()

f = open("C_has.csv","w")
f.write("oid|iid|quantity")
for i in cid:
    item_num = random.choice(list(range(1,11)))
    item_ids = random.sample(iid,k=item_num)
    for j in item_ids:
        qu = random.choice(list(range(1,6)))
        f.write("\n")
        f.write(str(i)+"|"+str(j)+"|"+str(qu))
f.close()


f = open("add.csv","w")
f.write("oid|username|iid|quantity")
for i in a:
    add_oid = i[0]
    add_usr = i[1]
    print(add_oid,add_usr)
    add_item_num = random.choice(list(range(1,21)))
    add_item_ids = random.sample(iid,k=add_item_num)
    for j in add_item_ids:
        add_qu = random.choice(list(range(1,6)))
        f.write("\n")
        f.write(str(add_oid)+"|"+str(add_usr)+"|"+str(j)+"|"+str(add_qu))
f.close()

f = open("add.csv")
from collections import defaultdict
myadd = defaultdict(int)
for line in f:
    if line.strip().startswith("oid"):
        continue
    ll = line.strip().split("|")
    add_oid = ll[0]
    add_username = ll[1]
    add_iid = ll[2]
    add_quantity = int(ll[3])
    myadd[(add_oid,add_iid)] += add_quantity
    
f.close()


f = open("O_has.csv","w")
f.write("oid|iid|quantity")
for key, value in myadd.items():
    ohas_oid = key[0]
    ohas_iid = key[1]
    ohas_qu = value
    f.write("\n")
    f.write(str(ohas_oid)+"|"+str(ohas_iid)+"|"+str(ohas_qu))
f.close()

myorder_c = defaultdict(int)
for i in a:
    myorder_c[i[0]]+=1

myorder_i = defaultdict(int)
for key,value in myadd.items():
    myorder_i[key[0]]+=value

#myorder_i
itemdict = {}
f = open("item.csv")
for line in f:
    if line.startswith("iid"):
        continue
    ll = line.strip().split("|")
    itemdict[ll[0]] = float(ll[2])
f.close()  

myorder_price = defaultdict(float)
for key,value in myadd.items():
    myorder_price[key[0]] += value*itemdict[key[1]]

myorder_final = list(zip(oid,otime_from,otime_to))

o_status = ["Y"]*10
d_status = ["Y"]*4 + ["N"]*6
opm_psid = [6,1,6,8,2,3,6,6,10,7]
opm_mid = [16,11,26,28,2,13,16,26,30,7]

ptime = ['2019-10-07 12:05:14','2019-10-07 16:07:26','2019-10-07 20:10:58','2019-10-08 00:03:45','2019-10-08 08:20:34',
        '2019-10-08 12:07:32','2019-10-08 16:04:28','2019-10-08 20:08:45','2019-10-09 00:14:29','2019-10-09 08:07:31']

track_link = ["https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=9400111899562555258445",
             "https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=9400111899556745258567",
             "https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=9400111899562935637372",
             "https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=9400111899562559756363",
             "https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=9400111899562558562855",
             "https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=9400111899562551273414",
             "https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=9400111899562552147465",
             "",
             "",
             ""]
f = open("Order_PS_Mgr.csv","w")
f.write("oid|otime_from|otime_to|total_price|cnum|inum|o_status|d_status|mid|ptime|ps_id|track_link")
for i in range(10):
    f.write("\n")
    f.write(str(myorder_final[i][0])+"|"+str(myorder_final[i][1])+"|"+str(myorder_final[i][2])+"|"+str(myorder_price[myorder_final[i][0]])+"|"+str(myorder_c[myorder_final[i][0]])+"|"+str(myorder_i[myorder_final[i][0]])+"|"+str(o_status[i])+"|"+str(d_status[i])+"|"+str(opm_mid[i])+"|"+str(ptime[i])+"|"+str(opm_psid[i])+"|"+str(track_link[i]))
f.close()

choose_psid = random.choices(ps_id,k=10)
oid_to_psid = {}
for i in range(10):
    oid_to_psid[oid[i]] = choose_psid[i]
oid_to_psid
f = open("choose.csv","w")
f.write("oid|username|ps_id")
for i in range(len(a)):
    f.write("\n")
    f.write(str(a[i][0])+"|"+str(a[i][1])+"|"+str(oid_to_psid[a[i][0]]))
f.close()
