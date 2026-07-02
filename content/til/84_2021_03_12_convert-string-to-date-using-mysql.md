title: Convert string to date using MySQL
date: March 12th, 2021
slug: convert-string-to-date-using-mysql
category: MySQL
status: active

Today, I was debugging a piece of code that is supposed to return a list of data based on the year, the funny thing is that the data was being returned on the development server but not on the production one.

Weird, so I opened up **MySQL Workbench** and wrote a simple query to see if the dates were being returned because who knows maybe they weren't stored at all.

```mysql
SELECT YEAR(date_posted) FROM posts;
```

The values returned were `null`. Now, that's strange because the dates were present in the column. So, I took a deep look and figured out that the dates were stored in `VARCHAR` instead of `DATETIME` data type! &#x1F614;

Luckily, I figured that there's a way to resolve this by `STR_TO_DATE()` function:
```mysql
SELECT YEAR(STR_TO_DATE(date_posted, '%Y-%m-%d')) FROM posts;
```

Bam! The results were coming now! &#x1F60C;

Hope this helps you out!