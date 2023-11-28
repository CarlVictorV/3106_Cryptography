encrypted_text = '\$uB$#rUlR2(dMEbgc30QS)#uCMfs31SR{?eC@%GS0SS`dHq#fs30nT{eLB?frnOPO\#vE$PKU2US\!LZbesU2S2QNuo?^JS1Qm\#JD@eHTl3PQ$upcecUT4T/!uoMfs31SR{?epcfsSQVO`@uFc*H22nP/?HEd%Jn0PSP%ID#Ps2OTT>dHZ!fI3TS1QNtq$eISPQ'
        print("Encrypted File Data:\n " + encrypted_text)
        print("ARE THEY THE SAME? : ")
        print(self.file_data == encrypted_text)
        self.file_data =  self.file_data[1:]
        print("ARE THEY THE SAME? : ")
        print(self.file_data == encrypted_text)