

CREATE TABLE Customer
( username varchar(20),
password text NOT NULL,
c_phone varchar(15) NOT NULL,
c_email varchar(50),
c_address varchar(50),
PRIMARY KEY (username));


CREATE TABLE PickUpStation
( ps_id integer,
ps_address varchar(50) NOT NULL,
detail varchar(50),
city varchar(20) NOT NULL,
state varchar(20) NOT NULL,
zip_code varchar(10) NOT NULL CHECK (zip_code ~ '[0-9][0-9][0-9][0-9][0-9]' OR zip_code ~ '[0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]'),
bank_account varchar(50) NOT NULL,
ps_phone varchar(15) NOT NULL,
PRIMARY KEY (ps_id));


CREATE TABLE Manager
( mid integer,
first_name varchar(20) NOT NULL,
last_name varchar(20) NOT NULL,
ssn char(11) CHECK (ssn ~ '[0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]'),
gender char(1) CHECK (gender ~ '[MFO]'),
phone varchar(15) NOT NULL,
email varchar(50),
UNIQUE (ssn, phone, email),
PRIMARY KEY (mid));


CREATE TABLE Order_PS_Mgr
( oid char(10),
otime_from timestamp NOT NULL,
otime_to timestamp NOT NULL,
total_price numeric NOT NULL CHECK (total_price > 0),
cnum integer CHECK (cnum > 0),
inum integer CHECK (inum > 0),
o_status char(1) CHECK (o_status ~ '[YN]'),
d_status char(1) CHECK (d_status ~ '[YN]'),
mid integer NOT NULL,
ptime timestamp NOT NULL,
ps_id integer NOT NULL,
track_link varchar(100),
PRIMARY KEY (oid),
FOREIGN KEY (mid) REFERENCES Manager(mid),
FOREIGN KEY (ps_id) REFERENCES PickUpStation(ps_id));


CREATE TABLE Item
( iid char(10),
iname varchar(50) NOT NULL,
unit_price numeric NOT NULL CHECK (unit_price > 0),
PRIMARY KEY (iid));


CREATE TABLE Cart_Customer
( cid char(10),
username varchar(20) NOT NULL,
PRIMARY KEY (cid),
UNIQUE (username),
FOREIGN KEY (username) REFERENCES Customer(username) ON DELETE CASCADE);


CREATE TABLE Choose
( oid char(10), 
username varchar(20),
ps_id integer NOT NULL,
PRIMARY KEY (oid, username),
FOREIGN KEY (oid) REFERENCES Order_PS_Mgr(oid),
FOREIGN KEY (username) REFERENCES Customer(username));


CREATE TABLE Add
( oid char(10),
username varchar(20),
iid char(10),
quantity integer NOT NULL CHECK (quantity > 0),
PRIMARY KEY (oid, username, iid),
FOREIGN KEY (oid) REFERENCES Order_PS_Mgr(oid),
FOREIGN KEY (username) REFERENCES Customer(username),
FOREIGN KEY (iid) REFERENCES Item(iid));


CREATE TABLE C_has
( cid char(10),
iid char(10),
quantity integer NOT NULL CHECK (quantity > 0),
PRIMARY KEY (cid, iid),
FOREIGN KEY (cid) REFERENCES Cart_Customer(cid),
FOREIGN KEY (iid) REFERENCES Item(iid));


CREATE TABLE O_has
( oid char(10),
iid char(10),
quantity integer NOT NULL CHECK (quantity > 0),
PRIMARY KEY (oid, iid),
FOREIGN KEY (oid) REFERENCES Order_PS_Mgr(oid),
FOREIGN KEY (iid) REFERENCES Item(iid));


CREATE TABLE Manage
( mid integer,
ps_id integer,
mtime_from timestamp NOT NULL,
mtime_to timestamp NOT NULL,
period_type char(1) NOT NULL CHECK (period_type ~ '[FST]'),
PRIMARY KEY (mid, ps_id),
FOREIGN KEY (mid) REFERENCES Manager(mid),
FOREIGN KEY (ps_id) REFERENCES PickUpStation(ps_id));


CREATE TABLE Join_in
( oid char(10),
username varchar(20),
join_time timestamp,
PRIMARY KEY (oid, username),
FOREIGN KEY (oid) REFERENCES Order_PS_Mgr(oid),
FOREIGN KEY (username) REFERENCES Customer(username));
