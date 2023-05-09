# PFCH23 - Ancient Wonders through Art
## About
Ancient Wonders through Art aims to showcase the Seven Wonders of the Ancient World through the art that was created in the same time period. The project uses a map and timeline generated with Python to showcase the wonders. It also uses the search function of the Metropolitan Museum of Art's API to locate art from the corresponding time period of each wonder. The goal is to help contextualize the cultural environment that existed alongside the creation of the wonders. 
It was created for the final project of the INFO-664 Programming For Cultural Heritage course. This course is offered through the School of Information at Pratt Institute.
It was created out of my personal interest in ancient history and architecture. I was interested displaying the art that was created alongside the wonders. 
## How to use this code
The project was completed in parts and used multiple Python scripts.
### The Map
The Map was created using the Folium library in Python. It is named wondersmap.py. 

To run this script yourself, install the Folium library to the operating system running Python. 
### The Timeline
I used Matplotlib library because it was interactive and showed the comparative spans of each wonder. I listed each wonder and the start and finish date. I added style formatting to ensure that the entire span would be covered and used MPLD3 to make it interactive in the browser. It is named wonderstimeline.py.

To run this script yourself, install X. 
### The Art
This project uses the Metropolitan Museum of Art API. In the future, I hope to expand to the Brooklyn Museum and the NYPL Digital Collections. 
My Python script aimed locate all art and artifacts from the desired time period. However, I found many objects included in the Met's API did not have values for the parameters set. For example, setting the Dynasty parameter as "4th Dynasty" did not yield any results, but the general search parameter for "4th Dynasty" did. 

For each wonder, I relied on general queries to narrow down the art to the same approximate time period as the creation. For example, I looked at works from the Old Kingdom of Egypt for the Great Pyramid of Giza page. 

After my parameters were set, I extracted a list of object IDs that matched my criteria. I used a loop to get data using the object IDs. This portion was difficult at first and involved trial and error to ensure the list properly generated. I then made an HTML table by looping through the objects and including the relevant information (image, URL, name, date). I decided to use an HTML string for this function, Lastly, the HTML string was written to an HTML file. 

To run this script yourself, you should install X 
## Final Output
The final output for this project is located at URL. 
