class Animal: 
    def __init__ (self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama 
        self.makanan= makanan 
        self.hidup= hidup 
        self.berkembang_biak= berkembang_biak 

    def cetak(self):
        print("Nama \t\t\t\t\t\t: ", self.nama,
                "\nmakanan \t\t\t\t", self.makanan,
                "\nHidup \t\t\t\t\t: ",self.hidup,
                "\nberkembang biak : ",self.berkembang_biak,
               )
# object = Animal ("buaya", "daging" ,"amphibi", "bertelur", "makanan",)
# object.nama()


