from django.db import models

class Profil(models.Model):
    nama = models.CharField(max_length=100)
    profesi = models.CharField(max_length=100)
    email = models.EmailField()
    tentang = models.TextField()

    def __str__(self):
        return self.nama

class Keahlian(models.Model):
    profil = models.ForeignKey(
        Profil,
        on_delete=models.CASCADE
    )
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class Pendidikan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    nama_sekolah = models.CharField(max_length=150)
    jurusan = models.CharField(max_length=100)
    tahun_mulai = models.PositiveBigIntegerField()
    tahun_selesai = models.PositiveBigIntegerField()

    def __str__(self):
        return self.nama_sekolah

class Proyek(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    nama_proyek = models.CharField(max_length=150)
    deskripsi = models.TextField()
    tahun = models.PositiveBigIntegerField()

    def __str__(self):
        return self.nama_proyek