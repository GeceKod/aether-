# 🎬 Güneş TV - Aether.ist & TMDB Otomatik Katalog Sistemi

Bu depo; TMDB üzerindeki **50.000 Film** ile **30.000 Diziyi** (%100 Türk yapımı öncelikli, çift dilli, tüm sezon/bölüm linkli ve Aether.ist doğrudan sayfa oynatma linkli) **minimal JSON formatında** üreten ve **GitHub Actions** ile her gün otomatik olarak güncelleyen tam otomatik bir katalog sistemidir.

---

## 🚀 Temel Özellikler

* **⚡ Ultra Hafif JSON:** Detaylar kullanıcı sayfaya girene kadar canlı çekilir; dosya boyutları optimum düzeydedir.
* **📺 Tüm Sezon ve Bölüm Linkleri Gömülü:** Her dizinin yayınlanmış tüm sezon ve bölümleri `episodes: [...]` dizisinde hazırdır.
* **🛡️ Yayın Tarihi Koruması (No Fake Episodes):** Henüz televizyonda/internette yayınlanmamış gelecek bölümler otomatik olarak filtrelenir; yanlış bölüm oynatma hatası yaşanmaz.
* **🇹🇷 %100 Yerli Önceliklendirme (TR Boost):** Yeşilçam'dan en yeni 2026 yapımlarına kadar tüm yerli içerikler eksiksiz yer alır.
* **🌐 Çift Dilli Arama:** Hem Türkçe (`title`) hem orijinal/İngilizce (`original_title`) adlar tutulur.
* **🏷️ Zengin Kategoriler:** `Türk Yapımı`, `Kore Yapımı`, `Animasyon`, `Anime`, `Netflix`, `Disney+`, `Aksiyon`, `Korku`, `Dram` vb.
* **🔄 Akıllı Sıralama & Güncel Bölümler:** Yeni bölümü çıkan dizi anında listenin **en başına (Index 0)** taşınır.
* **🤖 Sıfır Bakım (GitHub Actions):** Her sabah saat `08:30 UTC`'de yeni çıkan filmler ve yeni bölümler bota düşer, JSON güncellenip otomatik commit edilir.

---

## 📂 Dosya Yapısı

```text
├── .github/
│   └── workflows/
│       └── daily_sync.yml          # Her gün 08:30 UTC'de çalışan GitHub Action
├── data/
│   ├── catalog.json                # 🌟 Birleşik Tüm Katalog (50.000 Film + 30.000 Dizi = 80.000 İçerik)
│   ├── movies.json                 # Sadece Filmler (50.000 İçerik)
│   └── series.json                 # Sadece Diziler (30.000 Dizi, Tüm Sezon & Bölümleriyle)
├── scripts/
│   ├── config.py                   # TMDB ve Aether.ist sabitleri
│   ├── tmdb_client.py              # TMDB API istemcisi & URL oluşturucu
│   ├── generate_catalog.py         # 50k film + 30k dizi katalog üretici
│   ├── seed_initial.py             # İlk arşiv üretim betiği
│   └── update_daily.py             # Günlük yeni bölümleri en başa ekleyen bot
├── tests/
│   └── test_catalog.py             # Otomatik testler
└── README.md
```

---

## 📦 JSON Veri Modeli

```json
{
  "type": "dizi",
  "tmdb_id": 108978,
  "title": "Reacher",
  "original_title": "Reacher",
  "genres": [
    "Aksiyon",
    "Suç",
    "Dram"
  ],
  "category": "Aksiyon, Suç, Dram",
  "platform": "Amazon",
  "imdb_id": "",
  "imdb": "8.1",
  "year": "2022",
  "added_date": "28 Ağustos, 2026",
  "poster": "https://image.tmdb.org/t/p/w500/j1X4v18P0iTqLw7t6v7vE4gDk3P.jpg",
  "url": "https://aether.ist/media/tmdb-tv-108978-reacher",
  "episodes": [
    {
      "title": "1. Sezon 1. Bölüm",
      "videoUrl": "https://aether.ist/media/tmdb-tv-108978-reacher/1/1"
    },
    {
      "title": "1. Sezon 2. Bölüm",
      "videoUrl": "https://aether.ist/media/tmdb-tv-108978-reacher/1/2"
    }
  ]
}
```

---

## 📱 Güneş TV Entegrasyonu

Güneş TV uygulamanızda VOD kaynak listesi eklerken doğrudan aşağıdaki **Raw bağlantıları** kullanabilirsiniz:

* **🌟 Birleşik Tüm Katalog (50.000 Film + 30.000 Dizi = 80.000 İçerik):**
  ```text
  https://raw.githubusercontent.com/GeceKod/aether-/main/data/catalog.json
  ```

* **🎬 Sadece Film Kaynağı (Movies - 50.000 Film):**
  ```text
  https://raw.githubusercontent.com/GeceKod/aether-/main/data/movies.json
  ```

* **📺 Sadece Dizi Kaynağı (Series - 30.000 Dizi, Sezon & Bölümlü):**
  ```text
  https://raw.githubusercontent.com/GeceKod/aether-/main/data/series.json
  ```

Kullanıcı kartı tıkladığında `TmdbMetadataFetcher.kt` eksik olan tüm detayları (oyuncular, fragman, Türkçe özet, bölüm küçük resimleri) anında cihazın sistem dilinde canlı olarak çekecektir.