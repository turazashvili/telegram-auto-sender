<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]




<!-- PROJECT LOGO -->
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple PyAUTOGUI based script.
1) Set UP the script based on instructions below
2) Open Telegram
3) Run the script
4) Enjoy AutoSending of your messages!

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)
* [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
* [KeyBoard](https://pypi.org/project/keyboard/)
* [Threaded](https://pypi.org/project/threaded/)
*  WebBrowser


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/turazashvili/telegram-auto-sender.git
   ```
2. Install Python
   Choose latest release for your OS https://www.python.org/downloads/
3. Install all libraries one by one
     ```py
      pip install webbrowser 
      pip install  pyautogui
      pip install  threading
      pip install  keyboard
     ```
     
4. Export database from Telegram
    1) Click on Settings >>> Advanced >>> Export Telegram Data.
    2) Select the box “Contacts List” only.
    3) Scroll down and click on Json format.
    4) Save the file in the same folder with this project and call it contacts
    5) Delete everything except List category. So it  looks like on the screenshot below
      <img width="175" alt="image" src="https://user-images.githubusercontent.com/74835523/174530668-9b959bf3-87bd-4d8a-b8ac-b3e334a2ca5a.png">


5. Run the script
   ```py
    python getlist.py
   ```
   It will generate the file copyToMain.txt with proper formatting to insert it to Array of clients we want to send our message to!
   <img width="115" alt="image" src="https://user-images.githubusercontent.com/74835523/174530839-7c1a6da1-57da-482d-84ac-5c7d67e8dd9c.png">

6. Insert the names from copyToMain.txt to names array and Message you want to send to your contacts.
<img width="709" alt="image" src="https://user-images.githubusercontent.com/74835523/174532212-2022a550-1124-4117-bb52-eb037024f869.png">

7.Run the script
   ```py
    python main.py
   ```
8. Open Telegram (you will have 5 seconds before the script starts sending messages
**9. Long Press 'S' key on your keyboard to stop the script!**

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage






<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add other ways to extract data from contacts.
- [ ] Add more styling to messages.


See the [open issues](https://github.com/turazashvili/telegram-auto-sender/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project 
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nikoloz Turazashvili - [@axrisi](https://twitter.com/axrisi) - turazashvili@gmail.com

Project Link: [https://github.com/turazashvili/telegram-auto-sender/](https://github.com/turazashvili/telegram-auto-sender/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/turazashvili/telegram-auto-sender.svg?style=for-the-badge
[contributors-url]: https://github.com/turazashvili/telegram-auto-sender/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/turazashvili/telegram-auto-sender.svg?style=for-the-badge
[forks-url]: https://github.com/turazashvili/telegram-auto-sender/network/members
[stars-shield]: https://img.shields.io/github/stars/turazashvili/telegram-auto-sender.svg?style=for-the-badge
[stars-url]: https://github.com/turazashvili/telegram-auto-sender/stargazers
[issues-shield]: https://img.shields.io/github/issues/turazashvili/telegram-auto-sender.svg?style=for-the-badge
[issues-url]: https://github.com/turazashvili/telegram-auto-sender/issues
[license-shield]: https://img.shields.io/github/license/turazashvili/telegram-auto-sender.svg?style=for-the-badge
[license-url]: https://github.com/turazashvili/telegram-auto-sender/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/turazashvili
[product-screenshot]: images/screenshot.png
