# DominionEnergyMonitor

A lightweight Python-based container to scrape your daily energy usage from the Dominion Energy website and publish it via MQTT to Home Assistant.

## 🔧 Features

- Authenticates with the Dominion Energy web portal using user-provided credentials
- Fetches your most recent daily kWh usage from the Dominion API
- Publishes the data to an MQTT broker (e.g., for use in Home Assistant)
- Built to run as a one-off Docker container triggered via cron

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hughNeutron314/DominionEnergyMonitor.git
cd DominionEnergyMonitor
```

### 2. Configure Environment Variables

Rename the `.env.template` file to `.env`:

```bash
cp .env.template .env
```

Then, populate it with your:
- Dominion Energy login credentials
- Account number
- MQTT broker connection details

### 3. Build and Run the Docker Container

```bash
docker compose build
docker compose up
```

The container will authenticate, retrieve the latest usage data, publish it via MQTT, and then terminate.

---

## ⏱️ Automating with Cron

Since Dominion's API updates once per day, it's recommended to run the container once daily via `cron`:

Example cron job (runs every day at 7am):

```bash
0 7 * * * docker compose -f /path/to/DominionEnergyMonitor/docker-compose.yml up --build
```

---

## 🧪 Technologies Used

- Python
- Docker
- MQTT (via `paho-mqtt`)
- Selenium (for session handling)
- Home Assistant integration (via MQTT)

---

## 📜 License

MIT License – see [`LICENSE`](./LICENSE) for details.

---

## 🙋‍♂️ Contributions

Feel free to open issues or submit PRs to improve reliability, support more features, or handle edge cases!

---

## 📫 Contact

Maintained by [@hughNeutron314](https://github.com/hughNeutron314)
