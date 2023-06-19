# Apache Kafka ile Basit CDC Uygulaması Geliştirme Projesi



## Açıklama
Proje kısaca bir producer ve bir consumerdan oluşan iki uygulamadır. 

A uygulaması: Mesaj üreten uygulama 10 saniyede bir MongoDB veritabanındaki bir collection’ı sorgular ve bir
önceki çalışmasından sonra eklenmiş yeni dökümanları tespit eder, ardından yeni dökümanı JSON
mesajı olarak Apache Kafka’ya publish eder

B uygulaması: Subscriber uygulaması ise Apache Kafka’dan consume ettiği mesajı System Out olarak konsola yazdırır.



## Başlama

  ```
  git clone https://github.com/yasinrumel/ossfinal_proje.git
  ```
  ```
  cd cdc
  ```
  ```
  docker-compose up
  ```


