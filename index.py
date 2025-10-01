from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'rendi'

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

# =================== PROJECT =============================
@app.route("/project", methods=['GET'])
def project():
    return render_template('project/project.html')

# ======================================= RUNTUTAN ===============================================

                                # ======= BIODATA =========

@app.route("/biodata", methods=['GET','POST'])
def biodata():
    if request.method == 'POST':
        NISgrandy = request.form['NISgrandy']
        namaGrandy = request.form['namaGrandy']
        smpGrandy = request.form['smpGrandy']
        tahunGrandy = request.form['tahunGrandy']
        bulanGrandy = request.form['bulanGrandy']
        jurusanGrandy = request.form['jurusanGrandy']
        tempatGrandy = request.form['tempatGrandy']
        tglGrandy = request.form['tglGrandy']
        jenisGrandy = request.form['jenisGrandy']
        alamatGrandy = request.form['alamatGrandy']
        HobiGrandy = request.form.getlist('HobiGrandy')

        return render_template('runtutan/biodata/2.runtutan_biodata.html', NISgrandy=NISgrandy,
                                            namaGrandy=namaGrandy,
                                            smpGrandy=smpGrandy,
                                            tahunGrandy=tahunGrandy,
                                            bulanGrandy=bulanGrandy,
                                            jurusanGrandy=jurusanGrandy,
                                            tempatGrandy=tempatGrandy,
                                            tglGrandy=tglGrandy,
                                            jenisGrandy=jenisGrandy,
                                            alamatGrandy=alamatGrandy,HobiGrandy=HobiGrandy)
    return render_template('runtutan/biodata/1.runtutan_biodata.html')

                            # ================== GAJI ====================
@app.route("/gajiruntutan", methods=['POST','GET'])
def gajiruntutan():
    if request.method == 'POST':
        namaGrandy=request.form['namaGrandy']
        gajipokokGrandy=float(request.form['gajipokokGrandy'])

        makanGrandy = gajipokokGrandy*0.05
        transfortasiGrandy=gajipokokGrandy*0.10
        gajikotorGrandy=gajipokokGrandy+makanGrandy+transfortasiGrandy
        pajakGrandy=gajikotorGrandy*0.15
        bersihGrandy=gajikotorGrandy-pajakGrandy

        return render_template('runtutan/gaji/2.runtutan_gaji.html',
                            namaGrandy=namaGrandy,
                            gajipokokGrandy=gajipokokGrandy,
                            makanGrandy=makanGrandy,
                            transfortasiGrandy=transfortasiGrandy,
                            gajikotorGrandy=gajikotorGrandy,
                            pajakGrandy=pajakGrandy,
                            bersihGrandy=bersihGrandy)
    return render_template('runtutan/gaji/1.runtutan_gaji.html')

                            # ========= SEGITIGA DAN PERSEGIPANJANG =========

@app.route("/bangundatar", methods=['GET', 'POST'])
def bangundatar():
    if request.method == 'POST':
        try:
            pilih = int(request.form['pilih'])
            if pilih == 1:
                return render_template('runtutan/bangundatar/1.runtutan_segitiga.html')
            elif pilih == 2:
                return render_template('runtutan/bangundatar/1.runtutan_persegipanjang.html')
            else:
                return render_template('runtutan/bangundatar/0.runtutan_persegi_segitiga.html', error="Pilihan tidak valid.")
        except ValueError:
            return render_template('runtutan/bangundatar/0.runtutan_persegi_segitiga.html', error="Masukkan angka yang valid.")
    return render_template('runtutan/bangundatar/0.runtutan_persegi_segitiga.html')
@app.route("/segitiga", methods=['POST'])
def segitiga():
    try:
        alas = float(request.form['alas'])
        tinggi = float(request.form['tinggi'])
        luas = 0.5 * alas * tinggi
        return render_template('runtutan/bangundatar/2.runtutan_segitiga.html', luas=luas)
    except ValueError:
        return render_template('runtutan/bangundatar/1.runtutan_segitiga.html',alas=alas,tinggi=tinggi,
                                error="Masukkan angka yang valid untuk alas dan tinggi.")

@app.route("/persegipanjang", methods=['POST'])
def persegipanjang():
    try:
        panjang = float(request.form['panjang'])
        lebar = float(request.form['lebar'])
        luas = panjang * lebar
        return render_template('runtutan/bangundatar/2.runtutan_persegipanjang.html', luas=luas)
    except ValueError:
        return render_template('runtutan/bangundatar/1.runtutan_persegipanjang.html',panjang=panjang,lebar=lebar,luas=luas,
                            error="Masukkan angka yang valid untuk panjang dan lebar.")
    
                                    # ======= SUHU =========
@app.route("/suhu", methods=['POST','GET'])
def suhu():
    if request.method == 'POST':
        fahrenheit=float(request.form['fahrenheit'])
        celcius=(fahrenheit-32)*5/9
        return render_template('runtutan/suhu/2.runtutan_suhu.html',celcius=celcius)
    return render_template('runtutan/suhu/1.runtutan_suhu.html')

                        # ============== KALKULATOR =============
@app.route("/kalkulator", methods=['GET','POST'])
def kalkulator():
    if request.method == 'POST':
        nilai1=float(request.form['nilai1Grandy'])
        nilai2=float(request.form['nilai2Grandy'])

        tambah=nilai1+nilai2
        kurang=nilai1-nilai2
        kali=nilai1*nilai2
        bagi=nilai1/nilai2
        return render_template('runtutan/kalkulator/2.kalkulator.html',nilai1=nilai1,
                               nilai2=nilai2,tambah=tambah,kurang=kurang,kali=kali,bagi=bagi)
    return render_template('runtutan/kalkulator/1.kalkulator.html')


# ======================================= IF ELSE ===============================================

                            # ========= BEASISWA ==========
@app.route("/beasiswa", methods=['GET','POST'])
def beasiswa():
    if request.method == 'POST':
        namagrandy = request.form['namagrandy']
        nilaigrandy = float(request.form['nilaigrandy'])
        penghasilangrandy = float(request.form['penghasilangrandy'])
        saudaragrandy = int(request.form['saudaragrandy'])
        statusgrandy = request.form['statusgrandy']


        if nilaigrandy >= 85 :
            poin1grandy=30
        else:
            poin1grandy=0
        if penghasilangrandy <=2000000 :
            poin2grandy=20
        else:
            poin2grandy=0
        if saudaragrandy > 2 :
            poin3grandy=10
        else:
            poin3grandy=0
        if statusgrandy != "Milik Sendiri":
            poin4grandy=10
        else:
            poin4grandy=0
        

        totalpoin_grandy = poin1grandy + poin2grandy + poin3grandy + poin4grandy

        if totalpoin_grandy >= 60 :
            hasilgrandy = "BERHAK MENDAPATKAN BEASISWA"
        else:
            hasilgrandy = "BELUM BERHAK"

        

        return render_template('if_else/beasiswa/2.ifelse_beasiswa.html',namagrandy=namagrandy,
                                            nilaigrandy=nilaigrandy,
                                            penghasilangrandy=penghasilangrandy,
                                            saudaragrandy=saudaragrandy,
                                            statusgrandy=statusgrandy,
                                            totalpoin_grandy=totalpoin_grandy,
                                            hasilgrandy=hasilgrandy)
    else:
        return render_template('if_else/beasiswa/1.ifelse_beasiswa.html')

                                # =========== BELANJA =============
@app.route("/belanja", methods=['POST','GET'])
def belanja():
    if request.method == 'POST':
        namagrandy = request.form['namagrandy']
        baranggrandy = request.form['baranggrandy']
        hargagrandy = float(request.form['hargagrandy'])
        jumlahgrandy = int(request.form['jumlahgrandy'])
        
        totalgrandy =hargagrandy*jumlahgrandy

        if totalgrandy >=50000 :
            Jdiskongrandy = totalgrandy*0.10
        elif totalgrandy >=20000 :
            Jdiskongrandy = totalgrandy*0.05
        else:
            Jdiskongrandy = totalgrandy*0
        
        
        totalakhirgrandy = totalgrandy-Jdiskongrandy
        return render_template('if_else/belanja/2.ifelse_belanja.html', namagrandy=namagrandy,
                                             baranggrandy=baranggrandy,
                                             hargagrandy=hargagrandy,
                                             jumlahgrandy=jumlahgrandy,
                                             totalgrandy=totalgrandy,
                                             Jdiskongrandy=Jdiskongrandy,
                                             totalakhirgrandy=totalakhirgrandy)
    return render_template('if_else/belanja/1.ifelse_belanja.html')

                            # ================ NILAI ====================
@app.route("/nilai", methods=['POST','GET'])
def nilai():
    if request.method == 'POST':
        namagrandy = str(request.form['namagrandy'])
        mapel1grandy = str(request.form['mapel1grandy'])
        nilai1grandy = float(request.form['nilai1grandy'])
        mapel2grandy = str(request.form['mapel2grandy'])
        nilai2grandy = float(request.form['nilai2grandy'])
        mapel3grandy = str(request.form['mapel3grandy'])
        nilai3grandy = float(request.form['nilai3grandy'])
        
        
        ratagrandy = (nilai1grandy+nilai2grandy+nilai3grandy)/3

        if ratagrandy >= 90 :
            kategorigrandy = "A (Sangat Baik)"
        elif ratagrandy >= 75 :
            kategorigrandy = "B (Baik)"
        elif ratagrandy >= 60 :
            kategorigrandy = "C (Cukup)"
        else:
            kategorigrandy = "D (Kurang)"
        
        return render_template('if_else/nilai/2.ifelse_nilai.html', namagrandy=namagrandy,
                                             mapel1grandy=mapel1grandy,
                                             nilai1grandy=nilai1grandy,
                                             mapel2grandy=mapel2grandy,
                                             nilai2grandy=nilai2grandy,
                                             mapel3grandy=mapel3grandy,
                                             nilai3grandy=nilai3grandy,
                                             ratagrandy=ratagrandy,
                                             kategorigrandy=kategorigrandy)
    return render_template('if_else/nilai/1.ifelse_nilai.html')

                            # ================ PEMESANAN ===============
@app.route("/pemesanan", methods=['GET','POST'])
def pemesanan():
    if request.method == 'POST':
        namaGrandy = request.form['namaGrandy']
        hargaGrandy = float(request.form['hargaGrandy'])
        jumlahGrandy = int(request.form['jumlahGrandy'])
        kategoriGrandy = request.form['kategoriGrandy']
        metodeGrandy = request.form['metodeGrandy']
        tambahanGrandy = request.form['tambahanGrandy']

        total1Grandy = (hargaGrandy*jumlahGrandy)
        if kategoriGrandy == "VIP":
            diskonGrandy = (total1Grandy*0.15)
        elif kategoriGrandy == "member":
            diskonGrandy = (total1Grandy*0.1)
        elif kategoriGrandy == "biasa":
            diskonGrandy = 0

        biayaGrandy = 0
        total2Grandy = (total1Grandy-diskonGrandy)
        if tambahanGrandy == "bungkus (Rp 2.000)":
            biayaGrandy += 2000
        elif tambahanGrandy == "Extra Toping(Rp 5.000)":
            biayaGrandy += 5000
        totalakhirGrandy = (total2Grandy + biayaGrandy)

        if metodeGrandy == "Transfer":
            bayarGrandy="Silahkan Transfer ke rekening BCA 145-275-924"
        elif metodeGrandy == "Cash":
            bayarGrandy="Silahkan bayar cash"
        else:
            bayarGrandy="silahkan pilih metode pembayaran"

        return render_template('if_else/pemesanan/2.ifelse_pemesanan.html',namaGrandy=namaGrandy,
                                            hargaGrandy=hargaGrandy,
                                            jumlahGrandy=jumlahGrandy,
                                            kategoriGrandy=kategoriGrandy,
                                            metodeGrandy=metodeGrandy,
                                            tambahanGrandy=tambahanGrandy,
                                            total1Grandy=total1Grandy,
                                            diskonGrandy=diskonGrandy,
                                            total2Grandy=total2Grandy,
                                            biayaGrandy=biayaGrandy,
                                            totalakhirGrandy=totalakhirGrandy,
                                            bayarGrandy=bayarGrandy)
    return render_template('if_else/pemesanan/1.ifelse_pemesanan.html')

                            # ============ STRUK BELANJA ===============
@app.route("/strukB", methods=['GET','POST'])
def strukB():
    if request.method == 'POST':
        namagrandy = request.form['namagrandy']
        baranggrandy = request.form['baranggrandy']
        hargagrandy = float(request.form['hargagrandy'])
        jumlahgrandy = float(request.form['jumlahgrandy'])
        statusgrandy = request.form['statusgrandy']
        pembayarangrandy = request.form['pembayarangrandy']

        total1grandy=(hargagrandy*jumlahgrandy)
        if statusgrandy == 'Gold':
            diskongrandy = (0.2)
        elif statusgrandy == 'Silver':
            diskongrandy = (0.1)
        elif statusgrandy == 'non-member':
            diskongrandy = 0

        totaldiskongrandy=(total1grandy*diskongrandy)
            
        if pembayarangrandy == 'Transfer':
            biayaadmingrandy =2500
        elif pembayarangrandy == 'Cash':
            biayaadmingrandy = 0

        total2grandy = int(total1grandy-totaldiskongrandy+biayaadmingrandy)

        if total2grandy > 500000 and statusgrandy == 'Gold':
            bonusgrandy="Voucher Belanja"
        else:
            bonusgrandy='-'
        

        return render_template('if_else/struk belanja/2.ifelse_strukbelanja.html',namagrandy=namagrandy,
                                            baranggrandy=baranggrandy,
                                            hargagrandy=hargagrandy,
                                            jumlahgrandy=jumlahgrandy,
                                            statusgrandy=statusgrandy,
                                            pembayarangrandy=pembayarangrandy,
                                            total1grandy=total1grandy,
                                            totaldiskongrandy=totaldiskongrandy,
                                            biayaadmingrandy=biayaadmingrandy,
                                            total2grandy=total2grandy,
                                            bonusgrandy=bonusgrandy)
    return render_template('if_else/struk belanja/1.ifelse_strukbelanja.html')

# ======================================= IF BERSARANG ===============================================

                                        # ===== CUACA ======
@app.route("/cuaca", methods=['GET','POST'])
def cuaca():
    if request.method == "POST":
        cuacagrandy = request.form["cuacagrandy"]
        suhugrandy = int(request.form["suhugrandy"])
        if cuacagrandy == "Hujan":
            if suhugrandy < 25:
                sarangrandy = "bawa payung dan jaket"
            else:
                sarangrandy = "bawa payung saja"
        elif cuacagrandy == "Cerah":
            if suhugrandy > 30:
                sarangrandy = "pakai kacamata hitam dan minum air putih"
            else:
                sarangrandy = "nikmati hari ini"
        else:
            sarangrandy = "data cuaca tidak valid"

        return render_template('if_bersarang/cuaca/2.cuaca.html',sarangrandy=sarangrandy,
                                            cuacagrandy=cuacagrandy,
                                            suhugrandy=suhugrandy)
    return render_template('if_bersarang/cuaca/1.cuaca.html')

                                        # ======= GAJI =======
@app.route("/gaji", methods=["GET","POST"])
def gaji():
    if request.method == "POST":
        namagrandy = request.form["namagrandy"]
        statusgrandy = request.form["statusgrandy"]
        gajigrandy = float(request.form["gajigrandy"])
        lemburgrandy = request.form["lemburgrandy"]
        jamgrandy = float(request.form["jamgrandy"])
        if statusgrandy == "Tetap":
            if gajigrandy >= 5000000:
                bonusgrandy = 0.1 * gajigrandy
                bonusstrgrandy = '10%'
            elif gajigrandy < 5000000:
                bonusgrandy = 0.05 * gajigrandy
                bonusstrgrandy = '5%'
        elif statusgrandy == "Kontrak":
            if gajigrandy >= 5000000:
                bonusgrandy = 0.03 * gajigrandy
                bonusstrgrandy = '3%'
            elif gajigrandy < 5000000:
                bonusgrandy = 0
                bonusstrgrandy = 'Tidak ada bonus'
        
        if lemburgrandy == "Ya":
            if jamgrandy >= 10:
                tambahangrandy = 200000
                tambahanstrgrandy = 'Rp 200,000'
            elif jamgrandy < 10:
                tambahangrandy = 100000
                tambahanstrgrandy = 'Rp 100,000'
        elif lemburgrandy == "Tidak":
            tambahangrandy = 0
            tambahanstrgrandy = 'Tidak ada tambahan'
            

        
        gajikotorgrandy = gajigrandy + bonusgrandy + tambahangrandy
        pajakgrandy = 0.02*gajikotorgrandy
        gajibersihgrandy = gajikotorgrandy - pajakgrandy
        
        return render_template('if_bersarang/gaji/2.gaji.html',namagrandy=namagrandy,
                                            statusgrandy=statusgrandy,
                                            gajigrandy=gajigrandy,
                                            bonusstrgrandy=bonusstrgrandy,
                                            bonusgrandy=bonusgrandy,
                                            lemburgrandy=lemburgrandy,
                                            jamgrandy=jamgrandy,
                                            tambahangrandy=tambahangrandy,
                                            tambahanstrgrandy=tambahanstrgrandy,
                                            gajikotorgrandy=gajikotorgrandy,
                                            pajakgrandy=pajakgrandy,
                                            gajibersihgrandy=gajibersihgrandy)
    return render_template('if_bersarang/gaji/1.gaji.html')

                                # ===================== NILAI ===================
@app.route("/ifbnilai", methods = ['GET','POST'])
def ifbnilai():
    if request.method == 'POST':
        namagrandy = str(request.form['namagrandy'])
        nilaiUTSgrandy = float(request.form['nilaiUTSgrandy'])
        nilaiUASgrandy = float(request.form['nilaiUASgrandy'])
        nilaiTugasgrandy = float(request.form['nilaiTugasgrandy'])
        nilaiPraktekgrandy = float(request.form['nilaiPraktekgrandy'])
        
        
        nilaiAkhirgrandy = (nilaiUTSgrandy * 0.25) + (nilaiUASgrandy * 0.35) + (nilaiTugasgrandy * 0.20) +  (nilaiPraktekgrandy * 0.20)

        if nilaiAkhirgrandy >= 85:
             keterangangrandy = " Lulus dengan Predikat A"
        elif nilaiAkhirgrandy >= 75:
            if nilaiPraktekgrandy >= 80:
                keterangangrandy = " Lulus dengan Predikat B"
            else:
                keterangangrandy = " Remedial Praktek"
        elif nilaiAkhirgrandy >= 65:
            if nilaiTugasgrandy >=70:
                keterangangrandy = " Lulus dengan Predikat C"
            else:
                keterangangrandy = " Remedial Tugas"
                 
        elif nilaiAkhirgrandy >= 50:
            if nilaiUASgrandy >=60:
                keterangangrandy = " Remedial UTS & Tugas"
            else:
                keterangangrandy = " Remedial UAS"
        else:
            keterangangrandy = "Tidak Lulus"
        return render_template('if_bersarang/nilai/2.nilai.html', namagrandy=namagrandy,
                                             nilaiUTSgrandy=nilaiUTSgrandy,
                                             nilaiUASgrandy=nilaiUASgrandy,
                                             nilaiTugasgrandy=nilaiTugasgrandy,
                                             nilaiPraktekgrandy=nilaiPraktekgrandy,
                                             nilaiAkhirgrandy=nilaiAkhirgrandy,
                                             keterangangrandy=keterangangrandy)
    return render_template('if_bersarang/nilai/1.nilai.html')

# ===================================== INTERNET ================================
@app.route("/internet", methods=['GET','POST'])
def internet():
    if request.method == 'POST':
        namaGrandy = request.form['namaGrandy']
        kecepatanGrandy = float(request.form['kecepatanGrandy'])
        kuotaGrandy = float(request.form['kuotaGrandy'])
        berlanggananGrandy = float(request.form['berlanggananGrandy'])
        pembayaranGrandy = request.form['pembayaranGrandy']

        if kecepatanGrandy >=50 and kuotaGrandy >= 200 :
            ketGrandy = 'Premium'
        elif kecepatanGrandy >= 30 and kuotaGrandy >= 100 :
            ketGrandy = 'GOld'
        elif kecepatanGrandy >= 10 and kuotaGrandy >= 50 :
            ketGrandy = 'Silver'
        else :
            ketGrandy = 'Basic'
        diskonGrandy = 0
        if berlanggananGrandy >= 24 :
            diskonGrandy += 50000
        elif berlanggananGrandy >= 12 :
            diskonGrandy += 25000
        else :
            diskonGrandy += 0

        if pembayaranGrandy == 'Ya':
            diskonGrandy += 15000
        else :
            diskonGrandy += 0
        
        if ketGrandy == 'Premium':
            hargaGrandy = 500000
        elif ketGrandy == 'Gold':
            hargaGrandy = 350000
        elif ketGrandy == 'Silver':
            hargaGrandy = 200000
        else :
            hargaGrandy = 100000
        totaldiskonGrandy = 0
        totaldiskonGrandy = diskonGrandy
        totalGrandy = hargaGrandy - diskonGrandy
        return render_template('if_bersarang/internet/2.internet.html',namaGrandy=namaGrandy,
                                            kecepatanGrandy=kecepatanGrandy,
                                            kuotaGrandy=kuotaGrandy,
                                            berlanggananGrandy=berlanggananGrandy,
                                            pembayaranGrandy=pembayaranGrandy,
                                            ketGrandy=ketGrandy,
                                            diskonGrandy=diskonGrandy,
                                            totaldiskonGrandy=totaldiskonGrandy,
                                            hargaGrandy=hargaGrandy,
                                            totalGrandy=totalGrandy)
    return render_template('if_bersarang/internet/1.internet.html')

# ===================================================== LOOPING ============================================================
# ================================================= FOR ==========================================================
@app.route("/operasi", methods=['GET','POST'])
def operasi():
    if request.method == 'POST':
        bilanganGrandy = int(request.form['bilanganGrandy'])
        namaGrandy = request.form['namaGrandy']

        jumlahgenapGrandy=0
        for genapGrandy in range(2, bilanganGrandy+1, 2):
            jumlahgenapGrandy +=genapGrandy
            
        jumlahganjilGrandy=0
        for ganjilGrandy in range(1, bilanganGrandy+1, 2):
            jumlahganjilGrandy += ganjilGrandy
            
        jumlahkel5Grandy=0
        for kel5Grandy in range(5, bilanganGrandy+1, 5):
            jumlahkel5Grandy += kel5Grandy
            
        jumlahnamaGrandy=0
        for x in range(1, bilanganGrandy+1):
            jumlahnamaGrandy += 1
            
        return render_template('looping/for/operasi/2.operasi.html',namaGrandy=namaGrandy,
                               bilanganGrandy=bilanganGrandy,
                               ganjilGrandy=ganjilGrandy,
                               jumlahgenapGrandy=jumlahgenapGrandy,
                               jumlahganjilGrandy=jumlahganjilGrandy,
                               jumlahkel5Grandy=jumlahkel5Grandy,
                               jumlahnamaGrandy=jumlahnamaGrandy)
    return render_template('looping/for/operasi/1.operasi.html')

# ===================================== GANJIL GENAP ============================
@app.route("/ganjilgenap", methods=['GET','POST'])
def ganjilgenap():
    if request.method == 'POST':
        awalGrandy = int(request.form['awalGrandy'])
        akhirGrandy = int(request.form['akhirGrandy'])

        for bilanganGrandy in range(awalGrandy,akhirGrandy+1):
            if bilanganGrandy % 2 == 0:
                genapGrandy = "genap"
            else:
                ganjilGrandy = "ganjil"
            
        return render_template('looping/for/ganjilgenap/2.ganjilgenap.html',
                               bilanganGrandy=bilanganGrandy,
                               awalGrandy=awalGrandy,
                               akhirGrandy=akhirGrandy,
                               genapGrandy=genapGrandy,
                               ganjilGrandy=ganjilGrandy)
    return render_template('looping/for/ganjilgenap/1.ganjilgenap.html')

# =============================== CEK KELIPATAN 3 =========================
@app.route("/cek3", methods=['GET','POST'])
def cek3():
    if request.method == 'POST':
        awalGrandy = int(request.form['awalGrandy'])
        akhirGrandy = int(request.form['akhirGrandy'])

        for bilanganGrandy in range(awalGrandy,akhirGrandy+1):
            if bilanganGrandy % 3 == 0:
                hasilGrandy = "kelipatan 3"

            
        return render_template('looping/for/cek kelipatan 3/2.cek3.html',
                               bilanganGrandy=bilanganGrandy,
                               awalGrandy=awalGrandy,
                               akhirGrandy=akhirGrandy,
                               hasilGrandy=hasilGrandy)
    return render_template('looping/for/cek kelipatan 3/1.cek3.html')

# ================================== CEK KELIPATAN 2 dan 5 ====================
@app.route("/cek25", methods=['GET','POST'])
def cek25():
    if request.method == 'POST':
        awalGrandy = int(request.form['awalGrandy'])
        akhirGrandy = int(request.form['akhirGrandy'])

        hasilGrandy = []
        for bilanganGrandy in range(awalGrandy,akhirGrandy+1):
            if bilanganGrandy == 0:
                hasilGrandy.append(f'{bilanganGrandy} = bilangan 0')
            elif bilanganGrandy % 5 == 0 and bilanganGrandy % 2 ==0 :
                hasilGrandy.append(f'{bilanganGrandy} = kelipatan 2 dan 5')
            elif bilanganGrandy % 2 == 0:
                hasilGrandy.append(f'{bilanganGrandy} = kelipatan 2')
            elif bilanganGrandy % 5 == 0 :
                hasilGrandy.append(f'{bilanganGrandy} = kelipatan 5')
            else:
                hasilGrandy.append(f'{bilanganGrandy}')

        return render_template('looping/for/cek kelipatan 2 dan 5/2.cek2&5.html',
                               bilanganGrandy=bilanganGrandy,
                               awalGrandy=awalGrandy,
                               akhirGrandy=akhirGrandy,
                               hasilGrandy=hasilGrandy)
    return render_template('looping/for/cek kelipatan 2 dan 5/1.cek2&5.html')

# ============================ BARANG ==================================
@app.route("/indexbarang", methods=['GET', 'POST'])
def indexbarang():
    if request.method == 'POST':
        JBGrandy = int(request.form['JBGrandy'])

        return render_template('looping/for/barang/2.barang.html', JBGrandy=JBGrandy)
    return render_template('looping/for/barang/1.barang.html')


@app.route("/formbarang", methods=['POST'])
def formbarang():
    namaGrandy = request.form.getlist('namaGrandy')
    hargaGrandy = list(map(int, request.form.getlist('hargaGrandy')))
    QtyGrandy = list(map(int, request.form.getlist('QtyGrandy')))

    totalGrandy = 0
    baranglist = []

    for nama, harga, qty in zip(namaGrandy, hargaGrandy, QtyGrandy):
        jumlah = harga * qty
        totalGrandy += jumlah
        baranglist.append((nama, harga, qty, jumlah))

    return render_template('looping/for/barang/3.barang.html',
                           baranglist=baranglist,
                           totalGrandy=totalGrandy)

# ================================= WHILE =====================================================
# ================= CEK KELIPATAN 4 =====================

@app.route("/cek4", methods=['GET','POST'])
def cek4():
    if request.method == 'POST':
        akhirGrandy = int(request.form['akhirGrandy'])

        awalGrandy = 4
        jumlahGrandy = 0
        hasilGrandy = []
        while awalGrandy <= akhirGrandy :
            jumlahGrandy += awalGrandy
            hasilGrandy.append(f'{awalGrandy}')
            awalGrandy += 4
            
        return render_template('looping/while/cek kelipatan 4/2.cek4.html',
                               awalGrandy=awalGrandy,
                               akhirGrandy=akhirGrandy,
                               hasilGrandy=hasilGrandy,
                               jumlahGrandy=jumlahGrandy)
    return render_template('looping/while/cek kelipatan 4/1.cek4.html')

# ============================== TEBAK ANGKA ==========================
@app.route('/tebak', methods=['GET', 'POST'])
def tebak():
    grandy_hasil = ""
    grandy_angka = 25
    
    if request.method == 'POST':
        grandy_tebak = int(request.form['grandy_tebak'])
        while True:
            if grandy_tebak == grandy_angka :
                grandy_hasil =f"Tebakan Anda Benar, Angka Nya Adalah {grandy_angka}"
                break
            elif grandy_tebak < grandy_angka :
                grandy_hasil="Tebakan Anda Terlalu Kecil"
                break
            elif grandy_tebak > grandy_angka :
                grandy_hasil="Tebakan Anda Terlalu Besar"
                break
    return render_template('looping/while/tebak angka/1.tebak.html',grandy_hasil=grandy_hasil)

# ====================================== ANGKA ===============================
@app.route("/angka", methods=["GET", "POST"])
def angka():
    if "arrayGrandy" not in session:
        session["arrayGrandy"] = []
        session["done"] = False

    if request.method == "POST":
        angka = int(request.form["angka_grandy"])

        while True:
            if angka != 0:
                session["arrayGrandy"].append(angka)
                session.modified = True
                break
            else:

                session["done"] = True
                break
        return redirect(url_for("angka"))

    hasil = None
    jumlah = None
    if session.get("done"):
        hasil = session["arrayGrandy"]
        jumlah = sum(session["arrayGrandy"])

    return render_template(
        "looping/while/angka/1.angka.html",
        arrayGrandy=session["arrayGrandy"],
        hasil=hasil,
        jumlah=jumlah,
        done=session.get("done", False)
    )

@app.route("/resetangka")
def resetangka():
    session.pop("arrayGrandy", None)
    session.pop("done", None)
    return redirect(url_for("angka"))

if __name__ == "__main__":
    app.run(debug=True)

