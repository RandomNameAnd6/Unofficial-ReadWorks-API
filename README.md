# Unofficial ReadWorks API
An unofficial Python API for ReadWorks lessons
---
Here's some example code using the API to print the title of a lesson:
```python
import readworks_api

rw = readworks_api.ReadWorks("https://dnmkr7tf85gze.cloudfront.net/data/p/81159e0e-0d97-43f8-a0f5-c3718305e708_0031")
print(rw.title())
```

To get the lesson data link, you can run the following JavaScript code when you are on a ReadWorks lesson:
```javascript
function monitorFetchAndCopyCloudfrontUrls() {
  const cloudfrontUrls = [];
  const requests = performance.getEntriesByType('resource');
  for (const request of requests) {
    const url = request.name;
    if (url.startsWith('https://dnmkr7tf85gze.cloudfront.net/data/p/')) {
      cloudfrontUrls.push(url);
    }
  }
  return cloudfrontUrls;
}

console.log(monitorFetchAndCopyCloudfrontUrls());
```
