<div id="top"></div>
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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Release date][releases-shield]][releases-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Remote Target</h3>

  <p align="center">
    A tool for automating software deployments and directory replication over sftp
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Installation</a>
    </li>
    <li>
      <a href="#getting-started">Installing from source</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

remote_target lets you synchronize project directories to remote machines via SFTP on a per-project basis. This is done using a `.remote_target` file in the project root which specifies the hostname, connection information and remote directory to push to.

[![remote_target usage example][usage_example]](https://example.com)


<p align="right">(<a href="#top">back to top</a>)</p>

## Installation

To simply install remote_target on a Linux machine, head on over to [the releases][license-url] and download the latest binary for your platform, and place it in a directory that's accessible in your path (for example ~/.local/bin). That's it!

If a prebuilt binary isn't available for your platform yet, you can install from source using the instructions below.

<!-- INSTALLING FROM SOURCE -->
## Installing from source

To install from source, follow the instructions below:

### Prerequisites

In order to build the tool you'll need to install the following tools:
* Python >=3.7 (either from [the official website](https://www.python.org/), your system package manager or a python version manager)
* Poetry ([official instructions here](https://python-poetry.org/docs/master/#installing-with-the-official-installer))

### Installation

1. Clone the repo
   ```
   git clone https://github.com/dylan-robins/remote_target.git
   cd remote_target
   ```
2. Install Python library dependencies
   ```
   poetry install
   ```
3. Build the project
   ```
   poetry build
   ```
3. Install the library
   ```
   pip install --user dist/remote_target*.whl
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

```
usage: remote_target [-h] {info,init,push} ...

A tool for automating software deployments and directory replication over sftp

optional arguments:
  -h, --help        show this help message and exit

subcommands:
  {info,init,push}
    info            Displays information about the current remote_target configuration
    init            Initializes a .remote_target file in the current working directory
    push            Pushes the local files to the remote target
```

Example usage:  
[![remote_target usage example][usage_example]](https://example.com)


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

Distributed under the MIT License. See [LICENCE.txt][license-url] for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dylan-robins/remote_target.svg?style=for-the-badge
[contributors-url]: https://github.com/dylan-robins/remote_target/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dylan-robins/remote_target.svg?style=for-the-badge
[forks-url]: https://github.com/dylan-robins/remote_target/network/members
[stars-shield]: https://img.shields.io/github/stars/dylan-robins/remote_target.svg?style=for-the-badge
[stars-url]: https://github.com/dylan-robins/remote_target/stargazers
[issues-shield]: https://img.shields.io/github/issues/dylan-robins/remote_target.svg?style=for-the-badge
[issues-url]: https://github.com/dylan-robins/remote_target/issues
[license-shield]: https://img.shields.io/github/license/dylan-robins/remote_target.svg?style=for-the-badge
[releases-url]: https://github.com/dylan-robins/remote_target/releases
[releases-shield]: https://img.shields.io/github/release-date/dylan-robins/remote_target?style=for-the-badge
[license-url]: https://github.com/dylan-robins/remote_target/blob/master/LICENSE.txt
[usage_example]: img/usage_example.png
