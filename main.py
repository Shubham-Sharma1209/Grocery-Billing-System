import sqlite3
from tkinter import *
import random
import sqlite3

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+5+0")
        self.root.maxsize(width = 1300,height = 680)
        self.root.minsize(width = 1280,height = 680)
        self.root.title("Grocery Billing System")
                                                    
        #Variables#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        
        x = random.randint(1000,9999) 
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))
        self.Potatoes = IntVar()
        self.Broccoli = IntVar()
        self.Tomatoes = IntVar()
        self.Onions = IntVar()
        self.Bottlegourd = IntVar()
        self.rice = IntVar()
        self.salt = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.melon = IntVar()
        self.cucumber = IntVar()
        self.mango = IntVar()
        self.Apple = IntVar()
        self.banana = IntVar()
        self.total_veggies = StringVar()
        self.total_fruit = StringVar()
        self.total_other = StringVar()
        self.total_amt=IntVar()
        self.tax = StringVar()
        #
        bg_color = "#004d80"
        fg_color = "White"
        lbl_color = 'black'
        #Title of App
        title = Label(self.root,text = "Grocery Billing System",bd = 12,relief = GROOVE,fg = fg_color,bg = "#004d80",font=("times new roman",30,"bold"),pady = 3).pack(fill = X)
        #Customers Frame#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = "#004d80",relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 75,relwidth = 1)
        #Customer Name#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)
        #Customer Phone#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable=self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)
        #Customer Bill No#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)        
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        #Vegetable Frame
        F2 = LabelFrame(self.root,text = 'Vegetables(in kg)',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"),padx=20,pady=20)
        F2.place(x = 0,y = 155,width = 325,height = 380)
        #Frame Content
        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Potatoes")
        bath_lbl.grid(row = 0,column = 0)    
        bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Potatoes)
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)
        #Broccoli
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Broccoli")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Broccoli)
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)
        #Tomatoes
        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Tomatoes")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Tomatoes)
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)
        #Onions
        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Onions")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Onions)
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)
        #Bottlegourd
        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bottlegourd")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Bottlegourd)
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)
        
        #Fruits #
        F2 = LabelFrame(self.root,text = 'Fruit(in kg)',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 325,y = 155,width = 325,height = 380)
        #Frame Content
        melon_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Melon")
        melon_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        melon_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.melon)
        melon_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)
        #Cucumber
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "cucumber")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.cucumber)
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)
        #mango
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "mango")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.mango)
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)
        #apple
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Apple")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Apple)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)
        #banana
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Banana(12 pcs)")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.banana)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)
       
        #Others Frame
        F2 = LabelFrame(self.root,text = 'Others(in ltr ot kg)',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 650,y = 155,width = 325,height = 380)
        #Frame Content
        rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Rice")
        rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        rice_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.rice)
        rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)
        #food oil
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Oil")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.food_oil)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)
        #salt
        daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Salt")
        daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        daal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.salt)
        daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)
        #wheat
        wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Wheat")
        wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        wheat_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.wheat)
        wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)
        #sugar
        sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sugar")
        sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        sugar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.sugar)
        sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #Bill Area
        F3 = LabelFrame(self.root,text='Options',bd =12,relief=GROOVE,bg=bg_color,fg='gold',font = ("times new roman",13,"bold"))
        F3.place(x = 975,y = 155,width = 325,height = 380)
        #total
        total_btn = Button(F3,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 2,column = 1,ipadx = 50,padx = 70,pady=20)
        #bill
        genbill_btn = Button(F3,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row =4,column = 1,ipadx = 20,padx=70,pady=20)
        #clear
        clear_btn = Button(F3,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 6,column = 1,ipadx = 50,padx = 70,pady=20)
        #exit
        exit_btn = Button(F3,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 8,column = 1,ipadx = 55,padx=70,pady=20)
            
        #Money show case
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 535,relwidth = 1,height = 145)
        #veggies
        vegg_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total vegetables")
        vegg_lbl.grid(row = 0,column = 0,padx = (50,5),pady=40)
        vegg_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_veggies,width=15)
        vegg_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5,pady=40)    
        #fruirs
        fru_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Fruits")
        fru_lbl.grid(row = 0,column =2 ,padx = (60,5),pady = 40)
        fru_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_fruit,width=15)
        fru_en.grid(row = 0,column = 5,ipady = 2,ipadx = 5,pady=40)
        #others
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Others")
        oth_lbl.grid(row = 0,column = 4,padx = (60,5),pady = 0)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_other,width=15)
        oth_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5,pady=40)
        #tax
        tax_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Tax")
        tax_lbl.grid(row = 0,column = 6,padx = (60,5),pady = 40)
        tax_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax,width=15)
        tax_en.grid(row = 0,column = 7,ipady = 2,ipadx = 5,pady=40)
        
#Function to get total prices
    def total(self):
        #Total Food Prices
        self.total_veggies_prices = (
            (self.Potatoes.get() * 30)+
            (self.Broccoli.get() * 100)+
            (self.Tomatoes.get() *20)+
            (self.Onions.get() * 30)+
            (self.Bottlegourd.get() * 20)
        )
        self.total_veggies.set("₹"+str(self.total_veggies_prices))
        #Total fruit Prices
        self.total_fruit_prices = (
            (self.wheat.get()*60)+
            (self.food_oil.get() * 100)+
            (self.salt.get() * 65)+
            (self.rice.get() *70)+
            (self.sugar.get() * 60)

        )
        self.total_fruit.set("₹"+str(self.total_fruit_prices))
        #Total other Prices
        self.total_other_prices = (
            (self.melon.get() * 40)+
            (self.mango.get() * 100)+
            (self.cucumber.get() * 30)+
            (self.Apple.get() * 200)+
            (self.banana.get() * 25)
        )
        self.total_other.set("₹"+str(self.total_other_prices))
        #tax prices
        self.total_amt=round((self.total_other_prices+self.total_fruit_prices+self.total_veggies_prices)*0.05)
        self.tax.set("₹"+str(round((self.total_other_prices+self.total_fruit_prices+self.total_veggies_prices)*0.05)))


#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"   \t\t\t   Welcome To Store's Retail\n")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n")
        self.txt.insert(END,"\nProduct        |   Qty     |   Price")
        self.txt.insert(END,"\n")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('2.0',END)        

#Add Product name , qty and price to bill area
    def bill_area(self):    
        self.total()
        n_frame=Tk()
        n_frame.title("Bill")

        scroll_y = Scrollbar(n_frame,orient = VERTICAL)
        self.txt = Text(n_frame,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        self.welcome_soft()
        if self.Potatoes.get() != 0:
            self.txt.insert(END,f"\nPotatoes       |   {self.Potatoes.get()}       |    {self.Potatoes.get() * 1}")
        if self.Broccoli.get() != 0:
            self.txt.insert(END,f"\nBroccoli       |   {self.Broccoli.get()}       |    {self.Broccoli.get() * 3}")
        if self.Tomatoes.get() != 0:
            self.txt.insert(END,f"\nTomatoes       |   {self.Tomatoes.get()}       |    {self.Tomatoes.get() * 8}")
        if self.Onions.get() != 0:  
            self.txt.insert(END,f"\nOnions         |   {self.Onions.get()}         |    {self.Onions.get() * 6}")
        if self.Bottlegourd.get() != 0 :
            self.txt.insert(END,f"\nBottlegourd    |   {self.Bottlegourd.get()}        |    {self.Bottlegourd.get() * 4}")
        if self.wheat.get() != 0:
            self.txt.insert(END,f"\nWheat          |   {self.wheat.get()}          |    {self.wheat.get() * 1}")
        if self.food_oil.get() != 0:
            self.txt.insert(END,f"\nFood Oil       |   {self.food_oil.get()}       |    {self.food_oil.get() * 5}")
        if self.salt.get() != 0:
            self.txt.insert(END,f"\nSalt           |   {self.salt.get()}           |    {self.salt.get() * 1}")
        if self.rice.get() != 0:
            self.txt.insert(END,f"\nRice           |   {self.rice.get()}           |    {self.rice.get() * 3}")
        if self.sugar.get() != 0:
            self.txt.insert(END,f"\nSugar          |   {self.sugar.get()}          |    {self.sugar.get() * 2}")
        if self.melon.get() != 0:
            self.txt.insert(END,f"\nmelon          |   {self.melon.get()}           |    {self.melon.get() * 4}")
        if self.mango.get() != 0:
            self.txt.insert(END,f"\nmango          |   {self.mango.get()}          |    {self.mango.get() * 2}")
        if self.cucumber.get() != 0:
            self.txt.insert(END,f"\ncucumber       |   {self.cucumber.get()}        |    {self.cucumber.get() * 2}")
        if self.Apple.get() != 0:
            self.txt.insert(END,f"\nApple          |   {self.Apple.get()}          |    {self.Apple.get() * 2}")
        if self.banana.get() != 0:
            self.txt.insert(END,f"\nBanana(12 pcs) |   {self.banana.get()}         |    {self.banana.get() * 2}")
        self.txt.insert(END,"\n")
        self.txt.insert(END,f"\n                      Total : ₹{self.total_veggies_prices+self.total_fruit_prices+self.total_other_prices+self.total_veggies_prices * 0.05+self.total_fruit_prices * 0.05+self.total_other_prices * 0.05}")


    def exit(self):
        self.root.destroy()
if __name__=='__main__':
    root = Tk() 
    object = Bill_App(root)
    root.mainloop()
    print(object.total_amt)
    conn=sqlite3.connect('data.db')
    # conn.execute("""CREATE TABLE BILL
    #             (c_bill_no TEXT PRIMARY KEY NOT NULL,
    #             cus_name TEXT NOT NULL,
    #             c_phone TEXT NOT NULL,
    #             total_amt INT ) """)
    conn.execute('INSERT INTO BILL VALUES (object.c_bill_no,object.cus_name,object.c_phone,object.total_amt')
    
    conn.close()

