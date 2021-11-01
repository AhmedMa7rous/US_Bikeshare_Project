# Explore US Bikeshare Data
<a href="https://ibb.co/BLNPsw1"><img src="https://i.ibb.co/rkstyvW/us-bikeshare.png" alt="us-bikeshare" border="0"></a>


## Overview
<p>In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States — Chicago, New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics.
You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.</p>

<p>In this project, you will use data provided by <a href="https://www.motivateco.com/">Motivate</a>, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.</p>

## What Software Do you Need?
To complete this project, the following software requirements apply:

<li>You should have Python 3, NumPy, and pandas installed using Anaconda
<li>A text editor, like <a href="https://www.sublimetext.com/">Sublime</a> or <a href="https://atom.io/">Atom</a> or <a href="https://www.jetbrains.com/pycharm/">pyCharm</a>.
<li>A terminal application (Terminal on Mac and Linux or Cygwin on Windows).
  
## Getting Started  
  
*To get this project and running it on your local machine for development and try it.* 
<li> Make sure all prerequisties are met  
<li> Clone this project on your machine by running  

     git clone https://github.com/ma7ros/US_Bikeshare_Project.git  

Or you can simply download the code from here    https://github.com/ma7ros/US_Bikeshare_Project/archive/refs/heads/master.zip
  
  
## Project details
  
  ### Bike Share Data
  
<p>Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.</p>
  
  ### The Datasets
  
<b>Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:</b>

<li>Start Time (e.g., 2017-01-01 00:07:57)
<li>End Time (e.g., 2017-01-01 00:20:53)
<li>Trip Duration (in seconds - e.g., 776)
<li>Start Station (e.g., Broadway & Barry Ave)
<li>End Station (e.g., Sedgwick St & North Ave)
<li>User Type (Subscriber or Customer) </br>
<b>The Chicago and New York City files also have the following two columns:</b>

<li>Gender
<li>Birth Year
  </br>
  <a href="https://ibb.co/Tvx9YTj"><img src="https://i.ibb.co/znTqQ59/new-york-data.png" alt="new-york-data" border="0"></a>
  
  
  ### Statistics Computed
  
<p>You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:</p>

<b>#1 Popular times of travel (i.e., occurs most often in the start time)</b>

<li>most common month
<li>most common day of week
<li>most common hour of day
</br>

<b>#2 Popular stations and trip</b>

<li>most common start station
<li>most common end station
<li>most common trip from start to end (i.e., most frequent combination of start station and end station)
</br>

<b>#3 Trip duration</b>

<li>total travel time
<li>average travel time
  </br>
  
<b>#4 User info</b>

<li>counts of each user type
<li>counts of each gender (only available for NYC and Chicago)
<li>earliest, most recent, most common year of birth (only available for NYC and Chicago)
  </br>
  
  ### The Files
  
<p>To answer these questions using Python, you will need to write a Python script. To help guide your work in this project, a template with helper code and comments is provided in a folder: <b>template</b> in <b>bikeshare.py</b> file, and you will do your scripting in there also. You will need the three city dataset files too:</p>

<li>chicago.csv
<li>new_york_city.csv
<li>washington.csv
<p>All three of these files are inside the csv_files folder . You may download and open up that zip file to do your project work on your local machine.</p>

<p>Some versions of this project also include a Project Workspace page in the classroom where the bikeshare.py file and the city dataset files are all included, and you can do all your work with them there.</p>
  

  
  
  
  

  
  
