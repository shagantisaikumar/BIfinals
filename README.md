MY JOURNEY WITH NASA ASTEROID DATA: BUILDING A REAL-TIME ETL PIPELINE

There is something profoundly humbling about working with data that actually comes from space. The asteroids, stars, and planets fascinated me as a child, so when I discovered that NASA has publically accessible APIs, it was like an open door to the cosmos. I wanted to create something useful—something that combined my passion for space with my data engineering skills. That is how I ended up developing an ETL (Extract, Transform, Load) project based on asteroid information.

It began with NASA's Near-Earth Object Web Service (NeoWs), a database of asteroids making their way into our cosmic neighborhood. It provides detailed data about the size of each asteroid, its velocity, its distance from our world, and even whether or not it's potentially harmful. When I first saw it, I knew that this was going to be the foundation of my project.

Obtaining Data from NASA's API

My first job was to pull data out of the API. I wrote a Python script that called the endpoint with my own API key. The response format of the API was deep, with nested JSON arrays containing everything from estimated diameters to orbital data. It was intimidating initially. But once I worked out how to get around the structure, it was simply a case of writing a loop to iterate around each of the asteroid objects and pull out the correct fields.

I prioritized pulling key facts that would provide scientific worth as well as analytical richness—fields such as asteroid name, maximum and minimum estimated diameter, speed, closest approach to Earth, and whether potentially hazardous. I restricted the data to roughly 40 objects and 10 key attributes so that the data would remain manageable yet rich with insight.

Transforming the Chaos

Once I had the raw data, I went on to the transformation phase. This was all cleaning and normalization. The fields were a mix of being received as strings, nested dictionaries, and also null. I created a transformation script with Python which flattened the JSON format and converted all this into a neat table-like structure.

The transform script also did data type conversions—i.e., string to float for numerical analysis and date standardization. I added some derived measurements like averaging diameter from min and max. This made the dataset more ready for downstream analysis and easier to visualize subsequently.




Loading into PostgreSQL

With the clean data in hand, I created a PostgreSQL database to store it. I created a table schema particular to the fields that I had extracted. Using the psycopg2 library in Python, I wrote a loader script which inserted the data into my database. Every cycle of the ETL process would now extract new data and overwrite the existing table, keeping my dataset up to date without any work on my end.

This was a massive achievement in the project. I now had a queryable, structured representation of live space data, sitting in a relational database on my local machine. It wasn't just an API response any more; it was an active data source.

Visualizing in Power BI

![image](https://github.com/user-attachments/assets/06d38b07-5d5b-4a3c-8081-4d53ba95b9af)

 
The final element of the project was to put the data into Power BI and visualize it. I imported the data from my PostgreSQL database and started building dashboards that could tell revealing stories. One of the initial things I created was a bar chart showing the 10 biggest asteroids by diameter. It was awe-inspiring to see how much variation exists in the size, which can go from very small pebbles to objects kilometers in width.

I then constructed a pie chart to compare the number of hazardous vs. safe asteroids. Of course, the majority were harmless, but there were a few that lit up red that gave me the shudders. I wanted to drill further, so I added a line chart to demonstrate how the speeds of the asteroids changed over time. It's amazing to see these space rocks move at tens of thousands of kilometers per hour.

I believe my favorite graph was a scatter plot of asteroid size along the X and miss distance along the Y, colored by hazard status. The large, close asteroids were all clumped in one corner of the graph like a space danger zone. That graph said it all—all of the largest asteroids were hurtling in toward Earth at alarming speeds.

To make the dashboard interactive, I added slicers on bodies and dates and tooltips with asteroid names, approach velocities, and other metadata. It transformed a two-dimensional dataset into an inquiry space for wonder and concern both.

Insights I Found

One of the things that struck me was that many of the asteroids that were labeled as hazardous weren't necessarily the largest. Hazard status is not size; it's trajectory and how close they approach. I also noticed some orbital body trends—most of the objects were tracked orbiting around Earth, but some were linked to other planets. It referenced the type of orbital mechanics and how dynamically these bodies move.



Challenges Along the Way

As with any real project, there were challenges. The API rate limit necessitated creating logic around retries and not over-polling. Converting the nested data structure was difficult—particularly when handling multiple close approach events for a single asteroid. Getting the PostgreSQL schema consistent with the data types of the API took multiple attempts. And arranging Power BI visuals in an intuitive manner required a fair amount of experimentation.

But all of those issues were learning opportunities. It allowed me to become more comfortable with API integration, Python data manipulation, and the power of SQL as a data storage foundation.

What I Learned

This project taught me to take something abstract—like space data—and make it meaningful. It taught me how ETL pipelines work in real life: from intake, to processing, to warehousing, to analysis. Most importantly, it reminded me that data is most powerful when it tells a story, especially when the story is of the universe blurring past us at thousands of kilometers per second.

The Bigger Picture

This is not just data pipelines and dashboards—it's a small part of the greater endeavor of space science. The data is NASA's. I imposed a layer of structure, storage, and visualization on that data that makes it more accessible and understandable. Whatever you are—a scientist, policymaker, curious individual—seeing these insights helped me gain a better understanding of our place in the solar system.

I plan to continue expanding this project—maybe add warnings for future releases of asteroids coming through or track year-over-year trends. There's just so much there, and space is not running out of stories anytime soon.
