# Shukra - Open Source Generalist AI Agent (Beta)

> **Note**: Shukra is currently in closed beta, with access limited to select users. [Request early access](https://shukra.so).

![Shukra Screenshot](frontend/public/banner.png)

Shukra is a fully open source AI assistant that helps you accomplish real-world tasks with ease. Through natural conversation, Shukra becomes your digital companion for research, data analysis, and everyday challenges—combining powerful capabilities with an intuitive interface that understands what you need and delivers results. Currently in closed beta, available to select users only.

Shukra's powerful toolkit includes seamless browser automation to navigate the web and extract data, file management for document creation and editing, web crawling and extended search capabilities, command-line interface for system operations, and much more. All these capabilities work together harmoniously, allowing Shukra to solve your complex problems and automate workflows through simple conversations!

[![GitHub Repo stars](https://img.shields.io/github/stars/kortix-ai/shukra)](https://github.com/kortix-ai/shukra)
[![Issues](https://img.shields.io/github/issues/kortix-ai/shukra)](https://github.com/kortix-ai/shukra/labels/bug)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Shukra Architecture](#project-architecture)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Shukra consists of four main components:

1. **Frontend**: A Next.js application that provides the user interface
2. **Backend**: A FastAPI server that handles the core logic and agent execution
3. **Sandbox**: A secure environment for running untrusted code and browser automation
4. **Database**: A Supabase PostgreSQL database for storing user data and agent state

## Features

Here are some examples of what you can do with Shukra:

1. **Competitor Analysis** ([Watch](https://www.shukra.so/share/5ee791ac-e19c-4986-a61c-6d0659d0e5bc)) - _"Analyze the market for my next company in the healthcare industry, located in the UK. Give me the major players, their market size, strengths, and weaknesses."_

2. **VC List** ([Watch](https://www.shukra.so/share/804d20a3-cf1c-4adb-83bb-0e77cc6adeac)) - _"Give me the list of the most important VC Funds in the United States based on Assets Under Management. Give me website URLs, and if possible an email address."_

3. **Looking for Candidates** ([Watch](https://www.shukra.so/share/3ae581b0-2db8-4c63-b324-3b8d29762e74)) - _"Go on LinkedIn, and find me 10 profiles available - they are not working right now - for a junior software engineer position, who are located in London."_

4. **Planning Company Trip** ([Watch](https://www.shukra.so/share/725e64a0-f1e2-4bb6-8a1f-703c2833fd72)) - _"Generate me a route plan for my company. We should go to California. We'll be in 8 people. Compose the trip from the departure (Paris, France) to the arrival (San Francisco, USA)."_

5. **Working on Excel** ([Watch](https://www.shukra.so/share/128f23a4-51cd-42a6-97a0-0b458b32010e)) - _"My company asked me to set up an Excel spreadsheet with all the information about Italian lottery games (Lotto, 10eLotto, and Million Day). Based on this information, I need to create a PowerPoint presentation."_

6. **Automate Event Speaker Prospecting** ([Watch](https://www.shukra.so/share/7a7592ea-ed44-4c69-bcb5-5f9bb88c188c)) - _"Find 20 AI ethics speakers from Europe who've spoken at conferences in the past year. Scrapes conference sites, cross-references LinkedIn and YouTube, and outputs contact info + talk summaries."_

7. **Summarize and Cross-Reference Scientific Papers** ([Watch](https://www.shukra.so/share/c2081b3c-786e-4e7c-9bf4-46e9b23bb662)) - _"Research and compare scientific papers talking about Alcohol effects on our bodies during the last 5 years. Generate a report about the most important scientific papers talking about the topic I wrote before."_

8. **Research + First Contact Draft** ([Watch](https://www.shukra.so/share/6b6296a6-8683-49e5-9ad0-a32952d12c44)) - _"Research my potential customers (B2B) on LinkedIn. They should be in the clean tech industry. Find their websites and their email addresses. After that, write me a first contact email."_

9. **SEO Analysis** ([Watch](https://www.shukra.so/share/43491cb0-cd6c-45f0-880c-66ddc8c4b842)) - _"Based on my website shukra.so, generate an SEO report analysis, find top-ranking pages by keyword clusters, and identify topics I'm missing."_

10. **Generate a Personal Trip** ([Watch](https://www.shukra.so/share/37b31907-8349-4f63-b0e5-27ca597ed02a)) - _"Generate a personal trip to London, with departure from Bangkok on the 1st of May. The trip will last 10 days. Find an accommodation in the center of London."_

11. **Recently Funded Startups** ([Watch](https://www.shukra.so/share/8b2a897e-985a-4d5e-867b-15239274f764)) - _"Go on Crunchbase, Dealroom, and TechCrunch, filter by Series A funding rounds in the SaaS Finance Space, and build a report with company data, founders, and contact info for outbound sales."_

12. **Scrape Forum Discussions** ([Watch](https://www.shukra.so/share/7d7a5d93-a20d-48b0-82cc-e9a876e9fd04)) - _"I need to find the best beauty centers in Rome, but I want to find them by using open forums that speak about this topic. Go on Google, and scrape the forums by looking for beauty center discussions located in Rome."_

## Self-Hosting

Shukra can be self-hosted on your own infrastructure using our setup wizard. For a comprehensive guide to self-hosting Shukra, please refer to our [Self-Hosting Guide](./docs/SELF-HOSTING.md).

### Quick Start

1. Clone the repository:

```bash
git clone https://github.com/kortix-ai/shukra.git
cd shukra
```

2. Run the setup wizard:

```bash
python3 setup.py
```

The wizard will guide you through all necessary steps to get your Shukra instance up and running. For detailed instructions, troubleshooting tips, and advanced configuration options, see the [Self-Hosting Guide](./docs/SELF-HOSTING.md).

## Contributing

We welcome contributions! Please see our [Contributing Guide](./CONTRIBUTING.md) for details.

## License

Kortix Shukra is licensed under the Apache License, Version 2.0. See [LICENSE](./LICENSE) for the full license text.
