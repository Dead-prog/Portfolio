#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library for ST7735
#include <Adafruit_ST7789.h> // Hardware-specific library for ST7789
#include <SPI.h>
#include <DHT.h>

// Broche ecran tft
#define TFT_CS         8
#define TFT_RST        10                                            
#define TFT_DC         9

// Broche DHT11
#define DHT_PIN 12
#define DHT_TYPE DHT11

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);
DHT dht(DHT_PIN, DHT_TYPE);

int temp;
int hum;

void setup(void) {

  Serial.begin(9600);
  dht.begin();
  // Initialisation de l'ecran tft
  tft.initR(INITR_BLACKTAB);

  tft.fillScreen(ST77XX_BLACK);

  // Titre
  tft.setTextColor(ST77XX_BLUE);
  tft.setTextSize(3);

  tft.setCursor(5, 10);
  tft.println("Meteo");
 
}

void loop() {
  // Lecture temperature et humidité
  temp = dht.readTemperature();
  hum = dht.readHumidity();

  // affichage de la temperature
  tft.setTextColor(ST77XX_RED);
  tft.setTextSize(1);
  tft.setCursor(5, 50);
  tft.print("TEMPERATURE");
  tft.setCursor(80, 50);
  tft.fillRect(80, 48, 20, 12, ST77XX_BLACK);
  tft.print(temp);
  tft.println("C");
  delay(1000);

  // affichage de l'humidité
  delay(1000);
  tft.setTextColor(ST77XX_GREEN);
  tft.setTextSize(1);
  tft.setCursor(5, 70);
  tft.print("HUMIDITE");
  tft.setCursor(80, 70);
  tft.fillRect(80, 68, 20, 12, ST77XX_BLACK);
  tft.print(hum);
  tft.print("%"); }
