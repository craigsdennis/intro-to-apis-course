# Introduction to APIs

## Unit 1 - What is an API

In this unit we'll define what an API, or Application Programming Interface is and why you should use them.

### Video 1 - Welcome

👋 Hello and welcome to the course and your notes! Make sure you check this area out often!

#### 👀 - Beginner content

* [freeCodeCamp.org](https://www.freecodecamp.org/) is a great place to get started and I recommend jumping [right in](https://www.freecodecamp.org/learn/responsive-web-design/basic-html-and-html5/say-hello-to-html-elements).
* [freeCodeCamp on YouTube](https://www.youtube.com/freecodecamp) provides a wonderful collection of beginning programming courses. I recommend the [🎥 JavaScript](https://www.youtube.com/watch?v=PkZNo7MFNFg) and [🎥 Python](https://www.youtube.com/watch?v=rfscVS0vtbw) tutorials.

#### 📚 - Designing API Content

* [ProgrammableWeb 101 - What exactly is an API](https://www.youtube.com/watch?v=cpRcK4GS068&list=PLcgRuP1JhcBP8Kh0MC53GH_pxqfOhTVLa)
* [moseif - API Guide](https://www.moesif.com/blog/api-guide/)

### Video 2 - Defining Interface

#### 📚 - Learn more

##### Media Player APIs

Don't worry about understanding it, just appreciate their complexity

* [Android MediaPlayer API documentation](https://developer.android.com/reference/android/media/MediaPlayer). (
* [iOS Media Player API documentation](https://developer.android.com/reference/android/media/MediaPlayer)
* [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)

### Video 3 - Defining API

#### 📚 - Learn more

* [mdn - Web APIs](https://developer.mozilla.org/en-US/docs/Web/API)
* [Google vs. Oracle on the rights to the Java API](https://www.theverge.com/2019/11/15/20946398/oracle-google-java-copyright-lawsuit-trial-supreme-court-request)

### Video 4 - Remote APIs

* [Wikipedia - SOAP](https://en.wikipedia.org/wiki/SOAP)
* [Wikipedia - Remote Procedure Call (RPC)](https://en.wikipedia.org/wiki/Remote_procedure_call)
* [SOAP and REST at Odds](https://thehistoryoftheweb.com/soap-rest-odds/)
* [SOAP vs. REST](https://stackify.com/soap-vs-rest/)
* [REST vs. RPC](https://cloud.google.com/blog/products/application-development/rest-vs-rpc-what-problems-are-you-trying-to-solve-with-your-apis)

### Video 5 - How the web works

* [Wikipedia - HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
* [Space Jam Website](http://www.spacejam.com)

### Video 6 - RESTful API Constraint Scavenger Hunt

* [Wikipedia - Representational State Transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)

## Unit 2 - Exploring APIs

### Video 1 - Exploring an API online

* [Spotify for Developers](https://developer.spotify.com/)
* [Spotify - Search API {BETA}](https://developer.spotify.com/documentation/web-api/reference-beta/#category-search)
* [Lizzo's Spotify Page](https://open.spotify.com/artist/56oDRnqbIiwx4mymNEv7dS)
* Lizzo's Spotify ID: `56oDRnqbIiwx4mymNEv7dS`

#### 👀 - Explore

ProgrammableWeb provides [a categorized directory of APIs](https://www.programmableweb.com/category-api). API List provides [categories and a powerful search feature](https://apilist.fun/).

### Video 2 - Using an API from the command line

* [Twilio](www.twilio.com/referral/d4X15O)
* [Twilio Console](https://twilio.com/console?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)
* [SMS Getting Started](https://www.twilio.com/console/sms/getting-started/build?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)
* Check out the [jq tutorial](https://stedolan.github.io/jq/tutorial/) for parsing JSON on the command line

#### cURL

##### Mac OS

###### Using Homebrew

```bash
brew install curl
```

###### Download

[⬇️ - Download cURL for MacOSX](https://curl.haxx.se/dlwiz/?type=bin&os=Mac+OS+X)

##### Windows

[⬇️ - Download cURL for Windows](https://curl.haxx.se/windows/)

NOTE: If you are running PowerShell, delete the `curl` alias for `Invoke-WebRequest` by adding the following command to your profile (`C:\Users\<username>\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1)`:

```bash
Remove-Item alias:curl
```

#### 📚 - Learn More

* [cURL manpage](https://curl.haxx.se/docs/manpage.html)
* [Wikipedia - POST (HTTP)](https://en.wikipedia.org/wiki/POST_(HTTP)) (For info on `form-urlencoded` search for "Use for submitting web forms)

### Video 3 - Using Postman to explore APIs

⬇️ - Download [Postman](https://getpostman.com)

The Twilio Messages API URL is:

```bash
https://api.twilio.com/2010-04-01/Accounts/<Your Account SID Here>/Messages.json
```

Make sure to replace that `SID` with your Account SID which can be found in the [Twilio console](https://twilio.com/console)

### Video 4 - Please please Mr. Postman

⬇️ - Many wonderful API Collections can be downloaded for exploration in the [Postman API Network](https://explore.postman.com/)

#### 📚 - Learn more

* [How Collaboration Works in Postman](https://www.getpostman.com/how-api-collaboration-works)
* [Official Postman Tutorials](https://www.getpostman.com/resources/videos-tutorials/)

### Video 5 - Using Helper Libraries (JavaScript)

* [Install Node.js](https://nodejs.org/en/download/)
* [Install Python 3](https://www.python.org/downloads/)
* [Install Visual Studio Code](https://code.visualstudio.com/download)
  * [macOS](https://code.visualstudio.com/docs/setup/mac)
  * [Windows](https://code.visualstudio.com/docs/setup/windows)
  * [Linux](https://code.visualstudio.com/docs/setup/linux)

To use the [Twilio Node Helper Library](https://www.twilio.com/docs/libraries/node#installation)

```bash
npm install twilio
```

#### 📚 - Learn More

* [Wikipedia - Boilerplate code](https://en.wikipedia.org/wiki/Boilerplate_code)

### Video 6 - Using Helper Libraries (Python)

* [Install Python 3](https://www.python.org/downloads/)

To use the [Twilio Python Helper Library](https://www.twilio.com/docs/libraries/python)

```bash
pip install twilio
```

## Unit 3 - Using APIs

### Video 1 - Introducing the project

* [Glitch](https://glitch.com)

#### 📚 - Learn more

* [Slack API](https://api.slack.com/)
* [Sportsball APIs](https://rapidapi.com/blog/best-sports-apis-ranked/)
* [Philips Hue API](https://developers.meethue.com/)
* [🎥 Furby Hacking 101 w/ Chloe Condon](https://www.youtube.com/watch?v=dWpqoMObX54)

### Video 2 - Flask app

⚠️ Several students have reported that cloning sets up a default Glitch application. If this happens to you, in the Glitch app that is created choose "Tools >> Extras >> Git Import and Export >> Import from GitHub" when prompted enter "craigsdennis/intro-to-apis-node" or "craigsdennis/intro-to-apis-flask"

[Complimentr Flask GitHub repository](https://github.com/craigsdennis/intro-to-apis-flask) is located at `https://github.com/craigsdennis/intro-to-apis-flask.git`

* [Twilio docs - Create a Message with Python](https://www.twilio.com/docs/sms/api/message-resource?code-sample=code-create-a-message&code-language=Python&utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)
* [Twilio docs - List all Messages with Python](https://www.twilio.com/docs/sms/api/message-resource?code-sample=code-create-a-message&code-language=Python&utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)

#### 📚 - Learn more

* [Flask documentation](https://flask.palletsprojects.com/)
* [Environment Variables](https://www.twilio.com/docs/usage/secure-credentials)

### Video 3 - Dealing with API Limits

#### 📚 - Learn more

* [Nordic APIs - Everything You Need To Know About API Rate Limiting](https://nordicapis.com/everything-you-need-to-know-about-api-rate-limiting/)

### Video 4 - JavaScript Single Page Application

⚠️ Several students have reported that cloning sets up a default Glitch application. If this happens to you, in the Glitch app that is created choose "Tools >> Extras >> Git Import and Export >> Import from GitHub" when prompted enter "craigsdennis/intro-to-apis-node" or "craigsdennis/intro-to-apis-flask"

[Complimentr Node.js GitHub repository](https://github.com/craigsdennis/intro-to-apis-node) is located at `https://github.com/craigsdennis/intro-to-apis-node.git`

* [Twilio docs - Create a Message with Node.js](https://www.twilio.com/docs/sms/api/message-resource?code-sample=code-create-a-message&code-language=Node.js&utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)
* [Twilio docs - List all Messages with Node.js](https://www.twilio.com/docs/sms/api/message-resource?code-sample=code-create-a-message&code-language=Node.js&utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)

#### 📚 - Learn more

* [mdn - Async / Await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Async_await)
* [Vue.js - Getting Started](https://vuejs.org/v2/guide/)
* [Node.js - Getting Started](https://nodejs.org/en/docs/guides/getting-started-guide/)

### Video 5 - Moar JavaScript and Recap

* [Wikipedia - REST Architectural Constraints](https://en.wikipedia.org/wiki/Representational_state_transfer#Architectural_constraints)

### Video 6 - Review

I built a little Twilio application using [Studio](https://www.twilio.com/docs/studio?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis) and some APIs to gather your feedback.

Please text `FEEDBACK` to me at [(503) 461-5537](tel:+15034615537) and let me know what you thought about this course! (You can also call if that's your jam)

👋 Thanks for hanging out! 🙏 Keep me updated on your journey 💪🚀!

[@craigsdennis](https://twitter.com/craigsdennis)

PS. If you want to keep on learning for free, I can't recommend [the video game TwilioQuest 🎮](https://twilio.com/quest?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis) enough.
