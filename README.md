## Project Overview
This project, developed by Drew Rigby as a capstone for the Applied Computing major at the University of Washington Bothell, integrates computer science concepts with oceanography, reflecting the intersection of my major and minor. The objective was to design and build an automated pH sensor capable of sampling water and providing accurate pH measurements.

An important goal of this project is to make it accessible for high school students, even those with little to no background in oceanography, coding, or electrical engineering. To achieve this, the project includes a comprehensive manual that provides detailed, step-by-step instructions, ensuring that anyone can build, use, and understand the sensor regardless of prior experience. This focus on accessibility aims to inspire students and foster interest in STEM and environmental science.

### What is pH and how is it important to oceanography?
pH measures the acidity or alkalinity of a substance. This project focuses specifically on the pH of water, a critical parameter in oceanography. One of the most pressing issues in this field is ocean acidification, a phenomenon where the ocean's pH decreases, becoming more acidic.

Ocean acidification has far-reaching consequences for marine ecosystems. For example, reduced levels of calcium carbonate in acidic waters hinder marine organisms, such as mollusks and corals, from forming their shells and skeletons. This disruption cascades through the food chain, potentially impacting human industries and livelihoods. Monitoring pH levels in vulnerable areas can provide valuable insights into the causes and effects of ocean acidification, aiding research and mitigation efforts.

### What relevance does this have to computer science?
This project leverages computer science principles through the use of a Raspberry Pi Pico and embedded systems programming to bring the sensor to life. I applied my expertise to develop a library that simplifies interaction with the sensor, enabling users to perform essential tasks with straightforward functions while maintaining flexibility for advanced customization.

For example, users can easily explore different configurations, such as testing alternative calibration curves using purple instead of green color indicators, by utilizing specific functions provided in the library. This design empowers users to adapt the sensor's functionality to their needs, balancing ease of use with the ability to conduct more complex experiments.


### What Use Might This Project Have in High School Curriculums?
This project is an excellent tool for high school science curriculums, offering students hands-on experience with STEM concepts while encouraging critical thinking and hypothesis testing. The sensor’s flexibility, made possible through its programmable library, allows students to explore a variety of experiments and customize its functionality to suit their needs. For instance, the library includes functions that enable users to adjust calibration curves or test alternative parameters, such as using different color indicators for measurements.

This adaptability provides students with the opportunity to investigate real-world scientific questions, such as how environmental factors like temperature or salinity influence pH levels. By designing and conducting their experiments, students can better understand the scientific method and the role of data in validating hypotheses. The comprehensive manual ensures accessibility, making the sensor usable even by those with little to no prior knowledge of oceanography, coding, or electrical engineering. This combination of flexibility, ease of use, and educational potential makes the project an invaluable resource for inspiring curiosity and fostering skills in STEM fields.

## Why use this as a project?
This project offers a unique blend of accessibility, adaptability, and real-world relevance, making it an excellent choice for educators, students, and STEM enthusiasts alike.

Hands-On Learning: The sensor provides a tangible way to explore STEM concepts, bridging the gap between theory and practice. Students can learn about coding, embedded systems, and environmental science while working on a meaningful, real-world application.

Flexibility: The custom library included with the project allows for significant experimentation and customization. Users can test various calibration methods, explore alternative parameters, and tailor the sensor’s functionality to align with specific learning objectives or experiments.

Accessibility: Designed with ease of use in mind, this project is accessible to individuals with minimal background knowledge in coding, oceanography, or electrical engineering. The detailed manual ensures that even beginners can confidently assemble, program, and operate the sensor.

Real-World Relevance: By focusing on issues like ocean acidification, this project highlights the critical role of technology in addressing environmental challenges. It inspires students to think about how STEM disciplines can be applied to solve pressing global problems.

Incorporating this project into a classroom or individual learning plan can spark curiosity, enhance problem-solving skills, and encourage exploration in the interconnected fields of science and technology.




## What will I need?

|ITEM|QUANTITY|PRICE|
|---|---|---|
|[Raspberry Pi Pico](https://www.adafruit.com/product/5525)|1|$5|
|[Submersible 3V DV Water Pump](https://www.adafruit.com/product/4547)|1|$2.95|
|[Adafruit TSL2591](https://www.adafruit.com/product/1980)|1|$6.95|
|[Common Cathode RGB Light](https://www.sparkfun.com/products/105)|1|$2.25|
|[Phenol Red pH Indicator Dye](https://www.poolweb.com/products/taylor-ph-indicator-solution-3-4-oz-dropper-bottle-r-0014-a)|1|$3.38|
|[GT-U7 GPS](https://www.amazon.com/Navigation-Satellite-Compatible-Microcontroller-Geekstory/dp/B07PRGBLX7)|1|$14.99|
|[Cuvette 1.5ML *This link only sells by the 10s*](https://www.amazon.com/Standard-Disposable-Professional-Transparent-Spectrophotometers/dp/B07VGDLMMH/ref=sr_1_3?c=ts&dib=eyJ2IjoiMSJ9.Wdu-PneNgzy9HWgzqQpF4NBLH8vNxU3TnJP97jJI6K5CkgJXkyv-UAtbcqg3fmO8-xdRdEMT4H2ownpaVPMMaHXzsNkF2tbxrW2HuE7zxEcOtA-MBHBYkHV6HmPOE7fLuzGbI9rZSdy10q5kvpcnMFaT6kUqf7-DJbqa2snUjLDDArWAbArXT2QCQDNtBNRAVqzQem_6vUD536fPMKD2lA25uliqrV63WyjNQt6MhQQZa2gJIJN3Nr4TtDbrs_wtAlUK7JVekIs8ODg29hQC5DgXq_pKflS9gyPv6p5u7JI.71dC1E2u98ecs3xq6WpQIMiJ2LN3HRsqwCd--ipGPMc&dib_tag=se&keywords=Lab+Cuvettes&qid=1731213259&s=industrial&sr=1-3&ts_id=318063011)|1|$11.89|
|[20ML Syringe](https://aaprintsupplyco.com/products/neo-sy?variant=32983529488468&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&srsltid=AfmBOoqIWNiGqBFyY0_SuPJI8O2K_qD1SE5h-Gxxlw2TRUkzQtm_g3tpRyg)|1|$2|
|[Plastic Water Resivour of your choosing](https://www.berlinpackaging.com/3600b03-2-oz-natural-hdpe-plastic-wide-mouth-packer-bottles-white-screw-top-cap/?utm_source=google&utm_medium=cpc&utm_campaign=PMax%3A%20%28ROI%29%20Shopping%20-%20Smart%20-%20Bottles%20-%20HDPE&utm_id=21016660230&utm_content=&utm_term=&gad_source=1&gclid=CjwKCAjw9cCyBhBzEiwAJTUWNQKtTxFOMuFaX5nl7jv3UimzFBc7M9naBo_MlGrCpJRQH1XFCfGRXBoCqS4QAvD_BwE)|1|$0.38|
|[Water Proof Casing](https://www.amazon.com/Waterproof-Plastic-Electronic-Junction-Enclosure/dp/B07M5SZNR9/ref=asc_df_B07M5SZNR9/?tag=hyprod-20&linkCode=df0&hvadid=693308318554&hvpos=&hvnetw=g&hvrand=13402671431230684644&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9033316&hvtargid=pla-615797795038&psc=1&mcid=7bd63229ef183828938a82ddd5446444&gad_source=1)|1|$9.49|
|[Peristaltic Pump](https://www.adafruit.com/product/1150)|1|$24.95|
|Total||$69.55|

This does not include perfboards, wires, wiring tools, solder, soldering tools, or resistors. Those can be found below if you do not have them otherwise please skip past to the FILL IN NAME HERE section
### Perfboard or Breadboard?
Perfboards are used when you are creating electrical circuits and would like a stable connection that doesnt require having jumper cables. This
does require soldering for connection of pins which can be dangerous if unsupervised. This also allows for less errors as things are easier to 
break. If you are going with perfboards I recomend a breadboard layout as there are the easiest to use as they have power buses(See Vocabulary)
built in. If you are going to use perfboards I would recomend using a bread board to make sure that you have a good understanding of the 
electronics before soldering things into place.
![alt text](https://cdn-shop.adafruit.com/970x728/1609-00.jpg)

You can find a good perfboard [here](https://www.adafruit.com/product/1609) for $4.50

Breadboards on the other hand are less permenant but can have issues with pins not touching metal properly and are often seens as temporary solutions.
As said above in the perfboard section one should at least use a breadboard to plan out their circuit so one could save money by only using breadboards.
![alt text](https://cdn-shop.adafruit.com/970x728/4539-03.jpg)

You can find a good breadboard [here](https://www.mouser.com/ProductDetail/SparkFun/PRT-12002?qs=WyAARYrbSnYNJEbsmDuXsA%3D%3D&mgh=1&srsltid=AfmBOopsiO3PD5JWbhyFv99flrAnsKZhypC7DzSwbdvFXANliHVx4DNLneM) for $4.95

### Wires or Jumpers?
Choosing between bbuying wires or jumpers is very difficult. If possible one should buy both as it allows for modularity when creating the ciruits however
if you can only afford one option then there are many things to consider.

#### What tools do I have acccess too?
If you have access to no tools and are trying to do this project without using any you are going to have a difficult time. If you are still going to try to
replicate the project without tools then you are going to want to go with jumpers as you wont have to wory as much about shortening them to the size that 
you need. However you will have to at least have access to solder for this project as not every module on the project has headers and to use jumpers you will
need to solder on headers. If you have access to things like wire cutters and wire strippers then normal wire should work perfectly. This will allow you to 
have more modularity and wires also just feel more professional. It also helps if you have solder sleeves and a heat gun as it allows for less precision when
soldering as for difficult things you can use said solder sleeves instead.

### How do I solder?
Soldering is a skill in its own right that is very difficult to master. For this project you should allocate a week or more to making sure that your skills 
are properly up to par with solder before permently setting things into place. I reccomend starting with watching this video:
<a href="http://www.youtube.com/watch?feature=player_embedded&v=rK38rpUy568
" target="_blank"><img src="http://img.youtube.com/vi/rK38rpUy568/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="970" height="728" border="10" /></a>

## First Steps
Going forward I am going to assume that you are going to be working with proper tools, wire, perfboards, and will be soldering. I am also going to assume that
you 3D printed the parts that are required in the project. If you do not then you will have to go off from the instructions. If you have questions you can email
me at the email phsensorguide@gmail.com.

## Soldering Your PerfBoard
When soldering your perfboard it is very important to try and avoid errors as these sre semi permanent. 
![Raspberry Pi Pico Pinout](https://microcontrollerslab.com/wp-content/uploads/2021/01/Raspberry-Pi-Pico-pinout-diagram.svg)
I personally recommend that you dtart by soldering female header pins into the perfboard. The pico is 20 pins long so you will need a long enough strip of pins.
If you have a strip that us longer then you can use wire cutters to cut it down to size. Try and solder in a digonal pattern, soldering one corner then another.
This along with a stabilization method(Tape the item into place in the back side) should help keep the female headers straight so you can slot the pico in flush.
![Flush Pico](data:image/jpeg;base64,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)

