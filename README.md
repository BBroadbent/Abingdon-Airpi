# Abingdon-Airpi

Introduction
Since January 2017 a group of 4-5 students have worked on a system to track air
quality, light levels, temperature, humidity and barometric pressure.
Components
 Raspberry Pi – to monitor the sensors
 MCP3008 – An analogue to digital converter to enable the Raspberry Pi to
read the analogue Air quality and light sensors
 TGS2600 – An Analogue component which reads the number of Air
Contaminants
 LDR – An analogue component to monitor the amount of light
surrounding the setup
 AM2302/DHT22 – This sensor records Temperature and Humidity. It
uses the 1-wire interface and data is Digital
 BME280 – This sensor records temperature and barometric pressure It
communicates with the Pi digitally using either I2C or SPI.
Our Aim
In January 2017 Dr Frampton emailed Middle School with an invitation to take
part in a project.
“This project will involve designing, building and using a small air quality
monitoring station. I think it would be interesting to use our device to firstly test
the device under lab conditions (for example in monitoring air quality during
science lessons) before we launch in to a wider study of the air quality in a parts of
the school.
We will be using a Raspberry pi and some electronics to create the device and the
project itself will also suit those with some interest in programming, probably with
Python, but this is not an essential skill. Any interest in doing science will be
enough.”
Everybody who was interested met to discuss the ideas of what we wanted to
achieve and how we should approach this project. It became clear that I was the
most experienced having worked on a similar project before. We met in
February and got the project started.
Now
Currently we have a working breadboard that uses all the sensors to record each
value into a SQLite Database. This is so that in the future we can integrate the
database into a locally hosted webpage that could graph the data.
Over the summer holidays I designed and ordered custom PCBs which allowed
us to do all the functions of the breadboard while being much smaller and more
permanent.

Future
In the future we will be able to provide the data in a visual graph that can be
accessed from anyway on the school network. I have also considered adding an
LCD display to display the latest reading of the different variables. We also want
to have the graph and data displayed live on the TV screens in the science center.
We want
