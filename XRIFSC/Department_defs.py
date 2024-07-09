import tkinter
import subprocess
from tkinter import *
from tkinter import ttk


class dep_defs():
    #=======smallers def for deparment=========
    def barriers(self,t):
        if self.d["x " + str(t)] < self.d["vnumwall " + str(t)].get():
            while self.d["x " + str(t)] < self.d["vnumwall " + str(t)].get():
                self.d["x " + str(t)] += 1
                # ==============αρχικοποίηση τιμών ==================
                for u in range(1, 7):
                    self.thm["xbar {0}".format(str(self.d["x " + str(t)])) + str(u) + self.d["nr " + str(t)]] = 0
                    self.xlmat["thic {0}".format(str(self.d["x " + str(t)])) + str(u) + self.d["nr " + str(t)]] = 0
                e = self.d["x " + str(t)]
                nr = self.d["nr " + str(t)]
                self.d["titleresul {0}".format(str(e)) + nr] = None
                self.d["lau {0}".format(str(self.d["x " + str(t)]))] = None
                self.d["use_ent {0}".format(str(self.d["x " + str(t)]))] = None
                self.d["presh {0}".format(str(self.d["x " + str(t)]))] = None
                self.d["preshvar {0}".format(str(e) + nr)] = IntVar(value=0)
                self.d["preshuns {0}".format(str(e)) + nr] = IntVar(value=0)
                self.d["radbucky {0}".format(str(self.d["x " + str(t)]))] = None
                self.d["radcross {0}".format(str(self.d["x " + str(t)]))] = None
                self.d["radiob_pre {0}".format(str(e)) + nr] = IntVar(value=0)
                self.d["radside {0}".format(str(e) + nr)]= None
                self.d["radforward {0}".format(str(e) + nr)]= None
                self.d["radiob_leak {0}".format(str(e)) + nr] = IntVar(value=0)
                self.d["leak {0}".format(str(e)) + nr] = None
                self.d["leakvar {0}".format(str(e) + nr)] = IntVar(value=0)
                self.d["sellocation {0}".format(str(e) + nr)] = None
                self.d["airkerv {0}".format(str(e) + nr)] = IntVar(value=0)
                self.d["forw {0}".format(str(e)) + nr] = None
                self.d["side {0}".format(str(e)) + nr] = None
                self.d["laks {0}".format(str(e) + nr)]=None
                self.d["entk {0}".format(str(e) + nr)]=None
                #=========================barrier notebook============================================================================
                self.d["barrierf {0}".format(str(e)) + nr] \
                    = ttk.Frame(self.d["noteb " + str(t)+self.d["nr "+str(t)]], width=190)
                self.d["barrierf " + str(e) + nr].pack()
                if self.d["x " + str(t)] <= 3:
                    if self.d["x " + str(t)] == 1:
                        self.barn["lab_bar {0}".format(str(e) + nr)] = Label(text="Floor")
                        self.d["noteb " + str(t)+self.d["nr "+str(t)]].add(self.d["barrierf 1"+self.d["nr "+str(t)]], text="Floor")
                    elif self.d["x " + str(t)] == 2:
                        self.barn["lab_bar {0}".format(str(e) + nr)] \
                            = Label(text="Ceilng")
                        self.d["noteb " + str(t)+self.d["nr "+str(t)]].add(self.d["barrierf 2"+self.d["nr "+str(t)]], text="Ceilng")
                    else:
                        self.barn["lab_bar {0}".format(str(e) + nr)] = Label(text="Door")
                        self.d["noteb " + str(t)+self.d["nr "+str(t)]].add(self.d["barrierf 3"+self.d["nr "+str(t)]], text="Door")
                else:
                    self.barn["lab_bar {0}".format(str(e) + nr)]\
                        = Label(text="Barrier " + str(self.d["x " + str(t)] - 3))
                    self.d["noteb " + str(t)+self.d["nr "+str(t)]].add(self.d["barrierf " + str(e) + nr],
                                                  text="Barrier " + str(self.d["x " + str(t)] - 3))
                self.barr["{}".format(
                    self.barn["lab_bar " + str(e) + nr].cget("text"))] = 0

                if self.d["vselroom {0}".format(str(t))].get()=="CT Room":
                    # ===================distance from source====================
                    self.dist_label = ttk.Label(master=self.d["barrierf " + str(e) + nr], style="AL.TLabel",
                                                text='Distance from the CT Unit Isocenter (m):')
                    self.dist_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
                    self.d["dist_var {0}".format(str(e) + nr)] = StringVar()
                    self.dist_entry = ttk.Entry(self.d["barrierf " + str(e) + nr],
                                                textvariable=self.d["dist_var "+ str(e) + nr], width=10)
                    self.dist_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")

                else:
                    # ==============barrier type selection=================================
                    self.d["label_B {0}".format(str(self.d["x " + str(t)]))] = ttk.Label(
                        master=self.d["barrierf " + str(e) + nr],
                        style="BL.TLabel", text="Select Barrier Type")
                    self.d["label_B " + str(self.d["x " + str(t)])].grid(row=0, column=0, pady=10, padx=10, sticky="w")
                    self.d["radiob_w {0}".format(str(e) + nr)] = IntVar(value=0)
                    self.d["radpw {0}".format(str(e) + nr)] = ttk.Radiobutton(
                        master=self.d["barrierf " + str(e) + nr],
                        variable=self.d["radiob_w " + str(e) + nr],
                        text="Primary Barrier", value=1,
                        command=lambda e=self.d["x " + str(t)], nr=self.d["nr " + str(t)]: self.barrier_sel(e, nr, t))
                    self.d["radpw " + str(e) + nr].grid(row=1, column=0,
                                                                                                pady=10, padx=10,
                                                                                                sticky="w")
                    self.d["radsw {0}".format(str(e) + nr)] = ttk.Radiobutton(
                        master=self.d["barrierf " + str(e) + nr],
                        variable=self.d["radiob_w " + str(e) + nr],
                        text="Secondary Barrier", value=2,
                        command=lambda e=self.d["x " + str(t)], nr=self.d["nr " + str(t)]: self.barrier_sel(e, nr, t))
                    self.d["radsw " + str(e) + nr].grid(row=1, column=1,
                                                                                                pady=10, padx=10,
                                                                                                sticky="w")
                    # ===================distance from source====================
                    self.lad = ttk.Label(master=self.d["barrierf " + str(e) + nr], style="AL.TLabel",
                                         text="Distance from the Source (m):")
                    self.lad.grid(row=7, column=0, pady=10, padx=10, sticky="w")
                    self.d["entryd {0}".format(str(e)) + nr] = ttk.Entry(
                        master=self.d["barrierf " + str(e) + nr], width=10)
                    self.d["entryd " + str(e) + nr].grid(row=7, column=1, pady=10, padx=10, sticky="w")
                #===============Materials selection===============
                self.d["m {0}".format(str(e) + nr)] = 0  # Για το Spinbox του material
                self.matlab = ttk.Label(master=self.d["barrierf " + str(e) + nr], style="AL.TLabel",
                                     text="Select Materials:")
                self.matlab.grid(row=8, column=0, padx=10,pady=10, sticky="w")

                self.d["vnumbmat {0}".format(str(e)) + nr]=IntVar(value=1)
                if self.d["vselroom " + str(t)].get() == "CT Room":
                    self.d["numbmat {0}".format(str(e)) + nr]= ttk.Spinbox(
                        master=self.d["barrierf " + str(e) + nr], from_=1 ,to=2, width=5,
                        textvariable=self.d["vnumbmat " + str(e) + nr] ,
                        command=lambda e=self.d["x " + str(t)],nr=self.d["nr "+str(t)] : self.numbmater(e,nr,t))
                else:
                    self.d["numbmat {0}".format(str(e)) + nr] = ttk.Spinbox(
                        master=self.d["barrierf " + str(e) + nr], from_=1, to=6,
                        width=5, textvariable=self.d["vnumbmat " + str(e) + nr],
                        command=lambda e=self.d["x " + str(t)], nr=self.d["nr " + str(t)]: self.numbmater(e, nr, t))
                self.d["numbmat "+ str(e) + nr].grid(row=8, column=1, padx=10,pady=10, sticky="w")


                self.numbmater(e, nr, t)
                """""# ===========Existing Barier===========
                self.d["existvar {0}".format(str(e))+nr] = IntVar(value=0)
                self.d["check_ex {0}".format(str(e))+nr] \
                    = ttk.Checkbutton(master=self.d["barrierf " + str(e)+nr],
                                                text="Existing Barrier",
                                                variable=self.d["existvar " + str(e)
                                                            +nr], onvalue=1,
                                                offvalue=0, command=lambda e=e,nr=nr: self.existbarrier(e,nr,t))
                self.d["check_ex "+str(e)+nr] .grid(row=5, column=0, pady=10, padx=10, sticky="w")
                #=====αρχικοποίηση existing barrier=================
                self.d["existla {0}".format(str(e))+nr] = None
                self.d["existmat {0}".format(str(e))+nr] = None
                self.d["vmaterex {0}".format(str(e))+nr] = None
                self.d["materex {0}".format(str(e))+nr] =None"""
                self.d["K {0}".format(self.barn["lab_bar " + str(e) + nr].cget("text")) + nr]=0
                if self.d["vselroom {0}".format(str(t))].get()=="X-Ray room":
                    # =========Occupation Factor=================
                    self.title_ocupat = ttk.Label(
                        master=self.d["barrierf " + str(e) + nr], style="BL.TLabel",
                        text="Shielding Area")
                    self.title_ocupat.grid(row=13, column=0, pady=10, padx=10, sticky="w")
                    # =========Classify area=============
                    self.d["area {0}".format(str(e)) + nr] = StringVar()
                    self.d["area {0}".format(str(e)) + nr] = ttk.Combobox(
                        master=self.d["barrierf " + str(e) + nr],
                        textvariable=self.d["area " + str(e) + nr],
                        values=["Cotrolled Area", "Uncontrolled Area", "Supervised Area"], state="readonly")
                    self.d["area " + str(e) + nr].grid(row=13, column=1, sticky="w")
                    self.d["area {0}".format(str(e)) + nr].set("Classify the area")
                    self.d["vraoccup {0}".format(str(e)) + nr] = IntVar(value=0)
                    self.raoccup = ttk.Radiobutton(
                        master=self.d["barrierf " + str(e) + nr],
                        variable=self.d["vraoccup " + str(e) + nr], text="Write occupancy factor (T):",
                        value=1, command=lambda e=self.d["x " + str(t)], nr=self.d["nr "+str(t)]: self.occupation3(e,nr,t))
                    self.raoccup.grid(row=14, column=0, pady=10, padx=10, sticky="w")
                    self.d["occupentry {0}".format(str(self.d["x " + str(t)]))+ self.d["nr " + str(t)]] = None
                    self.raseloccup = ttk.Radiobutton(
                        master=self.d["barrierf " + str(e) + nr],
                        text="or select Location ""[suggested NCRP 147]",
                        variable=self.d["vraoccup " + str(e) + nr], value=2,
                        command= lambda e=self.d["x " + str(t)], nr=self.d["nr "+str(t)]: self.occupation3(e,nr,t))
                    self.raseloccup.grid(row=15, column=0, pady=10, padx=10, sticky="w")
                    # ========Design Kerma Goal===========
                    self.ladike = ttk.Label(master=self.d["barrierf " + str(e) + nr], style="AL.TLabel",
                                            text="Design Kerma Goal (mGy/week):")
                    self.ladike.grid(row=16, column=0, pady=10, padx=10, sticky="w")
                    self.d["dikeent {0}".format(str(e)) + nr] = ttk.Entry(master=self.d["barrierf " + str(e) + nr], width=10)
                    self.d["dikeent " + str(e) + nr].grid(row=16, column=1, pady=10, padx=10, sticky="w")
                    # ==========
                elif self.d["vselroom {0}".format(str(t))].get()=="From X-Ray room":
                    self.d["selxroom {0}".format(str(e)) + nr] = None
                    # ========Workload===========
                    self.title_workload = ttk.Label(master=self.d["barrierf " + str(e) + nr], style="BL.TLabel",
                                                    text="Workload")
                    self.title_workload.grid(row=13, column=0, pady=10, padx=10, sticky="w")
                    # =========X-ray Rooms============
                    self.xrayLabel = ttk.Label(master=self.d["barrierf " + str(e) + nr],
                                               text="Select X-Ray room or give tube kVp")
                    self.xrayLabel.grid(row=14, column=0, padx=10, pady=10, sticky="w")
                    # ======X-ray Room or kVp==========
                    self.d["vselxray {0}".format(str(e)) + nr] = IntVar(value=0)
                    self.d["selxray1 {0}".format(str(e)) + nr] = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                                                                            variable=self.d["vselxray "+ str(e) + nr],
                                                                            text="Select X-Ray Room", value=1,
                                                                            command=lambda e=self.d["x " + str(t)], nr=self.d["nr "+str(t)]: self.XrRoom1(e,nr,t))
                    self.d["selxray1 "+ str(e) + nr].grid(row=15, column=0, pady=10, padx=10, sticky="w")

                    self.d["selxray2 {0}".format(str(e)) + nr] = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                                                                            variable=self.d["vselxray "+ str(e) + nr],
                                                                            text="Give kVp", value=2,
                                                                            command=lambda e=self.d["x " + str(t)], nr=self.d["nr "+str(t)]: self.XrRoom1(e,nr, t))
                    self.d["selxray2 " + str(e) + nr].grid(row=15, column=1, pady=10, padx=10, sticky="w")

                    # =====================Write workload========================
                    self.d["worentry {0}".format(str(e)) + nr] = None
                    self.d["numpapwe {0}".format(str(e)) + nr] = None
                    self.d["vrawork {0}".format(str(e)) + nr] = IntVar(value=0)
                    self.raworkl = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                                                   variable=self.d["vrawork " + str(e) + nr],
                                                   text="Write total Workload (mA∙min∙week\u207B\u00b9):", value=1,
                                                   command=lambda e=self.d["x " + str(t)], nr=self.d["nr "+str(t)]: self.workload2(e, nr, t))
                    self.raworkl.grid(row=17, column=0, pady=10, padx=10, sticky="w")

                    self.ranumb = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                                                  text="or the number of patients per week:",
                                                  variable=self.d["vrawork " + str(e) + nr], value=2,
                                                  command=lambda e=self.d["x " + str(t)], nr=self.d["nr "+str(t)]: self.workload2(e, nr, t))
                    self.ranumb.grid(row=18, column=0, pady=10, padx=10, sticky="w")
                #=======================CT=====================================================
                elif self.d["vselroom {0}".format(str(t))].get() == "CT Room":

                    self.sh_label = ttk.Label(master=self.d["barrierf " + str(e) + nr],
                                              text='Shielding design Goal(P)\n in air kerma(mGy∙week\u207B\u00b9):')
                    self.sh_label.grid(row=11, column=0, padx=10, pady=10, sticky="w")
                    self.d["sh_var {0}".format(str(e)+nr)] = DoubleVar()
                    self.sh_entry = ttk.Entry(master=self.d["barrierf " + str(e) + nr],
                                              textvariable=self.d["sh_var " + str(e) + nr], width=10)
                    self.sh_entry.grid(row=11, column=1, padx=10, pady=10, sticky="w")

                #============Calculation Button====================
                self.d["calbutton {0}".format(str(self.d["x " + str(t)]))] \
                    = ttk.Button(master=self.d["barrierf " + str(e) + nr], text="Calculate",
                                            command=lambda e=self.d["x " + str(t)], nr=self.d["nr "+str(t)], ep=self.ep: self.choosetype(e,nr,ep,t))
                self.d["calbutton "+str(self.d["x " + str(t)])].grid(row=19, column=1, pady=10, padx=10, sticky="w")



            self.d["noteb " + str(t)+self.d["nr "+str(t)]].grid(row=0, column=4, rowspan=10,
                                           columnspan=self.d["x " + str(t)], pady=10, padx=10,
                                           sticky="wn")
        else:
            while self.d["x " + str(t)] > self.d["vnumwall " + str(t)].get():
                self.d["barrierf " + str(e) + nr].destroy()
                self.d["label_B " + str(self.d["x " + str(t)])].destroy()
                self.d["radpw " + str(e) + nr].destroy()
                self.d["radsw " + str(e) + nr].destroy()
                self.d["x " + str(t)] -= 1

    def occupation3(self,e,nr,t):
        if self.d["vraoccup " + str(e)+nr].get() == 1:
            if self.d["sellocation " + str(e)+nr] is not None:
                self.d["sellocation " + str(e)+nr].destroy()
            if self.d["occupentry " + str(e)+nr] is not None:
                self.d["occupentry " + str(e)+nr].destroy()
            self.d["vselocation {0}".format(str(e)) + nr]=StringVar()
            self.d["occupentry " + str(e)+nr] = ttk.Entry(master=self.d["barrierf " + str(e)+nr], width=10)
            if self.d["area " + str(e)+nr].get() == "Cotrolled Area":
                self.d["occupentry " + str(e)+nr].insert(0,str(1))
            elif self.d["area " + str(e)+nr].get() == "Uncontrolled Area":
                self.d["occupentry " + str(e)+nr].insert(0,str(1/16))
            elif self.d["area " + str(e)+nr].get() == "Supervised Area":
                self.d["occupentry " + str(e)+nr].insert(0,str(1/4))
            self.d["occupentry " + str(e)+nr].grid(row=14, column=1, pady=10, padx=10)
        elif self.d["vraoccup " + str(e)+nr].get() == 2:
            if self.d["occupentry " + str(e)+nr] is not None:
                self.d["occupentry " + str(e)+nr].destroy()
            if self.d["sellocation " + str(e)+nr] is not None:
                self.d["sellocation " + str(e)+nr].destroy()
            self.d["vselocation {0}".format(str(e))+nr] = StringVar()
            if self.d["area " + str(e)+nr].get() == "Cotrolled Area":
                self.control = ("Administrative or clerical offices", "Laboratories",
                                "Pharmacies and other work areas fully occupied by an individual", "Receptionist areas",
                                "Attended waiting rooms", "Children’s indoor play areas", "Adjacent x-ray rooms",
                                "Film reading areas", "Nurse’s stations", "X-ray control rooms",
                                "Rooms used for patient examinations and treatments")
                self.d["sellocation " + str(e)+nr] = ttk.OptionMenu(self.d["barrierf " + str(e)+nr],
                                                                 self.d["vselocation " + str(e)+nr], "Select Location",
                                                                 *self.control)
            elif self.d["area " + str(e)+nr].get() == "Uncontrolled Area":
                self.uncontroll = (
                "Public toilets", "Unattended vending areas", "Storage  rooms", "Outdoor areas with seating",
                "Unattended waiting rooms", "Patient holding areas",
                "Outdoor areas with only transient pedestrian or vehicular traffic", "Unattended parking lots",
                "Vehicular drop off areas (unattended)", "Attics", "Stairways", "Unattended elevators",
                "Janitor’s closets")
                self.d["sellocation " + str(e)+nr] = ttk.OptionMenu(self.d["barrierf " + str(e)+nr],
                                                                 self.d["vselocation " + str(e)+nr], "Select Location",
                                                                 *self.uncontroll)
            elif self.d["area " + str(e)+nr].get() == "Supervised Area":
                self.supervised = ("Corridors", "Patient rooms", "Employee lounges", "Staff restooms", "Corridor doors")
                self.d["sellocation " + str(e)+nr] = ttk.OptionMenu(self.d["barrierf " + str(e)+nr],
                                                                 self.d["vselocation " + str(e)+nr], "Select Location",
                                                                 *self.supervised)
            else:
                self.d["sellocation " + str(e)+nr] = ttk.Combobox(self.d["barrierf " + str(e)+nr], textvariable=self.d["vselocation " + str(e)+nr], state="readonly",
                                        values=["Administrative or clerical offices", "Laboratories",
                                                "Pharmacies and other work areas fully occupied by an individual",
                                                "Receptionist areas", "Attended waiting rooms",
                                                "Children’s indoor play areas", "Adjacent x-ray rooms",
                                                "Film reading areas", "Nurse’s stations", "X-ray control rooms",
                                                "Rooms used for patient examinations and treatments", "Corridors",
                                                "Patient rooms", "Employee lounges", "Staff restooms", "Corridor doors",
                                                "Public toilets", "Unattended vending areas", "Storage  rooms",
                                                "Outdoor areas with seating", "Unattended waiting rooms",
                                                "Patient holding areas",
                                                "Outdoor areas with only transient pedestrian or vehicular traffic",
                                                "Unattended parking lots", "Vehicular drop off areas (unattended)",
                                                "Attics", "Stairways", "Unattended elevators", "Janitor’s closets"])

            self.d["sellocation " + str(e)+nr].grid(row=15, column=1, pady=10, padx=10, sticky="w")
            self.d["sellocation " + str(e) + nr].config(width=15)
        if self.d["area " + str(e) + nr].get() == "Cotrolled Area":
            self.d["dikeent " + str(e) + nr].destroy()
            self.d["dikeent {0}".format(e) + nr] = ttk.Entry(
                master=self.d["barrierf " + str(e) + nr], width=10)
            self.d["dikeent " + str(e) + nr].grid(row=16, column=1, pady=10, padx=10, sticky="w")
            self.d["dikeent "+str(e)+nr].insert(0, str(0.01))
        elif self.d["area " + str(e) + nr].get() == "Uncontrolled Area":
            self.d["dikeent " + str(e) + nr].destroy()
            self.d["dikeent {0}".format(e) + nr] = ttk.Entry(master=self.d["barrierf " + str(e) + nr], width=10)
            self.d["dikeent " + str(e) + nr].grid(row=16, column=1, pady=10, padx=10, sticky="w")
            self.d["dikeent "+str(e)+nr].insert(0, str(0.006))
        elif self.d["area " + str(e) + nr].get() == "Supervised Area":
            self.d["dikeent " + str(e) + nr].destroy()
            self.d["dikeent {0}".format(e) + nr] = ttk.Entry(master=self.d["barrierf " + str(e) + nr], width=10)
            self.d["dikeent " + str(e) + nr].grid(row=16, column=1, pady=10, padx=10, sticky="w")
            self.d["dikeent "+str(e)+nr].insert(0, str(0.006))
    def workload2(self,e,nr, t):
        if self.d["vrawork " + str(e)+nr].get() == 1:
            if self.d["numpapwe " + str(e)+nr] is not None:
                self.d["numpapwe " + str(e)+nr].destroy()
            if self.d["worentry " + str(e)+nr] is not None:
                self.d["worentry " + str(e)+nr].destroy()
            self.d["worentry " + str(e)+nr] = ttk.Entry(master=self.d["barrierf " + str(e) + nr], width=10)
            self.d["worentry " + str(e)+nr].grid(row=17, column=1, pady=5, padx=5)
        elif self.d["vrawork " + str(e)+nr].get() == 2:
            if self.d["worentry " + str(e)+nr] is not None:
                self.d["worentry " + str(e)+nr].destroy()
            if self.d["numpapwe " + str(e)+nr] is not None:
                self.d["numpapwe " + str(e)+nr].destroy()
            self.d["numpapwe " + str(e)+nr] = ttk.Entry(master=self.d["barrierf " + str(e) + nr], width=10)
            self.d["numpapwe " + str(e)+nr].grid(row=18, column=1, pady=5, padx=5, sticky="w")

    def existbarrier(self, e,nr,t):
        if self.d["existvar " + str(e)+nr].get() == 1:
            if self.d["existla " + str(e) + nr] is not None:
                self.d["existla " + str(e) + nr].destroy()
                self.d["existmat " + str(e) + nr].destroy()
                self.d["materex " + str(e) + nr].destroy()
            self.d["existla "+str(e)+nr] \
                = ttk.Label(master=self.d["barrierf " + str(e)+nr], style="AL.TLabel",
                                                             text="Existing Barrier in mm:")
            self.d["existla " + str(e)+nr].grid(row=6, column=0, pady=10, padx=10, sticky="w")
            self.d["existmat "+str(e)+nr] \
                = ttk.Entry(master=self.d["barrierf " + str(e)+nr], width=10)
            self.d["existmat " + str(e)+nr].grid(row=6, column=1, pady=10, padx=10, sticky="w")

            self.d["vmaterex "+str(e)+nr] = StringVar()
            self.d["materex "+str(e)+nr] \
                = ttk.OptionMenu(self.d["barrierf " + str(e)+nr],
                self.d["vmaterex "+str(e)+nr], "Select Material", *self.mater)
            self.d["materex " + str(e)+nr].grid(row=7, column=0, pady=10, padx=10, sticky="w")
        elif self.d["existvar " + str(e)+nr].get() == 0:
            if self.d["existla " + str(e)+nr] is not None:
                self.d["existla " + str(e)+nr].destroy()
                self.d["existmat " + str(e)+nr].destroy()
                self.d["materex " + str(e)+nr].destroy()

    def barrier_sel(self, e,nr,t):
        if self.d["radiob_w "+str(e)+nr].get() == 1:
            if self.d["lau "+str(e)] is not None:
                self.d["lau " + str(e)].destroy()
                self.d["use_ent " + str(e)].destroy()
                self.d["presh " + str(e)].destroy()
                self.d["preunsh " + str(e)].destroy()
                if self.d["laks " + str(e) + nr] is not None:
                    self.d["laks " + str(e) + nr].destroy()
                    self.d["entk " + str(e) + nr].destroy()
            if self.d["leak " + str(e) + nr] is not None:
                if  self.d["airkerv " + str(e) + nr].get()== 1:
                    self.d["radside "+str(e)+nr].destroy()
                    self.d["radforward " +str(e)+nr].destroy()
                    self.d["leak " + str(e) + nr].destroy()
                    self.d["forw " + str(e) + nr].destroy()
                    self.d["side " + str(e) + nr].destroy()
                    self.d["write " + str(e) + nr].destroy()
                elif self.d["airkerv " + str(e) + nr].get()== 4:
                    self.d["leak " + str(e) + nr].destroy()
                    self.d["forw " + str(e) + nr].destroy()
                    self.d["side " + str(e) + nr].destroy()
                    self.d["write " + str(e) + nr].destroy()
                    self.d["laks " + str(e) + nr].destroy()
                    self.d["entk " + str(e) + nr].destroy()
                else:
                    self.d["leak " + str(e) + nr].destroy()
                    self.d["forw " + str(e) + nr].destroy()
                    self.d["side " + str(e) + nr].destroy()
                    self.d["write " + str(e) + nr].destroy()
            #=========use factor====================
            self.d["lau "+str(e)] = ttk.Label(master=self.d["barrierf " + str(e)+nr], style="AL.TLabel",
                                    text="Use Factor:")
            self.d["lau "+str(e)].grid(row=3, column=0, pady=10, padx=10, sticky="w")
            self.d["use_ent "+str(e)] = ttk.Entry(
                master=self.d["barrierf " + str(e)+nr], width=10)
            if e==1:
                if self.d["selxroom {0}".format(str(t))] is not None:
                    if self.d["vsexroom " + str(t)].get()=="Rad Room (floor or other barriers)":
                        self.d["use_ent " + str(e)].insert(0, str(0.89))
                else:
                    self.d["use_ent " + str(e)].insert(0, str(1))
            elif e==2:
                self.d["use_ent " + str(e)].insert(0, str(1/16))
            else:
                if self.d["selxroom {0}".format(str(t))] is not None:
                    if self.d["vsexroom " + str(t)].get()=="Rad Room (floor or other barriers)":
                        self.d["use_ent " + str(e)].insert(0, str(0.02))
                else:
                    self.d["use_ent " + str(e)].insert(0, str(1/4))
            self.d["use_ent " + str(e)].grid(row=3, column=1, pady=10, padx=10, sticky="w")
            #==========Preshielding===========
            self.d["presh "+str(e)]=ttk.Checkbutton(master=self.d["barrierf " + str(e)+nr], text= "Preshielding",
                                                    variable=self.d["preshvar "+str(e) + nr],
                                                    offvalue=0, onvalue=1, command=lambda: self.pres(e,nr))
            self.d["presh " + str(e)].grid(row=4, column=0, pady=10, padx=10, sticky="w")
            #===========unshielding air kerma=================
            self.d["preunsh " + str(e)] = ttk.Checkbutton(master=self.d["barrierf " + str(e) + nr], text="Unshielded air kerma",
                                                        variable=self.d["preshuns " + str(e) + nr], offvalue=0,
                                                        onvalue=1, command=lambda: self.uns(e, nr))
            self.d["preunsh " + str(e)].grid(row=4, column=1, pady=10, padx=10, sticky="w")


        elif self.d["radiob_w "+str(e)+nr].get() == 2:
            if self.d["leak " + str(e) + nr] is not None:
                self.d["leak " + str(e) + nr].destroy()
                self.d["side " + str(e) + nr].destroy()
                self.d["forw " + str(e) + nr].destroy()
                self.d["write " + str(e) + nr].destroy()
            if self.d["lau "+str(e)] is not None:
                self.d["lau " + str(e)].destroy()
                self.d["use_ent " + str(e)].destroy()
                self.d["preunsh " + str(e)].destroy()
                if  self.d["preshvar " + str(e) + nr].get()== 1:
                    self.d["radbucky " + str(e)].destroy()
                    self.d["radcross " + str(e)].destroy()
                    self.d["presh " + str(e)].destroy()
                elif self.d["preshvar " + str(e) + nr].get()== 0:
                    self.d["presh " + str(e)].destroy()
                if self.d["laks " + str(e) + nr] is not None:
                    self.d["laks " + str(e) + nr].destroy()
                    self.d["entk " + str(e) + nr].destroy()
            # ====================Leakage========================
            self.d["leak " + str(e) + nr] = ttk.Radiobutton(
                master=self.d["barrierf " + str(e) + nr],text="Leakage radiation",
                variable=self.d["airkerv " + str(e) + nr], value=1,
                 command=lambda : self.leakage(e, nr))
            self.d["leak " + str(e) + nr].grid(row=2, column=0, pady=10, padx=10, sticky="w")
            self.d["side " + str(e) + nr] = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                text="Side-Scatter", variable=self.d["airkerv " + str(e) + nr],value=2,
                 command=lambda : self.leakage(e, nr))
            self.d["side " + str(e) + nr].grid(row=2, column=1, pady=10, padx=10, sticky="w")
            self.d["forw " + str(e) + nr] = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                text="Forward/ Backscatter", variable=self.d["airkerv " + str(e) + nr], value=3,
                 command=lambda : self.leakage(e, nr))
            self.d["forw " + str(e) + nr].grid(row=3, column=0, pady=10, padx=10, sticky="w")
            self.d["write "+ str(e) + nr] = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                text="Unshielded air kerma", variable=self.d["airkerv " + str(e) + nr], value=4,
                 command=lambda : self.leakage(e, nr))
            self.d["write " + str(e) + nr].grid(row=3, column=1, pady=10, padx=10, sticky="w")

    def uns(self,e,nr):
        if self.d["preshuns " + str(e) + nr].get()== 1:
            self.d["laks " + str(e) + nr] = ttk.Label(master=self.d["barrierf " + str(e) + nr], text="K\u209b\u2091 (mGy/patient):")
            self.d["laks " + str(e) + nr].grid(row=6, column=0, pady=10, padx=10, sticky="w")
            self.d["entk " + str(e) + nr] = ttk.Entry(master=self.d["barrierf " + str(e) + nr], width=10)
            self.d["entk " + str(e) + nr].grid(row=6, column=1, pady=10, padx=10, sticky="w")

        elif self.d["preshuns " + str(e) + nr].get()==0:
            if self.d["laks " + str(e) + nr] is not None:
                self.d["laks " + str(e) + nr].destroy()
                self.d["entk " + str(e) + nr].destroy()


    def numbmater(self,e,nr,t):
        if self.d["vselroom "+ str(t)].get()=="CT Room":
            if self.d["m "+ str(e) + nr]  < self.d["vnumbmat " +str(e)+nr].get():
                while self.d["m "+ str(e) + nr]  < self.d["vnumbmat " +str(e)+nr].get():
                    self.d["m " + str(e) + nr]+=1
                    self.mater = ("Lead", "Concrete")
                    self.d["vmater {0}".format(str(e))+str(self.d["m " + str(e) + nr])+nr] = StringVar()
                    self.d["mater {0}".format(str(e))+str(self.d["m " + str(e) + nr])] = ttk.OptionMenu(
                        self.d["barrierf " + str(e) + nr],
                        self.d["vmater " +str(e)+str(self.d["m " + str(e) + nr])+nr], "Select Material", *self.mater)
                    if self.d["m " + str(e) + nr] <3:
                        self.d["matlab {0}".format(str(e)) + str(self.d["m " + str(e) + nr])]\
                            =ttk.Label(self.d["barrierf " + str(e) + nr],text="#"+str(self.d["m " + str(e) + nr])+":")
                        self.d["matlab "+str(e) + str(self.d["m " + str(e) + nr])].\
                            grid(row=10, column= -1+self.d["m " + str(e) + nr], sticky="w")
                        self.d["mater " + str(e)+str(self.d["m " + str(e) + nr])].\
                            grid(row=10, column= -1+self.d["m " + str(e) + nr],pady=10, padx=25, sticky="s")

            else:
                while self.d["m " + str(e) + nr] > self.d[
                    "vnumbmat " + str(e) + nr].get():
                    self.d["mater "+str(e)+str(self.d["m " + str(e) + nr])].destroy()
                    self.d["matlab " + str(e) + str(self.d["m " + str(e) + nr])].destroy()
                    self.d["m " + str(e) + nr] -= 1
        else:
            if self.d["m "+ str(e) + nr]  < self.d["vnumbmat " +str(e)+nr].get():
                while self.d["m "+ str(e) + nr]  < self.d["vnumbmat " +str(e)+nr].get():
                    self.d["m " + str(e) + nr]+=1
                    self.mater = ("Lead", "Concrete", "Gypsum Wallboard", "Steel", "Plate Glass", "Wood")
                    self.d["vmater {0}".format(str(e))+str(self.d["m " + str(e) + nr])+nr] = StringVar()
                    self.d["mater {0}".format(str(e))+str(self.d["m " + str(e) + nr])] = ttk.OptionMenu(
                        self.d["barrierf " + str(e) + nr],
                        self.d["vmater " +str(e)+str(self.d["m " + str(e) + nr])+nr], "Select Material", *self.mater)
                    if self.d["m " + str(e) + nr] <3:
                        self.d["matlab {0}".format(str(e)) + str(self.d["m " + str(e) + nr])]\
                            =ttk.Label(self.d["barrierf " + str(e) + nr],text="#"+str(self.d["m " + str(e) + nr])+":")
                        self.d["matlab "+str(e) + str(self.d["m " + str(e) + nr])].\
                            grid(row=10, column= -1+self.d["m " + str(e) + nr], sticky="w")
                        self.d["mater " + str(e)+str(self.d["m " + str(e) + nr])].\
                            grid(row=10, column= -1+self.d["m " + str(e) + nr],pady=5, padx=5, sticky="s")
                    elif 2<self.d["m "+ str(e) + nr] <5:
                        self.d["matlab {0}".format(str(e)) + str(self.d["m " + str(e) + nr])] = ttk.Label(
                            self.d["barrierf " + str(e) + nr], text="#" + str(self.d["m " + str(e) + nr]) + ":")
                        self.d["matlab " + str(e) + str(self.d["m " + str(e) + nr])].grid(row=11, column= -3+self.
                            d["m " + str(e) + nr], sticky="w")
                        self.d["mater " + str(e) + str(self.d["m " + str(e) + nr])].grid(row=11, column= -3+self.
                            d["m " + str(e) + nr ],pady=5, padx=5, sticky="s")
                    else:
                        self.d["matlab {0}".format(str(e)) + str(self.d["m " + str(e) + nr])] = ttk.Label(
                            self.d["barrierf " + str(e) + nr], text="#" + str(self.d["m " + str(e) + nr]) + ":")
                        self.d["matlab " + str(e) + str(self.d["m " + str(e) + nr])]. grid(row=12, column= -5+self.
                            d["m " + str(e) + nr], sticky="w")
                        self.d["mater " + str(e) + str(self.d["m " + str(e) + nr])].grid(row=12, column=-5 + self.d[
                            "m " + str(e) + nr], pady=5, padx=5, sticky="s")
            else:
                while self.d["m " + str(e) + nr] > self.d[
                    "vnumbmat " + str(e) + nr].get():
                    self.d["mater "+str(e)+str(self.d["m " + str(e) + nr])].destroy()
                    self.d["matlab " + str(e) + str(self.d["m " + str(e) + nr])].destroy()
                    self.d["m " + str(e) + nr] -= 1

    def pres(self,e,nr):
        if self.d["preshvar " + str(e) + nr].get()== 1:
            self.d["radbucky "+str(e)] = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                variable=self.d["radiob_pre " + str(e)+nr], text="Bucky", value=1)
            self.d["radbucky " + str(e)].grid(row=5, column=0, pady=10, padx=10, sticky="w")
            self.d["radcross " +str(e)] = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                variable=self.d["radiob_pre " + str(e)+nr], text="Cross-table", value=2)
            self.d["radcross " + str(e)].grid(row=5, column=1, pady=10, padx=10, sticky="w")

        elif self.d["preshvar "+str(e) + nr].get()==0:

            if self.d["radbucky " + str(e)] is not None:
                self.d["radbucky " + str(e)].destroy()
                self.d["radcross " +str(e)].destroy()

    def leakage(self,e,nr):
        if self.d["airkerv " + str(e) + nr].get()== 1:
            if self.d["radside " + str(e)+nr] is not None:
                self.d["radside " + str(e)+nr].destroy()
                self.d["radforward " +str(e)+nr].destroy()
                self.d["radleak " + str(e) + nr].destroy()
            if self.d["laks "+ str(e) + nr] is not None:
                self.d["laks " + str(e) + nr].destroy()
                self.d["entk " + str(e) + nr].destroy()
            self.d["radside "+str(e)+nr] = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                variable=self.d["radiob_leak " + str(e)+nr], text="Leakage and Side-Scatter", value=1)
            self.d["radside " + str(e)+nr].grid(row=4, column=0, pady=10, padx=10, sticky="w")
            self.d["radforward " +str(e)+nr] = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                variable=self.d["radiob_leak " + str(e)+nr], text="Leakage and Forward/ Backscatter", value=2)
            self.d["radforward " + str(e)+nr].grid(row=4, column=1, pady=10, padx=10, sticky="w")
            self.d["radleak " + str(e) + nr] = ttk.Radiobutton(master=self.d["barrierf " + str(e) + nr],
                                                                  variable=self.d["radiob_leak " + str(e) + nr],
                                                                  text="Only Leakage", value=0)
            self.d["radleak " + str(e) + nr].grid(row=5, column=0, pady=10, padx=10, sticky="w")

        elif self.d["airkerv " + str(e) + nr].get()== 4:
            if self.d["radside " + str(e)+nr] is not None:
                self.d["radside " + str(e)+nr].destroy()
                self.d["radforward " +str(e)+nr].destroy()
                self.d["radleak " + str(e) + nr].destroy()
            if self.d["laks "+ str(e) + nr] is not None:
                self.d["laks " + str(e) + nr].destroy()
                self.d["entk " + str(e) + nr].destroy()
            self.d["laks "+ str(e) + nr]=ttk.Label(master=self.d["barrierf " + str(e) + nr], text="K\u209b (mGy/patient):")
            self.d["laks "+ str(e) + nr].grid(row=4, column=0, pady=10, padx=10, sticky="w")
            self.d["entk "+ str(e) + nr]=ttk.Entry(master=self.d["barrierf " + str(e) + nr], width=10)
            self.d["entk " + str(e) + nr].grid(row=4, column=1, pady=10, padx=10, sticky="w")

        else:
            if self.d["radside " + str(e)+nr] is not None:
                self.d["radside " + str(e)+nr].destroy()
                self.d["radforward " +str(e)+nr].destroy()
                self.d["radleak " + str(e) + nr].destroy()
            if self.d["laks "+ str(e) + nr] is not None:
                self.d["laks " + str(e) + nr].destroy()
                self.d["entk " + str(e) + nr].destroy()

        # ============selection of X-ray room or X-ray tube=============
    def XrRoom1(self,e,nr, t):
        if self.d["vselxray " +str(e)+nr].get() == 1:
            if self.d["selxroom " +str(e)+nr] is not None:
                self.d["selxroom " +str(e)+nr].destroy()
            self.xrooms = (
            "Rad Room (chest bucky)", "Rad Room (floor or other barriers)", "Rad Room (all barriers)",
            "Fluoroscopy Tube (R&F room)","Rad Tube (R&F room)", "Chest Room", "Mammography Room", "Cardiac Angiography",
            "Peripheral Angiography")
            self.d["vsexroom {0}".format(str(e))+nr] = StringVar()
            self.d["selxroom " +str(e)+nr] = ttk.OptionMenu(self.d["barrierf " + str(e) + nr], self.d["vsexroom " + str(e)+nr],
                                                          "Select X-ray room", *self.xrooms)
            self.d["selxroom " +str(e)+nr].grid(row=16, column=0, columnspan=2, pady=10, padx=10, sticky="w")
        elif self.d["vselxray " +str(e)+nr].get() == 2:
            if self.d["selxroom " +str(e)+nr] is not None:
                self.d["selxroom " +str(e)+nr].destroy()
            self.d["vsexroom {0}".format(str(e))+nr] = IntVar(value=25)
            self.d["selxroom "+str(e)+nr] = ttk.Spinbox(master=self.d["barrierf " + str(e) + nr], from_=25, to=150,
                                                       increment=5, textvariable=self.d["vsexroom " + str(e)+nr],
                                                       width=10)
            self.d["selxroom " +str(e)+nr].grid(row=16, column=1, columnspan=2, pady=10, padx=10, sticky="w")
