# BPT Robotics – Engineering Documentation 2026


##### **Team name:** BPT Robotics
##### **Members:**
- **Boldizsár Szakács - Békési** *- software developer, algorithm manager, sensor data processing*
- **Péter Márkus** *- mechanical design, assembly, 3D printing and prototyping, electronic design*
- **Tibor Bogar** - *electronics, cabling*

**Country:** Hungary<br>
**Category:** WRO Future Engineers<br>
**Competition location:** Győr, Hungary<br>
**Date:** June 26–27, 2026

## 2. The task
The objective of the WRO Future Engineers category is to design and build a fully
autonomous robot capable of completing a randomly generated obstacle course without
any human intervention.
The robot must:
- Independently map its environment,
- Recognize and bypass obstacles,
- Make decisions based on visual information (such as colors and walls),
- Reach its destination via the shortest and most efficient route, as the elapsed time factors into the final score.

This task presents a simultaneous mechanical, electronic, and software engineering
challenge, as the robot must process incoming data and react in real-time.
An additional constraint during development was that the robot&#39;s dimensions could not
exceed 300 × 200 × 300 mm, and its total weight had to remain under 1.5 kilograms.
We began our work with thorough planning. First, based on our prior experience, we
designed the structure and operating principles of the robot. Following this, Boldizsár
initiated software development and integration with the operating system.
He first developed and fine-tuned the functionality for the Open Challenge. Once that
was operating stably and reliably, he expanded the system with features for the Obstacle
Challenge.
Following numerous testing and development cycles, the final robot configuration was
completed.

![Robot photo](./img/robots/Robot%20Casual%20(6).jpg)

## 3. Robot concept
Our robot is a four-wheeled, rear-wheel-drive, and rear-wheel-steering platform designed
with stability, modularity, and serviceability in mind. Our primary goal was to create a
system capable of real-time decision-making with minimal latency.

The driven and steered rear axle enables extremely precise maneuvering. The robot&#39;s
central processing unit is a Raspberry Pi 4 Model B (4 GB), running custom control
software written in Python.

**Key System Components**
- Pixycam 2.1: Used for fast image and color recognition (we utilized a Husky Lens
camera during the September competition).
- YDLIDAR X4 Pro: Provides 360-degree environmental mapping and delivers
precise data up to a distance of 10 meters.
- GY-BNO085 IMU: Responsible for precise heading retention and motion correction.
- L298N Motor Driver: Regulates the drive motor via PWM signals.
- PCA9685 Control Module: Ensures precise control of the steering servo motor.

One of the most critical elements of this concept is its modular design. Thanks to this,
any component can be quickly replaced, and the chassis architecture allows for future
upgrades, such as installing higher-performance motors or new sensors.


![Team photo](./img/robots/Robot%20Casual%20(4).jpg)![Team photo](./img/robots/Robot%20Casual%20(3).jpg)

## 4. Hardware details
![Circuit photo](./img/else/Untitled%20(1).jpg)
| Component             | Function                                                       | Comment                  | Justification                                                                 |
|-----------------------|----------------------------------------------------------------|--------------------------|-------------------------------------------------------------------------------|
| Raspberry Pi 4 (4GB)  | Central control, data processing                               | Running Python code      |A reliable and proven solution, though its performance is becoming a limiting factor, so we plan to upgrade to a aspberry Pi 5 in the future. |
| L298N motor controller| Driven motor control                                           | PWM signal-based         | Affordable and reliable device. |
| PCA9685               | Control of the rotation of the driven shaft                    |                          | Simple to use and stable module.                                       |
| MG995                 | Rotating the driven shaft                                      | Metal metatarsal         | High-torque and durable servo. |
| Blue TT motorcycle    | Propulsion / Drive | Metal metatarsal         | Provides adequate torque and is easily controlled within this price range.    |
| PixyCam2.1            | Color recognition                                              | Direct USB communication | Fast image processing; color recognition is natively supported.|
| YDLIDAR X4 Pro        | 360° mapping, guidance, precise location                       | 10 m range               | Reliable operation, but the initial setup is challenging; package installation is difficult and proper documentation is lacking. |


## 5. Software architecture

![Sensor circuit photo](./img/else/Untitled%20(3).jpg)

Our developer implemented an innovative approach to utilize multiple sensors collectively, which he named the "module system." Its core principle is that the control software processes sensor data by breaking it down into distinct operational states.

For example, while the robot is moving straight, it uses the LIDAR for distance measurements, while the gyroscope handles heading retention. This is designated as Module 1.
When the robot reaches a turn, the LIDAR is temporarily sidelined, and the turn is executed solely based on gyroscope data. This is designated as Module 2.
The robot continuously and dynamically switches between individual modules during operation.

### **Modules:**
![OPEN CHALLENGE](./img/else/Sprint%20Planning%20-%20OPEN.jpg)
![OBSTACLE CHALLENGE](./img/else/Sprint%20Planning%20-%20OBSTACLE.jpg)

##### **OPEN CHALLENGE's modules:**
![Module 1](./img/else/Sprint%20Planning%20-%20Module%201.jpg)
![Nodule 2](./img/else/Sprint%20Planning%20-%20Module%202.jpg)
##### **OBSTACLE CHALLENGE's modules:**
![Module 3](./img/else/Sprint%20Planning%20-%20Module%203.jpg)
![Module 4](./img/else/Sprint%20Planning%20-%20Module%203.jpg)
<sub>

**Open Challenge Modules**
- Module 1
- Module 2

**Obstacle Challenge Modules**
- Module 3
- Module 4


### **The Principle of Navigation**
The robot continuously reads:
- Distance data from the LIDAR,
- Colors detected by the camera,
- Heading data from the gyroscope.

If an obstacle is detected:

- It turns left upon detecting a red marker,
- It turns right upon detecting a blue marker,
- Otherwise, it stops and slowly bypasses the obstacle.

If no obstacle is detected, it continues forward in a straight line, using the gyroscope to continuously correct its heading.

**Running the Project**
Cloning the Repository
```
git clone https://github.com/BPTRobotics/bptrobotics-fe-26--wro.git
cd bptrobotics-Ljubjana-2025
```

Installing Dependencies
```
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip
pip install -r requirements.txt
```
Launching the Robot Software

```
python3 -m WRO.main
```

Testing Individual Modules
```
python3 -m WRO.control.servo.test
python3 -m WRO.control.motor.test
python3 -m WRO.sensors.camera.test
python3 -m WRO.sensors.lidar.test
python3 -m WRO.sensors.gyroscope.test
```

**Compatibility**
The system is exclusively compatible with Ubuntu Server 20.04.5 LTS, which can be deployed using the Raspberry Pi Imager.Implementing High-Precision Heading Retention – A LIDAR-Based SolutionDuring development, heading retention relying on the gyroscope (GY-BNO085) proved unreliable over longer durations: the sensor suffered from drift over time and required frequent recalibrations, posing a significant risk in a competitive environment. Consequently, we replaced the robot's heading retention with a purely LIDAR-based solution.This solution exploits the fact that the Future Engineers track runs between two parallel walls, allowing the robot to determine its angular orientation directly relative to the walls. From the LIDAR scan, the data points falling onto the side walls are projected into the robot's local coordinate system. A straight line is then fitted to these points using the least squares method (utilizing the atan2 or arc tangent function). The slope of the fitted line defines the heading error, where 0° corresponds to moving straight, parallel to the walls. The results from both side walls are averaged (rather than using the median), ensuring the measurement remains robust even against missing or noisy LIDAR points, thus precisely yielding the angle of parallelism deviation, known as the theta angle ($\theta$).(Note: atan2 was implemented instead of standard atan to prevent division sign errors; since $\tan = \sin/\cos$, both $-\sin/-\cos$ and $\sin/\cos$ would yield a positive result, while $-\sin/\cos$ and $\sin/-\cos$ would always be negative, making it impossible to determine the exact angle during large rotations).The primary advantages of this approach are that it eliminates drift, requires no calibration, and is perfectly tailored to the geometry of the task.

### **Operation of the Module System**
The control software divides navigation into well-defined operational states (modules):
- Module 1 (Straight Section): The robot travels forward using LIDAR-based heading retention to follow the walls while continuously monitoring the forward distance. When the distance to the front wall falls below a predefined threshold, this module terminates.
- Module 2 (Turn): The robot executes a 90-degree turn into the next corridor. The robot automatically determines the direction of the turn based on lateral clearance distances.

The robot continuously alternates between these two modules throughout the entire run to navigate the course.

**LIDAR Integration**
Environmental sensing is performed by a YDLIDAR X4 Pro sensor integrated into the system via the ydlidar_ros_driver package within a ROS Noetic environment. The X4 Pro requires a single-channel operating mode configuration; without this setting, the driver fails to initiate the scan—identifying this quirk required extensive debugging. The sensor data is read directly from the ROS /scan topic.

The LIDAR driver launches automatically at system startup as a systemd service, ensuring that sensor data is already available when the primary control program is initialized.

### **Approach to the Obstacle Challenge**
To complete the obstacle course, we developed and implemented a solution that blends camera-based color recognition with LIDAR distance measurements. The operating principle is as follows:

- The camera detects the colored marker pillars placed on the track.
- The LIDAR provides the exact distance and heading of the specific obstacle.
- Based on the identified color, the robot decides which side to bypass the obstacle, and once clear, it returns to standard corridor-following navigation.

Color recognition was initially handled by a HuskyLens camera, which was later upgraded to a more advanced camera module to achieve faster and more accurate processing.

## 6. Development 
##### **Transfer of previous experiences:**
Our previous robot was too heavy. To reduce overall mass, we fabricated several
components using 3D printing and replaced multiple ultrasonic sensors with a single
LIDAR unit—this optimized configuration was already implemented for the competition in
Slovenia last September.

Although we increased the battery count for the Slovenian event to optimize power
delivery and extend battery life, this significantly increased the weight. Consequently, the
motor lacked sufficient torque. To remedy this, we are reducing the battery configuration
back to 3 cells but using higher-capacity batteries, and we will carry multiple spares to
swap out during testing.
Instead of the older USB webcam, we integrated a PixyCam 2.1 camera, which allows
for significantly faster and more accurate color recognition.
Additionally, we selected a more modern and precise gyroscope module, which
enhances heading retention and minimizes unnecessary path corrections.

#### **Key Stages of Development:**
1. Conceptual design and creation of initial CAD models.
2. Assembly of the first prototype and baseline drivetrain configuration.
3. Integration of the LIDAR, PixyCam, and IMU modules.
4. Development and refinement of navigation and obstacle avoidance algorithms.
5. System fine-tuning, comprehensive testing, and bug fixing.
6. Pre-competition calibration and preventative mechanical maintenance.

## 7. Mechanical Operation and Structure
On our very first robot design, we intended to use front-wheel drive or at least front-axle
steering (similar to standard passenger or RC cars). However, modifying a pre-built RC
car did not offer enough of an engineering challenge and would have severely limited
our design freedom, so we discarded that path. This led to our current drivetrain and
steering layout: we handle all movement via rear-wheel steering combined with rear-
wheel drive. This approach is highly advantageous because it makes maneuvering far
simpler (forklifts in large warehouses operate on this identical principle). It enables the
robot to execute tight turns in highly restricted spaces, whereas front-wheel steering
would require a much larger turning radius.

### **The Robot Consists of Three Main Tiers:**
- **Control Tier (Lowest Deck):** Houses the power supply infrastructure (dual 3x 18650
battery holders), the servo controller (PCA9685), the motor controller (L298N), the
primary processing unit (Raspberry Pi), and the IMU sensor (GY-BNO085).
- **LIDAR Tier (Middle Deck):** Contains the high-torque servo motor (MG995) that steers
the rear axle, along with 3 buck converters and the LIDAR unit. A key design challenge
here was positioning components so that the steering servo would not obstruct the LIDAR&#39;s line of sight, ensuring unhindered 360° visibility while strictly adhering to the
maximum dimensional boundaries.
- **Camera Tier (Top Deck):** Accommodates the primary camera and the system display.
During benchmarking, displaying critical diagnostics on screen is immensely helpful; it
lets us spot anomalies instantly (e.g., if it misses a wall, indicating the LIDAR needs
adjustment or is not perfectly horizontal), and displays system boot and readiness
status. Boldizsár programmed a short launch animation—a liftoff spaceship—that plays
while the camera, LIDAR, and gyroscope initialize. Although it compromises aesthetics
slightly, all excess cabling is coiled and secured on this top deck (we kept the original
lengths so the cables remain reusable for our other project platforms). Everything is
centralized here via WAGO blocks, routing all 12V and 5V power lines to their respective
components.

### **Drivetrain Layout**
I engineered a custom motor mount attached directly to the rotating output shaft of the
servo, allowing the drive motor to be bolted longitudinally. This integrates the driven and
steered axle into a single compact subassembly, which proved significantly simpler and
more robust than fabricating an entire separate steering rack mechanism.


## 8. Electronics
The 18650 battery carriers (configured as 2x3 cells) are wired in parallel to maximize
current capacity. From there, the power rails run up to the camera tier, where current is
distributed across 3 buck converters via WAGO connectors. WAGO blocks are an
excellent choice because they allow clean, secure multi-directional power distribution
without soldering or relying on unreliable twisted-wire connections. The entire robot
utilizes a unified common ground rail to prevent electrical floating and signal anomalies.
Three separate buck converters were essential because, based on past experience, the
Raspberry Pi is highly sensitive and malfunctions if any other peripheral shares its power
regulator. The same applies to the PCA9685 servo controller. Thus, a third buck
converter was dedicated strictly to stepping down the main voltage to prevent overvolting
our 6V drive motor with 12V. For a long time, we supplied exactly 5.0V to the Pi to stay
safe, but it consistently triggered undervoltage warnings under load, so I increased the
regulator output to 5.2V (5.25V being the absolute maximum threshold). Even now,
minor power dips occur occasionally because we power quite a few hardware
components directly from its logic rails—including the camera, the LIDAR, the servo
driver chip, and the IMU sensor.
Up until the Slovenia competition, we relied entirely on ultrasonic distance sensors (three
mounted at the front at 45° angles and one facing dead center). For September, we fully
swapped them out for a YDLIDAR X4 Pro, which has made mapping walls and tracking
obstacles immensely easier. Product reviews and documentation claimed this LIDAR
was incredibly straightforward to deploy with comprehensive libraries. However, while

our initial basic checks on Windows went smoothly, we faced major software roadblocks
on Linux once the robot was assembled. Despite the provided guides, a large portion of
the required package repositories returned &#39;404 Not Found&#39; errors. Following extensive
troubleshooting, AI-assisted debugging, and leveraging notes from an older X4 setup, it
took roughly a week to fully bring the LIDAR online—but it now operates flawlessly. We
also 3D-printed a custom leveling fixture for it because space constraints forced us to
mount the LIDAR upside down. Over time, mechanical vibration and rotation cause one
side to sag slightly. The fixture features 4 extended alignment brackets with hollow V-
notches and matching vertical guide posts below, allowing us to calibrate the LIDAR to
be perfectly horizontal (assuming a level floor surface). When we get consistent long-
range returns on all four sides and can perfectly see the base of the V-notches, the
LIDAR is properly calibrated.
We read similar claims about the gyroscope being completely plug-and-play in any
physical orientation—which, unsurprisingly, turned out to be false as well. Although the
packages and documentation were reasonably complete, the module over I2C regularly
outputs completely random, erratic data at arbitrary intervals, which causes the robot to
lose track if not heavily filtered and smoothed in code. It also suffers from occasional bus
lockups where it stops transmitting entirely. To mitigate this, we ignore sudden extreme
spikes, but when the sensor freezes or transmits corrupt streams for consecutive
seconds during a turn approach, the robot executes the maneuver incorrectly.
Consequently, the gyroscope was utilized merely as a general directional guide in
Slovenia, as we unfortunately could not fully rely on its raw data streams.

## 9. Innovations
- Real-Time Sensor Fusion: One of our platform&#39;s most vital innovations is the
implementation of real-time sensor fusion combining LIDAR and vision data, allowing
for highly accurate, low-latency decision-making.
- Modular Architecture: The modular layout allows for rapid plug-and-play component
replacement, which is incredibly advantageous during high-stakes competition
environments by streamlining field repairs and adjustments.
- High-Precision Tracking: Utilizing advanced sensor modules ensures that both
Open Challenge and Obstacle Challenge routines are completed with significantly
higher accuracy, speed, and repeatability.

## 10. Future Plans
- We intend to upgrade to a Raspberry Pi 5 to harness its expanded computational
overhead, allowing us to execute more complex filtering algorithms and process
sensor data faster and more precisely.
- We plan to re-engineer a lighter yet structurally stronger chassis. Ideally, the frame
will be fabricated out of high-strength, thin-gauge sheet metal, achieving an optimal
balance between low weight and rigidity.
- We aim to integrate a drive motor with higher power and torque. A clear limitation of
our current setup is that the standard TT motor lacks the torque needed to reliably
propel the robot at target velocities. When battery levels drop or if the motor is dialed
to lower speeds, it tends to stall entirely, even though it spins freely when
lifted—proving the urgent need for a more robust powertrain.
- In terms of power distribution, we want to implement a higher-capacity, lighter
battery pack. While the current system easily covers a full day of testing, we want to
achieve a regulated power rail where motor output torque remains completely
unaffected by low battery voltage states.

## 11 Problems and Challenges
In March, we attended a robotics demonstration organized by Edutus University in collaboration with the Eger Vocational Training Center. Several teams from our school participated, and we also brought along our custom RMRC competition track. Prior to the event, as we began preparing and booted up the robot for the first time in months, we discovered that the SD card containing our stable September build had corrupted and was completely unreadable on both Windows and Linux platforms. Unfortunately, my local backup had been misplaced, and our cloned secondary SD card contained an older iteration, leaving us with no viable restore point. Consequently, we had to redownload all the required packages, and any code changes that had not been pushed to GitHub were permanently lost. This severely hindered our preparation for this year's finals, as multiple subroutines that worked flawlessly in September had to be re-engineered from scratch.

Furthermore, during the weekend immediately preceding the competition, the SD card failed entirely along with all its data during a critical backup operation. While pushing vital updates to GitHub—including the LIDAR fix, camera integration, and gyroscope calibration—the SD card short-circuited. When inserted into a card reader or laptop, it immediately begins to overheat, confirming a hardware short-circuit; fortunately, the Raspberry Pi itself remained undamaged. Nevertheless, this failure destroyed all our recent progress, forcing us to completely reconstruct weeks of engineering work in the final days leading up to the competition.

## 12. BOM
|product name | modell                                                             | unite price       | piece  |shop                                                                                                                                                                                                                                                            |             |
| ------------------ | ------------------------------------------------------------------ | ----------------- | ------ | --------------------------------- |  ----------- |
| controll panel     | Raspberry pi 4 mdell B, 4gb                                        |        40 900 Ft | 1 pcs  | [pi shop](https://www.pi-shop.hu/raspberry-pi-4-model-b-4gb?gad_source=1&gad_campaignid=376802345)                                                                                                                                                              |             |
| sd card            | sandisk 128gb sd card                                               |          17 520 Ft | 1 pcs  | [alza](https://www.alza.hu/sandisk-microsdxc-128-gb-extreme-action-cams-and-drones-rescue-pro-deluxe-sd-adapter-d7261110.htm?o=1) |             |
| motor controller   | L298N                                                              |        1 700 Ft | 1 pcs  |[hestore](https://www.hestore.hu/prod_10036621.html?gross_price_view=1&source=gads&lang=hu&gad_source=1&gad_campaignid=17335669125)                                                                                                                             |             |
| servo controller   | PCA9685                                                            |        1 616 Ft | 1 pcs  | [hestore](https://www.hestore.hu/prod_10046486.html?gross_price_view=1&source=gads&lang=hu&gad_source=1&gad_campaignid=17335669125)                                                                                                                             |             |
| motor              | blue TT motor                                                      |        1 138 Ft | 1 pcs  | [techfun](https://techfun.hu/termek/egyenaramu-motor-sebessegvaltoval-3v-6v-fem-fogaskerekekkel/?gad_source=1&gad_campaignid=21163362174)                                                                                                                       |             |
| servo              | MG995                                                              |        2 490 Ft | 1 pcs  | [hestore](https://www.hestore.hu/prod_10035811.html)                                                                                                                                                                                                            |             |
| lidar              | YDliDar x4 Pro                                                     |        34 931 Ft | 1 pcs | [sos electronic](https://www.soselectronic.com/hu-hu/products/ydlidar/x4-pro-375552)                                                                                                                                                                            |             |
| camera             | PixiCam 2.1                                                        |        33 170 Ft | 1 pcs  | [tribotix](https://tribotix.com/product/pixycam2-1/)                                                                                                                                                                                                            | (107,7 usd) |
| gyroscope | GY-BNO085 | 12 238 |1 pcs | [hestore](https://www.hestore.hu/prod_10044901.html) |
| buck 1             | LM2596S-M-PSU                                                      |        1 413 Ft | 1 pcs  |  [hestore](https://www.hestore.hu/prod_10035610.html?gross_price_view=1&source=gads&lang=hu&gad_source=1&gad_campaignid=17335669125)                                                                                                                             |             |
| buck 2             | XL4015 DC-DC Konverter, Step Down - 5-35V max 5A, CC,CV, "Origin'" |        990 Ft | 2 pcs  | [modulshop](https://modulshop.hu/dc-dc-konverter-step-down-300w-20a-800)                                                                                                                                                                                        |             |
| buck 3             | DC-DC konverter Step down 300W 20A                                 |        2 700 Ft | 1 pcs  |  [modulshop](https://modulshop.hu/xl4015-dc-dc-konverter-step-down-converter-5-35v-max-5a-cccv-akku-tolto-tapegyseg-662)                                                                                                                                         |             |
| battery            | 18650 battery                                                      |        2 558 Ft | 12 pcs | [tme](https://www.tme.eu/hu/details/us18650vtc6/akkumulatorok/murata/us18650vtc6-3000mah/?brutto=1&currency=HUF&utm_source=google&utm_medium=cpc&utm_campaign=W%C4%98GRY%20%5BPMAX%5D%20Segment_A&gad_source=1&gad_campaignid=19869887707)                      |             |
| filament           | ecoPLA Silk blue, 1,75 mm / 1000 g                                 |        7 920 Ft | 1 pcs  |  [3d jake](https://www.3djake.hu/3djake/ecopla-silk-kek?sai=16756&gad_source=1&gad_campaignid=22839632862)                                                                                                                                                       |             |
| flexibily filament | Nylon PA12+CF15, 2,85 mm / 500 g                                   |        22 690 Ft | 1 pcs  |  [3d jake](https://www.3djake.hu/fiberlogy/nylon-pa12cf15)                                                                                                                                                                                                       |             |
| oter               | (shipping costs, customs, other)                                   |        20 000 Ft | 1 pcs  |        20 000 Ft |                                                                                                                                                                                                                                                                 |             |
