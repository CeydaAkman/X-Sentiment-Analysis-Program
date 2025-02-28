# X Sentiment Analysis Programı:
Bu proje X API'si kullanarak belirli bir hashtag ile ilgili tweet'leri toplayan ve bu tweet'ler üzerinde duygu analizi yaparak sonuçları görselleştiren bir uygulamadır. Kullanıcı, belirli bir hashtag ile ilgili tweet'lerin duygu durumunu analiz edebilir ve bu analizleri çubuk grafiği şeklinde görselleştirebilir. Projede kullanılan duygu analizi aracı TextBlob kütüphanesidir.

# Duygu Analizi:
Duygu analizi, bir metnin duygusal içeriğini belirlemeye yönelik bir yöntemdir. Bu analiz, metnin pozitif, negatif veya nötr olup olmadığını belirler. Bu tür analizler, sosyal medya, müşteri geri bildirimleri, ürün yorumları gibi büyük veri setlerinde duygusal eğilimleri anlamak için yaygın olarak kullanılır. Duygu analizi genellikle şu adımlarla yapılır:

1.Pozitif Duygu: Olumlu, neşeli veya heyecan verici gibi duygu durumlarıdır.

2.Negatif Duygu: Olumsuz, kızgınlık veya hayal kırıklığı gibi duygu durumlarıdır.

3.Nötr Duygu: Metnin herhangi bir duygu taşımadığı ve tarafsız olduğu durumlardır.

# Kullanım Adımları:
1.Projeyi bilgisayarınıza indirin veya GitHub'dan klonlayın.

2.Python yüklü olduğundan emin olun.

3.Gerekli kütüphaneleri indirmek için terminalde sırasıyla komutları çalıştırın:

pip install tweepy

pip install pandas

pip install matplotlib

pip install textblob

pip install python-dotenv

4.X API'sine erişim sağlamak için bir X geliştirici hesabınızın olması gerekir. X Developers sayfasına giderek bir uygulama oluşturun ve Bearer Token'ınızı alın.

5.Proje içinde .env dosyası oluşturarak Bearer Token'ınızı bu dosyaya yazın.

6.Terminal veya komut istemcisinde SentimentAnalysis.py komutunu çalıştırarak projeyi çalıştırın.

7.Çalıştırdıktan sonra belirlediğiniz hashtag için pozitif, negatif ve nötr tweet'lerin dağılımını gösteren bir çubuk grafik elde edeceksiniz.

# Programın İşleyişi:
1.Gerekli kütüphaneler (tweepy, pandas, matplotlib, textblob, dotenv) içe aktarılır.

2..env dosyasındaki X API Bearer Token, dotenv.load_dotenv() ile yüklenir.

3.X API'ye bağlanmak için tweepy.Client kullanılarak kimlik doğrulaması yapılır.

4.get_tweets fonksiyonu çağrılır, belirli bir hashtag ile ilgili tweet'ler çekilir.

5.Her bir tweet metni, TextBlob kullanılarak duygu analizi yapılır ve sonuçlar belirlenir.

6.Tweet'ler ve duygu etiketleri, bir pandas DataFrame'ine aktarılır.

7.matplotlib ile duygu durumu dağılımı görselleştirilir, her duygu kategorisinin sayısı hesaplanır.

8.Çubuk grafiği oluşturularak, pozitif, negatif ve nötr tweet'lerin dağılımı kullanıcıya sunulur.

# Kod Yapısı:
Tweetlerin Çekilmesi: get_tweets fonksiyonu, kullanıcı tarafından belirtilen hashtag veya anahtar kelimeye göre X’ten tweet'leri çeker. Bu işlem tweepy.Client aracılığıyla yapılır ve her tweet'in metni alınır.

Duygu Analizi: analyze_sentiment fonksiyonu, her tweet'in duygu analizini yapar. TextBlob kütüphanesi, tweet metninin duygu skorunu hesaplamak için kullanılır. Eğer skor pozitifse, tweet "Pozitif"; negatifse, tweet "Negatif"; sıfırsa, tweet "Nötr" olarak etiketlenir.

Veri Çerçevesi Oluşturma: Elde edilen tweet metinleri ve duygu etiketleri bir pandas DataFrame'ine aktarılır. Bu veri çerçevesi tweet'leri ve duygu etiketlerini düzenli bir şekilde saklar.

Veri Görselleştirme: matplotlib kullanılarak, her duygu kategorisinin tweet sayıları görselleştirilir. Duygu dağılımını daha kolay analiz etmek için çubuk grafiği olarak gösterilir.

# Kullanılan Teknolojiler:
Programlama Dili: Proje Python programlama dilinde yazılmıştır.

Tweepy: X API'sine bağlanmak için kullanılan Python kütüphanesidir.

Pandas: Veri işleme ve analiz için kullanılan kütüphanedir.

Matplotlib: Veriyi görselleştirmek için kullanılan kütüphanedir.

TextBlob: Duygu analizi yapmak için kullanılan kütüphanedir.

Python-dotenv: Ortam değişkenlerini yüklemek için kullanılan kütüphanedir.

X API: X’ten tweet'leri çekmek için kullanılan API’dir.

# Ekran Çıktısı:
![Sentiment Analysis Ekran Çıktısı](https://github.com/user-attachments/assets/29fb5c75-4e60-4a41-8f72-04867ee1f89f)
