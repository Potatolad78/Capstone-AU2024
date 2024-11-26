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
have more modularity and wires also just feel more professional.

### How do I solder?
Soldering is a skill in its own right that is very difficult to master. For this project you should allocate a week or more to making sure that your skills are properly up to par with solder before permently setting things into place. I reccomend starting with watching this video
<a href="http://www.youtube.com/watch?feature=player_embedded&v=rK38rpUy568
" target="_blank"><img src="http://img.youtube.com/vi/rK38rpUy568/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="970" height="728" border="10" /></a>