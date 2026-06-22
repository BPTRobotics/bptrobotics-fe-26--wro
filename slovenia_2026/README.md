<<<<<<< Updated upstream

# BPT Robotics – Engineering Documentation 


WRO Future Engineers – Slovenia 2025

##### **Team name:** BPT Robotics
##### **Members:**
- **Boldizsár Szakács - Békési** *- software developer, algorithm manager, sensor data processing*
- **Péter Márkus** *- mechanical design, assembly, 3D printing and prototyping, electronic design*
- **Tibor Bogar** - *electronics, cabling*

**Country:** Hungary
**Category:** WRO Future Engineers
**Competition location:** Slovenia, Ljubljana
**Date:** 2025, 2 - 5 of September


## 1. Team introduction
BPT Robotics is a young robotics team of three, born from a passion for technology, robotics and innovation. We all bring different strengths to the work together:
Boldizsár is the controller of programming logic and artificial intelligence, who builds the robot's brain.
Peti is a master of mechanical design and structural engineering, ensuring a stable and reliable frame, from CAD designs to 3D printed elements.
Tibi is an expert in precision electronics connections, ensuring that all hardware components communicate seamlessly and receive the proper power supply.
Our robot performed well in the Hungarian qualifiers, and thanks to this, we qualified for the 2025 WRO competition in Slovenia. Our goal is to present a technological solution that shows that anything can be achieved with a small team and limited resources. Although the Hungarian round did not start absolutely smoothly, we managed to make it to Slovenia. Gathering our experience from the competition, we rethought the entire robot and redesigned it in less than 3 months. Our motivation is to create a better world for our future children and grandchildren, so that we can participate in such big events of robotics at a young age.

![Team photo](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/Team/Very%20very%20Serious%20Team%20Photo.jpg)

## 2. The task
The challenge for the WRO Future Engineers category is to develop a fully autonomous robot that can navigate a changing obstacle course without human intervention. The robot:
must independently explore their environment,
must recognize and avoid obstacles,
must make decisions based on visual cues (such as color codes and walls),
you need to reach your destination via the shortest and most efficient route possible.
This task is a mechanical, electronic and software development challenge at the same time, as the robot has to process and react to complex data in real time. Another challenge during the preparation was that the robot had to be within a certain limit (300 x 200 x 300 mm) and could not exceed a weight limit of 1.5 kg. We started the work after a thorough planning. Initially, we thought about the structure and operation of the robot based on the experience gained so far. Later, Boldizsár started to do the programming part and integrate the software with the appropriate operating system. Initially, he did the Open challenge, refined it, and developed it, and when it worked perfectly, he supplemented it with the Obstacle challenge. After a lot of testing, our robot was created.


![Robot photo](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/robots/Robot%20Casual%20(6).jpg)

## 3. Robot concept
Our robot is a four-wheeled, back-wheel drive, back-wheel steering platform that we designed to be stable, modular, and easy to repair.
The main goal was to create a system that is capable of real-time decision-making with minimal latency. Our robot, has both a driven and steered rear axle, allowing for the most precise maneuvering possible.
Therefore, the main control unit is a Raspberry Pi 4 4GB model B, which runs the control program written in Python.

**Main features of the system:**
- **Husky Lens** camera for fast color recognition.
- **YDLIDAR X4 Pro** for 360° environmental mapping, which provides accurate data up to a distance of 10 meters. (which is enough)
- **GY-BNO085** IMU for precise heading and movement correction.
- **L298N** motor controller, which controls the drive motor with PWM control.
- **PCA9685**, this rotates our drive shaft for precise maneuvering


The core of the concept is the modular structure: any component can be quickly replaced, and the frame design allows for later expansions (for example, installing more powerful motors or new sensors).


![Team photo](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/robots/Robot%20Casual%20(4).jpg)![Team photo](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/robots/Robot%20Casual%20(3).jpg)

## 4. Hardware details
![Circuit photo](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/else/Untitled%20(1).jpg)
| Component             | Function                                                       | Comment                  | Justification                                                                 |
|-----------------------|----------------------------------------------------------------|--------------------------|-------------------------------------------------------------------------------|
| Raspberry Pi 4 (4GB)  | Central control, data processing                               | Running Python code      | It's proven, it works well, although it's a bit slow, so we plan to switch to Pi5 next year. |
| L298N motor controller| Driven motor control                                           | PWM signal-based         | Cheap, works well                                                             |
| PCA9685               | Control of the rotation of the driven shaft                    |                          | There was a lot of it and it works well                                       |
| MG995                 | Rotating the driven shaft                                      | Metal metatarsal         | Because it is very powerful and even a little electricity is not enough for it |
| Blue TT motorcycle    | Drive of the driven axle produces more torque than the front-wheel drive, thus providing greater speed against the small wheel. | Metal metatarsal         | Because it is easier to handle than other engines in this price range.        |
| PixyCam2.1            | Color recognition                                              | Direct USB communication | Because it provides a very fast image, and color detection is already implemented by default |
| YDLIDAR X4 Pro        | 360° mapping, guidance, precise location                       | 10 m range               | Because at the moment of purchase, there was strong documentation.            |


## 5. Software architecture

![Sensor circuit photo](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/else/Untitled%20(3).jpg)
Our developer decided to try a new approach into the sensor combination, which he called the **"module system"**, where he splits the software into different modules.

For example, when  the robot starts, it uses the lidar for navigation of distances and gyroscope to ensure the full forward direction he calls this state **"module 1"**. Then, when the robot approaches a corner, and needs to change its direction, then it turns off the lidar (since there's no need for that), and turns by only the data of the gyroscope. That state is called **"module 2"**. Then it changes between these modules.

### **Modules:**
![OPEN CHALLENGE](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/else/Sprint%20Planning%20-%20OPEN.jpg)
![OBSTACLE CHALLENGE](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/else/Sprint%20Planning%20-%20OBSTACLE.jpg)

##### **OPEN CHALLENGE's modules:**
![Module 1](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/else/Sprint%20Planning%20-%20Module%201.jpg)
![Nodule 2](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/else/Sprint%20Planning%20-%20Module%202.jpg)
##### **OBSTACLE CHALLENGE's modules:**
![Module 3](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/else/Sprint%20Planning%20-%20Module%203.jpg)
![Module 4](https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025/blob/main/img/else/Sprint%20Planning%20-%20Module%203.jpg)
<sub>
```
read LIDAR distance
read camera color
read gyro heading

IF obstacle detected (distance < safe_limit):
    IF camera sees red:
        turn left
    ELSE IF camera sees blue:
        turn right
    ELSE:
        stop, then go around slowly
ELSE:
    move forward straight

correct direction with gyro
```
</sub>

### **Download the repository**
**Clone the repository:**
`bash
git clone https://github.com/BPTRobotics/BPTRobotics-Ljubjana-2025.git
cd BPTrobotics-Ljubjana-2025`

**Download dependencies:**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip
pip install -r requirements.txt

Run the robot:
bash
python3 -m WRO.main
```
**Unit module tests**
```
python3 -m WRO.control.servo.test
python3 -m WRO.control.motor.test
python3 -m WRO.sensors.camera.test
python3 -m WRO.sensors.lidar.test
python3 -m WRO.sensors.gyroscope.test
```
**Compatibility**
Only compatible with `Ubuntu 20.04.5 Server`. (available in the `Raspberry PI Imager`)
[PI Imager -> Other Os -> Ubuntu 20.4.5 LTS]

## 6. Development 
##### **Transfer of previous experiences:**
Our previous robot was too heavy (in terms of weight) so we reduced its weight with 3D printed models and fewer components (Lidar instead of many ultrasonic sensors)
The batteries didn't last long, the power was low, so we used twice as many (i.e. 6) batteries.
Instead of an ultrasonic sensor, we use lidar, so we can see 360 ​​degrees
Instead of a USB webcam, we use a more professional camera, thus facilitating a more accurate solution to the obstacle challenge.
faster and more accurate gyroscope for more precise control and avoidance of unnecessary turns
Concept development – first CAD models and sensor placement.
First prototype – basic mechanical structure and motor control.
Sensor integration – Connecting LIDAR, PixyCam and IMU.
Algorithm development – writing navigation and obstacle avoidance code.
Fine tuning – testing and error correction on the test track.
Pre-competition calibration – sensor adjustments, mechanical repairs.

## 8. Innovations
Real-time sensor fusion, which combines data from LIDAR and PixyCam.
Energy-efficient motor control, which provides longer operating time and therefore requires less battery power.
Quick module replacement option(modularity) to eliminate errors during the competition and for quick and easy assembly.
development of componentsSince we have lidar and a more professional camera, we can solve both the open and obstacle challenges much more easily and accurately.

## 9. Future plans
Switching to Raspberry Pi 5 for faster processing. Since we want to process as much and as accurate data as possible, a fast controller is also important
Implementation of SLAM algorithm to improve mapping.
Designing a lighter, yet stronger frame. If it were possible to make the robot frame from a strong, yet lightweight sheet metal, that would be the best because it would be both lightweight and durable.
Better and longer battery capacity with less weight. Although it can withstand a full test day, it would be nice if it could not only withstand it, but also retain power and when the battery is low, the power would not drop, the engine would not slow down

## 10. BOM
|                    | modell                                                             | unite price       | piece  | price                             | shop                                                                                                                                                                                                                                                            |             |
| ------------------ | ------------------------------------------------------------------ | ----------------- | ------ | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| controll panel     | Raspberry pi 4 mdell B, 4gb                                        |        25 900 Ft | 1 pcs  |        25 900 Ft | [pi shop](https://www.pi-shop.hu/raspberry-pi-4-model-b-4gb?gad_source=1&gad_campaignid=376802345)                                                                                                                                                              |             |
| sd card            | sandisk 64gb sd card                                               |        8 490 Ft | 1 pcs  |        8 490 Ft | [alza](https://www.alza.hu/sandisk-microsdxc-64-gb-extreme-pro-rescue-pro-deluxe-sd-adapter-d7261114.htm?kampan=adw4_prislusenstvi-pro-it/tv_pla_all_roi-hunter_pametove-karty_c_1007633___762968889285_~182700993776~&gad_source=1&gad_campaignid=22775198043) |             |
| motor controller   | L298N                                                              |        1 751 Ft | 1 pcs  |        1 751 Ft | [hestore](https://www.hestore.hu/prod_10036621.html?gross_price_view=1&source=gads&lang=hu&gad_source=1&gad_campaignid=17335669125)                                                                                                                             |             |
| servo controller   | PCA9685                                                            |        1 812 Ft | 1 pcs  |        1 812 Ft | [hestore](https://www.hestore.hu/prod_10046486.html?gross_price_view=1&source=gads&lang=hu&gad_source=1&gad_campaignid=17335669125)                                                                                                                             |             |
| motor              | blue TT motor                                                      |        1 540 Ft | 1 pcs  |        1 540 Ft | [techfun](https://techfun.hu/termek/egyenaramu-motor-sebessegvaltoval-3v-6v-fem-fogaskerekekkel/?gad_source=1&gad_campaignid=21163362174)                                                                                                                       |             |
| servo              | MG995                                                              |        3 487 Ft | 1 pcs  |        3 487 Ft | [hestore](https://www.hestore.hu/prod_10035811.html)                                                                                                                                                                                                            |             |
| lidar              | YDliDar x4 Pro                                                     |        30 061 Ft | 1 pcs  |        30 061 Ft | [sos electronic](https://www.soselectronic.com/hu-hu/products/ydlidar/x4-pro-375552)                                                                                                                                                                            |             |
| camera             | PixiCam 2.1                                                        |        36 381 Ft | 1 pcs  |        36 381 Ft | [tribotix](https://tribotix.com/product/pixycam2-1/)                                                                                                                                                                                                            | (107,7 usd) |
| buck 1             | LM2596S-M-PSU                                                      |        1 411 Ft | 1 pcs  |        1 411 Ft | [hestore](https://www.hestore.hu/prod_10035610.html?gross_price_view=1&source=gads&lang=hu&gad_source=1&gad_campaignid=17335669125)                                                                                                                             |             |
| buck 2             | XL4015 DC-DC Konverter, Step Down - 5-35V max 5A, CC,CV, "Origin'" |        990 Ft | 2 pcs  |        1 980 Ft | [modulshop](https://modulshop.hu/dc-dc-konverter-step-down-300w-20a-800)                                                                                                                                                                                        |             |
| buck 3             | DC-DC konverter Step down 300W 20A                                 |        2 700 Ft | 1 pcs  |        2 700 Ft | [modulshop](https://modulshop.hu/xl4015-dc-dc-konverter-step-down-converter-5-35v-max-5a-cccv-akku-tolto-tapegyseg-662)                                                                                                                                         |             |
| battery            | 18650 battery                                                      |        2 858 Ft | 12 pcs |        34 296 Ft | [tme](https://www.tme.eu/hu/details/us18650vtc6/akkumulatorok/murata/us18650vtc6-3000mah/?brutto=1&currency=HUF&utm_source=google&utm_medium=cpc&utm_campaign=W%C4%98GRY%20%5BPMAX%5D%20Segment_A&gad_source=1&gad_campaignid=19869887707)                      |             |
| filament           | ecoPLA Silk blue, 1,75 mm / 1000 g                                 |        8 860 Ft | 1 pcs  |        8 860 Ft | [3d jake](https://www.3djake.hu/3djake/ecopla-silk-kek?sai=16756&gad_source=1&gad_campaignid=22839632862)                                                                                                                                                       |             |
| flexibily filament | Nylon PA12+CF15, 2,85 mm / 500 g                                   |        25 390 Ft | 1 pcs  |        25 390 Ft | [3d jake](https://www.3djake.hu/fiberlogy/nylon-pa12cf15)                                                                                                                                                                                                       |             |
| oter               | (shipping costs, customs, other)                                   |        20 000 Ft | 1 pcs  |        20 000 Ft |                                                                                                                                                                                                                                                                 |             |
=======

# BPT Robotics – Ljubljana 2025

Ez a projekt a **BPT Robotics** 2025-ös ljubljanai versenyére készült robotrendszer teljes kódját és dokumentációját tartalmazza.  
A rendszer **Ubuntu 20.04.5 Server** operációs rendszeren fut, Raspberry Pi és egyéb perifériák segítségével.

---

## 📌 Áttekintés

Ez a robot önálló navigációs képességekkel, érzékelőintegrációval és versenyre optimalizált vezérlési logikával rendelkezik.  
A projekt célja, hogy gyorsan telepíthető és karbantartható legyen, valamint biztosítsa a stabil teljesítményt a versenyhelyzetekben.

**Főbb jellemzők:**
- Raspberry Pi alapú vezérlés
- Lidar-alapú térérzékelés
- Több modulból álló kódstruktúra (navigáció, érzékelők, motorvezérlés)
- Könnyen telepíthető és futtatható

---

## 🛠 Hardverkövetelmények

- Raspberry Pi (Bookworm vagy újabb támogatással)
- **YDLidar X4 Pro** érzékelő
- Motorvezérlő modul(ok)
- 3D nyomtatott alkatrészek
- Egyéb szenzorok a feladatnak megfelelően

---

## 🚀 Telepítés és futtatás

1. Klónozd a repót:
   ```bash
   git clone https://github.com/BPTRobotics/BPTrobotics-Ljubjana-2025.git
   cd BPTrobotics-Ljubjana-2025


2. Függőségek telepítése:

   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3 python3-pip
   pip3 install -r requirements.txt
   ```

3. A robot futtatása:

   ```bash
   python3 main.py
   ```

---

## 🖥 Operációs rendszer kompatibilitás

✅ Teljes mértékben kompatibilis **Ubuntu 20.04.5 Server** verzióval.

---

## 📊 Rendszerfolyamat

![Untitled](https://github.com/user-attachments/assets/b90f29bd-58c5-48f3-bd24-31660947c774)


---

## 📄 YDLidar X4 Pro – Raspberry Pi Bookworm beállítás

A Raspberry Pi Bookworm OS-ben a `/dev/ttyUSB0` eszköz automatikusan csatlakozik a `dialout` és `plugdev` csoportokhoz.
Ezért szükséges hozzáadni a felhasználót ezekhez a csoportokhoz:

```bash
sudo usermod -aG dialout $USER
sudo usermod -aG plugdev $USER
```

Majd újraindítani a rendszert, vagy kijelentkezni és vissza.

A **YDLidar SDK** telepítéséhez:

```bash
sudo apt install cmake pkg-config
git clone https://github.com/YDLIDAR/YDLidar-SDK.git
cd YDLidar-SDK
mkdir build && cd build
cmake ..
make
sudo make install
```

Tesztelés:

```bash
ydlidar_test
```
>>>>>>> Stashed changes
