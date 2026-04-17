# map-pinner
makeshift tool to put pins on a map, slapped together for my Animal Crossing interactive map.
The map is hosted on https://snowcape.neocities.org/
 
 Let's not pretend anyone else is gonna use this thing, but whatever, here is an usage guide.
# The tool
I ran the whole thing in my IDE, no idea if it even works in terminal.  
The first step of using this tool is to add screenshots to the screenshot folder, as well as replacing mapnomarker.png with your own map(keep the name the same or edit the code in website.html)  
Run the backend, and then open the website in your browser.  
Click the map to move the pin.  
Change screenshots with prev and next, pin them with the attach button.  
Anything pinned will appear in the pins.txt file. They are formatted as [left],[top],[src]. (and a newline at the end that we remove later)  
When your pins.txt is done, run pagecreator.py to generate the html for the site and copy all pinned screenshots into the pinnedshots folder.  
generatedHTMLcode.txt can be copy pasted into the final webpage, while pinnedshots can be moved to the website folder and renamed to screenshots.