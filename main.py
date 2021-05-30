from tkinter import *
import random, math, os
from tkinter import messagebox

class billApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")

        title = Label(self.root, text="Billing System", font="AngsanaUPC 20 bold", bg="#5F4B8B", fg="yellow", bd="7", relief="groove", pady=10)
        title.pack(fill=X)

        #---------------Variable------------

        #-------Customer Detail--------
        self.cust_name = StringVar()
        self.cust_phn = StringVar()
        self.search_bill = StringVar()
        
        self.cust_bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.cust_bill_no.set(str(x))

        
        #---------Devive----------
        self.mob = IntVar()
        self.charger = IntVar()
        self.hdphn = IntVar()
        self.cabl = IntVar()
        self.adptr = IntVar()
        self.spkr = IntVar()
        self.pp = IntVar()

        #---------instrument------
        self.guitar = IntVar()
        self.piano = IntVar()
        self.flute = IntVar()
        self.violin = IntVar()
        self.harmo = IntVar()
        self.drum = IntVar()
        self.santr = IntVar()

        #---------Sports-------
        self.bat = IntVar()
        self.ball = IntVar()
        self.stump = IntVar()
        self.tpad = IntVar()
        self.pad = IntVar()
        self.helm = IntVar()
        self.glove = IntVar()

        #------------Total(Price and tax)---------
        self.dev_price = StringVar()
        self.instru_price = StringVar()
        self.sport_price = StringVar()

        self.dev_tax = StringVar()
        self.instru_tax = StringVar()
        self.sport_tax = StringVar()

        
        ##########-----Customer's Detail-------
        f1 = LabelFrame(self.root, text="Customer Details", bd=7, relief=GROOVE, font="lucida 10 bold", fg="yellow", bg="#5F4B8B", pady=6)
        f1.place(x=0, y=50, relwidth=1)

        c_name_lbl = Label(f1, text="Customer Name", fg="white", bg="#5F4B8B", font=("times new roman", 15, "bold"))
        c_name_lbl.grid(row=0, column=0, padx=15)
        c_name_txt = Entry(f1, textvariable=self.cust_name, width=18, font="ariel", bd=4, relief=SUNKEN)
        c_name_txt.grid(row=0,column=1, pady=2, padx=10)

        c_phn_lbl = Label(f1, text="Phone No.", fg="white", bg="#5F4B8B", font=("times new roman", 15, "bold"))
        c_phn_lbl.grid(row=0, column=2, padx=15)
        c_phn_txt = Entry(f1, textvariable=self.cust_phn, width=18, font="ariel", bd=4, relief=SUNKEN)
        c_phn_txt.grid(row=0,column=3, pady=2, padx=10)

        c_bill_lbl = Label(f1, text="Bill No.", fg="white", bg="#5F4B8B", font=("times new roman", 15, "bold"))
        c_bill_lbl.grid(row=0, column=4, padx=15)
        c_bill_txt = Entry(f1, textvariable=self.search_bill, width=18, font="ariel", bd=4, relief=SUNKEN)
        c_bill_txt.grid(row=0,column=5, pady=2, padx=10)

        bill_btn = Button(f1, text="Search", command=self.searchbill, bd=5, width=8, relief=RAISED, font=("lucida", 10, "bold"))
        bill_btn.grid(row=0,column=6, padx=15, pady=10)

        #--------Electronic Device Frame--------
        f2 = LabelFrame(self.root, text="Devices", bd=7, relief=GROOVE, font="lucida 10 bold", fg="yellow", bg="#5F4B8B" )
        f2.place(x=3, y=141, width=300, height=395)

        mob_lbl = Label(f2, text="Mobile", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        mob_lbl.grid(row=0, column=0, padx=15, pady=12, sticky="w")
        mob_txt = Entry(f2, textvariable=self.mob, width=10, font="ariel", bd=3, relief=SUNKEN)
        mob_txt.grid(row=0, column=1, pady=10, padx=15)

        chgr_lbl = Label(f2, text="Charger", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        chgr_lbl.grid(row=1, column=0, padx=15, pady=12, sticky="w")
        chgr_txt = Entry(f2, textvariable=self.charger, width=10, font="ariel", bd=3, relief=SUNKEN)
        chgr_txt.grid(row=1, column=1, pady=10, padx=15)

        Hdphn_lbl = Label(f2, text="Head Phone", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        Hdphn_lbl.grid(row=2, column=0, padx=15, pady=12, sticky="w")
        Hdphn_txt = Entry(f2, textvariable=self.hdphn, width=10, font="ariel", bd=3, relief=SUNKEN)
        Hdphn_txt.grid(row=2, column=1, pady=10, padx=15)

        cbl_lbl = Label(f2, text="Cable", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        cbl_lbl.grid(row=3, column=0, padx=15, pady=12, sticky="w")
        cbl_txt = Entry(f2, textvariable=self.cabl, width=10, font="ariel", bd=3, relief=SUNKEN)
        cbl_txt.grid(row=3, column=1, pady=10, padx=15)

        adp_lbl = Label(f2, text="Adaptor", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        adp_lbl.grid(row=4, column=0, padx=15, pady=12, sticky="w")
        adp_txt = Entry(f2, textvariable=self.adptr, width=10, font="ariel", bd=3, relief=SUNKEN)
        adp_txt.grid(row=4, column=1, pady=10, padx=15)

        spkr_lbl = Label(f2, text="Speaker", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        spkr_lbl.grid(row=5, column=0, padx=15, pady=12, sticky="w")
        spkr_txt = Entry(f2, textvariable=self.spkr, width=10, font="ariel", bd=3, relief=SUNKEN)
        spkr_txt.grid(row=5, column=1, pady=10, padx=15)

        pp_lbl = Label(f2, text="Power Point", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        pp_lbl.grid(row=6, column=0, padx=15, pady=12, sticky="w")
        pp_txt = Entry(f2, textvariable=self.pp, width=10, font="ariel", bd=3, relief=SUNKEN)
        pp_txt.grid(row=6, column=1, pady=10, padx=15)

        #-----------Musical Instrument frame---------
        f3 = LabelFrame(self.root, text="Musical Instrument", bd=7, relief=GROOVE, font="lucida 10 bold", fg="yellow", bg="#5F4B8B" )
        f3.place(x=303, y=141, width=300, height=395)

        guit_lbl = Label(f3, text="Guitar", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        guit_lbl.grid(row=0, column=0, padx=15, pady=12, sticky="w")
        guit_txt = Entry(f3, textvariable=self.guitar, width=10, font="ariel", bd=3, relief=SUNKEN)
        guit_txt.grid(row=0, column=1, pady=10, padx=15)

        pi_lbl = Label(f3, text="Piano", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        pi_lbl.grid(row=1, column=0, padx=15, pady=12, sticky="w")
        pi_txt = Entry(f3, textvariable=self.piano, width=10, font="ariel", bd=3, relief=SUNKEN)
        pi_txt.grid(row=1, column=1, pady=10, padx=15)

        flt_lbl = Label(f3, text="Flute", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        flt_lbl.grid(row=2, column=0, padx=15, pady=12, sticky="w")
        flt_txt = Entry(f3, textvariable=self.flute, width=10, font="ariel", bd=3, relief=SUNKEN)
        flt_txt.grid(row=2, column=1, pady=10, padx=15)

        vi_lbl = Label(f3, text="violin", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        vi_lbl.grid(row=3, column=0, padx=15, pady=12, sticky="w")
        vi_txt = Entry(f3, textvariable=self.violin, width=10, font="ariel", bd=3, relief=SUNKEN)
        vi_txt.grid(row=3, column=1, pady=10, padx=15)

        har_lbl = Label(f3, text="Harmonium", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        har_lbl.grid(row=4, column=0, padx=15, pady=12, sticky="w")
        har_txt = Entry(f3, textvariable=self.harmo, width=10, font="ariel", bd=3, relief=SUNKEN)
        har_txt.grid(row=4, column=1, pady=10, padx=15)

        drm_lbl = Label(f3, text="Drum", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        drm_lbl.grid(row=5, column=0, padx=15, pady=12, sticky="w")
        drm_txt = Entry(f3, textvariable=self.drum, width=10, font="ariel", bd=3, relief=SUNKEN)
        drm_txt.grid(row=5, column=1, pady=10, padx=15)

        sant_lbl = Label(f3, text="Santoor", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        sant_lbl.grid(row=6, column=0, padx=15, pady=12, sticky="w")
        sant_txt = Entry(f3, textvariable=self.santr, width=10, font="ariel", bd=3, relief=SUNKEN)
        sant_txt.grid(row=6, column=1, pady=10, padx=15)


        #----------- Sports Gear frame---------
        f4 = LabelFrame(self.root, text="Sports", bd=7, relief=GROOVE, font="lucida 10 bold", fg="yellow", bg="#5F4B8B" )
        f4.place(x=603, y=141, width=300, height=395)

        bat_lbl = Label(f4, text="Cricket Bat", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        bat_lbl.grid(row=0, column=0, padx=15, pady=12, sticky="w")
        bat_txt = Entry(f4, textvariable=self.bat, width=10, font="ariel", bd=3, relief=SUNKEN)
        bat_txt.grid(row=0, column=1, pady=10, padx=15)

        ball_lbl = Label(f4, text="Cricket Ball", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        ball_lbl.grid(row=1, column=0, padx=15, pady=12, sticky="w")
        ball_txt = Entry(f4, textvariable=self.ball, width=10, font="ariel", bd=3, relief=SUNKEN)
        ball_txt.grid(row=1, column=1, pady=10, padx=15)

        stmp_lbl = Label(f4, text="Stumps", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        stmp_lbl.grid(row=2, column=0, padx=15, pady=12, sticky="w")
        stmp_txt = Entry(f4, textvariable=self.stump, width=10, font="ariel", bd=3, relief=SUNKEN)
        stmp_txt.grid(row=2, column=1, pady=10, padx=15)

        tpad_lbl = Label(f4, text="Thigh Pad", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        tpad_lbl.grid(row=3, column=0, padx=15, pady=12, sticky="w")
        tpad_txt = Entry(f4, textvariable=self.tpad, width=10, font="ariel", bd=3, relief=SUNKEN)
        tpad_txt.grid(row=3, column=1, pady=10, padx=15)

        pad_lbl = Label(f4, text="Pad", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        pad_lbl.grid(row=4, column=0, padx=15, pady=12, sticky="w")
        pad_txt = Entry(f4, textvariable=self.pad, width=10, font="ariel", bd=3, relief=SUNKEN)
        pad_txt.grid(row=4, column=1, pady=10, padx=15)

        helm_lbl = Label(f4, text="Helmet", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        helm_lbl.grid(row=5, column=0, padx=15, pady=12, sticky="w")
        helm_txt = Entry(f4, textvariable=self.helm, width=10, font="ariel", bd=3, relief=SUNKEN)
        helm_txt.grid(row=5, column=1, pady=10, padx=15)

        glv_lbl = Label(f4, text="Gloves", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        glv_lbl.grid(row=6, column=0, padx=15, pady=12, sticky="w")
        glv_txt = Entry(f4, textvariable=self.glove, width=10, font="ariel", bd=3, relief=SUNKEN)
        glv_txt.grid(row=6, column=1, pady=10, padx=15)

        #Bill Reciept area
        f5 = Frame(self.root, bd=10, relief=GROOVE)
        f5.place(x=920, y=141, width=340, height=395)

        bill_title = Label(f5, text="Bill Reciept", font="ariel 15 bold",bd=5, relief=GROOVE)
        bill_title.pack(fill=X, padx=2)

        scrollbar = Scrollbar(f5)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text = Text(f5,  yscrollcommand=scrollbar.set)
        self.text.pack(fill="both", expand=1)
        scrollbar.config(command=self.text.yview)
        
        
        #----Bill Detail Area
        f6 = LabelFrame(self.root, text="Bill detail", bd=7, relief=GROOVE, font="lucida 10 bold", fg="yellow", bg="#5F4B8B" )
        f6.place(x=0, y=537, height=140,  relwidth=1)
        
        dev_tot_lbl = Label(f6, text="Device", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        dev_tot_lbl.grid(row=0, column=0, padx=20, pady=2, sticky="w")
        dev_tot_txt = Entry(f6, textvariable=self.dev_price, width=17, font="ariel", bd=3, relief=SUNKEN)
        dev_tot_txt.grid(row=0, column=1, padx=10, pady=2)

        mus_tot_lbl = Label(f6, text="Instrument", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        mus_tot_lbl.grid(row=1, column=0,padx=20, pady=2, sticky="w")
        mus_tot_txt = Entry(f6, textvariable=self.instru_price, width=17, font="ariel", bd=3, relief=SUNKEN)
        mus_tot_txt.grid(row=1, column=1, padx=10, pady=2)

        sprt_tot_lbl = Label(f6, text="Sports", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        sprt_tot_lbl.grid(row=2, column=0, padx=20, pady=2, sticky="w")
        sprt_tot_txt = Entry(f6, textvariable=self.sport_price, width=17, font="ariel", bd=3, relief=SUNKEN)
        sprt_tot_txt.grid(row=2, column=1, padx=10, pady=2)

        #-------Tax Area----
        dev_tax_lbl = Label(f6, text="Device Tax", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        dev_tax_lbl.grid(row=0, column=2, padx=20, pady=1, sticky="w")
        dev_tax_txt = Entry(f6, textvariable=self.dev_tax, width=17, font="ariel", bd=3, relief=SUNKEN)
        dev_tax_txt.grid(row=0, column=3, padx=10, pady=1)

        mus_tax_lbl = Label(f6, text="Instrument Tax", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        mus_tax_lbl.grid(row=1, column=2,padx=20, pady=1, sticky="w")
        mus_tax_txt = Entry(f6, textvariable=self.instru_tax, width=17, font="ariel", bd=3, relief=SUNKEN)
        mus_tax_txt.grid(row=1, column=3, padx=10, pady=1)

        sprt_tax_lbl = Label(f6, text="Sports Tax", font=("times new roman", 15, "bold"), bg="#5F4B8B", fg="white" )
        sprt_tax_lbl.grid(row=2, column=2, padx=20, pady=1, sticky="w")
        sprt_tax_txt = Entry(f6, textvariable=self.sport_tax, width=17, font="ariel", bd=3, relief=SUNKEN)
        sprt_tax_txt.grid(row=2, column=3, padx=10, pady=1)

        #Button Frame
        btn_f = Frame(f6, bd=4, width=515, height=110, relief=GROOVE, bg="white")
        btn_f.place(x=750, width=515, height=105)

        total = Button(btn_f, text="Total Bill", command=self.total,  font=("times new roman", 10, "bold"),width=30, height=2, bd=4,  bg="#6CB4EE", fg="white")
        total.grid(row=0, column=4, padx=15, pady=1)

        gen_bill = Button(btn_f, text="Generate Bill", command=self.genBill, font=("times new roman", 10, "bold"), width=30, height=2, bd=4, bg="#6CB4EE", fg="white")
        gen_bill.grid(row=0, column=5, padx=15, pady=1)

        clr = Button(btn_f, text="Clear Bill", command=self.clear, font=("times new roman", 10, "bold"), width=30, height=2, bd=4,  bg="#6CB4EE", fg="white")
        clr.grid(row=1, column=4, padx=15, pady=2)

        ext = Button(btn_f, text="Exit", command=self.exit_app, font=("times new roman", 10, "bold"), width=30, height=2, bd=4,  bg="#6CB4EE", fg="white")
        ext.grid(row=1, column=5, padx=15, pady=2)
        self.custDetail()
    
    def total(self):
        self.custDetail()
        self.d_m_p = self.mob.get()*10000
        self.d_ch_p = self.charger.get()*500
        self.d_hp_p = self.hdphn.get()*600
        self.d_ca_p = self.cabl.get()*200
        self.d_ad_p = self.adptr.get()*400
        self.d_sp_p = self.spkr.get()*300
        self.d_pp_p = self.pp.get()*1200

        self.total_device_price = float(
                                        self.d_m_p+
                                        self.d_ch_p+
                                        self.d_hp_p+
                                        self.d_ca_p+
                                        self.d_ad_p+
                                        self.d_sp_p+
                                        self.d_pp_p
                                        )
        self.dev_price.set(str(self.total_device_price) + " Rs")
        self.d_tax = round((self.total_device_price*0.05), 2)
        self.dev_tax.set(str(self.d_tax) + " Rs")

        
        self.mi_gr_p = self.guitar.get()*15000
        self.mi_pi_p = self.piano.get()*50000
        self.mi_fl_p = self.flute.get()*5000
        self.mi_vi_p = self.violin.get()*20000
        self.mi_hr_p = self.harmo.get()*100000
        self.mi_dr_p = self.drum.get()*50000
        self.mi_sr_p = self.santr.get()*12000

        self.total_instru_price = float(
                                        self.mi_gr_p+
                                        self.mi_pi_p+
                                        self.mi_fl_p+
                                        self.mi_vi_p+
                                        self.mi_hr_p+
                                        self.mi_dr_p+
                                        self.mi_sr_p
                                        )
        self.instru_price.set(str(self.total_instru_price) + " Rs")
        self.mi_tax = round((self.total_instru_price*0.07), 2)
        self.instru_tax.set(str(self.mi_tax) + " Rs")


        self.s_cb_p = self.bat.get()*1000
        self.s_bl_p = self.ball.get()*200
        self.s_st_p = self.stump.get()*500
        self.s_tp_p = self.tpad.get()*800
        self.s_pd_p = self.pad.get()*1500
        self.s_hl_p = self.helm.get()*5000
        self.s_gl_p = self.glove.get()*1200
        self.total_sport_price = float(
                                       self.s_cb_p+
                                       self.s_bl_p+
                                       self.s_st_p+
                                       self.s_tp_p+
                                       self.s_pd_p+
                                       self.s_hl_p+
                                       self.s_gl_p
                                      )
        self.sport_price.set(str(self.total_sport_price) + " Rs")
        self.s_tax = round((self.total_sport_price*0.06), 2)
        self.sport_tax.set(str(self.s_tax) + " Rs")

        self.total_bill = float(
                                self.total_device_price +
                                self.total_instru_price +
                                self.total_sport_price +
                                self.d_tax +
                                self.mi_tax +
                                self.s_tax
                                )


    def custDetail(self):
        self.text.delete('1.0', END)
        self.text.insert(END, "\t  Departmental Store \n")
        self.text.insert(END, f"\n Bill Number : {self.cust_bill_no.get()}")
        self.text.insert(END, f"\n Customer name : {self.cust_name.get()}")
        self.text.insert(END, f"\n Phone Number : {self.cust_phn.get()}")
        self.text.insert(END, f"\n=====================================")
        self.text.insert(END, f"\nProduct\t\tQTY\t\tPrice")
        self.text.insert(END, f"\n=====================================")

    def genBill(self):
        self.custDetail()

        if self.cust_name.get() == "" or self.cust_phn.get() == "":
            messagebox.showerror("Alert", "Customer details are required to proceed")

        elif self.dev_price.get() == "0.0 Rs" and self.instru_price.get() == "0.0 Rs" and self.sport_price.get() == "0.0 Rs":
            messagebox.showerror("Alert", "No product purchased")

        else:
            #---- Inserting device detail in bill----
            if self.mob.get() != 0:
                self.text.insert(END, f"\nMobile \t\t{self.mob.get()} \t\t{self.d_m_p}")
            
            if self.charger.get() != 0:
                self.text.insert(END, f"\nCharger \t\t{self.charger.get()} \t\t{self.d_ch_p}")

            if self.hdphn.get() != 0:
                self.text.insert(END, f"\nHead Phone \t\t{self.hdphn.get()} \t\t{self.d_hp_p}")

            if self.cabl.get() != 0:
                self.text.insert(END, f"\nCable \t\t{self.cabl.get()} \t\t{self.d_ca_p}")

            if self.adptr.get() != 0:
                self.text.insert(END, f"\nAdapter \t\t{self.adptr.get()} \t\t{self.d_ad_p}")

            if self.spkr.get() != 0:
                self.text.insert(END, f"\nSpeaker \t\t{self.spkr.get()} \t\t{self.d_sp_p}")

            if self.pp.get() != 0:
                self.text.insert(END, f"\nPower Point \t\t{self.pp.get()} \t\t{self.d_pp_p}")

            #---- Inserting musical instrument detail in bill----
            if self.guitar.get() != 0:
                self.text.insert(END, f"\nGuitar \t\t{self.guitar.get()} \t\t{self.mi_gr_p}")
            
            if self.piano.get() != 0:
                self.text.insert(END, f"\nPiano \t\t{self.piano.get()} \t\t{self.mi_pi_p}")

            if self.flute.get() != 0:
                self.text.insert(END, f"\nFlute \t\t{self.flute.get()} \t\t{self.mi_fl_p}")

            if self.violin.get() != 0:
                self.text.insert(END, f"\nViolin \t\t{self.violin.get()} \t\t{self.mi_vi_p}")

            if self.harmo.get() != 0:
                self.text.insert(END, f"\nHarmonium \t\t{self.harmo.get()} \t\t{self.mi_hr_p}")

            if self.drum.get() != 0:
                self.text.insert(END, f"\nDrum \t\t{self.drum.get()} \t\t{self.mi_dr_p}")

            if self.santr.get() != 0:
                self.text.insert(END, f"\nSantoor \t\t{self.santr.get()} \t\t{self.mi_sr_p}")

            #---- Inserting sports detail in bill----
            if self.bat.get() != 0:
                self.text.insert(END, f"\nBat \t\t{self.bat.get()} \t\t{self.s_cb_p}")

            if self.ball.get() != 0:
                self.text.insert(END, f"\nBat \t\t{self.ball.get()} \t\t{self.s_bl_p}")

            if self.stump.get() != 0:
                self.text.insert(END, f"\nBall \t\t{self.stump.get()} \t\t{self.s_st_p}")

            if self.tpad.get() != 0:
                self.text.insert(END, f"\nThigh Pad \t\t{self.tpad.get()} \t\t{self.s_tp_p}")

            if self.pad.get() != 0:
                self.text.insert(END, f"\nPad \t\t{self.pad.get()} \t\t{self.s_pd_p}")

            if self.helm.get() != 0:
                self.text.insert(END, f"\nHelmet \t\t{self.helm.get()} \t\t{self.s_hl_p}")

            if self.glove.get() != 0:
                self.text.insert(END, f"\nGlove \t\t{self.glove.get()} \t\t{self.s_gl_p}")

            #-----------Adding tax in bill-----------
            self.text.insert(END, f"\n-------------------------------------")

            #Tax on device
            if self.dev_tax.get() != "0.0 Rs":
                self.text.insert(END, f"\nDevice Tax\t\t\t{self.dev_tax.get()}")
            
            #Tax on Musical Instrument
            if self.instru_tax.get() != "0.0 Rs":
                self.text.insert(END, f"\nInstrument Tax\t\t\t{self.instru_tax.get()}")

            #Tax on Sports gear
            if self.sport_tax.get() != "0.0 Rs":
                self.text.insert(END, f"\nSports Tax\t\t\t{self.sport_tax.get()}")
            
            self.text.insert(END, f"\n-------------------------------------")
            self.text.insert(END, f"\nTotal Bill\t\t\t{self.total_bill}")
            self.text.insert(END, f"\n-------------------------------------")
            self.savebill()

    def savebill(self):
        sb = messagebox.askyesno("Save Bill", "Do you want to save bill")
        if sb > 0:
            self.bill_detail = self.text.get("1.0", END)
            with open("bill/" +str(self.cust_bill_no.get()) + ".txt", "w") as f:
                f.write(self.bill_detail)
            messagebox.showinfo("Bill", "Bill saved")

        else:
            return

    def searchbill(self):
        present="no"
        for i in os.listdir("bill/"):
            if i.split('.')[0]==self.search_bill.get():
                with open(f"bill/{i}", "r") as f:
                    self.text.delete("1.0", END)
                    for d in f:
                        self.text.insert(END, d)
                    f.close()
                    present="yes"
        if present=="no":
            messagebox.showerror("Error", "File not found!")
    
    def clear(self):
        cl = messagebox.askyesno("Clear App", "Do you want to clear the Aap?")
        if cl>0:

            #-------Customer Detail--------
            self.cust_name.set("")
            self.cust_phn.set("")
            self.search_bill.set("")
            
            self.cust_bill_no.set("")
            x = random.randint(1000, 9999)
            self.cust_bill_no.set(str(x))

            
            #---------Devive----------
            self.mob.set(0)
            self.charger.set(0)
            self.hdphn.set(0)
            self.cabl.set(0)
            self.adptr.set(0)
            self.spkr.set(0)
            self.pp.set(0)

            #---------instrument------
            self.guitar.set(0)
            self.piano.set(0)
            self.flute.set(0)
            self.violin.set(0)
            self.harmo.set(0)
            self.drum.set(0)
            self.santr.set(0)

            #---------Sports-------
            self.bat.set(0)
            self.ball.set(0)
            self.stump.set(0)
            self.tpad.set(0)
            self.pad.set(0)
            self.helm.set(0)
            self.glove.set(0)

            #------------Total(Price and tax)---------
            self.dev_price.set("")
            self.instru_price.set("")
            self.sport_price.set("")

            self.dev_tax.set("")
            self.instru_tax.set("")
            self.sport_tax.set("")

            self.text.delete("1.0", END)

    def exit_app(self):
        ex = messagebox.askyesno("Exit", "Do you want to exit the app?")
        if ex>0:
            self.root.destroy()

root = Tk()
obj = billApp(root)
root.mainloop()
