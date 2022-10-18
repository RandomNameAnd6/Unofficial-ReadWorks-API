# Unofficial ReadWorks API (DOES NOT WORK RIGHT NOW)
An unofficial API for ReadWorks lessons
---
Here's some example code using the API to print the title of a lesson:
```python
import readworks_api

ReadWorks = readworks_api.ReadWorks("https://dnmkr7tf85gze.cloudfront.net/data/p/81159e0e-0d97-43f8-a0f5-c3718305e708_0031", 3)
print(ReadWorks.title())
```
