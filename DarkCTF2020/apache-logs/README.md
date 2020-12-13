# Apache Logs - WEB - 113pts.

## Description
Our servers were compromised!!
Can you figure out which technique they used by looking at Apache access logs.

flag format: DarkCTF{}

## Attachments
> [logs.ctf](logs.ctf)

## Solution
After taking a look at the logfile i noticed two requests that caught my attention:


```
"GET /mutillidae/index.php?page=user-info.php&username=%27+union+all+select+1%2CString.fromCharCode%28102%2C+108%2C+97%2C+103%2C+32%2C+105%2C+115%2C+32%2C+83%2C+81%2C+76%2C+95%2C+73%2C+110%2C+106%2C+101%2C+99%2C+116%2C+105%2C+111%2C+110%29%2C3+--%2B&password=&user-info-php-submit-button=View+Account+Details HTTP/1.1"
```
```
"http://192.168.32.134/mutillidae/index.php?page=user-info.php&username=%27+union+all+select+1%2CString.fromCharCode%28102%2C%2B108%2C%2B97%2C%2B103%2C%2B32%2C%2B105%2C%2B115%2C%2B32%2C%2B68%2C%2B97%2C%2B114%2C%2B107%2C%2B67%2C%2B84%2C%2B70%2C%2B123%2C%2B53%2C%2B113%2C%2B108%2C%2B95%2C%2B49%2C%2B110%2C%2B106%2C%2B51%2C%2B99%2C%2B116%2C%2B49%2C%2B48%2C%2B110%2C%2B125%29%2C3+--%2B&password=&user-info-php-submit-button=View+Account+Details"
```


In both requests in the `username` parameter there is a function call to `fromCharCode` with a bunch of parameters next to it.
I decoded the URL with [this tool](https://www.url-encode-decode.com/) to get a better view of what was going on.


```
"GET /mutillidae/index.php?page=user-info.php&username=' union all select 1,String.fromCharCode(102, 108, 97, 103, 32, 105, 115, 32, 83, 81, 76, 95, 73, 110, 106, 101, 99, 116, 105, 111, 110),3 --+&password=&user-info-php-submit-button=View Account Details HTTP/1.1"
```
```
"http://192.168.32.134/mutillidae/index.php?page=user-info.php&username=' union all select 1,String.fromCharCode(102,+108,+97,+103,+32,+105,+115,+32,+68,+97,+114,+107,+67,+84,+70,+123,+53,+113,+108,+95,+49,+110,+106,+51,+99,+116,+49,+48,+110,+125),3 --+&password=&user-info-php-submit-button=View Account Details"
```

At this point i ran a js script to check the output of `fromCharCode` method.

```javascript
console.log(String.fromCharCode(102, 108, 97, 103, 32, 105, 115, 32, 83, 81, 76, 95, 73, 110, 106, 101, 99, 116, 105, 111, 110))
console.log(String.fromCharCode(102,+108,+97,+103,+32,+105,+115,+32,+68,+97,+114,+107,+67,+84,+70,+123,+53,+113,+108,+95,+49,+110,+106,+51,+99,+116,+49,+48,+110,+125))
```
```SQL_Injection```
```flag is DarkCTF{5ql_1nj3ct10n}```
