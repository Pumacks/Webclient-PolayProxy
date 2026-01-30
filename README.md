<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<div align="center">
  <img width="256" height="256" alt="Polarview-logo" src="https://github.com/user-attachments/assets/46a8dcc0-199a-470d-92df-af62a5f2e8c2" />

<h3 align="center">Polarview</h3>

  <p align="center">
    The Polarview webclient provides a simple Web-based dashboard for the transparent TLS and SSL inspection proxy: PolarProxy
    <br />
  </p>
</div>

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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

At the current state there are functions for connecting a PolarProxy instance and managing it. 
The following functions are included in this project right now:
- Starting & stopping PolarProxy
- Viewing logs
- Fast technology switching (docker or systemd service)
- Open a Wireshark instance which listens on the PCAP-over-IP address

> Please be aware that this dashboard is **not** for configuring PolarProxy itself.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1.2-darkcyan?logo=flask)
![pip](https://img.shields.io/badge/pip-latest-3776AB?logo=pypi)



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Install Python
  ```sh
  # Arch Linux
  sudo pacman -S python python-pip

  # Ubuntu or Debian
  sudo apt install python3 python3-pip python3-venv
  ``` 

### Installation

1. Create a folder
   ```sh
   mkdir polarview
   cd polarview
   ```
1. Clone this repo
   ```sh
   git clone https://github.com/Pumacks/Webclient-PolayProxy.git
   ```
2. Create a virtual environment
   ```sh
   python -m venv .venv
   ```
2. Activate the virtual environment
   ```
   source .venv/bin/activate
   ```
2. Install pip 
   ```sh
   python -m ensurepip --upgrade
   ```
3. Install Flask
   ```sh
   pip install flask
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

### Home and Options page
<img height="300" alt="home" src="https://github.com/user-attachments/assets/93afa557-58ff-4fad-b614-f53fc08b1edf" />
<img height="300" alt="options" src="https://github.com/user-attachments/assets/54b78e2b-3207-44e5-a8bc-6b9784c42295" />

### Switching technologies
![switch-technology](https://github.com/user-attachments/assets/dfc4d5c3-4fe0-4a47-ab4d-7b7f3b7baf1e)

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

<!-- LICENSE -->
## License

Distributed under the GPL-3.0 license. See `LICENSE.txt` for more information.  

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Pumacks/Webclient-PolayProxy.svg?style=for-the-badge
[contributors-url]: https://github.com/Pumacks/Webclient-PolayProxy/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Pumacks/Webclient-PolayProxy.svg?style=for-the-badge
[forks-url]: https://github.com/Pumacks/Webclient-PolayProxy/network/members
[stars-shield]: https://img.shields.io/github/stars/Pumacks/Webclient-PolayProxy.svg?style=for-the-badge
[stars-url]: https://github.com/Pumacks/Webclient-PolayProxy/stargazers
[issues-shield]: https://img.shields.io/github/issues/Pumacks/Webclient-PolayProxy.svg?style=for-the-badge
[issues-url]: https://github.com/Pumacks/Webclient-PolayProxy/issues
[license-shield]: https://img.shields.io/github/license/Pumacks/Webclient-PolayProxy.svg?style=for-the-badge
[license-url]: https://github.com/Pumacks/Webclient-PolayProxy/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white

[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
