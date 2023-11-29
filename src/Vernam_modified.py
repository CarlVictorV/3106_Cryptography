import hashlib


class Vernam_modified:
    def __init__(self, key):
        self.key = key
        self.key_length = len(key)

    def encrypt(self, message):
        encrypted_message = ""
        for i in range(len(message)):
            encrypted_char = chr(ord(message[i]) ^ ord(
                self.key[i % self.key_length]))
            encrypted_message += encrypted_char
        # convert to hex
        encrypted_message = encrypted_message.encode('utf-8').hex()
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        # convert from hex
        encrypted_message = bytearray.fromhex(encrypted_message).decode()
        for i in range(len(encrypted_message)):
            decrypted_char = chr(ord(encrypted_message[i]) ^ ord(
                self.key[i % self.key_length]))
            decrypted_message += decrypted_char
        return decrypted_message

    def getKey(self):
        return self.key


def main():
    myMessage = "(@IDb^GQ0Tm<euH+$EQT2m<euH+$EQT2m>dtHb*F22n3OdJo%eHRl41P#tHb%GnR2P<dtp@fcTPRQO$ICb^cTQS2/@MD?^cTPRQO$ICb^cR12O{?tq#^cS12UO^HodPISQ3O<^IC#PISQ3O<^IC#PISQ3O<^IC#PFQQ2R(!JocPFQQ2R(!JocPFQQ2R(!JocPt21S1{cJDM^GRP2S<!tFM$s2NVOOeKFMgr3Q2UO#IZ?#H2QTP>cuZ#eFR122>deF@%sPPVQ\$eF@%sPPVQ\$eC?%rSRQROdeF!$G2RRPO$eC?%rSRQROdeDdfKPPPP{ceDceEVN23($eqbfH2T2R<NMq+*GU12T`#uo%eKQ04m{eGH!&s2SnSO!IpbfH3lR3>?HGd@ERlT1>$vG$%JUlT1>$vG$%JUlT1>$vG$%JUlR2O?MBbgITlTQ<@tF!#rTlR3P^GD+#K2lS2O^tH?etnR2R(eLG@&Jn222>cMo@$cS12UO^HodPK4NVQ)dtGM$tSNQTQ?GDM^GRP2S<!tFM^HS1PQ{@HFM$s2NVOOeKFM*tPTRTPcLZ!gHPOU3/?IZ!gHPOU3/?IZ#%H3NRU<!KZ!gsVNRO\^tZdesS0V1>@eqbfH2T2R<NHC@eHTOS1PNMq+*GU12T`etp@eK2QRm<dtB%@r4RTm(@IDb^GQ0Tm(cHDcesS1nS<@Io#$F2RnQQ#GC$gEPPnSO#Kq$&HUSnSO!IpbfH3lTR>dGD%$FTlQP>cJF?%r3l41P#tHb%GnOQRO#KC@esnP31/^God^InRSRP?IH!#InOQRO#KC@esnR2R(eLG@&JnP42{?IB?*rnRSRP?IH!#InR2P<dtp@fcQOS1>$HEbfcTQS2/@MD?^cV2PU<%uo$PG30PU/cvF#PH30V1{!tqM^rSR4T)#LGM%s2T2U\cvZ!gHPOU3/?IZ#eFR122>deF!$G2RRPO$eFb%I4SUR)%eF@%sPPVQ\$eF!$G2RRPO$eF@%sPPVQ\$eDceEVN23($eqbfH2T2R<NKE@fERTRP(NIqc*ERNQUONJpb*rVO23`#uo%eKQ04m>dtHb*F22nUQ?MD$frUlT1>$vG$%JUlR3P^GD+#K2lR2O?MBbgITl41P#tHb%GnOQRO#KC@esnR2P<dtp@fcTQS2/@MD?^cTQS2/@MD?^cQOS1>$HEbfcTPRQO$ICb^cQOS1>$HEbfcR23U/@GC%ecR12O{?tq#^cTPRQO$ICb^cR23U/@GC%ecS12UO^HodPI2QT3)%JG$Pt21S1{cJDM%s2T2U\cvZ%gEVPU2O%eDd%EQS4O/@eF!$G2RRPO$eF@%sPPVQ\$eDceEVN23($eEceK2TQ1QNKE@fERTRP(NKE@fERTRP(Nvoc%rV0SQ`$JEc@GVPQS`$tC!fr3Q3mQcuEb*rSPnS<@Io#$F2RnSO#Kq$&HUSnQQ#GC$gEPPnQPcGH+etTRnSO!IpbfH3lV3/^IGceJnR2R(eLG@&Jn222>cMo@$cV2PU<%uo$PI2OR2OdJpM%s2T2U\cvZ?#H2QTP>cuZ!gsVNRO\^tZ%gEVPU2O%eDceEVN23($eF!$G2RRPO$eDdfKPPPP{ceEceK2TQ1QNKo@^tUSST)Nvoc%rV0SQ`#uo%eKQ04m{eGH!&s2SnQQ#GC$gEPPnS<@Io#$F2RnS>#uB!*GQRnQPcGH+etTRnUQ?MD$frUlR3>?HGd@ERlR3>?HGd@ERlTR>dGD%$FTlR3P^GD+#K2l41P#tHb%Gn222>cMo@$cQOS1>$HEbfcV2PU<%uo$Pt21S1{cJDM$s2NVOOeKFM^GRP2S<!tFM^rQP31P#uZ#$GR0TQ\cKZ!gHPOU3/?IZ#eHT2UT>%LZ#eFR122>deF@%sPPVQ\$eC?%rSRQROdeqbfH2T2R<NHC@eHTOS1PNIpb@KP04S(Nvoc%rV0SQ`^vB%$J30Um>dtHb*F22nUQ?MD$frUlT1\@uoc%snP4R/!Lq+@GnR2R(eLG@&JnR2R(eLG@&JnR2R(eLG@&JnP31/^God^In222>cMo@$cV2PU<%uo$PH30V1{!tqM*tPTRTPcLZ#eFR122>deDd%EQS4O/@eFb%I4SUR)%eFb%I4SUR)%eFb%I4SUR)%eDceEVN23($eEceK2TQ1QNKE@fERTRP(NKE@fERTRP(NKE@fERTRP(NHC@eHTOS1PNHC@eHTOS1PNHC@eHTOS1PNvoc%rV0SQ`$ID!eIRO2S`@uo+*E22TS`$JEc@GVPQS`!HEb%IQQ22`$tE#gJUQUT`@vp%@GPOV1`$JEc@GVPQS`$tC!fr3Q3m\!Jo@^FS03m(#Jp+$KROTm{eGH!&s2SnQPcGH+etTRnUQ?MD$frUlT1\@uoc%snP4R/!Lq+@GnR2P<dtp@fcTPRQO$ICb^cV2PU<%uo$PH30V1{!tqM%s2T2U\cvZ?#H2QTP>cuZ%gEVPU2O%eDceEVN23($eqbfH2T2R<NHC@eHTOS1PNKo?$s21S2`$JEc@GVPQS`$JEc@GVPQS`!HEb%IQQ22`$ID!eIRO2S`!HEb%IQQ22`@vp%@GPOV1`@uo+*E22TS`#uo%eKQ04m(#Jp+$KROTm(#Jp+$KROTm(#Jp+$KROTm\!Jo@^FS03m\!Jo@^FS03m\!Jo@^FS03mQcuEb*rSPnS<@Io#$F2RnQPcGH+etTRnRPcMo%#r4l41P#tHb%Gn222>cMo@$cT0QQPcuEcPI2QT3)%JG$PI2OR2OdJpM^HS1PQ{@HFM^GRP2S<!tFM^rSR4T)#LGM^rQP31P#u"
    md5 = hashlib.md5(myMessage.encode())
    sha256 = hashlib.sha256(myMessage.encode())
    myKey = md5.hexdigest() + sha256.hexdigest()
    print('Message  : %s' % (myMessage))

    myCipher = Vernam_modified(myKey)
    ciphertext = myCipher.encrypt(myMessage)
    print('Encrypted: ' + ciphertext)
    plaintext = myCipher.decrypt(ciphertext)
    print('Decrypted: %s' % (plaintext))


if __name__ == '__main__':
    main()
