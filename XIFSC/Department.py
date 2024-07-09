import os
import tkinter
from tkinter import *
from tkinter import ttk
import xlsxwriter

class ddepartment():
    # ============creating def for Deparment notebook===================================
    def creatdep(self):
        self.depbutton.destroy()
        self.roombutton.destroy()
        self.CTbutton.destroy()
        self.quickbutton.destroy()
        self.chooseCal.destroy()
        if self.depnote is None:
            self.depnote = ttk.Notebook(self.new_main_Frame, style="AL.TNotebook")
            self.depnote.configure(width=955, height=728)
            self.depnote.grid(row=0, sticky="w")

        self.depframe = ttk.Frame(self.depnote)
        self.depframe.pack(fill=BOTH, expand=1)
        self.depnote.add(self.depframe, text="Department")

        #======Departmet scrollbar=========
        self.depcanv= Canvas(self.depframe)
        self.depcanv.pack(side=LEFT, fill=BOTH, expand=1)
        self.scrolldep = ttk.Scrollbar (self.depframe, orient= VERTICAL, command= self.depcanv.yview)
        self.scrolldep.pack(side =RIGHT, fill=Y)
        self.depcanv.configure(yscrollcommand=self.scrolldep.set,bg="#f7faf9")
        # =========Department tab===========================
        self.roomsframe = ttk.Frame(self.depcanv)
        self.roomsframe.bind('<Configure>', lambda e: self.depcanv.configure(scrollregion=self.depcanv.bbox("all")))
        self.depcanv.create_window((0,0), window=self.roomsframe, anchor="nw")

        self.label_rooms = ttk.Label(master=self.roomsframe, style="BL.TLabel", text="Rooms of Department")
        self.label_rooms.grid(row=0, column=0, sticky="nswe")
        self.numrlab = ttk.Label(master=self.roomsframe, style="AL.TLabel", text="Number of Rooms:")
        self.numrlab.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.numrooms = IntVar(value=0)
        self.num_rooms = ttk.Spinbox(master=self.roomsframe, from_=0, to=100000, increment=1,
                                     textvariable=self.numrooms, width=5, command=self.createrooms)
        self.num_rooms.grid(row=1, column=1, pady=10, padx=20, sticky="e")


    def createrooms(self):
        if self.i< self.numrooms.get():
            while self.i <self.numrooms.get():
                self.i += 1
                self.d["labelname {0}".format(str(self.i))] \
                    = ttk.Label(master=self.roomsframe, style="AL.TLabel", text="Room Description " + str(self.i) + ":")
                self.d["labelname "+str(self.i)].grid(row=2+self.i, column=0,padx=10,pady=10, sticky ="w")
                self.d["name_room {0}".format(self.i)] = ttk.Entry(master=self.roomsframe)
                self.d["name_room "+str(self.i)].grid(row=2+self.i, column =1, sticky="w")
                self.d["vselroom {0}".format(self.i)] = StringVar()
                self.d["selroom {0}".format(self.i)] = ttk.Combobox(master=self.roomsframe, textvariable=self.d["vselroom "+str(self.i)],
                                        values=["X-Ray room", "From X-Ray room", "CT Room"], state="readonly")
                self.d["selroom "+str(self.i)].grid(row=2+self.i, column=2, pady=10, padx=20, sticky="w")
                self.d["selroom {0}".format(self.i)].set("Shield room")
                """self.method = ("BIR 2012","NCRP 147")
                self.d["vmethod {0}".format(self.i)] = StringVar()
                self.d["method {0}".format(self.i)] = ttk.OptionMenu(self.roomsframe, 
                                                                     self.d["vmethod "+str(self.i)],"Select Method", *self.method)
                self.d["method "+str(self.i)].grid(row=2+self.i, column=3, padx=10, pady=10, sticky="w")"""
                #======Design button===============
                self.d["run {0}".format(str(self.i))] = False # run every room only one
                self.d["crroomb {0}".format(self.i)] \
                    = ttk.Button(master=self.roomsframe, text="Design", command= lambda t=self.i :self.desroom(t))
                self.d["crroomb "+str(self.i)].grid(row=2+self.i, column=4, padx=10, pady=10, sticky="w")
                #=======export data to ecxel=========
                self.exp_but = ttk.Button(master=self.roomsframe, text="Export to Excel",
                                          command=lambda t=self.i: self.exp_dep(t))
                self.exp_but.grid(row=1, column=2, pady=10, padx=10, sticky="w")
            #==========αρχικοποίηση τιμών==============
                self.d["resframe {0}".format(str(self.i))]=None

        else:
            while self.i > self.numrooms.get():
                self.d["labelname "+str(self.i)].destroy()
                self.d["name_room "+str(self.i)].destroy()
                self.d["selroom " + str(self.i)].destroy()
                self.d["crroomb " + str(self.i)].destroy()
                #self.d["method " + str(self.i)].destroy()
                if self.d["run " + str(self.i)]==True:
                    self.d["newroomf " + str(self.i)].destroy()
                    self.d["resframe " + str(self.i)].destroy()
                    if self.i == 1:
                        self.resnote.destroy()
                self.i -= 1
    def desroom(self, t):
        if self.d["vselroom "+str(t)].get()!="Shield room":
            if self.d["run "+str(t)] == False:
                if self.i == 1:
                    self.resnote = ttk.Notebook(self.new_main_Frame, style="AL.TNotebook")
                    self.resnote.grid(row=0, column=1, sticky="w")
                    self.resnote.configure(width=562, height=728)
                elif self.i>0 and self.resnote is None:
                    self.resnote = ttk.Notebook(self.new_main_Frame, style="AL.TNotebook")
                    self.resnote.grid(row=0, column=1, sticky="w")
                    self.resnote.configure(width=562, height=728)
                #==========αρχικοποίηση τιμών =================
                self.d["selxroom {0}".format(str(t))] = None
                self.d["numpapwl {0}".format(str(t))] = None
                self.d["numpapwe {0}".format(str(t))] = None
                self.d["sellocation {0}".format((str(t)))] = None

                self.d["newroomf {0}".format(str(t))] = ttk.Frame(self.depnote)
                self.d["newroomf " + str(t)].pack()
                self.depnote.add(self.d["newroomf " + str(t)], text=self.d["name_room " + str(t)].get())
                self.depnote.grid()
                #======================scrollbars============
                self.roomcanv = Canvas(self.d["newroomf " + str(t)])

                self.xscrollroom = ttk.Scrollbar(self.d["newroomf " + str(t)], orient=HORIZONTAL, command=self.roomcanv.xview)
                self.xscrollroom.pack(side=BOTTOM, fill=X)
                self.yscrollroom = ttk.Scrollbar(self.d["newroomf " + str(t)], orient=VERTICAL, command=self.roomcanv.yview)
                self.yscrollroom.pack(side=RIGHT, fill=Y)
                self.roomcanv.configure(yscrollcommand=self.yscrollroom.set, xscrollcommand=self.xscrollroom.set, bg="#f7faf9")
                self.roomcanv.pack(side=LEFT, fill=BOTH, expand=1)
                self.d["frame_1 {0}".format(str(t))] = ttk.Frame(self.roomcanv)
                self.d["frame_1 " + str(t)].bind('<Configure>',
                                                 lambda e: self.roomcanv.configure(scrollregion=self.roomcanv.bbox("all")))
                self.roomcanv.create_window((0, 0), window=self.d["frame_1 " + str(t)], anchor="nw")
                #============ονομάζουμε κάποιες τιμές=================
                self.d["x {0}".format(str(t))] = 0
                self.d["y {0}".format(str(t))] = 0
                self.d["nr {0}".format(str(t))] = self.d["labelname "+str(t)].cget("text")
                self.ep=1
                self.d["noteb {0}".format(str(t) + self.d["nr "+str(t)])] = ttk.Notebook(self.d["frame_1 " + str(t)],
                                                                       style="BL.TNotebook")
                #==============Number of Barriers in the Room==========
                self.lanumwall = ttk.Label(master=self.d["frame_1 "+str(t)], style="AL.TLabel", text="Number of Barriers")
                self.lanumwall.grid(row=0, column=0, pady=5, padx=5, sticky="w")
                self.d["vnumwall {0}".format(str(t))] = IntVar(value=7)
                self.d["numwall {0}".format(str(t))] \
                    = ttk.Spinbox(master=self.d["frame_1 "+str(t)], textvariable=self.d["vnumwall "+str(t)],
                                           from_=7, to=50, width=5, command= lambda :self.barriers(t))
                self.d["numwall "+str(t)].grid(row=0, column=1, pady=5, padx=5, sticky="w")
                self.barriers(t)
                # ======Destroy button======
                self.closBut = ttk.Button(self.d["newroomf " + str(t)], text="X", width=4, command=lambda: self.closedeproom(t))
                self.closBut.pack()
                #===========Combine Barriers as one=======================
                if self.d["vselroom "+str(t)].get() != "CT Room":
                    self.d["comnum {0}".format(str(t))] = 0
                    self.d["combarr {0}".format(str(t)) + str(self.d["comnum " + str(t)])]=None
                    self.d["varcompb {0}".format(str(t))] = IntVar(value=0)
                    self.d["compb {0}".format(str(t))]=ttk.Checkbutton(master=self.d["frame_1 "+str(t)],text="Combine Barriers as one",
                                                                       variable=self.d["varcompb "+str(t)], onvalue=1, offvalue=0, command=lambda: self.combination(t))
                    self.d["compb "+str(t)].grid(row=10, column=0, pady=5, padx=5, sticky="w")

                if self.d["vselroom {0}".format(str(t))].get()=="From X-Ray room":
                #=========Occupation Factor not xray room=================
                    self.title_ocupat =ttk.Label(master=self.d["frame_1 "+str(t)], style="BL.TLabel", text="Occupancy Factor (T)")
                    self.title_ocupat.grid(row=1, column=0, pady=5, padx=5, sticky="w")
                    # =========Classify area=============
                    self.d["area {0}".format(str(t))] = StringVar()
                    self.d["area {0}".format(str(t)) ] = ttk.Combobox(
                        master=self.d["frame_1 "+str(t)],
                        textvariable=self.d["area " + str(t) ],
                        values=["Cotrolled Area", "Uncontrolled Area", "Supervised Area"], state="readonly")
                    self.d["area " + str(t)].config(width= 16)
                    self.d["area " + str(t) ].grid(row=1, column=1, pady=5, padx=5, sticky="w")
                    self.d["area {0}".format(str(t)) ].set("Classify the area")
                    # ====radiobutton_occupancy factor==================
                    self.d["vraoccup {0}".format(str(t))] = IntVar(value=0)
                    self.raoccup = ttk.Radiobutton(master=self.d["frame_1 " + str(t)], variable=self.d["vraoccup " + str(t)],
                                                   text="Write occupancy factor (T):", value=1,
                                                   command=lambda: self.occupation(t))
                    self.raoccup.grid(row=2, column=0, pady=10, padx=10, sticky="w")
                    self.d["occupentry {0}".format(str(t))] = None
                    self.raseloccup = ttk.Radiobutton(master=self.d["frame_1 " + str(t)], text="or select Location "
                                                                                               "[suggested NCRP 147]",
                                                  variable=self.d["vraoccup " + str(t)], value=2,
                                                  command=lambda: self.occupation(t))
                    self.raseloccup.grid(row=3, column=0, pady=10, padx=10, sticky="w")
                    # ========Design Kerma Goal===========
                    self.ladike = ttk.Label(master=self.d["frame_1 " + str(t)], style="AL.TLabel",
                                            text="Design Kerma Goal (mGy/week):")
                    self.ladike.grid(row=4, column=0, pady=10, padx=10, sticky="w")
                    self.d["dikeent {0}".format(str(t))] = ttk.Entry(master=self.d["frame_1 " + str(t)], width=10)
                    self.d["dikeent " + str(t)].grid(row=4, column=1, pady=10, padx=10, sticky="w")
                elif self.d["vselroom {0}".format(str(t))].get() == "X-Ray room":
                    # ========Workload===========
                    self.title_workload =ttk.Label(master=self.d["frame_1 "+str(t)], style="BL.TLabel", text="Workload")
                    self.title_workload.grid(row=1, column=0, pady=5, padx=5, sticky="w")
                    # =========X-ray Rooms============
                    self.xrayLabel = ttk.Label(master=self.d["frame_1 " + str(t)],
                                               text="Select X-Ray room or give tube kVp")
                    self.xrayLabel.grid(row=2,column=0, padx=5, pady=5, sticky="w")
                    #======X-ray Room or kVp==========
                    self.d["vselxray {0}".format(str(t))] = IntVar(value=0)
                    self.d["selxray1 {0}".format(str(t))] = ttk.Radiobutton(master=self.d["frame_1 " + str(t)],
                                                                            variable=self.d["vselxray "+str(t)], text="Select X-Ray Room",
                                                   value=1, command=lambda : self.XrRoom(t))
                    self.d["selxray1 " +str(t)].grid(row=3, column=0, pady=5, padx=5, sticky="w")

                    self.d["selxray2 {0}".format(str(t))] = ttk.Radiobutton(master=self.d["frame_1 " + str(t)],
                                                                            variable=self.d["vselxray "+str(t)], text="Give kVp", value=2,
                                                   command=lambda : self.XrRoom(t))
                    self.d["selxray2 "+str(t)].grid(row=3, column=1, pady=5, padx=5, sticky="w")

                    #=====================Write workload========================
                    self.d["worentry {0}".format(str(t))] = None
                    self.d["vrawork {0}".format(str(t))]=IntVar(value=0)
                    self.raworkl = ttk.Radiobutton(master=self.d["frame_1 " + str(t)], variable=self.d["vrawork "+str(t)],
                                                   text="Write total Workload (mA min/week):",
                                                   value=1,command= lambda : self.workload(t))
                    self.raworkl.grid(row=5, column=0, pady=5, padx=5, sticky="w")

                    self.ranumb = ttk.Radiobutton(master=self.d["frame_1 " + str(t)], text="or the number of patients per week:",
                                                   variable=self.d["vrawork " + str(t)], value=2,command=lambda :self.workload(t))
                    self.ranumb.grid(row=6, column=0, pady=5, padx=5, sticky="w")
            #==============CT==================================================
                elif self.d["vselroom {0}".format(str(t))].get() == "CT Room":
                    self.bp_label = ttk.Label(
                        master=self.d["frame_1 " + str(t)],
                        text='Body Procedures (weekly):')
                    self.bp_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
                    self.d["bp_var {0}".format(str(t))] = IntVar()
                    self.bp_entry = ttk.Entry(
                        master=self.d["frame_1 " + str(t)],
                        textvariable=self.d["bp_var "+str(t)], width=10)
                    self.bp_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
                    self.hp_label = ttk.Label(
                        master=self.d["frame_1 " + str(t)],
                        text='Head Procedures (weekly):')
                    self.hp_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
                    self.d["hp_var {0}".format(str(t))] = IntVar()
                    self.hp_entry = ttk.Entry(
                        master=self.d["frame_1 " + str(t)],
                        textvariable=self.d["hp_var " + str(t)], width=10)
                    self.hp_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
                    self.kvp_label = ttk.Label(master=self.d["frame_1 " + str(t)], text='Give kVp:')
                    self.kvp_label.grid(row=6, column=0, padx=10, pady=10, sticky = "w")
                    self.d["kvp_var {0}".format(str(t))] = IntVar()
                    self.d["kvp_var "+ str(t)].set(120)  # default value
                    self.kvp_dropdown = ttk.Combobox(master=self.d["frame_1 " + str(t)],
                                                     textvariable=self.d["kvp_var "+ str(t)], values=[120, 140], state="readonly", width=7)
                    self.kvp_dropdown.grid(row=6, column=1, padx=10, pady=10, sticky = "w")
                    # ==============CT=====DLP==================================
                    self.dlpb_label = ttk.Label(master=self.d["frame_1 " + str(t)], text='DLP for body (mGy∙cm):')
                    self.dlpb_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
                    self.d["dlpb_var {0}".format(str(t))] = ttk.Entry(master=self.d["frame_1 " + str(t)],
                                                                           width=10)
                    self.d["dlpb_var " + str(t)].grid(row=4, column=1, padx=10, pady=10, sticky="w")

                    self.dlph_label = ttk.Label(master=self.d["frame_1 " + str(t)], text='DLP for head (mGy∙cm):')
                    self.dlph_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
                    self.d['dlph_var {0}'.format(str(t))] = ttk.Entry(master=self.d["frame_1 " + str(t)],
                                                                           width=10)
                    self.d['dlph_var ' + str(t)].grid(row=5, column=1, padx=10, pady=10, sticky="w")
                #==========Results==============
                if self.d["resframe "+ str(t)] is None:
                    self.d["resframe "+ str(t)] = ttk.Frame(self.resnote)
                    self.d["resframe "+ str(t)].pack()

                self.resnote.add(self.d["resframe "+ str(t)], text="Results of "+ self.d["name_room " + str(t)].get())

                # ======Results scrollbar=========
                self.rescanv = Canvas(self.d["resframe "+ str(t)])

                self.scrollres = ttk.Scrollbar(self.d["resframe "+ str(t)], orient=VERTICAL, command=self.rescanv.yview)
                self.scrollres.pack(side=RIGHT, fill=Y)
                self.xscrollres = ttk.Scrollbar(self.d["resframe "+ str(t)], orient=HORIZONTAL,
                                                 command=self.rescanv.xview)
                self.xscrollres.pack(side=BOTTOM, fill=X)
                self.rescanv.configure(yscrollcommand=self.scrollres.set, xscrollcommand=self.xscrollres.set, bg="#f7faf9")
                self.rescanv.pack(side=LEFT, fill=BOTH, expand=1)
                # =========Results tab===========================
                self.d["resultframe {0}".format(str(t))+self.d["nr "+str(t)]] = ttk.Frame(self.rescanv)
                self.d["resultframe "+str(t)+self.d["nr "+str(t)]].bind('<Configure>', lambda e: self.rescanv.configure(scrollregion=self.rescanv.bbox("all")))
                self.rescanv.create_window((0, 0), window=self.d["resultframe "+str(t)+self.d["nr "+str(t)]], anchor="nw")


                self.reshield= ttk.Label(self.d["resultframe "+str(t)+self.d["nr "+str(t)]], style="BL.TLabel",text="The Shielding of:")
                self.reshield.grid(sticky="w")
                self.d["run "+str(t)] = True
            self.depnote.select(self.d["newroomf " + str(t)])
            self.resnote.select(self.d["resframe "+ str(t)])
    #============selection of X-ray room or X-ray tube=============
    def XrRoom(self,t):
        if self.d["vselxray "+ str(t)].get() == 1:
            if self.d["selxroom " + str(t)] is not None:
                self.d["selxroom " + str(t)].destroy()
            self.xrooms = ("Rad Room (chest bucky)","Rad Room (floor or other barriers)","Rad Room (all barriers)", "Fluoroscopy Tube (R&F room)","Rad Tube (R&F room)", "Chest Room", "Mammography Room",
                           "Cardiac Angiography", "Peripheral Angiography")
            self.d["vsexroom {0}".format(str(t))] = StringVar()
            self.d["selxroom " + str(t)] = ttk.OptionMenu(self.d["frame_1 " + str(t)], self.d["vsexroom " + str(t)],
                                                          "Select X-ray room", *self.xrooms)
            self.d["selxroom " + str(t)].grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="w")
        elif self.d["vselxray "+ str(t)].get() == 2:
            if self.d["selxroom " + str(t)] is not None:
                self.d["selxroom " + str(t)].destroy()
            self.d["vsexroom {0}".format(str(t))] = IntVar(value=25)
            self.d["selxroom " + str(t)] = ttk.Spinbox(master=self.d["frame_1 " + str(t)], from_=25, to=150,
                                                       increment=5, textvariable=self.d["vsexroom " + str(t)], width=10)
            self.d["selxroom " + str(t)].grid(row=4, column=1, columnspan=2, pady=10, padx=10, sticky="w")

    def occupation(self, t):
        if self.d["vraoccup " + str(t)].get() == 1:
            if self.d["sellocation " + str(t)] is not None:
                self.d["sellocation " + str(t)].destroy()
            if self.d["occupentry " + str(t)] is not None:
                self.d["occupentry " + str(t)].destroy()
            self.d["vselocation {0}".format(str(t))] = StringVar()
            self.d["occupentry " + str(t)] = ttk.Entry(master=self.d["frame_1 " + str(t)], width=10)
            if self.d["area " + str(t)].get() == "Cotrolled Area":
                self.d["occupentry " + str(t)].insert(0,str(1))
            elif self.d["area " + str(t)].get() == "Uncontrolled Area":
                self.d["occupentry " + str(t)].insert(0,str(1/16))
            elif self.d["area " + str(t)].get() == "Supervised Area":
                self.d["occupentry " + str(t)].insert(0,str(1/4))
            self.d["occupentry " + str(t)].grid(row=2, column=1, pady=5, padx=5)
        elif self.d["vraoccup " + str(t)].get() == 2:
            if self.d["occupentry " + str(t)] is not None:
                self.d["occupentry " + str(t)].destroy()
            if self.d["sellocation " + str(t)] is not None:
                self.d["sellocation " + str(t)].destroy()
            self.d["vselocation {0}".format(str(t))] = StringVar()
            if self.d["area " + str(t)].get() == "Cotrolled Area":
                self.control = ("Administrative or clerical offices", "Laboratories",
                                "Pharmacies and other work areas fully occupied by an individual", "Receptionist areas",
                                "Attended waiting rooms", "Children’s indoor play areas", "Adjacent x-ray rooms",
                                "Film reading areas", "Nurse’s stations", "X-ray control rooms",
                                "Rooms used for patient examinations and treatments")
                self.d["sellocation " + str(t)] = ttk.OptionMenu(self.d["frame_1 " + str(t)],
                                                                 self.d["vselocation " + str(t)], "Select Location",
                                                                 *self.control)
            elif self.d["area " + str(t)].get() == "Uncontrolled Area":
                self.uncontroll = (
                "Public toilets", "Unattended vending areas", "Storage  rooms", "Outdoor areas with seating",
                "Unattended waiting rooms", "Patient holding areas",
                "Outdoor areas with only transient pedestrian or vehicular traffic", "Unattended parking lots",
                "Vehicular drop off areas (unattended)", "Attics", "Stairways", "Unattended elevators",
                "Janitor’s closets")
                self.d["sellocation " + str(t)] = ttk.OptionMenu(self.d["frame_1 " + str(t)],
                                                                 self.d["vselocation " + str(t)], "Select Location",
                                                                 *self.uncontroll)
            elif self.d["area " + str(t)].get() == "Supervised Area":
                self.supervised = ("Corridors", "Patient rooms", "Employee lounges", "Staff restooms", "Corridor doors")
                self.d["sellocation " + str(t)] = ttk.OptionMenu(self.d["frame_1 " + str(t)],
                                                                 self.d["vselocation " + str(t)], "Select Location",
                                                                 *self.supervised)
            else:
                self.d["sellocation " + str(t)] = ttk.Combobox(self.d["frame_1 " + str(t)], textvariable=self.d["vselocation " + str(t)], state="readonly",
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
                                                "Attics", "Stairways", "Unattended elevators", "Janitor’s closets"],)
            self.d["sellocation " + str(t)].config(width=14)
            self.d["sellocation " + str(t)].grid(row=3, column=1,columnspan=2, pady=5, padx=5, sticky="w")
        if self.d["area " + str(t)].get() == "Cotrolled Area":
            self.d["dikeent "+str(t)].destroy()
            self.d["dikeent {0}".format(str(t))] = ttk.Entry(master=self.d["frame_1 " + str(t)], width=10)
            self.d["dikeent " + str(t)].grid(row=4, column=1, pady=5, padx=5, sticky="w")
            self.d["dikeent "+str(t)].insert(0, str(0.2))
        elif self.d["area " + str(t)].get() == "Uncontrolled Area":
            self.d["dikeent " + str(t)].destroy()
            self.d["dikeent {0}".format(str(t))] = ttk.Entry(master=self.d["frame_1 " + str(t)], width=10)
            self.d["dikeent " + str(t)].grid(row=4, column=1, pady=5, padx=5, sticky="w")
            self.d["dikeent "+str(t)].insert(0, str(0.006))
        elif self.d["area " + str(t)].get() == "Supervised Area":
            self.d["dikeent " + str(t)].destroy()
            self.d["dikeent {0}".format(str(t))] = ttk.Entry(master=self.d["frame_1 " + str(t)], width=10)
            self.d["dikeent " + str(t)].grid(row=4, column=1, pady=5, padx=5, sticky="w")
            self.d["dikeent "+str(t)].insert(0, str(0.06))

    def workload(self, t):
        if self.d["vrawork " + str(t)].get() == 1:
            if self.d["numpapwe " + str(t)] is not None:
                self.d["numpapwe " + str(t)].destroy()
            if self.d["worentry " + str(t)] is not None:
                self.d["worentry " + str(t)].destroy()
            self.d["worentry " + str(t)] = ttk.Entry(master=self.d["frame_1 " + str(t)], width=10)
            self.d["worentry " + str(t)].grid(row=5, column=1, pady=5, padx=5)
        elif self.d["vrawork " + str(t)].get() == 2:
            if self.d["worentry " + str(t)] is not None:
                self.d["worentry " + str(t)].destroy()
            if self.d["numpapwe " + str(t)] is not None:
                self.d["numpapwe " + str(t)].destroy()
            self.d["numpapwe " + str(t)] = ttk.Entry(master=self.d["frame_1 " + str(t)], width=10)
            self.d["numpapwe " + str(t)].grid(row=6, column=1, pady=5, padx=5, sticky="w")

    def combination(self,t):
        if self.d["varcompb "+str(t)].get() == 1:
            self.d["vnumbar {0}".format(str(t)) ] = IntVar(value=1)
            self.d["spincom {0}".format(str(t))]=ttk.Spinbox(master=self.d["frame_1 " + str(t)], from_=0 ,to=100,
                        width=5,textvariable=self.d["vnumbar " +str(t)],
                        command=lambda e=self.d["x " + str(t)],nr=self.d["nr "+str(t)] : self.numbcom(e,nr,t))
            self.d["spincom "+ str(t) ].grid(row=10, column=1, padx=10,pady=10, sticky="w")
            self.d["combutton {0}".format(str(t))]=ttk.Button(master=self.d["frame_1 " + str(t)],text="Combine",
                                        command=lambda e=self.d["x " + str(t)],nr=self.d["nr "+str(t)],b=self.d["vnumbar " +str(t)].get() : self.calcom(e,nr,b,t))
            self.d["combutton " + str(t)].grid(row=11, column=1, padx=10,pady=10, sticky="w")
            #==========Combining material==============
            self.mater = ("Lead", "Concrete", "Gypsum Wallboard", "Steel", "Plate Glass", "Wood")
            self.d["vcommater {0}".format(t)] = StringVar()
            self.d["commatter {0}".format(str(t))] = ttk.OptionMenu(self.d["frame_1 " + str(t)]
                , self.d["vcommater " + str(t)],"Select Material", *self.mater)
            self.d["commatter "+str(t)].grid(row=11, column=0, padx=10,pady=10, sticky="w")

        elif self.d["varcompb "+str(t)].get()==0:
            self.d["spincom "+ str(t) ].destroy()
            self.d["combutton " + str(t)].destroy()
            self.d["commatter " + str(t)].destroy()
            if self.d["combarr "+str(t) + str(self.d["comnum " + str(t)])] is not None:
                for i in range(1,self.d["vnumbar " +str(t)].get()+1):
                    self.d["combarr " + str(t) + str(i)].destroy()


    def numbcom(self,e,nr,t):

        if self.d["comnum "+str(t)]  <= self.d["vnumbar " +str(t)].get():
            while self.d["comnum "+str(t)]  < self.d["vnumbar " +str(t)].get():
                self.d["comnum "+str(t)]+=1
                self.d["vcombar {0}".format(nr + str(self.d["comnum "+str(t)]))] = StringVar()
                self.d["combarr "+str(t) + str(self.d["comnum " + str(t)])] = ttk.OptionMenu(
                    self.d["frame_1 " + str(t)],self.d["vcombar "+nr+str(self.d["comnum "+str(t)])],
                    "Select Barrier", *self.barr)
                self.d["combarr "+str(t) + str(self.d["comnum " + str(t)])].grid(row=12+self.d["comnum "+str(t)])
        elif self.d["comnum "+str(t)]  > self.d["vnumbar " +str(t)].get():
            while self.d["comnum "+str(t)]  > self.d["vnumbar " +str(t)].get():
                self.d["combarr " + str(t) + str(self.d["comnum " + str(t)])].destroy()
                self.d["comnum " + str(t)] -= 1


    def exp_dep(self,t):
        import pandas as pd
        for b in range (1,t+1):
            p=self.d["labelname "+str(b)].cget("text")
            for a in range(1,self.d["vnumwall " + str(b)].get()+1):
                    self.wa[self.barn["lab_bar "+str(a) + p].cget("text")]=\
                        [str(self.xlmat["thic "+str(a) + str(1) + p]),str(self.xlmat["thic "+str(a) + str(2) + p]),
                         str(self.xlmat["thic "+str(a) + str(3) + p]),str(self.xlmat["thic "+str(a) + str(4) + p]),
                         str(self.xlmat["thic "+str(a) + str(5) + p]),str(self.xlmat["thic "+str(a) + str(6) + p])]
            self.d["room_data {0}".format(str(b))]=pd.DataFrame(data=self.wa,
                                                                index=["Lead (mm)","Concrete (mm)","Gypsum Wallboard (mm)","Steel (mm)","Plate Glass (mm)","Wood (mm)"])
          user_home = os.path.expanduser('~')  # Get user's home directory
            excel_file_path = os.path.join(user_home, 'Department.xlsx')

        with pd.ExcelWriter(excel_file_path, engine='xlsxwriter',
                            engine_kwargs={'options': {'strings_to_numbers': True}}) as writer:
            for b in range(1, t + 1):
                self.d["room_data " + str(b)].to_excel(writer, sheet_name=self.d["name_room " + str(b)].get())
        os.system(excel_file_path)

    def closedeproom(self,t):
        self.d["newroomf " + str(t)].destroy()
        self.d["labelname " + str(t)].destroy()
        self.d["name_room " + str(t)].destroy()
        self.d["selroom " + str(t)].destroy()
        self.d["crroomb " + str(t)].destroy()
        self.d["resframe " + str(t)].destroy()
        self.d["resultframe " + str(t)+self.d["nr "+str(t)]].destroy()
