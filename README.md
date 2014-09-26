#  kWh Analytics Interview Project
## Looking for engineers to join the fight against climate change: Building software for solar performance analytics

Welcome to the kWh Analytics interview project. Our goal in this project is to both (a) show you the types of problems we solve, and (b) get an idea of how you approach the problems. This is a simple, mostly fictional project -- it's far more simple than our typical tasks. However, we hope you walk away understanding a bit more of what would be expected of you.

## General rules

-  **Time Limit**: This interview should take you 1-2 hours. Please do not spend more than 4 hours on the project (we trust you). 
-  **Your Work**: The results should be your own work. Feel free to consult with Google or Stack Overflow, but cite any sources that you borrow substantial ideas or code from.
-  **No Other People**: No one else should help you on the project.
-  **Keep Your Results Private**: Make sure to keep your results private -- please don't publicly fork this repository, answer the questions, and submit a pull request.

# Part 1

In solar energy, one of the most common metrics used in understanding solar production is the performance ratio. In it's most basic form, it can be defined as:

```
performanceratio = sum(actual production (kWh)) / sum(expected production (kWh))
```

Much of the challenge in calculating a performance ratio comes from calculating `expected production (kWh)`. For larger, utility scale systems, irradiance (W/m^2) is often directly measured and can be used to calculate `expected production (kWh)`. However, for residential systems, such measurements are not available, and `expected production (kWh)` must be estimated over longer periods of time using historical data.

In the current problem, you'll be asked to calculate and manipulate the lifetime performance ratio for a set of systems. The test database provided in this interview problem contains reduced, daily data for eight systems -- in our actual database, we have over 40,000 systems along with metadata, many forms of `expected production`, and often 15-minute level data. The calculation for expected power has already been performed, saving you the trouble.

## Solar Module

Your basic task consists of creating a python module to grab data from a backend database, calculate the lifetime performance ratio, and store the results in an efficient data structure.


## Instructions

1.  **Clone the repository** - Grab all of the code: ` git clone https://github.com/kwhanalytics/solar-interview`.
2.  **Install third party modules** - Install the required dependencies for the solar modules: `pip install -r requirements.txt`.
3.  **Familiarize yourself with the existing code** - Check out the `test.db` file -- this is the sqlite3 database file. Check out files in the [`solar`](https://github.com/kwhanalytics/solar-interview/tree/master/solar) directory -- these are the files responsible for implementing the solar module. Check out the files in the [`test`](https://github.com/kwhanalytics/solar-interview/tree/master/test) directory -- these are the test which will now direct you.
4.  **Run the tests** - A number of tests have been written for the code base. These tests describe the functionality expected in the modules. Try running the tests: `nosetests`.
5.  **Write the code** - Write the code required to make the tests pass. In some cases, the tests haven't even been written -- in these cases, write the code for testing as well. In the process of writing the code, you may find that more tests are needed to cover your pases -- write them up!

You might want to consider a few things as you code:

-  How flexible is your code? Are the classes and the database closely or loosely coupled? Do the tests provide adequate coverage without being too implementation specific?
-  Is your code nicely formatted in and in-line with standard style guides? If you're unfamiliar with Python styles, a good resource is [pylint](http://www.pylint.org/).
-  What data structure did you use for the SolarPerformanceCollection? How quickly are the various operations performed (`add`, `min`, `max`, `count`, `top`)? Can you do better? How much does the implementation change if the dataset is frequently appended? Or if the dataset is rarely appended but frequently queried for the top k systems?

# Part 2

Not only do we hope to calculate and work with the data, but we also hope to display the data both internally and externally. How would you visualize the data (imagine that 40,000 sites are present in the database)? If you owned the systems in the dataset, what visualizations would be helpful? What would you visualize at the portfolio level, and what would you visualize at the system level?

## Instructions

1) **Sketch out visualizations** - Sketch out the dashboards on paper. __You do not need to code the front-end visualization__! Try to tell a story, and think from the user's perspective.


Good luck!
