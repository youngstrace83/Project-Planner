# Project-Planner
This planner will create a schedule to help users plan their work.

## How it works
The program will display a window with a button that a user can press to choose a project file. It will then read a list of tasks from the file and sort them in the order of their starting time based on certain prerequisites. The resulting data will be converted into a chart that will display when each task starts and ends.

## Program design
This project uses one continuous loop to check if users have pressed the Open project... button. If they have, the program opens a CSV file to read and order it's contents before they are displayed as a chart. The chart will display the amount of work to be done in the allotted time.
